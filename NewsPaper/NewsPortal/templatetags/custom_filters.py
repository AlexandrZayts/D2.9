from django import template


register = template.Library()

list=[
    #Список нежелательных слов
]

@register.filter()
def censor(value):
    value.split()
    for l in list:
        if l in value.lower():
            value = value.replace(l, "*"*len(l))
    return value

