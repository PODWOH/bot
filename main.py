import telebot
import psycopg2
import datetime

tooday = datetime.datetime.today().strftime('%w')


conn = psycopg2.connect(database="bot", user="postgres", password="1234",  host="localhost",   port="5432")
cursor = conn.cursor()

token = "2116521918:AAFc1SMTpoGUejNMJ8pi_axGK9C0XB95gDo"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=('letsgo'))
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row('/start')
    bot.send_message(message.chat.id, "Press /start to start", reply_markup=keyboard)


@bot.message_handler(commands=('start'))
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup()
    keyboard.row("monday", "tuesday", "wednesday")
    keyboard.row("thusday", "friday", "this week", "next week")
    keyboard.row("/mtuci", "/help")
    bot.send_message(message.chat.id, "Hello. What you want for today?", reply_markup=keyboard)

@bot.message_handler(commands=('help'))
def help(message):
    bot.send_message(message.chat.id, "I dead")


@bot.message_handler(commands=('week'))
def help(message):
    if int(tooday) % 2 == 0:
        bot.send_message(message.chat.id, "week is up")
    else:
        bot.send_message(message.chat.id, "week is down")


@bot.message_handler(commands=('mtuci'))
def help(message):
    bot.send_message(message.chat.id, "https://mtuci.ru/")

@bot.message_handler(commands=('prikol'))
def help(message):
    bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=G61ONwL5vh8")



@bot.message_handler(content_types=('text'))
def answer(message):
    if int(tooday) % 2 == 0:
        if  message.text.lower() == 'monday':
            cursor.execute("SELECT  full_name FROM teacher where id in (10,9,8)")
            rec = list(cursor.fetchall())
            for i in range(len(rec)):
                rec[i]
                m = (str(rec[i - 2]) + '\n')
                n = (str(rec[i - 1]) + '\n')
                b = (str(rec[i]) + '\n')
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day = 'Monday';")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                a = (str(records[i - 2]) + '\n')
                p = (str(records[i - 1]) + '\n')
                t = (str(records[i]) + '\n')
                e = a + b + '\n' + p + n + '\n' + t + m + '\n'
            bot.send_message(message.chat.id, 'week is up')
            bot.send_message(message.chat.id, e)
        elif message.text.lower() == 'tuesday':
            cursor.execute("SELECT  full_name FROM teacher where id in (3,1,6)")
            rec = list(cursor.fetchall())
            for i in range(len(rec)):
                rec[i]
                m = (str(rec[i - 2]) + '\n')
                n = (str(rec[i - 1]) + '\n')
                b = (str(rec[i]) + '\n')
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day in ('Tuesday', 'uTuesday');")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                a = (str(records[i - 3]) + '\n')
                p = (str(records[i - 2]) + '\n')
                t = (str(records[i - 1]) + '\n')
                c = (str(records[i]) + '\n')
                e = a + n +'\n' + p + n + '\n' + t +m+ '\n' + c + b + '\n'
            bot.send_message(message.chat.id, 'week is up')
            bot.send_message(message.chat.id, e)
        elif message.text.lower() == 'wednesday':
            cursor.execute("SELECT  full_name FROM teacher where id in (10,7)")
            rec = list(cursor.fetchall())
            for i in range(len(rec)):
                rec[i]
                n = (str(rec[i - 1]) + '\n')
                b = (str(rec[i]) + '\n')
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day in ('uWednesday', 'Wednesday');")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                t = (str(records[i - 1]) + '\n')
                c = (str(records[i]) + '\n')
                e = t + b +'\n' + c + n + '\n'
            bot.send_message(message.chat.id, 'week is up')
            bot.send_message(message.chat.id, e)
        elif message.text.lower() == 'thusday':
            cursor.execute("SELECT  full_name FROM teacher where id in (2,3,9)")
            rec = list(cursor.fetchall())
            for i in range(len(rec)):
                rec[i]
                m = (str(rec[i - 2]) + '\n')
                n = (str(rec[i - 1]) + '\n')
                b = (str(rec[i]) + '\n')
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day in ('uThusday');")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                a = (str(records[i - 3]) + '\n')
                p = (str(records[i - 2]) + '\n')
                t = (str(records[i - 1]) + '\n')
                c = (str(records[i]) + '\n')
                e = a + m+'\n' + p +n+ '\n' + t +n+ '\n' + c +b
            bot.send_message(message.chat.id, 'week is up')
            bot.send_message(message.chat.id, e)
        elif message.text.lower() == 'friday':
            cursor.execute("SELECT  full_name FROM teacher where id in (7,5)")
            rec = list(cursor.fetchall())
            for i in range(len(rec)):
                rec[i]
                n = (str(rec[i - 1]) + '\n')
                b = (str(rec[i]) + '\n')
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day in ('Friday');")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                t = (str(records[i - 1]) + '\n')
                c = (str(records[i]) + '\n')
                e = t +b+ '\n' + c +n+ '\n'
            bot.send_message(message.chat.id, 'week is up')
            bot.send_message(message.chat.id, e)
        else:
            bot.send_message(message.chat.id, "I dont ponimat")
    elif int(tooday) % 2 == 1:
        if message.text.lower() == 'monday':
            cursor.execute("SELECT  full_name FROM teacher where id in (10,9,8)")
            rec = list(cursor.fetchall())
            for i in range(len(rec)):
                rec[i]
                m = (str(rec[i - 2]) + '\n')
                n = (str(rec[i - 1]) + '\n')
                b = (str(rec[i]) + '\n')
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day = 'Monday';")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                a = (str(records[i - 2]) + '\n')
                p = (str(records[i - 1]) + '\n')
                t = (str(records[i]) + '\n')
                e = a + b + '\n' + p + n + '\n' + t + m + '\n'
            bot.send_message(message.chat.id, 'week is down')
            bot.send_message(message.chat.id, e)
        elif message.text.lower() == 'tuesday':
            cursor.execute("SELECT  full_name FROM teacher where id in (3)")
            rec = list(cursor.fetchall())
            for i in range(len(rec)):
                rec[i]
                b = (str(rec[i]) + '\n')
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day in ('Tuesday');")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                t = (str(records[i - 1]) + '\n')
                c = (str(records[i]) + '\n')
                e = t +b+ '\n' + c +b+ '\n'
            bot.send_message(message.chat.id, 'week is down')
            bot.send_message(message.chat.id, e)
        elif message.text.lower() == 'wednesday':
            cursor.execute("SELECT  full_name FROM teacher where id in (6,7)")
            rec = list(cursor.fetchall())
            for i in range(len(rec)):
                rec[i]
                n = (str(rec[i - 1]) + '\n')
                b = (str(rec[i]) + '\n')
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day in ('dWednesday', 'Wednesday');")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                t = (str(records[i - 1]) + '\n')
                c = (str(records[i]) + '\n')
                e = t + b+'\n' + c + n + '\n'
            bot.send_message(message.chat.id, 'week is down')
            bot.send_message(message.chat.id, e)
        elif message.text.lower() == 'thusday':
            cursor.execute("SELECT  full_name FROM teacher where id in (1)")
            rec = list(cursor.fetchall())
            for i in range(len(rec)):
                rec[i]
                b = (str(rec[i]) + '\n')
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day in ('dThusday');")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                c = (str(records[i]) + b + '\n')
            bot.send_message(message.chat.id, 'week is down')
            bot.send_message(message.chat.id, c)
        elif message.text.lower() == 'friday':
            cursor.execute("SELECT  full_name FROM teacher where id in (7,5)")
            rec = list(cursor.fetchall())
            for i in range(len(rec)):
                rec[i]
                n = (str(rec[i - 1]) + '\n')
                b = (str(rec[i]) + '\n')
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day in ('Friday');")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                t = (str(records[i - 1]) + '\n')
                c = (str(records[i]) + '\n')
                e = t + b +'\n' + c +n+ '\n'
            bot.send_message(message.chat.id, 'week is down')
            bot.send_message(message.chat.id, e)
        else:
            bot.send_message(message.chat.id, "I dont ponimat")
    if message.text.lower() == 'this week':
        if int(tooday) % 2 == 0:
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day = 'Monday';")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                a = (str(records[i - 2]) + '\n')
                p = (str(records[i - 1]) + '\n')
                t = (str(records[i]) + '\n')
                e = a + '\n' + p + '\n' + t + '\n'
            bot.send_message(message.chat.id, 'monday')
            bot.send_message(message.chat.id, e)
            cursor.execute(
                "SELECT start_time, subject, room_number FROM  timetabel where day in ('Tuesday', 'uTuesday');")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                a = (str(records[i - 3]) + '\n')
                p = (str(records[i - 2]) + '\n')
                t = (str(records[i - 1]) + '\n')
                c = (str(records[i]) + '\n')
                e = a + '\n' + p + '\n' + t + '\n' + c + '\n'
            bot.send_message(message.chat.id, 'tuesday')
            bot.send_message(message.chat.id, e)
            cursor.execute(
                "SELECT start_time, subject, room_number FROM  timetabel where day in ('uWednesday', 'Wednesday');")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                t = str(str(records[i - 1]) + '\n')
                c = str(str(records[i]) + '\n')
                e = t + '\n' + c + '\n'
            bot.send_message(message.chat.id, 'wednesday')
            bot.send_message(message.chat.id, e)
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day in ('uThusday');")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                a = str(str(records[i - 3]) + '\n')
                p = str(str(records[i - 2]) + '\n')
                t = str(str(records[i - 1]) + '\n')
                c = str(str(records[i]) + '\n')
                e = a + '\n' + p + '\n' + t + '\n' + c + '\n'
            bot.send_message(message.chat.id, 'thusday')
            bot.send_message(message.chat.id, e)
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day in ('Friday');")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                t = str(str(records[i - 1]) + '\n')
                c = str(str(records[i]) + '\n')
                e = t + '\n' + c + '\n'
            bot.send_message(message.chat.id, 'friday')
            bot.send_message(message.chat.id, e)
        else:
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day = 'Monday';")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                a = str(str(records[i - 2]) + '\n')
                p = str(str(records[i - 1]) + '\n')
                t = str(str(records[i]) + '\n')
                e = a + '\n' + p + '\n' + t + '\n'
            bot.send_message(message.chat.id, 'monday')
            bot.send_message(message.chat.id, e)
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day in ('Tuesday');")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                t = str(str(records[i - 1]) + '\n')
                c = str(str(records[i]) + '\n')
                e = t + '\n' + c + '\n'
            bot.send_message(message.chat.id, 'tuesday')
            bot.send_message(message.chat.id, e)
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day in ('dWednesday', 'Wednesday');")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                t = str(str(records[i - 1]) + '\n')
                c = str(str(records[i]) + '\n')
                e = t + '\n' + c + '\n'
            bot.send_message(message.chat.id, 'wednesday')
            bot.send_message(message.chat.id, e)
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day in ('dThusday');")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                c = str(str(records[i]) + '\n')
            bot.send_message(message.chat.id, 'thusday')
            bot.send_message(message.chat.id, c)
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day in ('Friday');")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                t = str(str(records[i - 1]) + '\n')
                c = str(str(records[i]) + '\n')
                e = t + '\n' + c + '\n'
            bot.send_message(message.chat.id, 'friday')
            bot.send_message(message.chat.id, e)
    elif message.text.lower() == 'next week':
        if (int(tooday) + 1) % 2 == 0:
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day = 'Monday';")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                a = str(str(records[i - 2]) + '\n')
                p = str(str(records[i - 1]) + '\n')
                t = str(str(records[i]) + '\n')
                e = a + '\n' + p + '\n' + t + '\n'
            bot.send_message(message.chat.id, 'monday')
            bot.send_message(message.chat.id, e)
            cursor.execute(
                "SELECT start_time, subject, room_number FROM  timetabel where day in ('Tuesday', 'uTuesday');")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                a = str(str(records[i - 3]) + '\n')
                p = str(str(records[i - 2]) + '\n')
                t = str(str(records[i - 1]) + '\n')
                c = str(str(records[i]) + '\n')
                e = a + '\n' + p + '\n' + t + '\n' + c + '\n'
            bot.send_message(message.chat.id, 'tuesday')
            bot.send_message(message.chat.id, e)
            cursor.execute(
                "SELECT start_time, subject, room_number FROM  timetabel where day in ('uWednesday', 'Wednesday');")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                t = str(str(records[i - 1]) + '\n')
                c = str(str(records[i]) + '\n')
                e = t + '\n' + c + '\n'
            bot.send_message(message.chat.id, 'wednesday')
            bot.send_message(message.chat.id, e)
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day in ('uThusday');")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                a = str(str(records[i - 3]) + '\n')
                p = str(str(records[i - 2]) + '\n')
                t = str(str(records[i - 1]) + '\n')
                c = str(str(records[i]) + '\n')
                e = a + '\n' + p + '\n' + t + '\n' + c + '\n'
            bot.send_message(message.chat.id, 'thusday')
            bot.send_message(message.chat.id, e)
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day in ('Friday');")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                t = str(str(records[i - 1]) + '\n')
                c = str(str(records[i]) + '\n')
                e = t + '\n' + c + '\n'
            bot.send_message(message.chat.id, 'friday')
            bot.send_message(message.chat.id, e)
        elif (int(tooday) + 1) % 2 == 1:
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day = 'Monday';")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                a = str(str(records[i - 2]) + '\n')
                p = str(str(records[i - 1]) + '\n')
                t = str(str(records[i]) + '\n')
                e = a + '\n' + p + '\n' + t + '\n'
            bot.send_message(message.chat.id, 'monday')
            bot.send_message(message.chat.id, e)
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day in ('Tuesday');")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                t = str(str(records[i - 1]) + '\n')
                c = str(str(records[i]) + '\n')
                e = t + '\n' + c + '\n'
            bot.send_message(message.chat.id, 'tuesday')
            bot.send_message(message.chat.id, e)
            cursor.execute(
                "SELECT start_time, subject, room_number FROM  timetabel where day in ('dWednesday', 'Wednesday');")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                t = str(str(records[i - 1]) + '\n')
                c = str(str(records[i]) + '\n')
                e = t + '\n' + c + '\n'
            bot.send_message(message.chat.id, 'wednasday')
            bot.send_message(message.chat.id, e)
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day in ('dThusday');")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                c = str(str(records[i]) + '\n')
            bot.send_message(message.chat.id, 'thusday')
            bot.send_message(message.chat.id, c)
            cursor.execute("SELECT start_time, subject, room_number FROM  timetabel where day in ('Friday');")
            records = list(cursor.fetchall())
            for i in range(len(records)):
                records[i]
                t = str(str(records[i - 1]) + '\n')
                c = str(str(records[i]) + '\n')
                e = t + '\n' + c + '\n'
            bot.send_message(message.chat.id, 'friday')
            bot.send_message(message.chat.id, e)


bot.infinity_polling()

