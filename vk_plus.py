import vk_api


def send_message(token, to_id, message):
    try:
        api = vk_api.VkApi(token=token)
        api._auth_token()
        api.method('messages.send', {"message": message, "user_id": to_id})
        return None
    except vk_api.AuthorizationError as error_msg:
        print(error_msg)
        return error_msg