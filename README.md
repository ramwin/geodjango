#### Xiang Wang @ 2017-12-18 17:09:02

# run a test
```
    find . -name 'migrations' | xargs rm
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py
```
