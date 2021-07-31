FROM python:3.9.6-slim-buster

COPY ./entrypoint.sh /
COPY ./test_assignment /test_assignment
RUN chmod 755 /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
