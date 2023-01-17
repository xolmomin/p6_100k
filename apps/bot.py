import telebot
from django.http import JsonResponse
from django.views import View
from telebot.types import ReplyKeyboardMarkup

from apps.models import User
from apps.models.users import Ticket
from root import settings

bot = telebot.TeleBot(settings.BOT_TOKEN)


# https://api.telegram.org/bot{token}/setWebhook?url=https://b63f-178-218-201-17.eu.ngrok.io/bot/

class UpdateBot(View):
    def post(self, request):
        json_string = request.body.decode('UTF-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return JsonResponse({'code': 200})

    def get(self, request):
        return JsonResponse({'code': 200})


def get_current_user(message):
    return User.objects.get(id=message.from_user.id)


def is_current_user_active(message):
    try:
        User.objects.values('bot_is_activate').get(id=message.from_user.id)
        return True
    except Exception as e:
        return False


def get_active_user(message, activate_token):
    try:
        user = User.objects.get(bot_active_token=activate_token)
        return user
    except Exception as e:
        return


@bot.message_handler(commands=['start'])
def start_message(message):
    print('start')
    if is_current_user_active(message):
        bot.send_message(message.from_user.id, 'shaxsiy kabinetdagi tokenni kiriting')
    else:
        bot.send_message(message.from_user.id, "Assalom aleykum, 100k.uz botiga xush kelibsiz!\nBotdan to'liq foydalanish uchun /activate komandasi bilan botni aktivlashtiring.")


@bot.message_handler(commands=['activate'])
def start_active_message(message):
    print('activate')
    if is_current_user_active(message):
        bot.send_message(message.from_user.id, "Bot allaqachon aktivlashtirib bo'lingan!")
    else:
        send = bot.send_message(message.from_user.id,
                                "Aktivlashtirish kodini kiriting:\n"
                                "Kodni olish uchun 100k.uz saytiga kirib mening sozlamalarim' bo'limiga o'ting.")
        bot.register_next_step_handler(send, process_token_verification)


def active_user_from_token(message):
    try:
        user = User.objects.get(bot_active_token=message.text)
        return user
    except Exception as e:
        raise e


def get_activated_user(message):
    user = User.objects.get(telegram_id=message.from_user.id)
    return user


def process_token_verification(message):
    try:
        user = active_user_from_token(message)
        user.bot_is_activate = True
        user.telegram_id = message.from_user.id
        user.save()
        bot.send_message(message.from_user.id, 'Activlashdingiz')
    except Exception as e:
        bot.send_message(message.from_user.id, 'Xato activlash kodi')
        return start_active_message()


@bot.message_handler(commands=['profile'])
def profile_info(message):
    user = get_activated_user(message)
    bot.send_message(
        message.from_user.id,
        f"Profilingiz haqida malumotlar:\nId: {user.id},\nBonus: 0,"
        f"\nIsm: {user.fist_name},\nFamiliya: {user.last_name},\nTelefon / Login: {user.phone}"
    )


@bot.message_handler(commands=['newticket'])
def start_ticket_message(message):
    rkm = ReplyKeyboardMarkup(True, False)
    rkm.add('Xaridor', 'Kuryer', 'Admin', 'Sotuvchi')
    rkm.add('Boshqa')
    send = bot.send_message(message.from_user.id, 'Ticket kim tomonidan ochilmoqda?', reply_markup=rkm)
    bot.register_next_step_handler(send, ticket_author)


def ticket_author(message):
    if message.text in ['Xaridor', 'Kuryer', 'Admin', 'Sotuvchi', 'Boshqa']:
        new_ticket = Tickets.objects.create(author_id=message.from_user.id)
        new_ticket.sender = message.text

# @bot.message_handler()
# def start_message(message):
#     print('message')
#     # count = User.objects.filter(is_active=True).count()
#     bot.send_message(message.from_user.id, f'Bazada aktiv userlar')
