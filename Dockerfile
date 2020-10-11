FROM python:3.8.2
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN python -m pip install --upgrade pip

RUN apt-get update && apt-get install nginx -y --no-install-recommends
COPY nginx.default /etc/nginx/sites-available/default

RUN mkdir -p /opt/djangoapp
RUN mkdir -p /var/log/gunicorn
WORKDIR  /opt/djangoapp

COPY . .
RUN pip install -r requirements.txt
RUN chown -R www-data:www-data /opt/djangoapp

EXPOSE 8030
STOPSIGNAL SIGTERM
CMD ["./start-server.sh"]