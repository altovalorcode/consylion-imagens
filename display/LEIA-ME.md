# Imagens de Display e Demand Gen (Google Ads)

Imagens para anúncios responsivos de Display e Demand Gen, para o remarketing de quem visitou o shop e não comprou. Geradas em 23/10/2026.

## Arquivos

- `<CODIGO>-1200x628.png` (paisagem 1,91:1), `<CODIGO>-1200x1200.png` (quadrado 1:1) e `<CODIGO>-960x1200.png` (retrato 4:5).
- `LOGO-1200x1200.png` e `LOGO-1200x300.png`: o símbolo e "CONSYLION" em creme sobre o verde da marca (#1E3B2C), fundo sólido.
- Todas em PNG, sRGB (com perfil embutido) e com menos de 0,5 MB.

| Código | Produto | Gancho | Linha de confiança |
|---|---|---|---|
| MFC | Manual de Fluxo de Caixa e Lucro | Lucro no papel, caixa vazio? | Planilha pronta · Garantia de 7 dias |
| MCE | Manual de Compras e Estoque | Estoque parado é dinheiro parado | Planilha pronta · Garantia de 7 dias |
| MPS | Manual de Precificação de Serviços | Quanto cobrar pelo seu serviço? | Planilha pronta · Garantia de 7 dias |
| MPP | Manual de Precificação de Produtos | Custo vezes dois não é preço | Planilha pronta · Garantia de 7 dias |
| MPE | Manual de Persuasão | Cliente pergunta o preço e some? | Planilha pronta · Garantia de 7 dias |
| TRF | Trilha Financeiro (16 manuais) | 16 manuais de finanças | Pagamento único · Garantia de 7 dias |
| B100 | Biblioteca Business (100 manuais e 100 planilhas) | 100 manuais, 100 planilhas | Pagamento único · Garantia de 7 dias |

## Como foram feitas

- **Capa:** recortada da `-01-capa.jpg` da galeria de cada manual, em `manuais/<slug>/`. Na TRF vai uma pilha com 5 capas da área Financeiro. Na B100 vão 6 capas, uma de cada departamento.
- **Planilha na tela:** recortada da `-07-planilha.jpg` da galeria. O notebook é redesenhado no mesmo traço da galeria (`gerar_galeria_1000.py` do Infoprodutos-Direct-Response).
  - A TRF usa a planilha do Manual de Orçamento Empresarial; a B100, a do Manual de Vendas.
  - O MPS usa a aba "Painel mensal" do PDF da planilha real (`planilha-custo-hora-margem-reajuste.pdf`, Consylion-Manuais), porque a imagem da galeria deixa meia tela vazia.
- **Texto:** o gancho vai em Newsreader, o nome do produto em Geist e a linha de confiança em Geist Mono, na cor ouro. O texto ocupa de 5,6% a 10,1% da área de cada imagem. Tudo, inclusive o logo e o visual, fica dentro da margem de 5%.
- **Conteúdo:** as frases da linha de confiança foram conferidas na página de cada produto em 23/10/2026. As imagens não têm preço, desconto, selo, depoimento nem botão desenhado.
- **A Trilha Financeiro não tem página própria no shop** (`/produto/trilha-financeiro` dá 404). A oferta aparece dentro de cada manual da área Financeiro.
