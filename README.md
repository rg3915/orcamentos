# Orçamentos

Python 3.5 e Django 1.9.1

## Objetivo

Sistema para controle de orçamentos.

Controla a sequência numérica dos orçamentos, seus valores e status.

Cadastro de clientes, obras e contatos.

## Baixando e rodando a app

Baixe e rode o `setup.sh`.

```
wget https://raw.githubusercontent.com/rg3915/orcamentos/master/setup.sh
source setup.sh
```

Ou siga o passo a passo.

1. Clone o repositório.
2. Crie um virtualenv com Python 3.5
3. Ative o virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Carregue os dados no banco
7. Execute os testes.

```bash
git clone https://github.com/rg3915/orcamentos.git
cd orcamentos
python -m venv .venv
source .venv/bin/activate
PS1="(`basename \"$VIRTUAL_ENV\"`):/\W$ " # opcional
pip install -r requirements-dev.txt
cp contrib/env-sample .env
make initial2
python manage.py test
```

## Convenções

**Título de entidades**: primeira maiúscula e no singular. Ex: *Person, Employee, Seller, Proposal, Entry*.

**Classes**: em nomes compostos maiúscula e juntas. Ex: *PersonCreate, PersonList, PersonDetail* ([PEP 8][4]).

**Funções**: nomes compostos minúsculos e separados com underline. Ex: *is_entry* ([PEP 8][4]).

**Templates**: usar a mesma convenção. Ex: *person_list.html, person_detail.html, person_form.html*.

## Gerando dados randômicos

Para gerar dados randômicos veja o [Makefile](https://github.com/rg3915/orcamentos/blob/master/Makefile).

## Comandos personalizados

Este projeto possui comandos personalizados


**Cria entrada**

```bash
$ python manage.py create_entry --priority='u' --category=1 --work='vila dos pães' --contact='Doris' --description='Lorem ipsum' --seller='regis'
$ python manage.py create_entry --work='tiree' --contact='alvin' --seller='regis'
```


**Lista as entradas urgentes**

```bash
$ python manage.py entrys --u
```

**Cria orçamento**

```bash
$ python manage.py create_proposal --user='regis' --id=1
```


**Concluir orçamento**

```bash
$ python manage.py conclude_proposal --num=1 --price=14350.09
```


**Cria contrato**

```bash
$ python manage.py create_contract --num=1
```


## [Changelog](https://github.com/rg3915/orcamentos/blob/master/CHANGELOG.md)


### Auto Flake

```bash
autoflake --in-place --remove-unused-variables file.py
```

[1]: http://django-extensions.readthedocs.org/en/latest/
[4]: http://www.python.org.br/wiki/GuiaDeEstilo
[8]: http://django-notes.blogspot.com.br/2012/07/vizualization.html
[9]: http://latexbr.blogspot.com.br/
[10]: https://bitbucket.org/pavel_calado/tikz-er2/wiki/Home
[11]: http://grandeportal.blogspot.com.br/2012/06/editando-imagens-no-imagemagick.html
[12]: http://perso.ensta-paristech.fr/~kielbasi/tikzuml/index.php?lang=en