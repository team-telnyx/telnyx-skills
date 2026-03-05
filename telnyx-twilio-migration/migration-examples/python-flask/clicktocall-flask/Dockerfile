FROM python:3.8

WORKDIR /usr/src/app

COPY requirements.txt ./

COPY Makefile ./

RUN make install

COPY . .

EXPOSE 5000

CMD ["sh", "-c", ". /usr/src/app/venv/bin/activate && make serve"]
