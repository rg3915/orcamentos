# Orçamentos

Python 3.5 e Django 1.10.3

## Objetivo

Sistema para controle de orçamentos.

Controla a sequência numérica dos orçamentos, seus valores e status.

Cadastro de clientes, obras e contatos.

## Live Demo

https://rg-orcamentos.herokuapp.com/

## Baixando e rodando a app

Baixe e rode o `setup.sh`.

```
wget https://raw.githubusercontent.com/rg3915/orcamentos/master/setup.sh
source setup.sh
```

Ou siga o passo a passo.

1. Clone o repositório
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
pip install -U pip # update the pip
pip install -r requirements/dev.txt
cp contrib/env-sample .env
make initial2
python manage.py test
```

## Convenções

Leia a wiki [convenções][13].

## Gerando dados randômicos

Para gerar dados randômicos veja o [Makefile](Makefile).

## Comandos personalizados

Veja os [comandos personalizados](dev/management.md).

## Changelog

Veja o [Changelog](CHANGELOG.md).

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
[13]: https://github.com/rg3915/orcamentos/wiki/Conven%C3%A7%C3%B5es
