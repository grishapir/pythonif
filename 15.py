n=''
while n!='конец':
    print('Введите название страны:')
    n=input()
    r='Вас поздравляет'
    if n=='Россия':
        print(r,'Дед Мороз из России:"С новым годом!"')
    elif n=='Италия':
        print(r,'Бабо Натале из Италии"Feliceannonuovo"')
    elif n=='Татарстан':
        print(r,'Кышбабай из татарстана:"Яңа ел белән"')
    elif n=='Финляндия':
        print(r,'Йоулупукки из Финляндии:"OnnellistaUuttaVuotta"')
    elif n=='Норвегия':
        print(r,'Юлебук из Норвегии:"GodtNyttar"')
    elif n=='ВБ':
        print(r,'Фазеркристмас из ВБ:"HappyNewYear"')
    elif n=='конец':
        break
    else:
        print('Нет данных по этой стране')
print('Спасибо за внимание!')