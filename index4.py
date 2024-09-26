lang = input('your language? en, ru')
time_zone = input('what is the time?:''morning'' day'' evening')
if lang == 'en':
    if time_zone == 'morning':
        print('good morning!')
    elif time_zone == 'day':
        print(' good day!')
    elif time_zone == 'evening':
        print(' good evening!')
if lang == 'ru':
    if time_zone == 'morning':
        print('добрый утра!!')
    elif time_zone == 'day':
        print(' добрый день!')
    elif time_zone == 'evening':
        print(' добрый ночь!')
if lang == 'кы':
    if time_zone == 'morning':
        print('куттуу тан!!')
    elif time_zone == 'day':
        print(' куттуу кун!')
    elif time_zone == 'evening':
        print(' куттуу кеч!')

else:
    print('пишите провельно')
