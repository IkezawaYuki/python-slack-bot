from slackbot.bot import Bot, respond_to


@respond_to('練習')
def sample(message):
    message.send("これは練習です。")


if __name__ == '__main__':
    bot = Bot()
    bot.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
