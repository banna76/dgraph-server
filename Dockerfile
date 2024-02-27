FROM python

WORKDIR /strawberry_server

COPY . .

RUN python -m venv virtualenv

RUN pip install strawberry-graphql[debug-server]

ENV PORT=8000

EXPOSE 8000

CMD strawberry server schema