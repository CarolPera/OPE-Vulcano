<h1 align="center"> OPE-Vulcano </h1>
<div align="center"><img height="150em" width="150em" src="https://down.imgspng.com/download/0720/volcano_PNG22.png"/></div> 


<h3> Sobre: </h3>

- Sistema de controle de fluxo de caixa e estoque para auxiliar microemprendedores;
- OPE: Oficiona Projeto Empresa, equivale ao trabalho de conclusão de curso da Faculdade Impacta.

## <h3> O que foi utilizdo:

- <a href="https://www.python.org/doc/">Python</a>
- <a href="https://docs.djangoproject.com/en/3.2/">Django</a>
- <a href="https://developer.mozilla.org/pt-BR/docs/Web/HTML">HTML</a>
- <a href="https://developer.mozilla.org/pt-BR/docs/Web/CSS">CSS</a>
- <a href="https://developer.mozilla.org/pt-BR/docs/Web/JavaScript">JavaScript</a>
- <a href="https://github.com/sqlitebrowser/sqlitebrowser/wiki">SQLite</a>

## <h3> Abrir o projeto e subir local:

- 1º : No CMD criar a maquina virtual dentro da pasta do projeto (OPE-Vulcano) -> `python -m venv venv`
- 2º : Ir até a pasta `Scripts` dentro da pasta `venv`-> `cd venv/Scripts` depois ativar a venv-> `activate`
- 3º : Voltar a raiz do projeto -> 2x `cd ..` e instalar o Django -> `pip install django`
- 4º : Fazer a migração do banco de dados caso tenha atualizações pendentes -> `python manage.py migrate`
- 5º : Rodar o servidor local -> `python manage.py runserver`
- 6º : Acessar a url `localhost:8000`