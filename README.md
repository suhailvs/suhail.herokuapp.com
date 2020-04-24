# suhail.herokuapp.com


## Heroku

+ create and app at https://dashboard.heroku.com/apps/
+ click `Deploy` Tab -> Deploy method `Github`
+ Manual deploy, select `heroku` branch, click `Deploy Branch`
+ Install heroku `$ sudo snap install --classic heroku`
+ logs `$ heroku logs -a suhail` 
+ `$ heroku run -a suhail python manage.py migrate`