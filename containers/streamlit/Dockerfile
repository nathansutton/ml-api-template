FROM continuumio/miniconda3

EXPOSE 8501

WORKDIR /app

COPY environment.yml ./environment.yml

RUN conda update -n base conda -y && conda env update

COPY app.py ./app.py

CMD streamlit run app.py
