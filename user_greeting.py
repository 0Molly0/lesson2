from pywebio.input import input as pw_input
from pywebio.output import put_success, put_warning, toast, put_markdown
from pywebio.input import NUMBER

user_nikname = str(pw_input('Enter your nik', required=False)).title().strip()
# user_age = str(pw_input('Enter your age')).lstrip('0')
user_age = str(pw_input('Enter your age', type=NUMBER, required=True)).lstrip('-')

admin = 'Molly'
promouter = 'John'

is_admin = user_nikname == admin
is_promouter = user_nikname == promouter
is_other_user = (user_nikname != admin) and (user_nikname != promouter)
is_authority = is_admin or is_promouter

print(len(admin))

if is_admin:
    put_success('Hi, my cat')

elif user_nikname:
    put_success(f'Hello, {user_nikname}')

    if user_age.isdigit():
        put_success(f'I know, you are {user_age} years old')

else:
    put_warning('You have not entered nik. Shame on you, pal')

toast('Yep')

if is_promouter:
    put_markdown('Salt')

