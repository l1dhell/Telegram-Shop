# Telegram-Shop
pyton3 aiogram postgresql
цель - пощупать базы данных

Макет бд
Таблица "USERS"
id (SERIAL, PRIMARY KEY) - уникальный идентификатор пользователя в базе данных
telegram_id (INTEGER, UNIQUE) - идентификатор пользователя в Telegram
telegram_username (TEXT) - имя пользователя в Telegram
balance (NUMERIC(10, 2)) - баланс пользователя в магазине

Таблица "PURCHASES"
id (SERIAL, PRIMARY KEY) - уникальный идентификатор покупки в базе данных
user_id (INTEGER, REFERENCES users(id)) - идентификатор пользователя в таблице "Пользователи"
product_id (INTEGER, REFERENCES products(id)) - идентификатор товара в таблице "Товары"
product_link (TEXT[]) – ссылка на товар
purchase_time (TIMESTAMP WITHOUT TIME ZONE) – время, совершения покупки

Таблица "TRANSACTIONS"
id (SERIAL, PRIMARY KEY) - уникальный идентификатор транзакции в базе данных
user_id (INTEGER, REFERENCES users(id)) - идентификатор пользователя в таблице "USERS"
transaction_type (TEXT) - тип транзакции (пополнение или покупка)
amount (NUMERIC(10, 2)) - сумма транзакции

Таблица "ADMINS"
id (SERIAL, PRIMARY KEY) - уникальный идентификатор администратора в базе данных
telegram_id (INTEGER, UNIQUE) - идентификатор администратора в Telegram
telegram_username (TEXT) - имя пользователя в Telegram




Таблица "CATEGORIES"
id (SERIAL, PRIMARY KEY) - уникальный идентификатор категории в базе данных
name (TEXT, UNIQUE) - название категории

Таблица "PRODUCTS"
id (SERIAL, PRIMARY KEY) - уникальный идентификатор товара в базе данных
category_id (INTEGER, REFERENCES categories(id)) - идентификатор категории в таблице "CATEGORIES"
name (TEXT) - название товара
description (TEXT) - описание товара
price (NUMERIC(10, 2)) - цена товара
quantity (INTEGER) - количество товара в наличии


Таблица "PRODUCT_linkS"
id (SERIAL, PRIMARY KEY) - уникальный идентификатор товара в базе данных
product_id (INTEGER NOT NULL REFERENCES products(id)) – идентификатор товара в таблице PRODUCTS
product_link VARCHAR(255) NOT NULL – ссылка на товар




Таблица "TRANSACTIONS_type"
id (SERIAL, PRIMARY KEY) - уникальный идентификатор пользователя в базе данных
name (TEXT, UNIQUE)


Таблица "BANS"
id (SERIAL, PRIMARY KEY) - уникальный идентификатор пользователя в базе данных
user_id (INTEGER, REFERENCES users(id)) - идентификатор пользователя в таблице "USERS"
reason (TEXT NOT NULL) – причина бана пользователя


в таблицы TRANSACTIONS, PURCHASES, BANNED из таблицы users ИМПОРТИРУЕТСЯ USER_id. 
В таблицу PURCHASES импоритурется product_id ИЗ ТАБЛИЦЫ PRODUCTS
В ТАБЛИЦУ products из таблицы CATEGORIES импоритруется CATEGOry_id
В таблицу TRANSACTIONS импортируется из таблицы TRANSACTIONS_ензу TRANSACTION_id
____________________________________________________________________________________________
SQL shell
1) Создание бд

CREATE DATABASE telegramshop
  WITH ENCODING='UTF8'
  LC_COLLATE='en_US.UTF-8'
  LC_CTYPE='en_US.UTF-8'
  TEMPLATE=template0;
  
  2) Подключение
  \c telegramshop
  
  3) Создание таблиц
  -- Таблица "USERS"
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  telegram_id INTEGER UNIQUE,
  telegram_username TEXT,
  balance NUMERIC(10, 2)
);

-- Таблица "PURCHASES"
CREATE TABLE PURCHASES (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    product_id INTEGER REFERENCES products(id),
    product_link TEXT[],
    purchase_time TIMESTAMP WITHOUT TIME ZONE
);

-- Таблица "TRANSACTIONS"
CREATE TABLE transactions (
  id SERIAL PRIMARY KEY,
  user_id INTEGER REFERENCES users(id),
  transaction_type TEXT,
  amount NUMERIC(10, 2)
);

-- Таблица "ADMINS"
CREATE TABLE admins (
  id SERIAL PRIMARY KEY,
  telegram_id INTEGER UNIQUE,
  telegram_username TEXT
);

-- Таблица "CATEGORIES"
CREATE TABLE categories (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE
);

-- Таблица "PRODUCTS"
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  category_id INTEGER REFERENCES categories(id),
  name TEXT,
  description TEXT,
  price NUMERIC(10, 2),
  quantity INTEGER
);

-- Таблица "TRANSACTION_TYPES"
CREATE TABLE transaction_types (
  id SERIAL PRIMARY KEY,
  name TEXT UNIQUE
);

-- Таблица "BANS"
CREATE TABLE BANS (
id SERIAL PRIMARY KEY,
user_id INTEGER NOT NULL,
reason TEXT NOT NULL);

-- Таблица "PRODUCT_linkS"
CREATE YABLE PRODUCT_linkS (
  id SERIAL PRIMARY KEY,
  product_id INTEGER NOT NULL REFERENCES products(id),
  product_link VARCHAR(255) NOT NULL 
)

4) Просмотр всех таблиц
\dt


ADMINS
INSERT INTO ADMINS (telegram_id, telegram_username) VALUES (663582079, '@Ai_digi_digi_dai');

For the "CATEGORIES" table:

INSERT INTO categories (name) VALUES ('VPN');
INSERT INTO categories (name) VALUES ('Accounts');
INSERT INTO categories (name) VALUES ('Steam Key');
INSERT INTO categories (name) VALUES ('Photo/Video Editing');
INSERT INTO categories (name) VALUES ('Courses');

For the "PRODUCTS" table:

-- For the "VPN" category:
INSERT INTO products (category_id, name, description, price, quantity) VALUES (1, 'AlyaskaVPN', 'Budget VPN with basic features and reliable protection.', 300, 100);
INSERT INTO products (category_id, name, description, price, quantity) VALUES (1, 'SuperVPN', 'Mid-level VPN, ideal for everyday use.', 200, 120);
INSERT INTO products (category_id, name, description, price, quantity) VALUES (1, 'Classic Access', 'Premium VPN with additional features, suitable for more advanced users.', 330, 27);
INSERT INTO products (category_id, name, description, price, quantity) VALUES (1, 'Express VPN', 'One of the best VPNs on the market, providing high speed and security, ideal for those who value quality and reliability.', 150, 74);

-- For the "Accounts" category:
INSERT INTO products (category_id, name, description, price, quantity) VALUES (2, 'Vkontakte', 'New account', 15, 400);
INSERT INTO products (category_id, name, description, price, quantity) VALUES (2, 'Instagram', 'New account', 25, 229);
INSERT INTO products (category_id, name, description, price, quantity) VALUES (2, 'Telegram', 'New account', 10, 375);
INSERT INTO products (category_id, name, description, price, quantity) VALUES (2, 'Steam', 'New account', 20, 178);

-- For the "Steam Key" category:
INSERT INTO products (category_id, name, description, price, quantity) VALUES (3, 'Cs:go', 'Prime account', 700, 30);
INSERT INTO products (category_id, name, description, price, quantity) VALUES (3, 'Squad', 'Game only', 750, 13);
INSERT INTO products (category_id, name, description, price, quantity) VALUES (3, 'Men of war assault squad 2', 'All DLCs', 1000, 24);
INSERT INTO products (category_id, name, description, price, quantity) VALUES (3, 'Arma 3', 'Veteran''s Pack', 4500, 3);
INSERT INTO products (category_id, name, description, price, quantity) VALUES (3, 'Cities: Skylines II', 'Ultimate Edition', 2000, 8);
INSERT INTO products (category_id, name, description, price, quantity) VALUES (3, 'Remnant II', 'Ultimate Edition', 2900, 5);

-- For the "Photo/Video Editing" category:
INSERT INTO products (category_id, name, description, price, quantity) VALUES (4, 'Happy New Year Pack', 'Pack of New Year graphics elements for creating congratulatory videos and cards', 1500, 0);
INSERT INTO products (category_id, name, description, price, quantity) VALUES (4, 'Instagram Stories', 'Pack of graphic elements for creating beautiful and original stories on Instagram. Includes templates and decor elements that will help you create professional stories that will attract the attention of your audience.', 1000, 0);
INSERT INTO products (category_id, name, description, price, quantity) VALUES (4, 'Film Noir', 'Pack of graphic elements for creating mysterious films in the noir style. Contains various templates, effects, and decor elements that will help create the atmosphere of classic cinema.', 2500, 0);

-- For the "Courses" category:
INSERT INTO products (category_id, name, description, price, quantity) VALUES (5, 'Python Course', 'Course on learning the Python programming language for beginners. Includes theory and practical exercises.', 5000, 15);
INSERT INTO products (category_id, name, description, price, quantity) VALUES (5, 'Photography Course', 'Course on learning the basics of photography, including camera settings, working with light, and composition. Suitable for beginner photographers.', 3500, 10);
INSERT INTO products (category_id, name, description, price, quantity) VALUES (5, 'Marketing Course', 'Course on learning the basics of marketing, including market research, product promotion, and results analysis. Suitable for beginner marketers.', 6000, 5);
INSERT INTO products (category_id, name, description, price, quantity) VALUES (5, 'Sales Course', 'Course on learning the basics of sales, including sales techniques, sales management, and improving results. Suitable for beginner salespeople.', 4500, 7);


TRANSACTION_TYPES
INSERT INTO transaction_types (name) VALUES ('refill'), ('payment');
