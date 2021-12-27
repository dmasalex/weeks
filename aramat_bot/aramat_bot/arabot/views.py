import telebot
from django.http import HttpResponseForbidden
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

API_TOKEN = '5081523960:AAFSpNT_9HhxOg2V0JQ6_Z385VbRZwI7670'

bot = telebot.TeleBot(API_TOKEN)


def index(requests):
    return HttpResponse('Отлично!')


@csrf_exempt
@require_http_methods(["POST"])
def webhook(request):
    if request.content_type == "application/json":
        update = telebot.types.Update.de_json(request.body.decode("utf-8"))
        try:
            bot.process_new_updates([update])
        except Exception as e:
            print("Error: {}".format(e))

        return HttpResponse('Неплохо для бота!')
    else:
        HttpResponseForbidden()


@bot.message_handler(commands=["whoami"])
def whoami(message):
    bot.send_message(message.chat.id, text="Your id: {}".format(message.from_user.id))
    bot.send_message(message.chat.id, text="Chat id: {}".format(message.chat.id))


@bot.message_handler(commands=["start"])
def start(message):
    name = message.from_user.username if message.from_user.username != '' else "незнакомец"
    bot.send_message(message.chat.id, text="Привет {}, пообщаемся?".format(name))


@bot.message_handler(content_types=['text'])
def callback_inline(message):
    bot.send_message(message.chat.id, text=message.text)





