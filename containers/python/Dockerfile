FROM continuumio/miniconda3

# load in the environment.yml file
COPY environment.yml /

# create the environmnt
RUN conda update -n base conda -y && conda env update