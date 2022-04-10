FROM python:3.7

LABEL maintainer=eray.liao@gmail.com

COPY requirements.txt /
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /app

COPY . .

EXPOSE 5000
ENV PORT 5000

# Use gunicorn as the entrypoint
CMD exec gunicorn --bind :$PORT app:app --workers 1 --threads 1 --timeout 60

#ENV APP_ENVIRONMENT development
#
#ENV FLASK_APP app.py

#EXPOSE 5000

#CMD ["sh", "-c", "python app.py"]
