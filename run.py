from dotenv import load_dotenv
load_dotenv()  # reads MAIL_USERNAME / MAIL_PASSWORD from .env in this folder

from ChatbotWebsite import create_app

# Create the app
app = create_app()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
