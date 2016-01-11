**TimeStampedModel**
created
modified

**Address**
address
complement
district
city
uf
cep

**MyUser**
first_name
last_name
email


**People(TimeStampedModel, Address)**
gender
treatment
company
department
phone1
phone2
phone3
cpf
rg
active (boolean)
blocked (boolean)


**Person(People)**
occupation (FK)


**Customer(MyUser, People)**
cnpj
ie
type_customer


**Employee(People)**
user(o2o)
occupation (FK)
date_entry
date_release


**Occupation**
occupation


**Seller**
employee (FK)
internal(boolean)
commissioned(boolean)
commission


**Entry(TimeStampedModel)**
priority
category (FK)
work (FK)
person(contato) (FK)
description
seller (FK)
is_entry(boolean)

**Category**
category

**Work(Address)**
name_work
person(contato) (FK)
customer(cliente) (FK)

**Proposal(TimeStampedModel)**
num_prop
type_prop ('R','OP')
num_type_prop (0,1,2,...)
category (FK)
description
work (FK)
person (FK) (contato)
employee (FK)
seller (FK)
status
date_conclusion
price
obs

**Contract**
proposal (o2o)
contractor (FK)
is_canceled (FK)

**NumLastProposal**
num_last_prop

15