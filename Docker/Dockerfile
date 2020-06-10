FROM continuumio/anaconda3:4.4.0
COPY . /app
EXPOSE 8004
WORKDIR /app
RUN pip install -r requirements.txt
CMD python flask_api.py