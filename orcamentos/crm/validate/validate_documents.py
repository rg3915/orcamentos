from django.core.exceptions import ValidationError


def cnpj(cnpj_document):
    cnpj_document = cnpj_document.replace('.', '')
    cnpj_document = cnpj_document.replace('/', '')
    cnpj_document = cnpj_document.replace('-', '')

    first_list = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    second_list = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    verifier = cnpj_document[-2:]

    if len(cnpj_document) != 14 and len(cnpj_document) > 0:
        raise ValidationError('Este CNPJ está incompleto.')

    id = 0
    add = 0

    for number in cnpj_document:
        try:
            first_list[id]
        except:
            break

        add += int(number) * int(first_list[id])
        id += 1

    add %= 11

    if add < 2:
        first_digit = 0
    else:
        first_digit = 11 - add

    first_digit = str(first_digit)

    id = 0
    add = 0

    for number in cnpj_document:
        try:
            second_list[id]
        except:
            break

        add += int(number) * int(second_list[id])
        id += 1

    add %= 11

    if add < 2:
        second_digit = 0
    else:
        second_digit = 11 - add

    second_digit = str(second_digit)

    if verifier != first_digit + second_digit:
        raise ValidationError('Este CNPJ é invalido.')
