Это Flask-приложение, работающее с базой данных PostgreSQL. Проект развертывается с использованием Docker Compose.

#Инструкция по установке и запуску

Склонируйте репозиторий на ваш сервер или локальную машину:  git clone https://github.com/kukidon820/yhjo67-Flask.git  

Далее cd yhjo67 

После этого установить на машину docker и docker-compose sudo apt-get update

sudo apt-get install docker.io -y

sudo systemctl start docker

sudo systemctl enable docker

sudo curl -L "https://github.com/docker/compose/releases/download/v2.17.3/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

Далее необходино собрать образ командой sudo docker-compose up --build -d

sudo docker-compose down

sudo docker-compose up -d

Далее необходимо перейти на старницы нужно перейти на старницу http://localhost:8000/ 

И того, после запуске будет две старницы - 1.http://localhost/ 2.http://localhost/results

Вся работа по развертыванию и запуску складывается на docker. Мы собираем образы сразу приложения, бд  
