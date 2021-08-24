# DjangoBlog
An application to manage a multilingual blog inside your Django website with Arabic and English languages

# Demo
## https://multilanguageblog.herokuapp.com/
 
# editor account
 ### https://multilanguageblog.herokuapp.com/en/login/
* username = demo
* password = demodemo123

### home page
![home page](https://user-images.githubusercontent.com/75542426/130702708-fde73a82-d410-45ee-868a-3879110dc236.png)

### author dashboard
![author dashboard](https://user-images.githubusercontent.com/75542426/130702746-178ec75f-c0d2-4861-95bc-ba1216fa1139.png)


# Usage
It's best to install Python projects in a Virtual Environment. Once you have set up a Virtual Environment, clone this project
 ```
 git clone https://github.com/M0hamedEmad/django-blog.git
 ```
 then cd to file and Run
 ```
pip install -r requirements.txt #install required packages
python manage.py migrate # run first migration
python manage.py runserver # run the server
 ```
 then open in your browser http://127.0.0.1:8000/
 
 # Make a Superuser
 Run
 ```
 python manage.py createsuperuser
 ```
 then write a username, email, password 
 go to http://127.0.0.1:8000/admin  a django admin
 or http://127.0.0.1:8000/dashboard  a dashboard for admin and editors
 

