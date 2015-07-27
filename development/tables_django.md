**Address**
address
complement
district
city
uf
cep


**People(TimeStampedModel, Address)**
gender
treatment
first_name
last_name
company
department
email
phone1
phone2
phone3
cpf
rg
active (boolean)
blocked (boolean)


**Person(People)**
occupation (fk)


**Customer(People)**
type_customer
cnpj
ie
person (fk)


**Employee(People)**
user(o2o)
occupation (fk)
date_entry
date_release


**Occupation**
occupation


**Seller**
employee (fk)
internal(boolean)
commissioned(boolean)
commission


**Work(Address)**
name_work
person(contato) (fk)
customer(cliente) (fk)


**Entry(TimeStampedModel)**
priority
category (fk)
work (fk)
person(contato) (fk)
description
employee (fk)
seller (fk)
entry_ok(boolean)


**Proposal(TimeStampedModel)**
num_prop
type_prop ('R','OP')
num_type_prop (0,1,2,...)
category (fk)
description
work (fk)
person (fk) (contato)
employee (fk)
seller (fk)
status
date_conclusion
price
obs


**Category**
category


**LastProposal**
num_last_prop