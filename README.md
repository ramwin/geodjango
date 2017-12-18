#### Xiang Wang @ 2017-12-18 17:09:02

# run a test
* create a database
* change your database name, user and password in `geodjango/settings.py` line 87 to line 89
* run the following code
```
    rm -rf world/migrations  # run this command if it is your first time to test the code
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py run
```
