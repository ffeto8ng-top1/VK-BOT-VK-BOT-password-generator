import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import random
import string

# Вставь сюда свои данные
TOKEN = "vk1.a.iZDwkpBUK9xcju7RVrpsffu7k7JbvXVW4Z-d_hZ9vaT26iGbVPM92BRLjLqnRBTQUSjczNsOirkHCdN7HGgd19YvtP7tXHBtQqgejmK0an8eMCuccKE3Xg7b871eJj8P7MTxLB3Fo_uLfOejROTInoesWT8LoOZouA72bxK1GCWuy-G_2sDaa0KM7uy6GtSkvlTB8RE4_xKi-gGEvnmHug"
GROUP_ID = 123456789  # ID твоего сообщества (без минуса)

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%"
    return "".join(random.choice(chars) for _ in range(length))

vk_session = vk_api.VkApi(token=TOKEN)
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

print("Бот запущен...")

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        user_id = event.user_id
        text = event.text.strip().lower()

        response = ""

        if text in ["привет", "хай", "здравствуй"]:
            response = "Привет! Чем могу помочь? Напиши /help, чтобы увидеть команды."

        elif text == "/help":
            response = (
                "Команды:\n"
                "/help — показать список команд\n"
                "/password — сгенерировать пароль\n"
                "Просто напиши «привет», если хочешь поболтать."
            )

        elif text == "/password":
            pwd = generate_password()
            response = f"Твой пароль: {pwd}\n(сохрани его в надёжном месте!)"

        else:
            response = "Я пока немного умею, но учусь! Попробуй /help."

        # Отправляем ответ
        vk.messages.send(
            user_id=user_id,
            message=response,
            random_id=0  # random_id нужен, чтобы не дублировать сообщения
        )
