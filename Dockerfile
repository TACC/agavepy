FROM ipython/notebook

COPY . /agavepy
WORKDIR /agavepy
RUN pip install -r requirements.txt
RUN python setup.py develop

COPY notebooks /notebooks
WORKDIR /notebooks
