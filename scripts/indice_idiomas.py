#!/usr/bin/env python3
"""Pastas e índices das edições em espanhol e inglês dos manuais.

Lê <idioma>/slugs.csv (numero, slug_pt, slug, titulo), a cópia versionada da
lista oficial de títulos traduzidos (titulos-es.csv e titulos-en.csv de
mercados/dinheiro/traducao/ no repositório Infoprodutos-Direct-Response), cria
<idioma>/manuais/<slug>/ com um .gitkeep e grava <idioma>/indice.csv com as
colunas numero, slug_pt, slug, titulo, pasta, imagens_prontas. slug_pt é a
pasta do manual em português em manuais/ (o slug de venda do catálogo).

Pode ser rodado de novo a qualquer momento: não apaga nem move nada, só cria as
pastas que faltam e reescreve o índice. imagens_prontas conta quantas das 10
imagens da galeria já estão na pasta e passam na conferência (1000×1000, JPG,
até 300 KB).

Uso:
    python3 scripts/indice_idiomas.py
    python3 scripts/indice_idiomas.py --traducao ../Infoprodutos-Direct-Response/mercados/dinheiro/traducao
    python3 scripts/indice_idiomas.py --verificar es/manuais/<slug>

Com --traducao, lê os titulos-<idioma>.csv oficiais em vez dos slugs.csv daqui
(têm de ter as colunas slug e slug_pt).
"""

import argparse
import csv
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
IDIOMAS = ("es", "en")
TIPOS = (
    "01-capa",
    "02-sumario",
    "03-ferramenta",
    "04-passo-a-passo",
    "05-exemplo",
    "06-diagrama",
    "07-planilha",
    "08-resultado",
    "09-checklist",
    "10-entrega",
)
LADO = 1000
LIMITE_BYTES = 300 * 1024
SLUG_VALIDO = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
COLUNAS_INDICE = ("numero", "slug_pt", "slug", "titulo", "pasta", "imagens_prontas")
TOTAL_POR_IDIOMA = 100


def tamanho_jpeg(caminho):
    """(largura, altura, componentes) do marcador SOF, ou None se não for JPEG."""
    dados = caminho.read_bytes()
    if dados[:2] != b"\xff\xd8":
        return None
    i = 2
    while i + 4 <= len(dados):
        if dados[i] != 0xFF:
            i += 1
            continue
        marcador = dados[i + 1]
        if marcador in (0xD8, 0x01) or 0xD0 <= marcador <= 0xD7 or marcador == 0xFF:
            i += 1 if marcador == 0xFF else 2
            continue
        tamanho = int.from_bytes(dados[i + 2 : i + 4], "big")
        if marcador in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
            altura = int.from_bytes(dados[i + 5 : i + 7], "big")
            largura = int.from_bytes(dados[i + 7 : i + 9], "big")
            return largura, altura, dados[i + 9]
        i += 2 + tamanho
    return None


def problemas_da_imagem(caminho):
    if not caminho.is_file():
        return ["falta o arquivo"]
    problemas = []
    tamanho = caminho.stat().st_size
    if tamanho > LIMITE_BYTES:
        problemas.append(f"{tamanho // 1024} KB (limite 300 KB)")
    info = tamanho_jpeg(caminho)
    if info is None:
        problemas.append("não é JPG")
    elif not caminho.read_bytes().rstrip(b"\x00").endswith(b"\xff\xd9"):
        problemas.append("JPG incompleto (sem o marcador de fim)")
    else:
        largura, altura, componentes = info
        if (largura, altura) != (LADO, LADO):
            problemas.append(f"{largura}×{altura} (esperado {LADO}×{LADO})")
        if componentes != 3:
            problemas.append(f"{componentes} canais (esperado RGB)")
    return problemas


def conferir_pasta(pasta, slug):
    """Dicionário arquivo -> lista de problemas, para as 10 imagens esperadas."""
    return {f"{slug}-{tipo}.jpg": problemas_da_imagem(pasta / f"{slug}-{tipo}.jpg") for tipo in TIPOS}


def ler_titulos(arquivo):
    with arquivo.open(newline="", encoding="utf-8-sig") as f:
        linhas = list(csv.DictReader(f))
    if not linhas:
        sys.exit(f"{arquivo}: vazio")
    colunas = linhas[0].keys()
    for obrigatoria in ("slug", "slug_pt"):
        if obrigatoria not in colunas:
            sys.exit(f"{arquivo}: falta a coluna {obrigatoria} (tem {', '.join(colunas)})")
    coluna_titulo = next((c for c in ("titulo", "title", "titulo_es", "titulo_en") if c in colunas), None)

    titulos = []
    for posicao, linha in enumerate(linhas, start=1):
        numero = (linha.get("numero") or "").strip() or str(posicao)
        titulos.append(
            {
                "numero": int(numero),
                "slug_pt": linha["slug_pt"].strip(),
                "slug": linha["slug"].strip(),
                "titulo": (linha[coluna_titulo] or "").strip() if coluna_titulo else "",
            }
        )
    return titulos


def validar(idioma, titulos):
    erros = []
    if len(titulos) != TOTAL_POR_IDIOMA:
        erros.append(f"{len(titulos)} títulos (esperado {TOTAL_POR_IDIOMA})")
    vistos = {}
    ligados = set()
    for t in titulos:
        if not SLUG_VALIDO.match(t["slug"]):
            erros.append(f"slug inválido: {t['slug']!r}")
        if t["slug"] in vistos:
            erros.append(f"slug repetido: {t['slug']}")
        vistos[t["slug"]] = t
        if t["slug_pt"] in ligados:
            erros.append(f"slug_pt repetido: {t['slug_pt']}")
        ligados.add(t["slug_pt"])
        if not (RAIZ / "manuais" / t["slug_pt"]).is_dir():
            erros.append(f"{t['slug']}: slug_pt {t['slug_pt']} não existe em manuais/")
    if erros:
        sys.exit(f"{idioma}:\n  " + "\n  ".join(erros))


def gerar(idioma, titulos):
    linhas = []
    for t in sorted(titulos, key=lambda t: t["numero"]):
        pasta = RAIZ / idioma / "manuais" / t["slug"]
        pasta.mkdir(parents=True, exist_ok=True)
        (pasta / ".gitkeep").touch(exist_ok=True)
        conferencia = conferir_pasta(pasta, t["slug"])
        prontas = sum(1 for problemas in conferencia.values() if not problemas)
        linhas.append({**t, "pasta": f"{idioma}/manuais/{t['slug']}/", "imagens_prontas": prontas})

    with (RAIZ / idioma / "indice.csv").open("w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=COLUNAS_INDICE, lineterminator="\n")
        escritor.writeheader()
        escritor.writerows(linhas)
    completos = sum(1 for linha in linhas if linha["imagens_prontas"] == len(TIPOS))
    print(f"{idioma}: {len(linhas)} pastas, {completos} com as 10 imagens prontas")


def verificar(pasta):
    pasta = Path(pasta).resolve()
    if not pasta.is_dir():
        print(f"ERRO {pasta}: pasta não existe")
        return False
    slug = pasta.name
    conferencia = conferir_pasta(pasta, slug)
    extras = sorted(
        p.name for p in pasta.iterdir() if p.name != ".gitkeep" and p.name not in conferencia
    )
    ok = True
    for arquivo, problemas in conferencia.items():
        print(f"{'ok  ' if not problemas else 'ERRO'} {arquivo}" + (f": {'; '.join(problemas)}" if problemas else ""))
        ok = ok and not problemas
    for nome in extras:
        print(f"ERRO {nome}: arquivo fora do padrão {slug}-NN-<tipo>.jpg")
        ok = False
    return ok


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "--traducao",
        type=Path,
        help="pasta mercados/dinheiro/traducao de um clone do Infoprodutos-Direct-Response "
        "(sem isso, lê <idioma>/slugs.csv)",
    )
    parser.add_argument("--verificar", metavar="PASTA", help="só confere as 10 imagens de uma pasta e sai")
    args = parser.parse_args()

    if args.verificar:
        sys.exit(0 if verificar(args.verificar) else 1)
    lidos = {}
    for idioma in IDIOMAS:
        arquivo = args.traducao / f"titulos-{idioma}.csv" if args.traducao else RAIZ / idioma / "slugs.csv"
        if not arquivo.is_file():
            sys.exit(f"não achei {arquivo}")
        lidos[idioma] = ler_titulos(arquivo)
        validar(idioma, lidos[idioma])
    for idioma in IDIOMAS:
        gerar(idioma, lidos[idioma])


if __name__ == "__main__":
    main()
