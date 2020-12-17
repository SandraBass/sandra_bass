import json
from typing import Text
import telebot
from telebot import types 
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from telebot.types import LabeledPrice
import requests 

TOKEN = '1436206524:AAGAOPXMmMVgdSRg6ZqLssFe_oUgX5A6m1E'

bot = telebot.TeleBot(TOKEN)

commands = {  # command description used in the "help" command
    'start'       : 'Get used to the bot',
    'help'        : 'Edit order'
}

user_dict = {}


class User:
    def __init__(self, name):
        self.name = name
        self.text = None
        self.menu1 = None
        self.item1 = None
        self.quant1 = None
        self.add = None
        self.menu2 = None
        self.item2 = None
        self.quant2 = None
        self.add2 = None
        self.menu3 = None
        self.item3 = None
        self.quant3 = None
        self.add3 = None
        self.menu4 = None
        self.item4 = None
        self.quant4 = None
        self.add4 = None
        self.menu5 = None
        self.item5 = None
        self.quant5 = None
        self.add5 = None
        self.menu6 = None
        self.item6 = None
        self.quant6 = None
        self.add6 = None
        self.menu7 = None
        self.item7 = None
        self.quant7 = None
        self.add7 = None
        self.menu8 = None
        self.item8 = None
        self.quant8 = None







menu = types.ReplyKeyboardMarkup()
menu.row_width = 1
menu.add('燒烤', '小菜', '派對', '酒', '飲料')

markup1 = types.ReplyKeyboardMarkup()
markup1.row_width = 1
markup1.add('豬肉 🐷 pork',
  '魚 🐟 fish',
   '雞腿 🍗 chickenLegs',
    '大雞 🐓 chicken', 
    '蘑菇 🍄 mushrooms',
     '迷你漢堡 🍔 burger',
      '返回 ↪️')

sidedish = types.ReplyKeyboardMarkup()
sidedish.row_width = 1
sidedish.add('套促銷 99 (白飯)  Set 99 (rice)',
 '套促銷 99 (土豆)  Set 99 (potato)',
  '茄子沙拉 🍆 ikra',
   '蟹肉沙拉 🦀 CrabSalad',
    '白飯 🍚 rice',
    '蕎麥 🥣 grechka',
     '土豆 🥔 potato',
      '蛋 🍡 egg',
       '甜點 🍪 dessert ',
        '返回 ↪️')

alcohol = types.ReplyKeyboardMarkup()
alcohol.row_width = 1
alcohol.add('海尼根 生啤酒 🍺 Heineken Draft',
 '朝日 生啤酒 🍺 Asahi Draft',
  '伏特 加酒 🥃 Vodka shot',
   '威士 忌酒 🥃 Whiskey shot',
    '可樂娜 瓶裝 🍾 Corona',
     '海尼根 大罐 🍾 Heineken bottle',
      '百威 大罐 🍾 Budweiser',
       '伏特 酒瓶 🍾 Vodka bottle',
        '威士 酒瓶 🍾 Whiskey bottle',
         '可樂娜 箱 📦 Corona Box',
          '海尼根 箱 📦 Heineken Box',
           '百威 箱 📦 Budweiser Box',
            '返回 ↪️')

beverages = types.ReplyKeyboardMarkup()
beverages.row_width = 1
beverages.add('可樂  🥤 Cola',
 '可爾必思 🥛 Yakult', 
 '橙汁 🧃  Orange Juice', '返回 ↪️')


waiter = types.ReplyKeyboardMarkup(one_time_keyboard=True)
waiter.row_width = 1

waiter.add('大軍', '小捲', 'admin')

table = types.ReplyKeyboardMarkup(one_time_keyboard=True)
table.row_width = 5
table.add('A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'B1', 'B2', 'B3')

markup = types.ReplyKeyboardMarkup()
markup.row_width = 2
markup.add('0', '1', '2', '3', '4', '5', '6', '-1', '-2', '-3', '-4', '-5', '-6', '返回 ↪️')

markupParty = types.ReplyKeyboardMarkup()
markupParty.row_width = 1
markupParty.add('蘑菇+豬肉+雞腿 888 shroom+pork+chickLeg', 
'烤雞+豬肉+烤魚 1399 Pork+Chicken+Fish',
 '牛肉派對套餐 2300 BeefPartySet', 
 '返回 ↪️' )
       
markupP = types.ReplyKeyboardMarkup()
markupP.row_width = 1
markupP.add('+', 'ok', '返回 ↪️')





# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    msg = bot.reply_to(message, "你叫什麼名字？", reply_markup=waiter)
    bot.register_next_step_handler(msg, process_name_step)
   
@bot.message_handler(commands=['help'])
def command_start(message):
    msg = bot.reply_to(message, "你叫什麼名字？", reply_markup=waiter)
    bot.register_next_step_handler(msg, process_name_step)
      

        

@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_help(m):
    cid = m.chat.id
    help_text = "The following commands are available: \n"
    for key in commands:  # generate help text out of the commands dictionary defined at the top
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)  # send the generated help page

def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        msg = bot.reply_to(message, '選擇桌子', reply_markup=table)
        bot.register_next_step_handler(msg, process_test_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_test_step(message):
    try:
        chat_id = message.chat.id
        text = message.text
        user = user_dict[chat_id]
        user.text = text
        msg = bot.reply_to(message, '選擇類別：', reply_markup=menu)
        bot.register_next_step_handler(msg, process_menu1_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_menu1_step(message):
    try:
        chat_id = message.chat.id
        menu1 = message.text
        user = user_dict[chat_id]
        user.menu1 = menu1
        if (menu1 == '燒烤'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=markup1)
            bot.register_next_step_handler(msg, process_item1_step)
        if (menu1 == '小菜'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=sidedish)
            bot.register_next_step_handler(msg, process_item1_step)
        if (menu1 == '派對'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=markupParty)
            bot.register_next_step_handler(msg, process_item1_step)
        if (menu1 == '酒'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=alcohol)
            bot.register_next_step_handler(msg, process_item1_step)
        if (menu1 == '飲料'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=beverages)
            bot.register_next_step_handler(msg, process_item1_step)

    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_item1_step(message):
    try:
        chat_id = message.chat.id
        item1 = message.text
        user = user_dict[chat_id]

        user.item1 = item1



        if (item1 == '豬肉 🐷 pork'):
            user.price = 440
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '牛肉 🥩 beef'):
            user.price = 520
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '魚 🐟 fish'):
            user.price = 520
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '雞腿 🍗 chickenLegs'):
            user.price = 420
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '大雞 🐓 chicken'):
            user.price = 660  
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '蘑菇 🍄 mushrooms'):
            user.price = 180
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '套促銷 99 (白飯)  Set 99 (rice)'):
            user.price = 99
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '套促銷 99 (土豆)  Set 99 (potato)'):
            user.price = 99
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '蟹肉沙拉 🦀 CrabSalad'):
            user.price = 50
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '茄子沙拉 🍆 ikra'):
            user.price = 50 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '白飯 🍚 rice'):
            user.price = 20
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '土豆 🥔 potato'):
            user.price = 20 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == u'返回 ↪️'):
            msg = bot.reply_to(message, '選擇類別：', reply_markup=menu)
            bot.register_next_step_handler(msg, process_menu1_step)

        if (item1 == '蟹肉沙拉 🦀 CrabSalad'):
            user.price = 50
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '茄子沙拉 🍆 ikra'):
            user.price = 50 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '白飯 🍚 rice'):
            user.price = 20
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '土豆 🥔 potato'):
            user.price = 20 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '蕎麥 🥣 grechka'):
            user.price = 50 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '蛋 🍡 egg'):
            user.price = 220
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '甜點 🍪 dessert'):
            user.price = 120
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
            
        if (item1 == '迷你漢堡 🍔 burger'):
            user.price = 120
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)

        if (item1 == '海尼根 生啤酒 🍺 Heineken Draft'):
            user.price = 150
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '朝日 生啤酒 🍺 Asahi Draft'):
            user.price = 150 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '伏特 加酒 🥃 Vodka shot'):
            user.price = 80
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '威士 忌酒 🥃 Whiskey shot'):
            user.price = 120
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
            
        if (item1 == '可樂娜 瓶裝 🍾 Corona'):
            user.price = 100
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)

        if (item1 == '海尼根 大罐 🍾 Heineken bottle'):
            user.price = 150
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '百威 大罐 🍾 Budweiser'):
            user.price = 150 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '伏特 酒瓶 🍾 Vodka bottle'):
            user.price = 800
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '威士 酒瓶 🍾 Whiskey bottle'):
            user.price = 1200
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)

        if (item1 == '可樂娜 箱 📦 Corona Box'):
            user.price = 600
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '海尼根 箱 📦 Heineken Box'):
            user.price = 900 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '百威 箱 📦 Budweiser Box'):
            user.price = 900
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)

        if (item1 == '蘑菇+豬肉+雞腿 888 shroom+pork+chickLeg'):
            user.price = 888
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '烤雞+豬肉+烤魚 1399 Pork+Chicken+Fish'):
            user.price = 1399 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '牛肉派對套餐 2300 BeefPartySet'):
            user.price = 2300
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)

        if (item1 == '可樂  🥤 Cola'):
            user.price = 40
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '可爾必思 🥛 Yakult'):
            user.price = 40 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        if (item1 == '橙汁 🧃  Orange Juice'):
            user.price = 40
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)
        

        if (item1 == u'返回 ↪️'):
            msg = bot.reply_to(message, '選擇類別：', reply_markup=menu)
            bot.register_next_step_handler(msg, process_menu1_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_quant1_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        quant1 = int(message.text)
        user.quant1 = quant1
        if (quant1 == 0, 1, 2, 3, 4, 5, 6):
            msg = bot.send_message(chat_id, '\n 來自的新訂單' + user.name + '\n 桌子:' +  user.text + '\n 項目1:' + str(user.item1) + " "  + " " + str(user.quant1) + "pcs" + ", " + str(user.price*float(user.quant1)) + '\n Total:' + ' ' + str(user.price*float(user.quant1) + 0.1 * (user.price*float(user.quant1))), reply_markup=markupP)
            bot.register_next_step_handler(msg, process_add_step)
        if(quant1 < 0):
            msg = bot.send_message(chat_id, '\n ! 取消訂單' + user.name + '\n 桌子:' +  user.text + '\n 項目1:' + str(user.item1) + " "  + " " + str(user.quant1) + "pcs" + ", " + str(user.price*float(user.quant1)), reply_markup=markupP)
            bot.register_next_step_handler(msg, process_add_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')
        




def process_add_step(message):
        
    try:
        chat_id = message.chat.id
        add = message.text
        user = user_dict[chat_id]
        user.add = add
        
        
        if (add == u'+'):
            msg = bot.reply_to(message, '選擇類別：', reply_markup=menu)
            bot.register_next_step_handler(msg, process_menu2_step)

        if (add == u'返回 ↪️'):
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant1_step)

        if (add == u'ok'):
            code = '\n 來自的新訂單' + user.name + '\n 桌子:' +  user.text + '\n 項目1:' + str(user.item1) + " "  + " " + str(user.quant1) + "pcs" + ", " + str(user.price*float(user.quant1)) + '\n Total:' + ' ' + str(user.price*float(user.quant1) + 0.1 * (user.price*float(user.quant1)))
            inline_kb_full = types.InlineKeyboardMarkup(row_width=1)
            inline_kb_full.add(InlineKeyboardButton("Share", switch_inline_query = code, switch_inline_query_current_chat= code))
            msg = bot.send_message(message.chat.id, text = code, reply_markup=inline_kb_full)
            bot.register_next_step_handler(msg, process_menu2_step)
      
    except Exception as e:
        bot.reply_to(message, '/ok')

def process_menu2_step(message):
    try:
        chat_id = message.chat.id
        menu2 = message.text
        user = user_dict[chat_id]
        user.menu2 = menu2
        if (menu2 == '燒烤'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=markup1)
            bot.register_next_step_handler(msg, process_item2_step)
        if (menu2 == '小菜'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=sidedish)
            bot.register_next_step_handler(msg, process_item2_step)
        if (menu2 == '派對'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=markupParty)
            bot.register_next_step_handler(msg, process_item2_step)
        if (menu2 == '酒'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=alcohol)
            bot.register_next_step_handler(msg, process_item2_step)
        if (menu2 == '飲料'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=beverages)
            bot.register_next_step_handler(msg, process_item2_step)

    except Exception as e:
        bot.reply_to(message, 'oooops')        

def process_item2_step(message):
    try:
        chat_id = message.chat.id
        item2 = message.text
        user = user_dict[chat_id]
        user.item2 = item2
        
        if (item2 == u'豬肉 🐷 pork'):
            user.price2 = 440
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == u'牛肉 🥩 beef'):
            user.price2 = 520
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == u'魚 🐟 fish'):
            user.price2 = 520
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == u'雞腿 🍗 chickenLegs'):
            user.price2 = 420
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == u'大雞 🐓 chicken'):
            user.price2 = 660  
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == u'蘑菇 🍄 mushrooms'):
            user.price2 = 180
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == u'套促銷 99 (白飯)  Set 99 (rice)'):
            user.price2 = 99
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == u'套促銷 99 (土豆)  Set 99 (potato)'):
            user.price2 = 99
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == u'蟹肉沙拉 🦀 CrabSalad'):
            user.price2 = 50
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == u'茄子沙拉 🍆 ikra'):
            user.price2 = 50 
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == u'白飯 🍚 rice'):
            user.price2 = 20
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == u'土豆 🥔 potato'):
            user.price2 = 20 
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == '蕎麥 🥣 grechka'):
            user.price2 = 50 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == '蛋 🍡 egg'):
            user.price2 = 220
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == '甜點 🍪 dessert'):
            user.price2 = 120
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
            
        if (item2 == '迷你漢堡 🍔 burger'):
            user.price2 = 120
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)

        if (item2 == '海尼根 生啤酒 🍺 Heineken Draft'):
            user.price2 = 150
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == '朝日 生啤酒 🍺 Asahi Draft'):
            user.price2 = 150 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == '伏特 加酒 🥃 Vodka shot'):
            user.price2 = 80
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == '威士 忌酒 🥃 Whiskey shot'):
            user.price2 = 120
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
            
        if (item2 == '可樂娜 瓶裝 🍾 Corona'):
            user.price2 = 100
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)

        if (item2 == '海尼根 大罐 🍾 Heineken bottle'):
            user.price2 = 150
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == '百威 大罐 🍾 Budweiser'):
            user.price2 = 150 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == '伏特 酒瓶 🍾 Vodka bottle'):
            user.price2 = 800
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == '威士 酒瓶 🍾 Whiskey bottle'):
            user.price2 = 1200
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)

        if (item2 == '可樂娜 箱 📦 Corona Box'):
            user.price2 = 600
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == '海尼根 箱 📦 Heineken Box'):
            user.price2 = 900 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == '百威 箱 📦 Budweiser Box'):
            user.price2 = 900
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)

        if (item2 == '蘑菇+豬肉+雞腿 888 shroom+pork+chickLeg'):
            user.price2 = 888
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == '烤雞+豬肉+烤魚 1399 Pork+Chicken+Fish'):
            user.price2 = 1399 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == '牛肉派對套餐 2300 BeefPartySet'):
            user.price2 = 2300
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)

        if (item2 == '可樂  🥤 Cola'):
            user.price2 = 40
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == '可爾必思 🥛 Yakult'):
            user.price2 = 40 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
        if (item2 == '橙汁 🧃  Orange Juice'):
            user.price2 = 40
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)


        

        elif (item2 == u'返回 ↪️'):
            msg = bot.reply_to(message, '選擇類別：', reply_markup=menu)
            bot.register_next_step_handler(msg, process_menu2_step)

        
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_quant2_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        quant2 = int(message.text)
        user.quant2 = quant2
        if (quant2 == 0, 1, 2, 3, 4, 5, 6):
            msg = bot.send_message(chat_id, '\n 來自的新訂單' + user.name + '\n 桌子:' +  user.text + '\n 項目1:' + str(user.item1) + " "  + str(user.quant1)  + "pcs" + ", " + '\n 項目2:' + str(user.item2) + str(user.quant2)  + "pcs" + ", " + '\n Total:' + str(user.price2*float(user.quant2) + user.price*float(user.quant1) + 0.1 * (user.price2*float(user.quant2) + user.price*float(user.quant1))), reply_markup=markupP)
            bot.register_next_step_handler(msg, process_add2_step)
        if(quant2 < 0):
            msg = bot.send_message(chat_id, '🚫編輯訂單來自' + user.name + '\n 桌子:' +  user.text + '\n 項目1:' + str(user.item1) + " "  + str(user.quant1) + "pcs" + ", " + '\n 項目2:' + str(user.item2) + str(user.quant2) + "pcs" + ", " + '\n Total:' + str(user.price2*float(user.quant2) + user.price*float(user.quant1)), reply_markup=markupP)
            bot.register_next_step_handler(msg, process_add2_step)
    


    except Exception as e:
        bot.reply_to(message, 'error2')





def process_add2_step(message):
    try:
        chat_id = message.chat.id
        add2 = message.text
        user = user_dict[chat_id]
        user.add2 = add2
        if (add2 == u'+'):
            msg = bot.reply_to(message, '選擇類別：', reply_markup=menu)
            bot.register_next_step_handler(msg, process_menu3_step)
        elif (add2 == u'ok'):
            code =  '\n 來自的新訂單' + user.name + '\n 桌子:' +  user.text + '\n 項目1:' + str(user.item1) + " "  + str(user.quant1)  + "pcs" + ", " + '\n 項目2:' + str(user.item2) + str(user.quant2)  + "pcs" + ", " + '\n Total:' + str(user.price2*float(user.quant2) + user.price*float(user.quant1) + 0.1 * (user.price2*float(user.quant2) + user.price*float(user.quant1)))

            inline_kb_full = types.InlineKeyboardMarkup(row_width=1)
            inline_kb_full.add(InlineKeyboardButton("Share", switch_inline_query = code, switch_inline_query_current_chat= code))
            msg = bot.send_message(message.chat.id, text = code, reply_markup=inline_kb_full)

            bot.register_next_step_handler(msg, process_menu3_step)

        elif (add2 == u'返回 ↪️'):
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant2_step)
    except Exception as e:
        bot.reply_to(message, '/ok')

def process_menu3_step(message):
    try:
        chat_id = message.chat.id
        menu3 = message.text
        user = user_dict[chat_id]
        user.menu3 = menu3
        if (menu3 == '燒烤'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=markup1)
            bot.register_next_step_handler(msg, process_item3_step)
        if (menu3 == '小菜'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=sidedish)
            bot.register_next_step_handler(msg, process_item3_step)
        if (menu3 == '派對'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=markupParty)
            bot.register_next_step_handler(msg, process_item3_step)
        if (menu3 == '酒'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=alcohol)
            bot.register_next_step_handler(msg, process_item3_step)
        if (menu3 == '飲料'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=beverages)
            bot.register_next_step_handler(msg, process_item3_step)

    except Exception as e:
        bot.reply_to(message, 'oooops')   

def process_item3_step(message):
    try:
        chat_id = message.chat.id
        item3 = message.text
        user = user_dict[chat_id]
        user.item3 = item3
        
        
        if (item3 == u'豬肉 🐷 pork'):
            user.price3 = 440
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == u'牛肉 🥩 beef'):
            user.price3 = 520
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == u'魚 🐟 fish'):
            user.price3 = 520
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == u'雞腿 🍗 chickenLegs'):
            user.price3 = 420
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == u'大雞 🐓 chicken'):
            user.price3 = 660  
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == u'蘑菇 🍄 mushrooms'):
            user.price3 = 180
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == u'套促銷 99 (白飯)  Set 99 (rice)'):
            user.price3 = 99
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == u'套促銷 99 (土豆)  Set 99 (potato)'):
            user.price3 = 99
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == u'蟹肉沙拉 🦀 CrabSalad'):
            user.price3 = 50
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == u'茄子沙拉 🍆 ikra'):
            user.price3 = 50 
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == u'白飯 🍚 rice'):
            user.price3 = 20
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == u'土豆 🥔 potato'):
            user.price3 = 20 
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)

        if (item3 == '蕎麥 🥣 grechka'):
            user.price3 = 50 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == '蛋 🍡 egg'):
            user.price3 = 220
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == '甜點 🍪 dessert'):
            user.price3 = 120
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
            
        if (item3 == '迷你漢堡 🍔 burger'):
            user.price3 = 120
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)

        if (item3 == '海尼根 生啤酒 🍺 Heineken Draft'):
            user.price3 = 150
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == '朝日 生啤酒 🍺 Asahi Draft'):
            user.price3 = 150 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == '伏特 加酒 🥃 Vodka shot'):
            user.price3 = 80
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == '威士 忌酒 🥃 Whiskey shot'):
            user.price3 = 120
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
            
        if (item3 == '可樂娜 瓶裝 🍾 Corona'):
            user.price3 = 100
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)

        if (item3 == '海尼根 大罐 🍾 Heineken bottle'):
            user.price3 = 150
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == '百威 大罐 🍾 Budweiser'):
            user.price3 = 150 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == '伏特 酒瓶 🍾 Vodka bottle'):
            user.price3 = 800
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == '威士 酒瓶 🍾 Whiskey bottle'):
            user.price3 = 1200
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)

        if (item3 == '可樂娜 箱 📦 Corona Box'):
            user.price3 = 600
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == '海尼根 箱 📦 Heineken Box'):
            user.price3 = 900 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == '百威 箱 📦 Budweiser Box'):
            user.price3 = 900
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)

        if (item3 == '蘑菇+豬肉+雞腿 888 shroom+pork+chickLeg'):
            user.price3 = 888
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == '烤雞+豬肉+烤魚 1399 Pork+Chicken+Fish'):
            user.price3 = 1399 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == '牛肉派對套餐 2300 BeefPartySet'):
            user.price3 = 2300
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)

        if (item3 == '可樂  🥤 Cola'):
            user.price3 = 40
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == '可爾必思 🥛 Yakult'):
            user.price3 = 40 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
        if (item3 == '橙汁 🧃  Orange Juice'):
            user.price3 = 40
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)




        if (item3 == u'返回 ↪️'):

            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=markup1)
            bot.register_next_step_handler(msg, process_test_step)

    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_quant3_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        quant3 = int(message.text)
        user.quant3 = quant3
        if (quant3 == 0, 1, 2, 3, 4, 5, 6):
            msg = bot.send_message(chat_id, '\n 來自的新訂單' + user.name + '\n 桌子:' +  user.text + '\n 項目1:' + str(user.item1) + " "  + str(user.quant1) + "pcs" + ", " + '\n 項目2:' + str(user.item2) + str(user.quant2) + "pcs" + ", " + '\n 項目3:' + str(user.item3) + str(user.quant3) + "pcs" + ", " + '\n Total:' + str(user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3) + 0.1 * (user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3))) + ' ' + '$', reply_markup=markupP)
            bot.register_next_step_handler(msg, process_add3_step)
        if(quant3 < 0):
            msg = bot.send_message(chat_id, '\n 來自的新訂單' + user.name + '\n 桌子:' +  user.text + '\n 項目1:' + str(user.item1) + " "  + str(user.quant1) + "pcs" + ", " + '\n 項目2:' + str(user.item2) + str(user.quant2) + "pcs" + ", " + '\n 項目3:' + str(user.item3) + str(user.quant3) + "pcs" + ", " + '\n Total:' + str(user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3)) + ' ' + '$', reply_markup=markupP)
            bot.register_next_step_handler(msg, process_add3_step)
      


        
    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_add3_step(message):
    try:
        chat_id = message.chat.id
        add3 = message.text
        user = user_dict[chat_id]
        user.add3 = add3
        if (add3 == u'+'):
            msg = bot.reply_to(message, '選擇類別：', reply_markup=menu)
            bot.register_next_step_handler(msg, process_menu4_step)
        elif (add3 == u'ok'):
            code = '\n 來自的新訂單' + user.name + '\n 桌子:' +  user.text + '\n 項目1:' + str(user.item1) + " "  + str(user.quant1) + "pcs" + ", " + '\n 項目2:' + str(user.item2) + str(user.quant2) + "pcs" + ", " + '\n 項目3:' + str(user.item3) + str(user.quant3) + "pcs" + ", " + '\n Total:' + str(user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3) + 0.1 * (user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3))) + ' ' + '$'

            inline_kb_full = types.InlineKeyboardMarkup(row_width=1)
            inline_kb_full.add(InlineKeyboardButton("Share", switch_inline_query = code, switch_inline_query_current_chat= code))
            msg = bot.send_message(message.chat.id, text = code, reply_markup=inline_kb_full)
            
        elif (add3 == u'返回 ↪️'):
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant3_step)
    except Exception as e:
        bot.reply_to(message, '/ok')

def process_menu4_step(message):
    try:
        chat_id = message.chat.id
        menu4 = message.text
        user = user_dict[chat_id]
        user.menu4 = menu4
        if (menu4 == '燒烤'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=markup1)
            bot.register_next_step_handler(msg, process_item4_step)
        if (menu4 == '小菜'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=sidedish)
            bot.register_next_step_handler(msg, process_item4_step)
        if (menu4 == '派對'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=markupParty)
            bot.register_next_step_handler(msg, process_item4_step)
        if (menu4 == '酒'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=alcohol)
            bot.register_next_step_handler(msg, process_item4_step)
        if (menu4 == '飲料'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=beverages)
            bot.register_next_step_handler(msg, process_item4_step)

    except Exception as e:
        bot.reply_to(message, 'oooops')


def process_item4_step(message):
    try: 
        chat_id = message.chat.id
        item4 = message.text
        user = user_dict[chat_id]
        user.item4 = item4
        
        
        if (item4 == u'豬肉 🐷 pork'):
            user.price4 = 440
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == u'牛肉 🥩 beef'):
            user.price4 = 520
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == u'魚 🐟 fish'):
            user.price4 = 520
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == u'雞腿 🍗 chickenLegs'):
            user.price4 = 420
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == u'大雞 🐓 chicken'):
            user.price4 = 660  
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == u'蘑菇 🍄 mushrooms'):
            user.price4 = 180
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == u'套促銷 99 (白飯)  Set 99 (rice)'):
            user.price4 = 99
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == u'套促銷 99 (土豆)  Set 99 (potato)'):
            user.price4 = 99
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == u'蟹肉沙拉 🦀 CrabSalad'):
            user.price4 = 50
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == u'茄子沙拉 🍆 ikra'):
            user.price4 = 50 
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == u'白飯 🍚 rice'):
            user.price4 = 20
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == u'土豆 🥔 potato'):
            user.price4 = 20 
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == '蕎麥 🥣 grechka'):
            user.price4 = 50 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == '蛋 🍡 egg'):
            user.price4 = 220
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == '甜點 🍪 dessert'):
            user.price4 = 120
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
            
        if (item4 == '迷你漢堡 🍔 burger'):
            user.price4 = 120
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)

        if (item4 == '海尼根 生啤酒 🍺 Heineken Draft'):
            user.price4 = 150
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == '朝日 生啤酒 🍺 Asahi Draft'):
            user.price4 = 150 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == '伏特 加酒 🥃 Vodka shot'):
            user.price4 = 80
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == '威士 忌酒 🥃 Whiskey shot'):
            user.price4 = 120
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
            
        if (item4 == '可樂娜 瓶裝 🍾 Corona'):
            user.price4 = 100
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)

        if (item4 == '海尼根 大罐 🍾 Heineken bottle'):
            user.price4 = 150
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == '百威 大罐 🍾 Budweiser'):
            user.price4 = 150 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == '伏特 酒瓶 🍾 Vodka bottle'):
            user.price4 = 800
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == '威士 酒瓶 🍾 Whiskey bottle'):
            user.price4 = 1200
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)

        if (item4 == '可樂娜 箱 📦 Corona Box'):
            user.price4 = 600
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == '海尼根 箱 📦 Heineken Box'):
            user.price4 = 900 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == '百威 箱 📦 Budweiser Box'):
            user.price4 = 900
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)

        if (item4 == '蘑菇+豬肉+雞腿 888 shroom+pork+chickLeg'):
            user.price4 = 888
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == '烤雞+豬肉+烤魚 1399 Pork+Chicken+Fish'):
            user.price4 = 1399 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == '牛肉派對套餐 2300 BeefPartySet'):
            user.price4 = 2300
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)

        if (item4 == '可樂  🥤 Cola'):
            user.price4 = 40
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == '可爾必思 🥛 Yakult'):
            user.price4 = 40 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
        if (item4 == '橙汁 🧃  Orange Juice'):
            user.price4 = 40
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)





        if (item4 == u'返回 ↪️'):

            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=markup1)
            bot.register_next_step_handler(msg, process_add3_step)

    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_quant4_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        quant4 = int(message.text)
        user.quant4 = quant4
        if (quant4 == 0, 1, 2, 3, 4, 5, 6):
            msg = bot.send_message(chat_id, '\n 來自的新訂單' + user.name + '\n 桌子:' +  user.text + '\n 項目1:' + str(user.item1) + " "  + str(user.quant1) + "pcs" + ", " + '\n 項目2:' + str(user.item2) + str(user.quant2) + "pcs" + ", " + '\n 項目3:' + str(user.item3) + str(user.quant3) + "pcs" + ", "  + '\n 項目4:' + str(user.item4) + str(user.quant4) + "pcs" + ", " +  '\n Total:' + str(user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3) + user.price4*float(user.quant4) + 0.1 * (user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3) + user.price4*float(user.quant4))) + ' ' + '$', reply_markup=markupP)
            bot.register_next_step_handler(msg, process_add4_step)
         
        elif(quant4 < 0 ):
            msg = bot.send_message(chat_id, '\n 來自的新訂單' + user.name + '\n 桌子:' +  user.text + '\n 項目1:' + str(user.item1) + " "  + str(user.quant1) + "pcs" + ", " + '\n 項目2:' + str(user.item2) + str(user.quant2) + "pcs" + ", " + '\n 項目3:' + str(user.item3) + str(user.quant3) + "pcs" + ", "  + '\n 項目4:' + str(user.item4) + str(user.quant4) + "pcs" + ", " +  '\n Total:' + str(user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3) + user.price4*float(user.quant4)) + ' ' + '$', reply_markup=markupP)
            bot.register_next_step_handler(msg, process_add4_step)

       

        
    except Exception as e:
            bot.reply_to(message, 'oooops')


def process_add4_step(message):
    try:
        chat_id = message.chat.id
        add4 = message.text
        user = user_dict[chat_id]
        user.add4 = add4
        if (add4 == u'+'):
            msg = bot.reply_to(message, '選擇類別：', reply_markup=menu)
            bot.register_next_step_handler(msg, process_menu5_step)
        elif (add4 == u'ok'):

            code = '\n 來自的新訂單' + user.name + '\n 桌子:' +  user.text + '\n 項目1:' + str(user.item1) + " "  + str(user.quant1) + "pcs" + ", " + '\n 項目2:' + str(user.item2) + str(user.quant2) + "pcs" + ", " + '\n 項目3:' + str(user.item3) + str(user.quant3) + "pcs" + ", "  + '\n 項目4:' + str(user.item4) + str(user.quant4) + "pcs" + ", " +  '\n Total:' + str(user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3) + user.price4*float(user.quant4) + 0.1 * (user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3) + user.price4*float(user.quant4))) + ' ' + '$'

            inline_kb_full = types.InlineKeyboardMarkup(row_width=1)
            inline_kb_full.add(InlineKeyboardButton("Share", switch_inline_query = code, switch_inline_query_current_chat= code))
            msg = bot.send_message(message.chat.id, text = code, reply_markup=inline_kb_full)
            
        elif (add4 == u'返回 ↪️'):
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant4_step)
    except Exception as e:
        bot.reply_to(message, '/ok')


def process_menu5_step(message):
    try:
        chat_id = message.chat.id
        menu5 = message.text
        user = user_dict[chat_id]
        user.menu5 = menu5
        if (menu5 == '燒烤'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=markup1)
            bot.register_next_step_handler(msg, process_item5_step)
        if (menu5 == '小菜'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=sidedish)
            bot.register_next_step_handler(msg, process_item5_step)
        if (menu5 == '派對'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=markupParty)
            bot.register_next_step_handler(msg, process_item5_step)
        if (menu5 == '酒'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=alcohol)
            bot.register_next_step_handler(msg, process_item5_step)
        if (menu5 == '飲料'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=beverages)
            bot.register_next_step_handler(msg, process_item5_step)

    except Exception as e:
        bot.reply_to(message, 'oooops')



def process_item5_step(message):
    try: 
         chat_id = message.chat.id
         item5 = message.text
         user = user_dict[chat_id]
         user.item5 = item5
        
        
         if (item5 == u'豬肉 🐷 pork'):
            user.price5 = 440
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == u'牛肉 🥩 beef'):
            user.price5 = 520
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == u'魚 🐟 fish'):
            user.price5 = 520
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == u'雞腿 🍗 chickenLegs'):
            user.price5 = 420
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == u'大雞 🐓 chicken'):
            user.price5 = 660  
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == u'蘑菇 🍄 mushrooms'):
            user.price5 = 180
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == u'套促銷 99 (白飯)  Set 99 (rice)'):
            user.price5 = 99
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == u'套促銷 99 (土豆)  Set 99 (potato)'):
            user.price5 = 99
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == u'蟹肉沙拉 🦀 CrabSalad'):
            user.price5 = 50
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == u'茄子沙拉 🍆 ikra'):
            user.price5 = 50 
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == u'白飯 🍚 rice'):
            user.price5 = 20
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == u'土豆 🥔 potato'):
            user.price5 = 20 
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == '蕎麥 🥣 grechka'):
            user.price5 = 50 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == '蛋 🍡 egg'):
            user.price5 = 220
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == '甜點 🍪 dessert'):
            user.price5 = 120
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
            
         if (item5 == '迷你漢堡 🍔 burger'):
            user.price5 = 120
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)

         if (item5 == '海尼根 生啤酒 🍺 Heineken Draft'):
            user.price5 = 150
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == '朝日 生啤酒 🍺 Asahi Draft'):
            user.price5 = 150 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == '伏特 加酒 🥃 Vodka shot'):
            user.price5 = 80
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == '威士 忌酒 🥃 Whiskey shot'):
            user.price5 = 120
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
            
         if (item5 == '可樂娜 瓶裝 🍾 Corona'):
            user.price5 = 100
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)

         if (item5 == '海尼根 大罐 🍾 Heineken bottle'):
            user.price5 = 150
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == '百威 大罐 🍾 Budweiser'):
            user.price5 = 150 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == '伏特 酒瓶 🍾 Vodka bottle'):
            user.price5 = 800
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == '威士 酒瓶 🍾 Whiskey bottle'):
            user.price5 = 1200
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)

         if (item5 == '可樂娜 箱 📦 Corona Box'):
            user.price5 = 600
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == '海尼根 箱 📦 Heineken Box'):
            user.price5 = 900 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == '百威 箱 📦 Budweiser Box'):
            user.price5 = 900
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)

         if (item5 == '蘑菇+豬肉+雞腿 888 shroom+pork+chickLeg'):
            user.price5 = 888
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == '烤雞+豬肉+烤魚 1399 Pork+Chicken+Fish'):
            user.price5 = 1399 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == '牛肉派對套餐 2300 BeefPartySet'):
            user.price5 = 2300
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)

         if (item5 == '可樂  🥤 Cola'):
            user.price5 = 40
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == '可爾必思 🥛 Yakult'):
            user.price5 = 40 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
         if (item5 == '橙汁 🧃  Orange Juice'):
            user.price5 = 40
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)





         if (item5 == u'返回 ↪️'):

            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=markup1)
            bot.register_next_step_handler(msg, process_add4_step)

    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_quant5_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        quant5 = int(message.text)
        user.quant5 = quant5
        if (quant5 == 0, 1, 2, 3, 4, 5, 6):
            msg = bot.send_message(chat_id, '\n 來自的新訂單' + user.name + '\n 桌子:' +  user.text + '\n 項目1:' + str(user.item1) + " "  + str(user.quant1) + "pcs" + ", "  + '\n 項目2:' + str(user.item2) + str(user.quant2) + "pcs" + ", "  + '\n 項目3:' + str(user.item3) + str(user.quant3)  + "pcs" + ", "  + '\n 項目4:' + str(user.item4) + str(user.quant4) + "pcs" + ", "  + '\n 項目5:' + str(user.item5) + str(user.quant5) +  "pcs" + ", "  + '\n Total:' + str(user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3) + user.price4*float(user.quant4) + user.price5*float(user.quant5) + 0.1 * (user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3) + user.price4*float(user.quant4) + user.price5*float(user.quant5))) + ' ' + '$', reply_markup=markupP)
            bot.register_next_step_handler(msg, process_add5_step)
         
        elif(quant5 < 0):
            msg = bot.send_message(chat_id, '\n 來自的新訂單' + user.name + '\n 桌子:' +  user.text + '\n 項目1:' + str(user.item1) + " "  + str(user.quant1) + "pcs" + ", "  + '\n 項目2:' + str(user.item2) + str(user.quant2) + "pcs" + ", "  + '\n 項目3:' + str(user.item3) + str(user.quant3)  + "pcs" + ", "  + '\n 項目4:' + str(user.item4) + str(user.quant4) + "pcs" + ", "  + '\n 項目5:' + str(user.item5) + str(user.quant5) +  "pcs" + ", "  + '\n Total:' + str(user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3) + user.price4*float(user.quant4) + user.price5*float(user.quant5)) + ' ' + '$', reply_markup=markupP)
            bot.register_next_step_handler(msg, process_add5_step)
            
        
        

            
    except Exception as e:
            bot.reply_to(message, 'oooops')



def process_add5_step(message):
    try:
        chat_id = message.chat.id
        add5 = message.text
        user = user_dict[chat_id]
        user.add5 = add5
        if (add5 == u'+'):
            msg = bot.reply_to(message, '選擇類別：', reply_markup=menu)
            bot.register_next_step_handler(msg, process_item6_step)
        elif (add5 == u'ok'):

            code = '\n 來自的新訂單' + user.name + '\n 桌子:' +  user.text + '\n 項目1:' + str(user.item1) + " "  + str(user.quant1) + "pcs" + ", "  + '\n 項目2:' + str(user.item2) + str(user.quant2) + "pcs" + ", "  + '\n 項目3:' + str(user.item3) + str(user.quant3)  + "pcs" + ", "  + '\n 項目4:' + str(user.item4) + str(user.quant4) + "pcs" + ", "  + '\n 項目5:' + str(user.item5) + str(user.quant5) +  "pcs" + ", "  + '\n Total:' + str(user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3) + user.price4*float(user.quant4) + user.price5*float(user.quant5) + 0.1 * (user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3) + user.price4*float(user.quant4) + user.price5*float(user.quant5))) + ' ' + '$'

            inline_kb_full = types.InlineKeyboardMarkup(row_width=1)
            inline_kb_full.add(InlineKeyboardButton("Share", switch_inline_query = code, switch_inline_query_current_chat= code))
            msg = bot.send_message(message.chat.id, text = code, reply_markup=inline_kb_full)
            
        elif (add5 == u'返回 ↪️'):
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant5_step)
    except Exception as e:
        bot.reply_to(message, '/ok')


def process_item6_step(message):
    try: 
         chat_id = message.chat.id
         item6 = message.text
         user = user_dict[chat_id]
         user.item6 = item6
        
        
         if (item6 == u'豬肉 🐷 pork'):
            user.price6 = 440
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == u'牛肉 🥩 beef'):
            user.price6 = 520
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == u'魚 🐟 fish'):
            user.price6 = 520
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == u'雞腿 🍗 chickenLegs'):
            user.price6 = 420
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == u'大雞 🐓 chicken'):
            user.price6 = 660  
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == u'蘑菇 🍄 mushrooms'):
            user.price6 = 180
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == u'套促銷 99 (白飯)  Set 99 (rice)'):
            user.price6 = 99
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == u'套促銷 99 (土豆)  Set 99 (potato)'):
            user.price6 = 99
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == u'蟹肉沙拉 🦀 CrabSalad'):
            user.price6 = 50
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == u'茄子沙拉 🍆 ikra'):
            user.price6 = 50 
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == u'白飯 🍚 rice'):
            user.price6 = 20
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == u'土豆 🥔 potato'):
            user.price6 = 20 
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == '蕎麥 🥣 grechka'):
            user.price6 = 50 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == '蛋 🍡 egg'):
            user.price6 = 220
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == '甜點 🍪 dessert'):
            user.price6 = 120
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
            
         if (item6 == '迷你漢堡 🍔 burger'):
            user.price6 = 120
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)

         if (item6 == '海尼根 生啤酒 🍺 Heineken Draft'):
            user.price6 = 150
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == '朝日 生啤酒 🍺 Asahi Draft'):
            user.price6 = 150 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == '伏特 加酒 🥃 Vodka shot'):
            user.price6 = 80
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == '威士 忌酒 🥃 Whiskey shot'):
            user.price6 = 120
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
            
         if (item6 == '可樂娜 瓶裝 🍾 Corona'):
            user.price6 = 100
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)

         if (item6 == '海尼根 大罐 🍾 Heineken bottle'):
            user.price6 = 150
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == '百威 大罐 🍾 Budweiser'):
            user.price6 = 150 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == '伏特 酒瓶 🍾 Vodka bottle'):
            user.price6 = 800
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == '威士 酒瓶 🍾 Whiskey bottle'):
            user.price6 = 1200
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)

         if (item6 == '可樂娜 箱 📦 Corona Box'):
            user.price6 = 600
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == '海尼根 箱 📦 Heineken Box'):
            user.price6 = 900 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == '百威 箱 📦 Budweiser Box'):
            user.price6 = 900
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)

         if (item6 == '蘑菇+豬肉+雞腿 888 shroom+pork+chickLeg'):
            user.price6 = 888
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == '烤雞+豬肉+烤魚 1399 Pork+Chicken+Fish'):
            user.price6 = 1399 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == '牛肉派對套餐 2300 BeefPartySet'):
            user.price6 = 2300
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == '可樂  🥤 Cola'):
            user.price6 = 40
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == '可爾必思 🥛 Yakult'):
            user.price6 = 40 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
         if (item6 == '橙汁 🧃  Orange Juice'):
            user.price6 = 40
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)




         if (item6 == u'返回 ↪️'):

            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=markup1)
            bot.register_next_step_handler(msg, process_add5_step)

    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_quant6_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        quant6 = int(message.text)
        user.quant6 = quant6
        if (quant6 == 0, 1, 2, 3, 4, 5, 6):
            msg = bot.send_message(chat_id, '\n 來自的新訂單' + user.name + '\n 桌子:' +  user.text + '\n 項目1:' + str(user.item1) + " "  + str(user.quant1) +  "pcs" + ", "  + '\n 項目2:' + str(user.item2) + str(user.quant2) +  "pcs" + ", "  + '\n 項目3:' + str(user.item3) + str(user.quant3)  +  "pcs" + ", "  + '\n 項目4:' + str(user.item4) + str(user.quant4) +  "pcs" + ", "  + '\n 項目5:' + str(user.item5) + str(user.quant5) +  "pcs" + ", "  + '\n 項目6:' + str(user.item6) + str(user.quant6) +  "pcs" + ", "  + '\n Total:' + str(user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3) + user.price6*float(user.quant6) +user.price4*float(user.quant4) + user.price5*float(user.quant5) + 0.1 * (user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3) + user.price6*float(user.quant6) +user.price4*float(user.quant4) + user.price5*float(user.quant5))) + ' ' + '$', reply_markup=markupP)
            bot.register_next_step_handler(msg, process_add6_step)
         
        elif(quant6 < 0):
            msg = bot.send_message(chat_id, '\n 來自的新訂單' + user.name + '\n 桌子:' +  user.text + '\n 項目1:' + str(user.item1) + " "  + str(user.quant1) +  "pcs" + ", "  + '\n 項目2:' + str(user.item2) + str(user.quant2) +  "pcs" + ", "  + '\n 項目3:' + str(user.item3) + str(user.quant3)  +  "pcs" + ", "  + '\n 項目4:' + str(user.item4) + str(user.quant4) +  "pcs" + ", "  + '\n 項目5:' + str(user.item5) + str(user.quant5) +  "pcs" + ", "  + '\n 項目6:' + str(user.item6) + str(user.quant6) +  "pcs" + ", "  + '\n Total:' + str(user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3) + user.price6*float(user.quant6) +user.price4*float(user.quant4) + user.price5*float(user.quant5)) + ' ' + '$', reply_markup=markupP)
            bot.register_next_step_handler(msg, process_add6_step)
            
        elif (quant6 == '返回 ↪️'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=markup1)
            bot.register_next_step_handler(msg, process_item6_step)
    
    except Exception as e:
            bot.reply_to(message, 'oooops')

def process_add6_step(message):
    try:
        chat_id = message.chat.id
        add6 = message.text
        user = user_dict[chat_id]
        user.add6 = add6
        if (add6 == u'+'):
            msg = bot.reply_to(message, '選擇類別：', reply_markup=menu)
            bot.register_next_step_handler(msg, process_item7_step)
        elif (add6 == u'ok'):

            code = '\n 來自的新訂單' + user.name + '\n 桌子:' +  user.text + '\n 項目1:' + str(user.item1) + " "  + str(user.quant1) +  "pcs" + ", "  + '\n 項目2:' + str(user.item2) + str(user.quant2) +  "pcs" + ", "  + '\n 項目3:' + str(user.item3) + str(user.quant3)  +  "pcs" + ", "  + '\n 項目4:' + str(user.item4) + str(user.quant4) +  "pcs" + ", "  + '\n 項目5:' + str(user.item5) + str(user.quant5) +  "pcs" + ", "  + '\n 項目6:' + str(user.item6) + str(user.quant6) +  "pcs" + ", "  + '\n Total:' + str(user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3) + user.price6*float(user.quant6) +user.price4*float(user.quant4) + user.price5*float(user.quant5) + 0.1 * (user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3) + user.price6*float(user.quant6) +user.price4*float(user.quant4) + user.price5*float(user.quant5))) + ' ' + '$'

            inline_kb_full = types.InlineKeyboardMarkup(row_width=1)
            inline_kb_full.add(InlineKeyboardButton("Share", switch_inline_query = code, switch_inline_query_current_chat= code))
            msg = bot.send_message(message.chat.id, text = code, reply_markup=inline_kb_full)
            
        elif (add6 == u'返回 ↪️'):
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant6_step)
    except Exception as e:
        bot.reply_to(message, '/ok')

def process_item7_step(message):
    try: 
         chat_id = message.chat.id
         item7 = message.text
         user = user_dict[chat_id]
         user.item7 = item7
        
        
         if (item7 == u'豬肉 🐷 pork'):
            user.price7 = 440
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == u'牛肉 🥩 beef'):
            user.price7 = 520
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == u'魚 🐟 fish'):
            user.price7 = 520
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == u'雞腿 🍗 chickenLegs'):
            user.price7 = 420
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == u'大雞 🐓 chicken'):
            user.price7 = 660  
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == u'蘑菇 🍄 mushrooms'):
            user.price7 = 180
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == u'套促銷 99 (白飯)  Set 99 (rice)'):
            user.price7 = 99
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == u'套促銷 99 (土豆)  Set 99 (potato)'):
            user.price7 = 99
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == u'蟹肉沙拉 🦀 CrabSalad'):
            user.price7 = 50
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == u'茄子沙拉 🍆 ikra'):
            user.price7 = 50 
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == u'白飯 🍚 rice'):
            user.price7 = 20
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == u'土豆 🥔 potato'):
            user.price7 = 20 
            msg = bot.reply_to(message, '數量:', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == '蕎麥 🥣 grechka'):
            user.price7 = 50 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == '蛋 🍡 egg'):
            user.price7 = 220
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == '甜點 🍪 dessert'):
            user.price7 = 120
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
            
         if (item7 == '迷你漢堡 🍔 burger'):
            user.price7 = 120
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)

         if (item7 == '海尼根 生啤酒 🍺 Heineken Draft'):
            user.price7 = 150
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == '朝日 生啤酒 🍺 Asahi Draft'):
            user.price7 = 150 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == '伏特 加酒 🥃 Vodka shot'):
            user.price7 = 80
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == '威士 忌酒 🥃 Whiskey shot'):
            user.price7 = 120
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
            
         if (item7 == '可樂娜 瓶裝 🍾 Corona'):
            user.price7 = 100
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)

         if (item7 == '海尼根 大罐 🍾 Heineken bottle'):
            user.price7 = 150
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == '百威 大罐 🍾 Budweiser'):
            user.price7 = 150 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == '伏特 酒瓶 🍾 Vodka bottle'):
            user.price7 = 800
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == '威士 酒瓶 🍾 Whiskey bottle'):
            user.price7 = 1200
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)

         if (item7 == '可樂娜 箱 📦 Corona Box'):
            user.price7 = 600
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == '海尼根 箱 📦 Heineken Box'):
            user.price7 = 900 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == '百威 箱 📦 Budweiser Box'):
            user.price7 = 900
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)

         if (item7 == '蘑菇+豬肉+雞腿 888 shroom+pork+chickLeg'):
            user.price7 = 888
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == '烤雞+豬肉+烤魚 1399 Pork+Chicken+Fish'):
            user.price7 = 1399 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == '牛肉派對套餐 2300 BeefPartySet'):
            user.price7 = 2300
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)

         if (item7 == '可樂  🥤 Cola'):
            user.price7 = 40
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == '可爾必思 🥛 Yakult'):
            user.price7 = 40 
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
         if (item7 == '橙汁 🧃  Orange Juice'):
            user.price7 = 40
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)



         if (item7 == u'返回 ↪️'):

            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=markup1)
            bot.register_next_step_handler(msg, process_add6_step)

    except Exception as e:
        bot.reply_to(message, 'oooops')

def process_quant7_step(message):
    try:
        chat_id = message.chat.id
        user = user_dict[chat_id]
        quant7 =int(message.text)
        user.quant7 = quant7
        if (quant7 == 0, 1, 2, 3, 4, 5, 6):
            msg = bot.send_message(chat_id, '\n 來自的新訂單' + user.name + '\n 桌子:' +  user.text + '\n 項目1:' + str(user.item1) + " "  + str(user.quant1) + '\n 項目2:' + str(user.item2) + str(user.quant2) + '\n 項目3:' + str(user.item3) + str(user.quant3)  + '\n 項目4:' + str(user.item4) + str(user.quant4) + '\n 項目5:' + str(user.item5) + str(user.quant5) + '\n 項目6:' + str(user.item6) + str(user.quant6) + '\n 項目7:' + str(user.item7) + str(user.quant7) + '\n Total:' + str(user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3) + user.price7*float(user.quant7) + user.price6*float(user.quant6) +user.price4*float(user.quant4) + user.price5*float(user.quant5) + 0.1 * (user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3) + user.price7*float(user.quant7) + user.price6*float(user.quant6) +user.price4*float(user.quant4) + user.price5*float(user.quant5))) + ' ' + '$', reply_markup=markupP)
            bot.register_next_step_handler(msg, process_add7_step)
         
        elif(quant7 < 0):
            msg = bot.send_message(chat_id, '\n 來自的新訂單' + user.name + '\n 桌子:' +  user.text + '\n 項目1:' + str(user.item1) + " "  + str(user.quant1) + '\n 項目2:' + str(user.item2) + str(user.quant2) + '\n 項目3:' + str(user.item3) + str(user.quant3)  + '\n 項目4:' + str(user.item4) + str(user.quant4) + '\n 項目5:' + str(user.item5) + str(user.quant5) + '\n 項目6:' + str(user.item6) + str(user.quant6) + '\n 項目7:' + str(user.item7) + str(user.quant7) + '\n Total:' + str(user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3) + user.price7*float(user.quant7) + user.price6*float(user.quant6) +user.price4*float(user.quant4) + user.price5*float(user.quant5)) + ' ' + '$', reply_markup=markupP)
            bot.register_next_step_handler(msg, process_add7_step)
            
        elif (quant7 == '返回 ↪️'):
            msg = bot.reply_to(message, '添加新訂單 ➕', reply_markup=markup1)
            bot.register_next_step_handler(msg, process_item7_step)

        
    except Exception as e:
            bot.reply_to(message, 'oooops')

def process_add7_step(message):
    try:
        chat_id = message.chat.id
        add7 = message.text
        user = user_dict[chat_id]
        user.add7 = add7
        if (add7 == u'+'):
            msg = bot.reply_to(message, '選擇類別：', reply_markup=menu)
            bot.register_next_step_handler(msg, process_item7_step)
        elif (add7 == u'ok'):

            code = '\n 來自的新訂單' + user.name + '\n 桌子:' +  user.text + '\n 項目1:' + str(user.item1) + " "  + str(user.quant1) + '\n 項目2:' + str(user.item2) + str(user.quant2) + '\n 項目3:' + str(user.item3) + str(user.quant3)  + '\n 項目4:' + str(user.item4) + str(user.quant4) + '\n 項目5:' + str(user.item5) + str(user.quant5) + '\n 項目6:' + str(user.item6) + str(user.quant6) + '\n 項目7:' + str(user.item7) + str(user.quant7) + '\n Total:' + str(user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3) + user.price7*float(user.quant7) + user.price6*float(user.quant6) +user.price4*float(user.quant4) + user.price5*float(user.quant5) + 0.1 * (user.price2*float(user.quant2) + user.price*float(user.quant1) + user.price3*float(user.quant3) + user.price7*float(user.quant7) + user.price6*float(user.quant6) +user.price4*float(user.quant4) + user.price5*float(user.quant5))) + ' ' + '$'

            inline_kb_full = types.InlineKeyboardMarkup(row_width=1)
            inline_kb_full.add(InlineKeyboardButton("Share", switch_inline_query = code, switch_inline_query_current_chat= code))
            msg = bot.send_message(message.chat.id, text = code, reply_markup=inline_kb_full)
            
        elif (add7 == u'返回 ↪️'):
            msg = bot.reply_to(message, '數量：', reply_markup=markup)
            bot.register_next_step_handler(msg, process_quant7_step)
    except Exception as e:
        bot.reply_to(message, '/ok')



# Enable saving next step handlers to file "./.handlers-saves/step.save".
# Delay=2 means that after any change in next step handlers (e.g. calling register_next_step_handler())
# saving will hapen after delay 2 seconds.
bot.enable_save_next_step_handlers(delay=0)

# Load next_step_handlers from save file (default "./.handlers-saves/step.save")
# WARNING It will work only if enable_save_next_step_handlers was called!
bot.load_next_step_handlers()

bot.polling(none_stop=True)
