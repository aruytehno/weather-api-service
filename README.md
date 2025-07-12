# weather-api-service
FastAPI + React + MongoDB
```
client/                # React-приложение (Vite или CRA)
server/
├── main.py            # FastAPI приложение
├── routes/            # Эндпоинты API (weather, users и т.д.)
├── services/          # Логика обработки данных
├── models/            # Pydantic-схемы
├── db/                # Подключение к MongoDB, репозитории
└── utils/             # Хелперы (например, вызовы к внешним API)
```

## 1. Создание виртуального окружения
```bash
python -m venv venv
```

## 2. Активация виртуального окружения

### На Windows (PowerShell):
```shell
.\venv\Scripts\Activate.ps1
```
```cmd
.\venv\Scripts\activate.bat
```

### На Linux / macOS:

```bash
source venv/bin/activate
```

## 3. Обновление
```bash
python.exe -m pip install --upgrade pip
```

## 4. Установка зависимостей
```bash
pip install -r requirements.txt
```

## 5. Выход из окружения

```bash
deactivate
```