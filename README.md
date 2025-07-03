# ai_bot
Запускать:

    # Установить венв
    sudo apt-get install -y python3-venv
    python3 -m venv .venv
    # Запустить венв
    source .venv/bin/activate
    #Запустить скрипт
    python main.py


Проверять:
    curl -X POST -F "file=@Nudity-detection.png" http://localhost:8000/moderate
