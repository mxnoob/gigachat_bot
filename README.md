# Giga Chat bot

Простой чат бот от Сбера

## Как настроить

> [!IMPORTANT]
> Зарегистрироваться на https://developers.sber.ru/dev. </br>
> Получить **CLIENT_ID** и **SECRET**. </br>
> Создать файл .env на примере файла [.env.example](.env.example)

## Как запустить

```shell
# Склонировать репозиторий
git clone https://github.com/mxnoob/gigachat_bot.git

# Создать виртуальное окружение и активировать его
python -m venv venv
. venv/Scripts/activate

# Установить зависимости
pip install -r requirements.txt

# Запустить бота
streamlit run main.py
```

