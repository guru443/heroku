import csv
import re
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


from time import sleep
from unittest import result
from click import option
from requests import options
from selenium import webdriver
from selenium.webdriver.common.by import By



from time import sleep
from unittest import result
from click import option
from requests import options
from selenium import webdriver
from selenium.webdriver.common.by import By

import os  
import pandas as pd

from bs4 import BeautifulSoup

def tem():
    m= r'C:\Users\MRMINH\Desktop\BOOT TELEGRAM\data.csv'
    df_data = pd.read_csv(m)
    # pd.set_option('display.max_rows')
    # print(df_data)    
    # print(type(df_data))

    minh = [df_data]
    return minh


# tem()
# print(tem())

async def hello(update: Update, context: ContextTypes.context) -> None:
    await update.message.reply_text(f'Em chào anh minh {update.effective_user.first_name}')

async def news(update: Update, context: ContextTypes.context) -> None:
    data = tem()
    # print(data)
    await update.message.reply_text(f'alo alo cái canh cần là {data}')

async def news20(update: Update, context: ContextTypes.context) -> None:
    data = tem()
    # print(data)
    await update.message.reply_text(f'alo alo cái canh cần là {data}')



app = ApplicationBuilder().token("5704774159:AAFSGr5pHPqZlow-l-JQVihbv7vVGoO0DA0").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("news", news))
app.add_handler(CommandHandler("news", news20))

app.run_polling()