# Django Custom User Template
- Custom User Authentication Template To Build Django App Faster Since Making Custom Authentication System Is So Annoying As Hell

### What Account Module consist of
- Name (Main ID)
- Email
- Phone-Number
- profile_image (Can be Null)
- Password

### How to start
1. Look for changes in model by typing: `python manage.py makemigrations account`
2. Migrate SQL: `python manage.py migrate`
3. Create Superuser Account: `python manage.py createsuperuser`
4. Run server: `python manage.py runserver`


### Files to look at other than Account Template
#### Settings.py
- AUTH_USER_MODEL variable
- INSTALLED_APPS variable (list)
