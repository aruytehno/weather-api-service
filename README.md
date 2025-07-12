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