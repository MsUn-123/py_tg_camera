import telebot, time, cv2cam
import settings, markups

bot = telebot.TeleBot(settings.key)
host = settings.host
bootTime = time.time()
camera = cv2cam.CV2Camera()

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Welcome back!", reply_markup = markups.showMenu())

@bot.message_handler(func=lambda message: True)
def handle_message(message):
	if message.from_user.id == host:
		match message.text:
			case "Take frame":
				camera.get_frame()
				bot.send_photo(message.from_user.id, open("frame.png", "rb"), caption = "Here is your photo!", reply_to_message_id = message)
			case "Ping":
				reply = f"Pong!\nCur. uptime: {int(time.time() - bootTime)} secs...\nAnd counting!"
				bot.reply_to(message, reply, reply_markup = markups.showMenu())
			case "Test menu":
				bot.reply_to(message, "Under construction! ~Te-he!~", reply_markup = markups.showMenu())

bot.infinity_polling()

#stop using remote desktop Donk 