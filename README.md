# DollarUaTracker
### Telegram Bot for Monitoring USD to UAH Exchange Rate

This bot is implemented to retrieve information about the dynamics of the USD to UAH exchange rate using the /get_exchange_rate command on Telegram.

### Description
The bot periodically fetches the current exchange rate value from the specified data source, Google Finance, and stores this data in a local relational database table. Users can then request the latest exchange rate information via the Telegram bot using the /get_exchange_rate command.

### Technologies Used
- Python
- SQLite3 for database management
- Requests and Beautiful Soup for web scraping
- pyTelegramBotAPI for Telegram bot implementation
- Docker for containerization

### Quick Start
#### Docker must be installed on your system
1. Clone the repository to your local machine:
```bash
git clone the-link-from-your-forked-repo
```
2. If you are using PyCharm - it may propose you to automatically create venv for your project and install requirements in it, but if not:
```bash
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
```
3. Create a .env file in the root directory of the project and add the following environment variables:
- API_TOKEN
- RATE_URL
- DB_NAME
- TABLE_NAME
- FILE_NAME
- TIME_ZONE

4. Build and run the Docker container:
```bash
docker-compose up --build
```
## Bot information:
- link: https://t.me/dollar_ua_tracker_bot
- commands: /start, /get_exchange_rate
- api token: you can get it from the BotFather

## Usage
- Start the bot in your Telegram app.
- Use the /get_exchange_rate command to receive an XLSX file with the latest exchange rate data.