FROM nginx:1.19.0-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY django-nginx.conf /etc/nginx/conf.d
RUN mkdir /usr/share/nginx/html/media
RUN mkdir /usr/share/nginx/html/static