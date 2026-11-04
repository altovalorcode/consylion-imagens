# Imagens públicas dos produtos Consylion

Capas e galerias dos manuais da Série Manuais Consylion, hospedadas aqui para a Yampi e o shop.

- Layout: `manuais/<slug>/<slug>-NN-<tipo>.jpg`, com o slug de venda do catálogo e as imagens em 1000×1000 (JPG, sRGB, até 300 KB).
- Link direto de cada imagem: `https://raw.githubusercontent.com/altovalorcode/consylion-imagens/main/manuais/<slug>/<arquivo>`.
- Fonte: pasta `saida/galeria-1000/` de cada manual no repositório `altovalorcode/Consylion-Manuais`. Não edite as imagens aqui; gere de novo lá e copie.
- Exceção: `manuais/playbook-da-segunda-renda/` (Playbook da Segunda Renda com o bônus Segunda Renda com IA, SKU `CNS-SR-001`, fora da Série) vem de `examples/generated/money-wealth/store/playbook-da-segunda-renda/galeria-1000/` no repositório `altovalorcode/Consylion-Ops`, gerada por `npm run store:kit:segunda-renda`.
- Exceção: `manuais/100-protocolos-para-fechar-vendas/` (100 Protocolos Para Fechar Vendas, SKU `CNS-PFV-001`, fora da Série) tem a capa copiada do bucket público `centurion-covers` do LMS (a mesma da Yampi) e as cenas 02 a 10 convertidas em JPG das imagens WebP da galeria do shop (`consylion-shop-shelf/public/manuais/100-protocolos-para-fechar-vendas/`). Entrou em 18/10/2026 para o catálogo Meta da loja.
- Exceção: `manuais/o-mapa-dos-clientes-ricos-2-0/` (O Mapa dos Clientes Ricos 2.0, SKU `CNS-MCR-001`, vendido só como order bump) tem só a capa, gerada em 21/10/2026 no Higgsfield (GPT Image 2.5) a partir da caixa do 100 Protocolos.
- Exceção: `manuais/programa-fluxo-de-caixa-e-lucro/` (Programa Fluxo de Caixa e Lucro na Prática, SKU `CNS-PRG-008`, fora da Série, categoria Finanças) vem de `mercados/dinheiro/shop/imagens/programa-fluxo-de-caixa-e-lucro/` do repositório `Infoprodutos-Direct-Response`, onde ficam o HTML e os scripts que geram as cenas a partir dos quadros das aulas. Entrou em 23/10/2026 para a Yampi.
- As 10 imagens de cada manual estão publicadas (01 capa, 02 sumário, 03 ferramenta, 04 passo a passo, 05 exemplo, 06 diagrama, 07 planilha, 08 resultado, 09 checklist, 10 entrega). A capa (`-01-capa.jpg`) é a foto do checkout.
- Vídeos: `videos/<slug>/<slug>-sumario.mp4`, o vídeo de sumário (versão I04, frases só no topo e no meio, 1080×1920, 26 s, ~4,5 MB) dos 21 manuais em anúncio, para o campo `video` do catálogo Meta Consylion Shop. Fonte: `criativos/lote-10-manuais/sumario/render.py` do repositório `MetaAds_Performance-Team`, comprimido com x264 CRF 28. Entrou em 18/10/2026.
- Planilha `videos/catalogo-videos.csv` (colunas `id`, `video[0].url`, `video[0].tag[0]`): lida todo dia pelo feed só de atualização `4771887926418007` do catálogo Meta Consylion Shop, que põe o vídeo de sumário nos 21 manuais sem mexer no resto do produto. Gerada por `catalogo/videos_catalogo.py planilha` do repositório `MetaAds_Performance-Team`. Não apague nem renomeie: o feed lê este caminho.
- Vídeos do YouTube (canal Consylion): `videos/<slug-do-manual>/<palavra-chave>.mp4`, com a legenda (`-legenda-pt-BR.srt`) e as 3 miniaturas do "Testar e comparar" (`-miniatura-*.jpg`, 1280×720) ao lado. Fonte: `mercados/dinheiro/youtube/videos/vNN-slug/` do repositório `Infoprodutos-Direct-Response`; o pacote de publicação de cada vídeo fica em `publicacao.md` nessa pasta. Não entram no `catalogo-videos.csv`.

## Edições em espanhol e inglês

- Layout ao lado do português, sem mexer em `manuais/` nem em `videos/` (a Yampi, o shop e o feed do catálogo Meta leem esses caminhos): `es/manuais/<slug-es>/<slug-es>-NN-<tipo>.jpg` e `en/manuais/<slug-en>/<slug-en>-NN-<tipo>.jpg`. Mesmos 10 tipos e mesmas especificações do português (1000×1000, JPG sRGB, até 300 KB), com os sufixos de tipo iguais nos três idiomas: `01-capa`, `02-sumario`, `03-ferramenta`, `04-passo-a-passo`, `05-exemplo`, `06-diagrama`, `07-planilha`, `08-resultado`, `09-checklist`, `10-entrega`.
- Link direto de cada imagem: `https://raw.githubusercontent.com/altovalorcode/consylion-imagens/main/es/manuais/<slug-es>/<arquivo>` e `https://raw.githubusercontent.com/altovalorcode/consylion-imagens/main/en/manuais/<slug-en>/<arquivo>`.
- Slugs: vêm da lista oficial de títulos em `mercados/dinheiro/traducao/titulos-es.csv` e `titulos-en.csv` do repositório `Infoprodutos-Direct-Response`. A cópia usada aqui fica em `es/slugs.csv` e `en/slugs.csv` (colunas `numero`, `slug_pt`, `slug`, `titulo`); `numero` é o número do manual na Série e `slug_pt` é a pasta do manual em português em `manuais/` (o slug de venda do catálogo, que pode diferir do slug do manual no motor). Quando a lista oficial mudar, troque esses arquivos e rode o script de novo; uma pasta com slug antigo não é apagada pelo script.
- Índices `es/indice.csv` e `en/indice.csv` (colunas `numero`, `slug_pt`, `slug`, `titulo`, `pasta`, `imagens_prontas`), com as 100 pastas de cada idioma. `imagens_prontas` é quantas das 10 imagens já estão na pasta e passam na conferência (0 a 10). Gerados por `scripts/indice_idiomas.py` a partir dos `slugs.csv`; o script cria as pastas que faltam (com um `.gitkeep`), nunca apaga nem move nada e pode ser rodado de novo: `python3 scripts/indice_idiomas.py`. Com `--traducao ../Infoprodutos-Direct-Response/mercados/dinheiro/traducao` ele lê direto os `titulos-*.csv` oficiais de um clone daquele repositório.
- Fonte: as imagens traduzidas saem do motor dos manuais, igual ao português: a galeria de 1000×1000 gerada do PDF traduzido em `Infoprodutos-Direct-Response`. Não edite as imagens aqui; corrija e gere de novo lá e copie.
- Vídeos de anúncio em inglês: `en/videos/<slug-en>/EN-<SIGLA>-<formato>.mp4` (vídeo-sumário `VID-sumario-V2`/`V3`, `teladividida-T1`, `narracao`), 1080×1920. Fonte e textos: `criativos/en/<área>/` do repositório `MetaAds_Performance-Team`. Não entram no `catalogo-videos.csv`.

### Publicar as imagens de um manual traduzido

1. Gere a galeria do manual a partir do PDF traduzido no motor dos manuais em `Infoprodutos-Direct-Response`.
2. Confira que saíram os 10 arquivos com o slug do idioma (`<slug-es>-01-capa.jpg` … `<slug-es>-10-entrega.jpg`), sem nenhum a mais, e que cada um tem 1000×1000, JPG sRGB e até 300 KB.
3. Copie os 10 arquivos para `es/manuais/<slug-es>/` (ou `en/manuais/<slug-en>/`) e rode `python3 scripts/indice_idiomas.py --verificar es/manuais/<slug-es>`: tem de dar `ok` nas 10 linhas e nenhum `ERRO`.
4. Atualize `imagens_prontas` rodando de novo `python3 scripts/indice_idiomas.py`; a linha do manual tem de ficar com 10. Faça o commit das imagens junto com o `indice.csv`.

## Pacotes das edições em inglês e espanhol (trilhas e coleção)

- Layout: `en/pacotes/<slug>/<slug>-01-capa.jpg` e `es/pacotes/<slug>/<slug>-01-capa.jpg`, uma caixa por pacote vendido na Digistore24: as 6 trilhas por área ("<Área> Set" / "Ruta <área>") e a coleção completa ("Consylion Handbook Series" / "Colección Manuales Consylion"). Mesmas especificações dos manuais (1000×1000, JPG sRGB, até 300 KB).
- Índice `pacotes.csv` (colunas `sku`, `digistore_product_id`, `idioma`, `nome`, `arquivo`, `url`): os 14 pacotes, com o SKU e o ID da Digistore24 de `mercados/dinheiro/traducao/digistore24-pacotes.csv` do repositório `Infoprodutos-Direct-Response` e o link direto de cada imagem.
- Fonte: geradas em 29/10/2026 no Higgsfield (GPT Image 2.5) a partir das caixas em português do shop (`consylion-shop-shelf/public/manuais/trilhas/<area>/caixa.jpg` e `public/manuais/combo/caixa.jpg`), trocando só o texto dourado da frente: o nome da área no idioma (MARKETING, SALES / VENTAS, OPERATIONS AND PRODUCT / OPERACIÓN Y PRODUCTO, FINANCE / FINANZAS, MANAGEMENT / GESTIÓN, BUSINESS OWNER / EL DUEÑO; na coleção, HANDBOOKS / MANUALES) e "TRILHA" por "SET" / "RUTA". A caixa, a faixa na cor da área e o lado com o "C" ficam iguais. A grafia de cada imagem foi conferida ampliada.

## Consylion Life: caixas das trilhas e do combo

- Layout: `life/trilhas/<categoria>/trilha-<categoria>-caixa.jpg` (uma caixa por categoria da Consylion Life: renda-e-patrimonio, saude-e-corpo, familia-e-relacionamentos, mente-e-habitos, sentido-e-espiritualidade, pets-e-hobbies) e `life/combo/consylion-life-combo-caixa.jpg` (os 100 manuais da Life). 1000×1000, JPG sRGB, até 300 KB. Preços: trilha R$ 297 e combo R$ 497 (decisão de 2026-11-01).
- Fonte: geradas em 01/11/2026 no Higgsfield (GPT Image 2.5) a partir das caixas em português do shop (`consylion-shop-shelf/public/manuais/trilhas/financeiro/caixa.jpg` para as trilhas e `public/manuais/combo/caixa.jpg` para o combo). Na frente: "CONSYLION LIFE™" no topo, o nome da categoria (no combo, "MANUAIS") e "TRILHA · PARA A SUA VIDA" (no combo, "PARA A SUA VIDA"). A faixa de baixo tem a cor da categoria, a do motor 2 (`mercados/life/producao/motor/design/tokens.json` do Infoprodutos-Direct-Response); no combo, as 6 cores. A grafia de cada imagem foi conferida ampliada.
- A publicação no shop, na Yampi e no LMS fica com os times de publicação.

## Marca

- `marca/consylion-logo-300x300.png`: o monograma da Consylion em 300×300 (PNG, creme sobre fundo escuro, ~15 KB), reduzido de `mercados/dinheiro/youtube/canal/logo-800x800.png` do repositório `Infoprodutos-Direct-Response`. Era a versão pensada para a fatura da Digistore24, que exige no mínimo 640×500; para lá, use a de 640×500. Entrou em 27/10/2026.
- Link direto: `https://raw.githubusercontent.com/altovalorcode/consylion-imagens/main/marca/consylion-logo-300x300.png`.
- `marca/consylion-logo-800x800.png`: o mesmo monograma em 800×800 (PNG), cópia de `mercados/dinheiro/youtube/canal/logo-800x800.png` do repositório `Infoprodutos-Direct-Response`. Entrou em 27/10/2026. Link direto: `https://raw.githubusercontent.com/altovalorcode/consylion-imagens/main/marca/consylion-logo-800x800.png`.
- `marca/consylion-logo-640x500.png`: o mesmo monograma em 640×500 (PNG, ~33 KB), o tamanho mínimo da imagem do logotipo do produtor na Digistore24. Recortado do fundo do 800×800 na proporção 640:500 e reduzido, sem esticar o desenho. Entrou em 27/10/2026. Link direto: `https://raw.githubusercontent.com/altovalorcode/consylion-imagens/main/marca/consylion-logo-640x500.png`.

## Consylion Life: manuais L001 a L100

- Layout igual ao da Série: `manuais/<slug>/<slug>-NN-<tipo>.jpg`, com o slug de venda do `dados/loja.json` (o L002 vende como `dinheiro-que-sobra`). 1000×1000, JPG sRGB, até 300 KB, as cenas 02 a 09 só com a página A4 inteira.
- Fonte: `life/<categoria>/LNNN-<slug>/saida/galeria-1000/` do repositório `altovalorcode/Consylion-Manuais`, gerada por `gerar_galeria_1000.py` do motor 2 (`mercados/life/producao/` no Infoprodutos-Direct-Response). Os links já estão no `dados/yampi.md` de cada título.
