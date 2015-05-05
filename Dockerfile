FROM ipython/notebook

COPY . /agavepy
WORKDIR /agavepy
RUN pip install -r requirements.txt
RUN python setup.py develop

ENV AGAVE_HOST ""

COPY notebooks /notebooks
COPY notebooks/notebook.sh /notebook.sh
RUN chmod +x /notebook.sh
WORKDIR /notebooks
