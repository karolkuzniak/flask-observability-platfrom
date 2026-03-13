FROM python:3.11

WORKDIR /app

#kopiuj link z bibliotekami
COPY app/requirements.txt .

#instalacja bibliotek
RUN pip install -r requirements.txt

#kupiuj kod aplikacji
COPY app/ .

#uruchamianie aplikacji
CMD ["python", "app.py"]