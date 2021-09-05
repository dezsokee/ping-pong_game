FROM python:3

HEALTHCHECK --interval=5s \
            --timeout=5s \
            CMD curl -f hhtp://127.0.0.1:8000

EXPOSE 8000