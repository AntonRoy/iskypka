import vk_api
import random


def send_message(token, to_id, message):
    api = vk_api.VkApi(token=token)
    api._auth_token()
    api.method('messages.send', {"message": message, "user_id": to_id, "random_id": str(random.randint(1, 100000000))})