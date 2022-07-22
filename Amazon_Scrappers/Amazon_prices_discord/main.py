from discord_webhook import DiscordEmbed, DiscordWebhook
from utilities import Help as help
from data import *

import dotenv
import os
import time


def main():
    while True:
        def discord_send(info):
            dotenv.load_dotenv()
            webhook_url = os.getenv('URL')
            webhook = DiscordWebhook(url=webhook_url)

            description = f'Price: £{info[1]}\nOriginal Price: £{info[2]}\nDiscount: -{info[3]}%'
            # create embed object for webhook
            embed = DiscordEmbed(
                title=info[0], description=description, url=info[4], color='03b2f8')

            # add embed object to webhook
            webhook.add_embed(embed)

            webhook.execute()

        def run_program():
            for item in data:
                for index in range(len(item)):
                    info = help.is_sale(item[index])
                    if info != None:
                        discord_send(info)

        run_program()
        # Runs every 2 hours
        time.sleep(7200)


if __name__ == '__main__':
    main()
