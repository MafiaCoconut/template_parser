# template_parser

Инструкция по загрузке проекта на ПК
1) Заходим в Pycharm
2) Отрываем папку где будет находится эта программа
3) В консоль пишем:
---------
      git clone https://github.com/MafiaCoconut/template_parser.git
      
4) Перейти через File/Open в папку template_parser 
---------
      pip install virtualenv
      virtualenv venv
      venv\Scripts\activate.bat
      
5) Закрываем консоль и открываем ещё раз, чтобы перед началом строки появилось (venv)
---------
      pip install -r requirements.txt

6) Теперь вам нужно перейти в ветку в которой вы будете работать, для этого пропишите код ниже и в конце через пробел добавьте название ветки, которое я вам скинул
---------
      git checkout
      
7) Если вы сделали всё правильно, то отобразится: Switched to a new branch 'Название ветки'
8) Теперь вы можете начинать работать

Инструкция по работе с проектом:
1) В функции main меняем url на тот, над которым вы будете работать
2) Запускаете сначала функцию get_data не меняя параметры для скачивания сайта на ПК
3) Комментируете функцию get_data и откомментируете функцию work_with_main_page, в ней будет весь основной код

Дополнительная информация:
1) Каждый пишет в своей ветке, чтобы не возникло трудностей в конце
2) В файле test.py и test.json показано как работает json и словари
3) Все данные сохраняем в папку data, для этого когда открываете файл, прописываете 'data/' перед названием файла.
Пример: 'data/test.txt'

