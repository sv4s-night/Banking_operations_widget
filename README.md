# `Banking operations widget`

Программа создана для разнообразных операций с банковскими счетами.
(С полными возможностями можно ознакомиться в графе Функции)

## Project dependencies:

- The program uses the version Python 3.12.4
- flake8 = "7.0.0"
- black = "24.4.2"
- isort = "5.13.2"
- mypy = "1.10.0"
- pytest = "^8.2.2"
- pytest-cov = "^5.0.0"
- python-dotenv = "^1.0.1"

## Функции, используемые для работы с банковскими счетами:

- Функция скрывающая номер карты и счета
- Функция сортировки по дате
- Функция фильтрации в операциях по счетам
- Функция отображающая операции по указанной валюте
- Функция возвращающая описание каждой операции по очереди
- Функция генерирующая номера карт в заданном диапазоне
- Функция выгружающая из json-файла информацию о финансовых транзакциях
- Функция проверки соответствия к выбранной валюте. 
```Если валюта не соответствует выбранной, то происходит процесс конвертации```
```Конвертация валюты происходит через сайт API Apilayer.com```

## Структура проекта

В проект добавлен директория tests, для тестирования кода программы c помощью фреймворка pytest,
так же реализован декоратор логирования, регистрирующий детали выполнения функций.

Декоратор логирования автоматически записывает начало и конец выполнения функции, 
а также ее результаты или возникшие ошибки.

Декоратор принимает в себя необязательный аргумент filename, который определяет, 
куда будут записываться логи (в файл или в консоль):

Если filename задан, логи записываются в указанный файл.
Если filename не задан, логи выводятся в консоль.

```Присутствует файл .env.example в котором указаны переменные окружения для работы с внешними ресурсами```

# Инструкция по установке

Чтобы скачать репозиторий:

`git clone https://github.com/sv4s-night/feature-homework_10_1.git`

Затем вам необходимо установить основные зависимости для запуска проекта в вашей системе:

```pip install -r requirements.txt```

Подождите, пока наборы данных загрузятся, это может занять некоторое время.


## Внешние ресурсы и работа с ними
В программе используется сервис:
- Exchange Rates Data API для конвертации валюты [apilayer.com](https://apilayer.com/marketplace/exchangerates_data-api)
```С документацией, по работе с продуктом, можно ознакомиться по вышеуказанной ссылке``` 


## Тестирование

Для проведения тестирования, Вам необходимо установить Pytest 🔧

```poetry add --group dev pytest```

Для анализа покрытия кода необходимо поставить библиотеку pytest-cov

```poetry add --group dev pytest-cov```

### Терминальные команды для тестирования:

Запуск тестов с оценкой покрытия

```poetry run pytest --cov```

Запуск теста по конкретному модулю

```pytest --cov=<Название модуля>```

В данном проекте можно ознакомиться с отчетами о покрытии тестами в файле index.html, которые находятся в папке htmlcov.
Для генерации повторного отчет в HTML-формате необходимо ввести команду:

```pytest --cov=<Название модуля> --cov-report html```

## Команда проекта:

`Александр Свешников — Back-End Engineer` 🔧👿

## Контакт для связи с командой разработки:

`sv4s-night@gmail.com` 🌒

## Источники

Программа создана при поддержке онлайн-школы [skypro@skyeng.ru](https://sky.pro/#giftpopup)

![alt текст](https://static.tildacdn.com/tild3364-3965-4237-b664-363533643431/Group_1321317003.svg)


