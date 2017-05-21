# multiDbApp
"""bash
#clone the project
git clone https://github.com/tusharcoder/multiDbApp.git

#make virtual environment
virtualenv venv -p python3
#activate the environment
source venv/bin/activate

cd multiDbApp

#install dependencies
pip install -r requirements.txt

#login to mysql and create databases user - root, password - root
mysql -u root -p
root

create database testdb1;
create database testdb2;
create database testdb3;
create database testdb4;
create database testdb5;

#run migrations
python manage.py migrate core testdb1 
python manage.py migrate core testdb2
python manage.py migrate core testdb3
python manage.py migrate core testdb4
python manage.py migrate core testdb5  
python manage.py migrate default

#create super user
python manage.py createsuperuser

#run command to populate the database, testdb1, testdb2.... are the arguments
python manage.py populate_db testdb1 
python manage.py populate_db testdb2
python manage.py populate_db testdb3
python manage.py populate_db testdb4
python manage.py populate_db testdb5  

#run the server
python manage.py runserver
#go to browser to see the test data from multiple databases
#http://localhost:8000/test/ 
#to go to admin backend of testdb1
#http://localhost:8000/testdb1_admin/
#enter crerdentials
#user:- admin
#password:- qazplmq1w2e3r4
#for admin of testdb2
#http://localhost:8000/testdb1_admin/ 
#and so on....
"""
