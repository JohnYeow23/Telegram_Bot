from imports import *

load_dotenv()

# Tracing via Langsmith
trace = os.getenv("LANGCHAIN_TRACING_V2")
langsmith = os.getenv("LANGCHAIN_API_KEY")

# Build a GPT model
gpt = ChatOpenAI(
    model = "gpt-4o",
    temperature=0, # We only change the temperature for OpenAI or top p not both at the same time.
    openai_api_key = os.getenv("OPENAI_API_KEY"),
)

# Create the telegram bot we need
tele = os.getenv("DAC_TOKEN")
dac = ApplicationBuilder().token(tele).build() 

def generate(full_prompt: str) -> str:
    try:
        response = gpt.invoke(full_prompt)
        return response.content if hasattr(response, 'content') else "Sorry, I couldn't generate a response."
    except Exception as e:
        return f"There was an error generating the response: {str(e)}"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.first_name
    system_message = f"Hello {user_id}! I am a chatbot. How can I help you today?"
    await update.message.reply_text(system_message)

async def chat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_message = update.message.text
    response_text = generate(user_message)
    await update.message.reply_text(response_text)

# Add handlers
dac.add_handler(CommandHandler("start", start))
dac.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, chat))

# Run the bot
dac.run_polling()