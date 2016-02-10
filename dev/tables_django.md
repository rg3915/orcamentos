### App: Core

**TimeStampedModel**
* created
* modified

**Address**
* address
* complement
* district
* city
* uf (list)
* cep

### App: CRM

**People(TimeStampedModel, Address)**
* gender (list)
* treatment (list)
* slug
* photo
* birthday
* company
* department
* cpf
* rg
* active (boolean)
* blocked (boolean)

**Phone**
* phone
* people (FK)
* phone_type (list)

**Person(People)**
* first_name
* last_name
* email
* occupation (FK)

**Customer(People)**
* first_name
* last_name
* email
* cnpj
* ie
* customer_type

**Employee(People)**
* user(o2o)
* occupation (FK)
* date_entry
* date_release

**Occupation**
* occupation

**Seller**
* employee (FK)
* internal(boolean)
* commissioned(boolean)
* commission


### App: Proposal

**Entry(TimeStampedModel)**
* priority (list)
* category (list)
* work (FK)
* person(contato) (FK)
* description
* seller (FK)
* is_entry(boolean)

**Work(Address)**
* name_work
* person(contato) (FK)
* customer(cliente) (FK)

**Proposal(TimeStampedModel)**
* num_prop
* prop_type ('R','OP')
* num_type_prop (0,1,2,...)
* category (list)
* description
* work (FK)
* person(contato) (FK)
* employee (FK)
* seller (FK)
* status (list)
* date_conclusion
* price
* obs

**Contract**
* proposal (o2o)
* contractor (FK)
* is_canceled (FK)

**NumLastProposal**
* num_last_prop
