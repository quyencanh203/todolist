## if you want to run app then you make to step by step below
#### clone and cd
git clone https://github.com/quyencanh203/todolist.git
cd todolist
#### run docker compose up 
docker compose up
#### open new terminal and change struction of database default
docker exec -it todolist-web-1 bash -c "python manage.py migrate"
#### make user of database
docker exec -it todolist-web-1 bash -c "python manage.py createsuperuser --username=username --email=email"
#### connect to phpmyadmin
docker run -d --name myphpmyadmin -e PMA_HOST=db -e PMA_PORT=3306 -e PMA_USER=your_username -e PMA_PASSWORD=your_password -p 8080:80 --network todolist_default phpmyadmin/phpmyadmin

http://localhost:8000/todo/
http://localhost:8000/diabetes/
http://localhost:8080/index.php?route=/sql&pos=0&db=todolist&table=todo_task
http://localhost:8000/admin/login/?next=/admin/
## --------------------note for command--------------------------
## Build a container from Dockerfile
docker build -t todolist .

## Make container for project todolist
docker run -v $(pwd):/app -p 8000:8000 todolist bash -c "django-admin startproject todolist ."

## execute a container
docker exec -it todolist-web-1 bash

## make the changing to database 
python manage.py migrate 

## make migration for todo 
python manage.py makemigrations todo 

## creating an admin user
python manage.py createsuperuser --username=nguyenvana --email=a.@gmail.com

## add header and footer template on each page in django
https://medium.com/@mshrimad/add-header-and-footer-template-on-each-page-in-django-f718774b3fdb

## format code in vscode 
https://sentry.io/answers/format-code-in-visual-studio-code/#:~:text=To%20format%20the%20contents%20of,and%20execute%20%E2%80%9CFormat%20Document%E2%80%9D.

## use phpmyadmin connecting to mariadb
docker run -d --name myphpmyadmin -e PMA_HOST=db -e PMA_PORT=3306 -e PMA_USER=your_username -e PMA_PASSWORD=your_password -p 8080:80 --network todolist_default phpmyadmin/phpmyadmin