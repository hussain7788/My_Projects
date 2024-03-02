# Hashtag Project
=======
# create a new virtual environment - .venv and activate it

    cd HashtagProject
    virtualenv .venv
    .venv\Scripts\activate

# Install the packages using given requirements.txt

    pip install -r requirements.txt

# How to run Django server

    cd HashtagProject\DjangoApp\
    python manage.py runserver

# How to run react server

    cd HashtagProject\react-app\
    npm install
    npm start

# How to run test cases

    cd HashtagProject\DjangoApp\tests\
    Run below command (make sure django server is running)
     - pytest test_hashtags.py -v -s --pdb