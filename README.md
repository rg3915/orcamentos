# Orçamentos

Python 3.5 e Django 1.9.1

## Objetivo

Sistema para controle de orçamentos.

Controla a sequência numérica dos orçamentos, seus valores e status.

Cadastro de clientes, obras e contatos.

## Baixando e rodando a app

```bash
git clone https://github.com/rg3915/orcamentos.git
python -m venv .venv
source .venv/bin/activate
cd orcamentos
PS1="(`basename \"$VIRTUAL_ENV\"`):/\W$ " # opcional
pip install -r requirements.txt
make initial
./manage.py test
./manage.py runserver
```

## Convenções

**Título de entidades**: primeira maiúscula e no singular. Ex: *Person, Employee, Seller, Proposal, Entry*.

**Classes**: em nomes compostos maiúscula e juntas. Ex: *PersonCreate, PersonList, PersonDetail* ([PEP 8][4]).

**Funções**: nomes compostos minúsculos e separados com underline. Ex: *is_entry* ([PEP 8][4]).

**Templates**: usar a mesma convenção. Ex: *person_list.html, person_detail.html, person_create_form.html*.

## Gerando dados randômicos

Para gerar dados randômicos veja o [Makefile](https://github.com/rg3915/orcamentos/blob/master/Makefile).

## Comandos personalizados

Este projeto possui comandos personalizados


**Cria entrada**

```bash
$ ./manage.py create_entry --priority='u' --category=1 --work='vila dos pães' --contact='Doris' --description='Lorem ipsum' --seller='regis'
$ ./manage.py create_entry --work='tiree' --contact='alvin' --seller='regis'
```


**Lista as entradas urgentes**

```bash
$ ./manage.py entrys --u
```

**Cria orçamento**

```bash
$ ./manage.py create_proposal --user='regis' --id=1
```


**Concluir orçamento**

```bash
$ ./manage.py conclude_proposal --num=1 --price=14350.09
```


**Cria contrato**

```bash
$ ./manage.py create_contract --num=1
```


## [Changelog](https://github.com/rg3915/orcamentos/blob/master/CHANGELOG.md)


[1]: http://django-extensions.readthedocs.org/en/latest/
[4]: http://www.python.org.br/wiki/GuiaDeEstilo
[8]: http://django-notes.blogspot.com.br/2012/07/vizualization.html
[9]: http://latexbr.blogspot.com.br/
[10]: https://bitbucket.org/pavel_calado/tikz-er2/wiki/Home
[11]: http://grandeportal.blogspot.com.br/2012/06/editando-imagens-no-imagemagick.html
[12]: http://perso.ensta-paristech.fr/~kielbasi/tikzuml/index.php?lang=en