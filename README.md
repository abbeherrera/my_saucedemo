# Тест сайта https://www.saucedemo.com
файл tz1_saucedemo_expl_wait.py для запуска теста сайта https://www.saucedemo.com в режиме explicit wait
файл tz1_saucedemo.py для запуска теста сайта https://www.saucedemo.com в режиме implicit wait

## Системные требования
	Windows 10 или Ubuntu >=20
## Установка и запуск
Скопировать файлы в директорию.
Установка окружения путем запуска в командной строке:
```sh
pip install -r requirements.txt
```
Переход в директорию для Windows:
```sh
cd C:\projects\example.py
```
для Linux:
```sh
cd /your_path
```
в файле .env  константа BROWSER="1" для драйвера selenium Chrome, BROWSER="2" для драйвера selenium Firefox, BROWSER=="3" для драйвера selenium Edge, BROWSER=="4"  для драйвера selenium  Safari (кавычки необходимы!).
Запуск
```sh
python tz1_saucedemo_expl_wait.py
```
или для другого скрипта:
```sh
python tz1_saucedemo.py
```
Команда "python", возможно, в виде "python3".


    
