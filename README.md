django-toronto
==============
Website for the Django Toronto meetup.

Local Development
=================

1. `pip install -r requirements.txt`
2. Set up database
3. Set up these environment variables:
  * AWS_ACCESS_KEY_ID
  * AWS_SECRET_ACCESS_KEY
  * SECRET_KEY

Database Setup
==============

1. Create local_settings.py
2. Add the following:

```python
import dj_database_url

DATABASES = {'default': dj_database_url.parse('sqlite:////path/to/dev/database.db')}
```
