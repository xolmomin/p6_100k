import telebot
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views import View

from root import settings

# from apps.models import User

bot = telebot.TeleBot(settings.TELEGRAM_BOT_API_KEY)


# https://api.telegram.org/bot5510654090:AAHXbgV0WKFpWF5LyTbKJeWBTOAqh6s_iN4/setWebhook?url=https://247b-178-218-201-17.in.ngrok.io/bot/

class UpdateBot(View):
    def post(self, request):
        json_string = request.body.decode('UTF-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return JsonResponse({'code': 200})


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, 'shaxsiy kabinetdagi tokenni kiriting')


@bot.message_handler()
def start_message(message):
    # count = User.objects.filter(is_active=True).count()
    bot.send_message(message.from_user.id, f'Bazada aktiv userlar')
