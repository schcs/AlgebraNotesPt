## Descrição 

Este repositório contem [apostilas para várias disciplinas](https://schcs.github.io/AlgebraNotesPt/) na Programa de Graduação de Matemática na UFMG. As apostilas foram preparadas por [Csaba Schneider](https://schcs.github.io/WP/), exceto a apostila para Álgebra Linear I que foi originalmente escrita por [John McQuarrie](https://johnmacquarrie.github.io/).


Estas notas foram criadas com o intuito de serem lidas no formato `html` no browser do seu computador, 
tablet, ou no celular. No entanto, se alguém precisar, 
um arquivo PDF destas notas pode ser encontrado [neste link](https://github.com/schcs/AlgebraNotesPt/blob/main/_book/%C3%81lgebra.pdf).

## Compilação

Para compilar os documentos no seu próprio computador, siga as instruções abaixo. Elas foram 
testadas em Linux Mint 22.3 ou superior; em sistemas baseados em Debian (por exemplo, Ubuntu), 
o procedimento deve ser o mesmo, e em outras distribuições Linux deve ser semelhante. 
Infelizmente, não sei dizer como fazer isso no Windows ou no macOS. Se alguém conseguir 
instalar e compilar o projeto nesses sistemas, avise-me para que eu possa acrescentar 
instruções correspondentes.

Primeiro, instale o software necessário para criar os documentos.

```
sudo apt install git
```

Depois, faça o download do `Quarto` [na página do sistema](https://quarto.org/docs/download/), escolhendo a 
versão apropriada para a sua distribuição. Instale o `Quarto` com o seguinte comando 
(ajustando a versão, se necessário).  

```
sudo dpkg -i ~/Download/quarto-1.9-36-linux-amd64.deb
```

Em seguida, instale uma versão mínima de TeX para uso com o `Quarto` (isso é desnecessário se 
você já tiver uma instalação completa de TeX no seu computador).

```
quarto install tinytex
```

Para clonar o repositório, execute:

```
git clone https://github.com/schcs/AlgebraNotesPt.git
```

Para gerar as páginas `html`, basta entrar na pasta `AlgebraNotesPt` e executar o `Quarto`: 

```
cd AlgebraNotesPt
quarto render
```

As páginas `html` podem ser acessadas por meio do arquivo `_book/index.html`, na pasta do 
repositório. 

Para gerar o arquivo PDF, execute o `Quarto` da seguinte forma:

```
quarto render --profile pdf --to pdf
```

O arquivo `Álgebra.pdf` vai aparecer na pasta `_book`. **Como o conteúdo foi otimizado para o formato `html`, a formatação do `pdf` pode não ser ideal, especialmente 
próximo às imagens. 



## Licença

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

Material disponibilizado sob a licença
[CC BY-SA 4.0][cc-by-sa].

Para mais informação, veja o arquivo LICENCE.txt no repositório.

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg


