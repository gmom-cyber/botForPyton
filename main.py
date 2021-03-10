import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor


def main():
    my_token = '3eb8b54644703cdcaa4f15851a1c5c154434ce801a03dca028ddc2f5fca83c8a8143e86f576fca3b7a294'
    vk_session = vk_api.VkApi(token=my_token)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    keyboard = VkKeyboard(one_time=False)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            print('New from {}, text = {}'.format(event.user_id, event.text))
            messange=event.text
if __name__ == '__main__':
    main()
