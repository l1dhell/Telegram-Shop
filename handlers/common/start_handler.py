from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data import ADMIN
from database.utils import check_ban
from keyboards import admin_main_keyboard, user_main_keyboard
from database import create_connection


async def start_handler(message: types.Message):
    user_id = message.from_user.id

    if user_id == ADMIN:
        await message.reply("ADMIN PANEL ACTIVATE", reply_markup=admin_main_keyboard)

    else:
        ban_info = await check_ban(user_id)

        if ban_info:
            ban_reason = ban_info[2]

            button_help = InlineKeyboardButton("Help", url="https://t.me/Ai_digi_digi_dai", callback_data="help")
            reply_markup = InlineKeyboardMarkup().add(button_help)

            await message.reply(f"Sorry, you were banned for the following reason: {ban_reason}", reply_markup=reply_markup)

        else:
            conn = await create_connection()
            user = await conn.fetchrow('SELECT * FROM users WHERE telegram_id = $1;', user_id)

            if user is None:
                await conn.execute('INSERT INTO users (telegram_id, telegram_username, balance) VALUES ($1, $2, $3);', user_id, message.from_user.username or '', 0)
            await conn.close()

            await message.reply("Hello!", reply_markup=user_main_keyboard)