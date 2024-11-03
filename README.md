# email-daemon

## Setup Steps

1. Create .env config with the following format

```
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_ADDRESS=your_email
EMAIL_PASSWORD=your_app_password
TO_ADDRESS=your_email
```

2. Run `crontab -e` and add the following line:

```
0 9 * * 1 /usr/bin/python3 <absolute path to reporter.py>
```