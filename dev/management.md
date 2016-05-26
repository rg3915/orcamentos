## Comandos personalizados

Este projeto possui comandos personalizados


**Cria entrada**

```bash
$ python manage.py create_entry --priority='u' --category=1 --work='vila dos pães' --contact='Doris' --description='Lorem ipsum' --seller='regis'
$ python manage.py create_entry --work='tiree' --contact='alvin' --seller='regis'
```


**Lista as entradas urgentes**

```bash
$ python manage.py entrys -u
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


**Atualiza data de orçamentos**

```bash
$ python manage.py fix_created_orc
```