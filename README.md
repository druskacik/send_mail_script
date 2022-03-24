## Send email script

Treba `.env` súbor tohto formátu:

```
SMTP_SERVER=smtp.office365.com
SMTP_PORT=587
SMTP_USER=
SMTP_PASS=
```

`SMTP_PASS` je kód zo stránky https://cdo.uniba.sk/public/ecp .

Inštalácia libiek:

```
pip install python-dotenv
pip install pystache
```

Spúšťa sa to nasledovne:

```
python index.py
```