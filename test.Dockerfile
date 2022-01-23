FROM tiangolo/uwsgi-nginx-flask:python3.7

LABEL maintainer=eray.liao@gmail.com

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

#ENV APP_ENVIRONMENT development
#
#ENV FLASK_APP app.py

#EXPOSE 5000

#CMD ["sh", "-c", "python app.py"]
