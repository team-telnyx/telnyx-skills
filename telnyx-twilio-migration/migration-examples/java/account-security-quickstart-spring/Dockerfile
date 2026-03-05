FROM openjdk:11

WORKDIR /usr/app/

RUN apt-get update && \
  apt-get upgrade -y && \
  apt-get install -y build-essential

COPY . .

RUN make install

EXPOSE 8080

CMD ["make", "serve"]
