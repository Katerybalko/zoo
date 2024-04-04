import telebot
import requests
from telebot import types




TOKEN = '7128809277:AAH9BUIYRr4EXWN9fl1NzrjJMjBRYiVfUkA'
bot = telebot.TeleBot(TOKEN)

class ConvertionExeption(Exception):
    pass

@bot.message_handler(commands=['start'])
def handle_start(message):
    keyboard = types.ReplyKeyboardMarkup(row_width=1)
    button1 = types.KeyboardButton('Узнай своего внутреннего зверя!')
    button2 = types.KeyboardButton('Стань опекуном для животного')
    button3 = types.KeyboardButton('Контакты')
    button4 = types.KeyboardButton('Связаться с работником зоопарка')
    keyboard.add(button1, button2, button3, button4)
    bot.send_photo(message.chat.id, photo='https://i.postimg.cc/MZcsYQCt/MZoo-logo-ircle-small-preview.jpg', caption=f"Рады приветствовать тебя, {message.chat.first_name}, в телеграм-ботe"
                                                                                             "\nМосковского зоопарка!\n"
                                                                                             "Выбирай кнопку и вперед! ", reply_markup=keyboard)
@bot.message_handler(commands=['choose'])
def choose(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup.add(types.InlineKeyboardButton(text='Камышовый кот', callback_data='cat'),
               types.InlineKeyboardButton(text='Золотистый тамарин', callback_data='tamarine'),
               types.InlineKeyboardButton(text='Шакал', callback_data='tiger'))
    bot.send_photo(message.chat.id, 'https://i.postimg.cc/MZcsYQCt/MZoo-logo-ircle-small-preview.jpg',
                   'Сейчас в Московском зоопарке содержится около 6 000 особей, относящихся примерно к 1 100 биологическим видам мировой фауны. '
                   '\n \nКаждое животное уникально и неповторимо. Взять под опеку можно животное, которое вам нравится и соответствует вашим финансовым возможностям.'
                   '\n \nСтоимость опеки рассчитывается из ежедневного рациона питания животного.'
                   '\n \nВыберите животное и отправьте запрос нам на почту', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data in ['cat', 'tamarine', 'tiger'])
def callback_query1(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    if call.data == 'cat':
        bot.send_photo(call.message.chat.id, photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkSJV6p6fDwT6GEJxHX2TmfNXaoX6NBCptoVRUr5XJgg&stext=',
                       caption='Камышовый кот крупнее любой домашней кошки: длина туловища - от 60 до 90 см, хвоста - 30-35 см.'
                 'Камышового кота не зря ещё называют болотной рысью - у него схожая с евразийской рысью окраска и чёрные кисточки на ушах.'
                 '\n \nОтправьте свой запрос на почту')
        bot.send_message(call.message.chat.id, 'zoofriends@moscowzoo.ru', parse_mode='html')
    elif call.data == 'tamarine':
        bot.send_photo(call.message.chat.id, photo='https://moscowzoo.ru/upload/resize_cache/iblock/447/350_350_1/447cd1f07180e63285dc96beeaa93344.jpg', caption='Вид находится под угрозой исчезновения'
                               '\n \nВ природе этих чудных обезьянок осталось немногим более 3000, ещё около 500 содержатся в зоопарках мира.'
                               'К сожалению, численность их в природе продолжает снижаться.\n \nОтправь свой запрос на почту')
        bot.send_message(call.message.chat.id, 'zoofriends@moscowzoo.ru', parse_mode='html')
    else:
        bot.send_photo(call.message.chat.id,
                       photo='https://moscowzoo.ru/upload/resize_cache/iblock/40f/350_350_1/40f135ade86add552dde32100a077088.jpg',
                       caption='Этот зверь часто живёт рядом с человеком, '
                               'кормится возле него, подбирает пищевые отходы, нападает на домашний скот и птицу. '
                               'Шакал хитрый и даже нахальный зверь. По степени дерзости нападений на птичники он превосходит лисиц.'
                               ' Вместе с тем, шакал довольно для человека не опасен\n \nОтправь свой запрос на почту')
        bot.send_message(call.message.chat.id, 'zoofriends@moscowzoo.ru', parse_mode='html')


@bot.message_handler(commands=['quize'])
def quize1(message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    markup.add(types.InlineKeyboardButton(text='Быстрый', callback_data='fast'),
               types.InlineKeyboardButton(text='Маленький', callback_data='small'),
               types.InlineKeyboardButton(text='Смелый', callback_data='brave'))
    bot.send_message(message.chat.id, text='Какой ты?', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in ['fast', 'small', 'brave'])
def quiz2(call):
    if call.data == 'fast' or 'small' or 'brave':
        markup = types.InlineKeyboardMarkup(row_width=3)
        markup.add(types.InlineKeyboardButton(text='Птицу', callback_data='bird'),
                   types.InlineKeyboardButton(text='Фрукты', callback_data='frts'),
                   types.InlineKeyboardButton(text='Мясо', callback_data='meat'))
        bot.send_message(call.message.chat.id, text='Что ты любишь есть?', reply_markup=markup)
    else:
        none

@bot.callback_query_handler(func=lambda call: call.data in ['bird', 'frts', 'meat'])
def quize3(call):
    if call.data == 'bird' or 'frts' or 'meat':
        markup = types.InlineKeyboardMarkup(row_width=3)
        markup.add(types.InlineKeyboardButton(text='Мурлкание', callback_data='mrr'),
                   types.InlineKeyboardButton(text='Писк', callback_data='pii'),
                   types.InlineKeyboardButton(text='Рев', callback_data='arr'))
        bot.send_message(call.message.chat.id, text='Какие звуки чаще всего издаешь?', reply_markup=markup)
    else:
        none

@bot.callback_query_handler(func=lambda call: call.data in ['mrr', 'pii', 'arr'])
def quize_rez(call):
    if call.data == 'mrr':
        bot.send_photo(call.message.chat.id,
                       photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkSJV6p6fDwT6GEJxHX2TmfNXaoX6NBCptoVRUr5XJgg&stext=',
                       caption=f'Поздравляем! Вы - Камышовый кот!\n \n Чтобы получить больше информации про опеку нажми\n/choose'
                               '\n \nДелись этим фото в соцсетях! Удерживай палец на фото, за тем нажми "выбрать" и внизу выбери значок "поделиться".')
    elif call.data == 'pii':
        bot.send_photo(call.message.chat.id,
                       photo='https://moscowzoo.ru/upload/resize_cache/iblock/447/350_350_1/447cd1f07180e63285dc96beeaa93344.jpg',
                       caption='Поздравляем! Вы -Золотистый тамарин!\n \nЧтобы получить больше информации про опеку нажми\n/choose'
                               '\n \nДелись этим фото в соцсетях! Удерживай палец на фото, за тем нажми "выбрать" и внизу выбери значок "поделиться".')
    else:
        bot.send_photo(call.message.chat.id,
                       photo='https://moscowzoo.ru/upload/resize_cache/iblock/40f/350_350_1/40f135ade86add552dde32100a077088.jpg',
                       caption='Поздравляем! Вы - шакал!\n \nЧтобы получить больше информации про опеку нажми\n/choose'
                               '\n \nДелись этим фото в соцсетях! Удерживай палец на фото, за тем нажми "выбрать" и внизу выбери значок "поделиться".')



@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == 'Контакты':
        bot.send_message(message.chat.id, 'Контакты можно найти по ссылке:\nhttp://moscowzoo.ru/about-zoo/contacts/')
    elif message.text == 'Стань опекуном для животного':
        bot.send_message(message.chat.id, ' Участие в программе «Возьми животное под опеку» — это ваш личный вклад в дело сохранения биоразнообразия Земли и развитие нашего зоопарка.\n \nОсновная задача Московского зоопарка с самого начала его существования это — сохранение биоразнообразия нашей планеты.\n \nКогда вы берете под опеку животное, вы помогаете нам в этом благородном деле. '
                                          'При нынешних темпах развития цивилизации к 2050 году с лица Земли могут исчезнуть около 10 000 биологических видов.\n'
                                          'Московский зоопарк вместе с другими зоопарками мира делает все возможное, чтобы сохранить их. '
                                          '\n \n Опека — это прекрасная возможность принять участие в деле сохранения редких видов, помочь нам в реализации природоохранных программ. '
                                          '\n \nПрограмма «Возьми животное под опеку» дает возможность опекунам ощутить свою причастность к делу сохранения природы, участвовать в жизни Московского зоопарка и его обитателей, видеть конкретные результаты своей деятельности. '
                                          '\n \nОпекать – значит помогать любимым животным.\n \nДавай перейдем к выбору животного. Жми/choose')
    elif message.text == 'Связаться с работником зоопарка':
        bot.send_contact(message.chat.id, phone_number='+380687660934', first_name='Екатерина' )
    elif message.text == 'Узнай своего внутреннего зверя!':
         bot.reply_to(message, 'Нажми /quize')
    else :
        bot.reply_to(message, 'Я тебя не совсем понял.\nДавай попробуем заново\nЖми /start')




bot.polling()



