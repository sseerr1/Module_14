from itertools import count

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

from crud_functions import *
api = "7772840862:AAEDn7Ofh69V9-YP0e767wpKw9Ij94Um0mY"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer('Привет! Я бот, помогающий твоему здоровью.', reply_markup=kb)


# Создание Inline клавиатуры
inline_kb = InlineKeyboardMarkup(resize_keyboard=True)
calculate_calories = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
formulas = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
inline_kb.add(calculate_calories, formulas)
############## module_14_3.py
products = [
    'Product1',
    'Product2',
    'Product3',
    'Product4'
]
inline_kb_sale = InlineKeyboardMarkup(resize_keyboard=True)
for product in products:
    button = InlineKeyboardButton(text=product, callback_data="product_buying")
    inline_kb_sale.insert(button)

# Обычное меню
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
kb.row(button2)
kb.insert(button1)
############## module_14_3.py
button3 = KeyboardButton(text='Купить')
kb.add(button3)


@dp.message_handler(text="Рассчитать")
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=inline_kb)


@dp.callback_query_handler(lambda c: c.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer("Формула Миффлина - Сан Жеора:\n"
                              "BMR = 10 * weight + 6.25 * height - 5 * age - 161")


@dp.callback_query_handler(lambda c: c.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await UserState.age.set()
    await call.message.answer("Введите свой возраст:")


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await UserState.next()
    await message.answer("Введите свой рост:")


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await UserState.next()
    await message.answer("Введите свой вес:")


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()

    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])

    # Упрощенная формула Миффлина - Сан Жеора для мужчин
    calories = 10 * weight + 6.25 * growth - 5 * age + 5

    await message.answer(f"Ваша норма калорий: {calories} ккал")
    await state.finish()


############## module_14_4.py

@dp.message_handler(text="Купить")
async def get_buying_list(message: types.Message, img=None):
    gap = get_all_products()
    for i in range(len(gap)):
        id_, title, description, price = get_all_products()[i]
        img_ = f'file/product{id_}.jpg'
        with open(img_, 'rb') as img:
            await message.answer_photo(img, f'Название: {title} | Описание: {description} | Цена: {price}')
    await message.answer('Выберите продукт для покупки:', reply_markup=inline_kb_sale)




@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")


######################################################################


@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
