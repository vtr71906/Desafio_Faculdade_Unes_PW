<h1 align="center"> Desafio da Universidade UNES</h1>


# :mag_right: Índice

* [Sobre o Desafio](#sobre)
* [Como Usar](#comoUsar)
* [Ferramentas Utilizadas](#ferramentas)

<span id="sobre"></span>

# Sobre o Desafio

Deverá ser feito um site semelhante ao protótipo do PDF, encontrado em  ```doc/```, utilizando somente as linguagens de marcação "<a href="https://www.w3schools.com/html/">HTML</a>" e "<a href="https://www.w3schools.com/css/">CSS</a>".

![print_faculdadeUnes](https://github.com/BrunoSerpa/Desafio_Faculdade_Unes_PW/blob/main/Doc/faculdadeUnes.gif?raw=true)

<span id="comoUsar"></span>

# Como Usar

<details>
  <summary><b>O que será necessário:</b></summary>

  - <a href="https://git-scm.com/downloads">Git</a> Será necessário o git para fazer uma clonagem do repositório.
</details>

<details>
  <summary><b>Clonando o repositório:</b></summary>
  
  1º Passo: Crie uma pasta vazia.

  2º Passo: Entre na pasta criada e clique no diretório na parte superior e digite cmd:

  ![print_passo2](https://github.com/BrunoSerpa/Desafio_Faculdade_Unes_PW/blob/main/Doc/Passo2.PNG?raw=true)

  3º Passo: Dentro do cmd insira o comando:
 
  `git clone "https://github.com/BrunoSerpa/Desafio_Faculdade_Unes_PW" .`
</details>


<details>
  <summary><b>Rodando Desafio:</b></summary>

  1° Passo: Dentro do Cmd criado em "Clonando o repositório" insira os comandos:
  
  `cd src`

  `py -m venv venv`
  >Caso os comando não funcionar, troque a palavra python do comando  por <b>py3</b>. 

  >> OBS: Se o seu python não for da versão  3.11.2 é possível os comandos não funcionarem. Para instalar a versão desejada <a href="https://www.python.org/downloads/release/python-3112/">Clique Aqui</a> ou vá para o site oficial da linguagem.

  2º Passo: Entre na sua Máquina Virtual com o comando:

  `.\venv\Scripts\activate`

  6º Passo: Instale os requerimentos com o comando:

  `pip install -r requirements.txt`

  7º Passo: Acesse o projeto com o comando:  (Isso executará o `app.py` e será possível ver o site funcional).

  `flask run`

  8º Passo: Quando finalzar insira o comando no cmd: (Isso vai parar o venv)

  `deactivate`

</details>

<span id="ferramentas"></span>

# Ferramentas Utilizadas

<a href="https://www.w3schools.com/html/">HTML</a>: Estruturação das páginas.<br/> Foram utilizados: `a`, `b`, `br`, `div`, `form`, `footer`, `img`, `hr`, `h1`, `input`, `li`, `nav`, `ol`, `p`, `section` e `textarea`.

<a href="https://www.w3schools.com/css/">CSS</a>: Estilização de todas as páginas.<br/>
Foram utilizados tags e classes que mudam de acordo com seu estado.