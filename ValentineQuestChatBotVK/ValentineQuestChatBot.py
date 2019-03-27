import requests
import config
import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api import VkUpload

session = requests.Session()

# Hello world!

def write_msg(user_id, message):
    randID = random.randint(0, 100000)
    vk.method('messages.send', {'user_id': user_id, 'random_id':randID, 'message': message})

vk = vk_api.VkApi(token=config.token)
longpoll = VkLongPoll(vk)



upload = VkUpload(vk)
attachments = []

image_url = 'https://media.wired.com/photos/5b8477b61419cf3acdceed27/master/pass/How%20Technology%20Is%20Changing%20the%20Way%20We%20Love.jpg'
image = session.get(image_url, stream=True)
photo = upload.photo_messages(photos=image.raw)[0]
attachments.append(
    'photo{}_{}'.format(photo['owner_id'], photo['id'])
)

#doc = session.get("tickets.pdf", stream=True)

for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text

            # Каменная логика ответа
            if request.lower() == "привет":
                write_msg(event.user_id, config.task1)
            elif request.lower() == "ярославль":
                write_msg(event.user_id, config.task2)
            elif request.lower() == "суперсемейка 2":
                write_msg(event.user_id, config.task3)
            elif request.lower() == "льговское":
                write_msg(event.user_id, config.task4)

            elif request.lower() == "i love you":
                vk.method('messages.send', {'user_id': event.user_id,
                                            'random_id': random.randint(0, 100000),
                                              'message': "URL HERE"})

                vk.method('messages.send', {'user_id': event.user_id,
                                            'random_id': random.randint(0, 100000),
                                            'attachment': ','.join(attachments),
                                            'message': "Зайка, я люблю тебя!"})
            else:
                write_msg(event.user_id, "Ерунда какая то")
