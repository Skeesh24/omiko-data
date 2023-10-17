
for /F "tokens=*" %%e in (cat .env) do set %%e

py app/main.py