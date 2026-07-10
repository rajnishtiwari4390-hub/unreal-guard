from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)
import os

TOKEN = os.getenv("BOT_TOKEN")

OWNER_ID = 8656839796
ADMINS = [8656839796, 7085991794]
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "help":
        await query.edit_message_text(
            "📖 <b>HELP MENU</b>\n\n"
            "/start - Start Bot\n"
            "/ping - Check Bot Speed\n"
            "/info - Bot Information",
            parse_mode="HTML"
        )

    elif query.data == "status":
        await query.edit_message_text(
            "🟢 <b>STATUS</b>\n\n"
            "Bot : Online ✅\n"
            "Mode : Private 🔒\n"
            "Version : Ultra Premium",
            parse_mode="HTML"
        )
elif query.data == "close":
        await query.message.delete()
app.add_handler(CallbackQueryHandler(button))

