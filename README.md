# projeto-semestral-nicolas-anelli

## Documentação

Toda documentação desse projeto poderá ser encontrada em arquivos markdown [aqui](./_doc).


## Ambiente de desenvolvimento

O que eu preciso instalar pra rodar esse app?
```
sudo apt-get install python3
  $ pip3 install django
  $ pip3 install django-active-link
  $ pip3 install django-summernote
  $ pip3 install pillow
```

Comandos para configurar um novo ambiente de desenvolviemtno:
```
  $ cd src
  $ python3 manage.py migrate
  $ python3 manage.py createsuperuser  # admin, admin@email.com, admin, admin, y
  $ python3 manage.py runserver
```
Acessar: [localhost:8000/admin](http://localhost:8000/admin) 

Usuário: admin/admin


## Ambiente de exemplo

Dentro da pasta _sample existe uma configuração inicial com banco de dados, diversos dados cadastrado e imagens.

Para utilizar esse ambiente basta mover o conteúdo da pasta _sample para a pasta src.

Dessa forma você terá a ficará com a seguinte estrutura:
- _doc
- _sample
- .vscode
- prototipo
- src
  - app
  - media <<<
  - mysite
  - db.sqlite3
  - manage.py <<<

Por fim basta iniciar o servidor como mostrado no ambiente de desenvolvimento.
