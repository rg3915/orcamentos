
Python 3.4 e Django 1.8.2

# Objetivo

Sistema para controle de orçamentos.

Controla a sequência numérica dos orçamentos, seus valores e status.

Cadastro de clientes, obras e contatos.

# Baixando e rodando a app

	git clone https://github.com/rg3915/orcamentos.git
	virtualenv -p python3 orcamentos
	cd orcamentos
	source bin/activate
	PS1="(`basename \"$VIRTUAL_ENV\"`):/\W$ " # opcional
	pip install -r requirements.txt
	make initial
	./manage.py runserver

# Convenções

**Título de entidades**: primeira maiúscula e no singular. Ex: *Person, Employee, Seller, Proposal, Entry*.

**Classes**: em nomes compostos maiúscula e juntas. Ex: *PersonCreate, PersonList, PersonDetail* ([PEP 8][4]).

**Funções**: nomes compostos minúsculos e separados com underline. Ex: *is_entry* ([PEP 8][4]).

**Templates**: usar a mesma convenção. Ex: *person_list.html, person_detail.html, person_create_form.html*.

# Gerando dados randômicos

Para gerar dados randômicos veja o Makefile.

# Comandos personalizados

Este projeto possui comandos personalizados

	$ ./manage.py entradas --urgentes


[1]: http://django-extensions.readthedocs.org/en/latest/
[4]: http://www.python.org.br/wiki/GuiaDeEstilo
[8]: http://django-notes.blogspot.com.br/2012/07/vizualization.html
[9]: http://latexbr.blogspot.com.br/
[10]: https://bitbucket.org/pavel_calado/tikz-er2/wiki/Home
[11]: http://grandeportal.blogspot.com.br/2012/06/editando-imagens-no-imagemagick.html
[12]: http://perso.ensta-paristech.fr/~kielbasi/tikzuml/index.php?lang=en

