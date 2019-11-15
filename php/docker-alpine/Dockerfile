FROM php:7.3-fpm-alpine

RUN apk update && apk upgrade \
  && apk add curl \
  && apk add zlib-dev libzip-dev
RUN docker-php-ext-install zip pdo_mysql

RUN curl -sS https://getcomposer.org/installer \
    | php -- --install-dir /usr/local/bin --filename composer
ENV COMPOSER_ALLOW_SUPERUSER 1
ENV COMPOSER_HOME /composer
ENV PATH $PATH:/composer/vendor/bin
