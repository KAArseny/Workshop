
# Импортируем библиотеку vk_api
import vk_api
import wikipedia
wikipedia.set_lang("RU")
# Достаём из неё longpoll
from vk_api.longpoll import VkLongPoll, VkEventType

# Создаём переменную для удобства в которой хранится наш токен от группы

token = "f2cca1ade558b8d7bb39ef0b15771f226010d84f640436bb85c4b099b134eaef8ddc78f411420e06c5458"  # В ковычки вставляем аккуратно наш ранее взятый из группы токен.

# Подключаем токен и longpoll
bh = vk_api.VkApi(token=token)
give = bh.get_api()
longpoll = VkLongPoll(bh)


# Создадим функцию для ответа на сообщения в лс группы
def blasthack(id, text):
    bh.method('messages.send', {'chat_id': id, 'message': text, 'random_id': 0})


# Слушаем longpoll(Сообщения)



for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        # Чтобы наш бот не слышал и не отвечал на самого себя
        if event.to_me:

            # Для того чтобы бот читал все с маленьких букв

            # Получаем id пользователя
            id = event.chat_id

            # Доисторическая логика общения на ифах
            # Перед вами структура сообщений на которые бот сможет ответить, elif можно создавать сколько угодно, if и else же могут быть только 1 в данной ситуации.
            # if - если, else - иначе(значит бот получил сообщение на которое не вызвана наша функция для ответа)

            if event.text == 'Привет':
                blasthack(id, 'Ку!')
            elif event.text == 'Учёбы много':
                bh.method("messages.send", {"peer_id": 2000000000 + id, "attachment": "photo-210448461_457239018", "random_id": 0})

            elif event.text == 'Пока':
                blasthack(id, 'Хилимся-живём)')

            elif event.text == 'Смотри':
                bh.method("messages.send", {"peer_id": 2000000000+id, "attachment": "photo-210448461_457239020", "random_id": 0})

            elif event.text == 'Спокойной ночи':
                bh.method("messages.send", {"peer_id": 2000000000+id, "attachment": "photo-210448461_457239024", "random_id": 0})

            elif event.text == 'В чём смысл жизни?':
                bh.method("messages.send", {"peer_id": 2000000000 + id, "attachment": "photo-210448461_457239025", "random_id": 0})
            elif event.text == "Вики":
                blasthack(id,"Что ищем?)")
                for event in longpoll.listen():
                    if event.type == VkEventType.MESSAGE_NEW:
                        if event.to_me:
                            blasthack(id, "Держи инфу\n" + str(wikipedia.summary(event.text)))
                            break
                continue
            elif event.text == 'Как дела?':
                blasthack(id, "Жду Судного дня)))")
                