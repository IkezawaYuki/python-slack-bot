from slackbot.bot import Bot, respond_to, listen_to
from datetime import datetime
import openpyxl


@respond_to('練習')
def sample(message):
    message.send("これは練習です。")


@listen_to('れんしゅう')
def sample2(message):
    message.send("これは「れんしゅう」です。")


@listen_to('trial')
def sample3(message):
    message.reply("trial")


@respond_to("出勤")
def punch_in(message):
    timestamp = datetime.now().strftime("%H:%M")
    message.send(f'出勤時刻は{timestamp}です。')


@respond_to("退勤")
def punch_out(message):
    timestamp = datetime.now().strftime("%H:%M")
    message.send(f'退勤時刻は{timestamp}です。')


if __name__ == '__main__':
    bot = Bot()
    bot.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
