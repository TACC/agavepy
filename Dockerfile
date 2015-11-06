FROM jupyter/scipy-notebook

COPY . /agavepy
WORKDIR /agavepy
RUN /opt/conda/envs/python2/bin/pip install -r requirements.txt
RUN /opt/conda/envs/python2/bin/python setup.py develop

ENV AGAVE_HOST ""

COPY notebooks /notebooks
COPY notebooks/notebook.sh /notebook.sh
RUN chmod +x /notebook.sh
WORKDIR /notebooks
