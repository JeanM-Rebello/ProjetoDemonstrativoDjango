FROM python:3.11.3-alpine3.18

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./django_project /django_project
COPY ./scripts /scripts
COPY ./entrypoint.sh /entrypoint.sh

WORKDIR /django_project

EXPOSE 8000

RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /django_project/requirements.txt && \
    apk add --no-cache postgresql-client&&\
    adduser --disabled-password --no-create-home appuser && \
    mkdir -p /django_project/staticfiles && \
    chown -R appuser:appuser /django_project && \
    chmod -R +x /scripts && \
    chmod +x /scripts/* && \
    chmod +x /entrypoint.sh

ENV PATH="/scripts:/venv/bin:$PATH"

RUN example.sh

ENTRYPOINT ["/entrypoint.sh"]