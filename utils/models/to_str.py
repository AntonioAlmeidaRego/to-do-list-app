def str_choices_color(instance):
    v = instance.type_color
    if v == 1:
        return 'Amarelo'
    elif v == 2:
        return 'Azul'
    elif v == 3:
        return 'Cinza'


def str_choices_model(instance):
    v = instance.type_model
    if v == 1:
        return 'Hatch'
    elif v == 2:
        return 'Sedan'
    elif v == 3:
        return 'Convertible'
