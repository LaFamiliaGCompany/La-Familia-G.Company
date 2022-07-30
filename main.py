#main commands

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from decouple import config

BOT_TOKEN = config('BOT_TOKEN')

APPLICATION_ID = config('X_PARSE_APPLICATION_ID')
REST_API_KEY = config('X_PARSE_REST_API_KEY')

choiceYesMeny = KeyboardButton("نعم")
choiceNoMeny = KeyboardButton("لا")
choiceMenu = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(choiceYesMeny).add(choiceNoMeny)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.answer("عظيم..😍😍\nيبدو أن لدينا فرد جديد في العائلة\n أهلا  "+message.from_user.first_name)
    await message.answer("دائما تستطيع الوصول لقائمة الأوامر السريعة من هنا\n ... \FCommand ")
    await message.answer("الأن نحتاج إلى بعض المعلومات عنك\n هل ترغب بأن نستخدم اسم المستخدم المحدد مسبقا من قبلك ("+
    message.from_user.first_name+" "+
    message.from_user.last_name+")",reply_markup=choiceMenu)

    await message.answer("والأن نحتاج لرقم الهاتف الخاص بك \n يجب أن يكون فعال على الشبكة السورية")
    await message.answer("ممتاز ،الأن أمر أخير هل ترغب بأن تصلك أخر العروض الخاصة بنا",reply_markup=choiceMenu)
    await message.answer("أمر محزن ولكن دائما تستطيع ألغاء أشتراكك معنا من خلال الأمر التالي \Unsubscribe \n وهذا سوف يوقف أستلام أخر العروض الخاص بنا")


@dp.message_handler()
async def choiceLangAndSingin(message: types.Message):
    if(message.text == "العربية"):
        await message.answer("اهلا بالعربية")
    elif(message.text == "English"):
        await message.answer("Welcome in English")


if __name__ == '__main__':
    executor.start_polling(dp)

