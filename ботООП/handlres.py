from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
from quiz import Quiz

class BotHandlers:
    def __init__(self, bot):
        self.bot = bot  
        self.router = Router()
        self.quiz = Quiz()
        self.user_data = {}  
        self.register_handlers()

    def register_handlers(self):
        self.router.message.register(self.start_command, Command("start"))
        self.router.message.register(self.start_quiz, Command("quiz"))
        self.router.callback_query.register(self.handle_answer)

    async def start_command(self, message: types.Message):
        welcome_text = (
            "**Пан или пропал!** \n\n"
            "Привет! Ты попал в мир, где мультяшные знания — "
            "это твоя единственная валюта.\n\n"
            "Напиши /quiz, чтобы начать викторину!"
        )
        await message.answer(welcome_text, parse_mode="Markdown")

    async def start_quiz(self, message: types.Message):
        user_id = message.from_user.id
        self.user_data[user_id] = {"score": 0, "q_index": 0}
        await self.send_question(message.chat.id, user_id)

    async def send_question(self, chat_id, user_id):
        data = self.user_data[user_id]
        question_data = self.quiz.get_question(data["q_index"])

        if not question_data:
            await self.finish_quiz(chat_id, user_id)
            return

        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=opt, callback_data=f"ans_{opt}")] 
                for opt in question_data["options"]
            ]
        )

        try:
            photo_path = f"images/{question_data['image']}"
            photo = FSInputFile(photo_path)
            
            await self.bot.send_photo(
                chat_id, 
                photo=photo, 
                caption=question_data["question"], 
                reply_markup=keyboard
            )
        except Exception as e:
            await self.bot.send_message(chat_id, f"[Ошибка фото]: {question_data['question']}", reply_markup=keyboard)
            print(f"Ошибка загрузки фото: {e}")

    async def handle_answer(self, callback: types.CallbackQuery):
        user_id = callback.from_user.id
        data = self.user_data.get(user_id)

        if not data:
            await callback.answer("Сначала начни викторину через /quiz")
            return

        selected_answer = callback.data.replace("ans_", "")
        question_data = self.quiz.get_question(data["q_index"])

        if selected_answer == question_data["correct"]:
            data["score"] += 1
            await callback.answer("Правильно! ")
        else:
            await callback.answer(f"Неверно! Правильный ответ: {question_data['correct']}")

        data["q_index"] += 1
        
        await callback.message.delete()
        await self.send_question(callback.message.chat.id, user_id)

    async def finish_quiz(self, chat_id, user_id):
        score = self.user_data[user_id]["score"]
        total = len(self.quiz.questions) 
        await self.bot.send_message(
            chat_id, 
            f"🏁 **Викторина окончена!**\n\n"
            f"Правильных ответов: **{score}**\n"
            f"Неправильных: **{total - score}**", 
            parse_mode="Markdown"
        )
        del self.user_data[user_id]