FROM continuumio/miniconda3

COPY environment.yml /

RUN conda update -n base conda -y && conda env update

WORKDIR /code

COPY ./app /code/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
