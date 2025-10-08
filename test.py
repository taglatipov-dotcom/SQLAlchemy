from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Создаем базовый класс для моделей
Base = declarative_base()


# Определяем модель User
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    email = Column(String(100))


# Настраиваем подключение к БД (файл example.db будет создан автоматически)
engine = create_engine('sqlite:///example.db', echo=True)  # echo=True для логирования SQL-запросов

# Создаем таблицы
Base.metadata.create_all(engine)

# Создаем сессию для работы с БД
Session = sessionmaker(bind=engine)
session = Session()

# Добавляем нового пользователя
new_user = User(name='Иван Иванов', age=30, email='ivan@example.com')
session.add(new_user)
session.commit()

# Примеры запросов:
# Выбрать всех пользователей
users = session.query(User).all()
for user in users:
    print(f'{user.id}. {user.name} ({user.age}) - {user.email}')

# Выбрать пользователя по имени
user = session.query(User).filter_by(name='Иван Иванов').first()
print(f'Найден пользователь: {user.email}')

# Обновить запись
user.age = 31
session.commit()

# Удалить запись
# session.delete(user)
# session.commit()

# Закрываем сессию
session.close()