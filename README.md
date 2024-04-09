# htmx examples

</br>

## Local Development
### prerequisites
1. git installed on the dev system
2. python installed on the dev system 


### setup steps (in a terminal)
1. clone the repo:

    ```
    git git@github.com:davidslusser/spug_20240416.git
    ```


2. cd into the repo directory
    ```
    cd spug_20240416
    ```

3. create a python virtual environment
    ```
    python -m venv venv
    ```

4. activate the python virutal environment
    ```
    source venv/bin/activate
    ```

5. install the python dependancies
    ```
    pip install -r requirements.txt
    ```

6. cd to the django_project directory
    ```
    cd django_project
    ```

7. create a local sqlite3 database by running django migrations
    ```
    ./manage.py migrate
    ```

8. create a local admin user
    ```
    ./manage.py createsuperuser
    ```


10. start the local demo server
    ```
    ./manage.py runserver
    ```

11. open a browser and navigate to http://127.0.0.1:8000


    ** you can stop the local demo server anytime via ```ctrl + c ```
