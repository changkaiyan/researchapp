# Research Management
[中文](https://github.com/changkaiyan/researchapp/blob/master/readme.md)

A management platform for reseachers.  
With this application, researchers can write summary with markdown.

![Reseach management](./Capture.PNG)

## How to use

1. Open cmd at root path:
~~~bash
pip install -r requirements.txt # install requirements
python manage.py runserver 8000 # launch sever and sqllite
~~~

2. Open browser, browse [http://127.0.0.1:8000/admin](browse http://127.0.0.1:8000/admin), then you can see the UI. The initial user and password are both *admin*.


> Note that each **paper** and **project** must belong to a **research**, and each **task** should be held under **researches** either. Make sure that you have built your own research before any further operation.


Have fun and star it!  
Please feel free to report bugs or post your comments on issue. Hope this app can boost your research!