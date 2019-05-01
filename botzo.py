from selenium import webdriver
from pathlib import Path

import time
import discord
from discord.ext import commands


class Wait():
    def __init__(self):
        self.time = 0
        self.cool = 60*60
    def getWait(self):
        if (time.time() - self.time) > self.cool:
            self.time = time.time()
            return True
        else:
            return False


token = 'YOUR TOKEN'
bot = commands.Bot(command_prefix = '!')

@bot.command(aliases=['v','w','vær'])
async def weather(ctx):
    if weit.getWait():
        await scrshot()
    with open('cap.png', 'rb') as img:
        await ctx.send(file=discord.File(img))

@bot.event
async def on_message(message):
    print(message.content)
    await bot.process_commands(message)

async def scrshot():
    driverPath = 'C:_URPATH_\\geckodriver.exe'
    driver = webdriver.Firefox(executable_path=driverPath)
    cssPath = 'SOME CSS PATH TO AN ELEMENT U WANT TO CAPTURE'

    driver.get('SOME URL')
    elem = driver.find_element_by_css_selector(cssPath)
    elem.screenshot('cap.png')
    driver.quit()

weit = Wait()
bot.run(token)


