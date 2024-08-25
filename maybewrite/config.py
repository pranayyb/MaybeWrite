# import os
# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY','default_sec_key')
#     SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
#     SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT', 'your_default_salt')
#     MAIL_SERVER='smtp.googlemail.com'
#     MAIL_PORT=587
#     MAIL_USE_TLS = True
#     MAIL_USERNAME = os.environ.get('EMAIL_USER')
#     MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

# # print("SQLALCHEMY_DATABASE_URI:", os.environ.get('SECRET_KEY'))
# # print("SECRET_KEY:", os.environ.get('SECRET_KEY'))
# # print("SQLALCHEMY_DATABASE_URI:", os.environ.get('SQLALCHEMY_DATABASE_URI'))
# # print("EMAIL_USER:", os.environ.get('EMAIL_USER'))
# # print("EMAIL_PASS:", os.environ.get('EMAIL_PASS'))
# # print("SECURITY_PASSWORD_SALT:", os.environ.get('SECURITY_PASSWORD_SALT'))

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', '5791628bb0b13ce0c676dfde280ba245')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///site.db')  # Default to SQLite
    SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT', '4dba005e18d58b6c1d8ba405bca4716e')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
