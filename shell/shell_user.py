from orcamentos.core.models import User

# definindo a senha padrão para todos os usuarios,
# como o django aceita apenas hash, criei uma senha padrão [password=1] e copiei o hash dela
# ou seja, para acessar cada uma das contas use como senha 1
hashpass = 'pbkdf2_sha256$12000$Pe4addAsDo1D$xEtHWLnSIVkEppr4pbK69SBhuLwWsSHdXyhkCZBNktA='

User.objects.create(
    username='amanda',
    first_name='Amanda',
    last_name='Santos',
    email='amanda@example.com',
    is_staff=True,
    password=hashpass
)
User.objects.create(
    username='caio',
    first_name='Caio',
    last_name='Gomes Oliveira',
    email='caio@example.com',
    is_staff=True,
    password=hashpass
)
User.objects.create(
    username='rebeca',
    first_name='Rebeca',
    last_name='Araujo Costa',
    email='rebeca@example.com',
    is_staff=True,
    password=hashpass
)
User.objects.create(
    username='douglas',
    first_name='Douglas',
    last_name='Cardoso Rodrigues',
    email='douglas@example.com',
    is_staff=True,
    password=hashpass
)
User.objects.create(
    username='jose',
    first_name='José',
    last_name='Carlos Frederico',
    email='jc@example.com',
    is_staff=True,
    password=hashpass
)
User.objects.create(
    username='alice',
    first_name='Alice',
    last_name='Cunha Santos',
    email='alice@example.com',
    is_staff=True,
    password=hashpass
)
User.objects.create(
    username='carla',
    first_name='Carla',
    last_name='Azevedo Santos',
    email='carla@example.com',
    is_staff=True,
    password=hashpass
)
User.objects.create(
    username='regis',
    first_name='Regis',
    last_name='da Silva Santos',
    email='regis@example.com',
    is_staff=True,
    is_superuser=True, password=hashpass
)
User.objects.create(
    username='adailton',
    first_name='Adailton',
    last_name='do Nascimento',
    email='adailton@example.com',
    is_staff=True,
    is_superuser=True, password=hashpass
)
