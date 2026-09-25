FROM python:3.14-slim AS build
WORKDIR /guide
COPY requirements-docs.lock .
RUN pip install --no-cache-dir -r requirements-docs.lock
COPY mkdocs.yml .
COPY docs docs
COPY overrides overrides
COPY data data
COPY scripts/render_data.py scripts/render_data.py
RUN python scripts/render_data.py && python -m mkdocs build --strict

FROM python:3.14-slim
WORKDIR /site
COPY --from=build /guide/site /site
USER 65532:65532
EXPOSE 8000
HEALTHCHECK --interval=30s --timeout=3s CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/', timeout=2)"
CMD ["python", "-m", "http.server", "8000", "--bind", "0.0.0.0", "--directory", "/site"]
