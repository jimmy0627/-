from response import give
import globals as gl
import random
from set import *

import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')


intents = Intents.default()
intents.message_content = True  # NOQA
client= Client(intents=intents)


async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('無訊息')
        return

    if want_code := user_message[0:6] == '/code ':
        user_message = user_message[6:]
    elif want_set := user_message[0:5] == '/set ':
        user_message =user_message[5:]
    elif want_luck := user_message[0:6] == '/lucky':
        user_message =user_message
    try:
        if want_code==True:
            if rotor_setting==[]:
                await message.author.send('請輸入配置,先轉子後步進 ex./set x,y,z,1,2,3')
                return
            else:
                response: str = give(user_message,gl.get_value("rotor_setting"),ko=gl.get_value("ko"),kt=gl.get_value("kt"),kc=gl.get_value("kc"))
            await message.author.send("密文: "+response)
        elif want_set==True:
            if rotor_setting!=[]:
                reset()
            set_up(user_message)
            await message.author.send("設置完成")
        elif want_luck==True:
            await message.author.send("你的幸運指數: "+str(random.randrange(1,100)))
        
    except Exception as e:
        print(e)






@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username= str(message.author)
    user_message= message.content
    channel= str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)



def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()