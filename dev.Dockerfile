FROM python:3.6.6-stretch


RUN apt-get update -y && apt-get install -yq git bash-completion \
    curl vim tree \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /src/.*deb

RUN git clone https://github.com/TACC/agavepy 

WORKDIR /agavepy

ADD https://raw.githubusercontent.com/alejandrox1/dev_env/master/local-setup/bashrc /home/$USER/.bashrc
ADD https://raw.githubusercontent.com/alejandrox1/dev_env/master/local-setup/bash_prompt /home/$USER/.bash_prompt

CMD ["/bin/bash"]
