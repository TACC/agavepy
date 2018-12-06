FROM python:3.6.6-stretch


# Install python $PYVERSION.
ARG PYVERSION=2.7.15

RUN apt-get update -y && apt-get install -yq git bash-completion \
    curl vim tree \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /src/.*deb \
    && wget https://www.python.org/ftp/python/${PYVERSION}/Python-${PYVERSION}.tgz \
    && tar -xvf Python-${PYVERSION}.tgz \
    && cd Python-${PYVERSION} \
    && ./configure --with-ensurepip=install \
    && make \
    && make altinstall \
    && ln -sf /usr/local/bin/python2.7 /usr/bin/python2 \
    && cd ../ \
    && rm -r Python-${PYVERSION}.tgz Python-${PYVERSION} \
    && pip install sphinx \
    && pip install pytest \
    && pip2.7 install mock

RUN git clone https://github.com/TACC/agavepy 

WORKDIR /agavepy

ADD https://raw.githubusercontent.com/alejandrox1/dev_env/master/local-setup/bashrc /root/.bashrc
ADD https://raw.githubusercontent.com/alejandrox1/dev_env/master/local-setup/bash_prompt /root/.bash_prompt

CMD ["/bin/bash"]
