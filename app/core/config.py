from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Бронирование переговорок'
    description: str = 'Описание проекта по бронированию переговорок'
    database_url: str
    secret: str = 'SECRET'

    class Config:
        extra = 'ignore'
        env_file = '.env'

settings = Settings()
