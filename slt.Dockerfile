FROM python:3.8-buster

RUN apt-get update -y && apt-get install -yq git bash-completion nano curl tree
        # && pip install sphinx \
        # && pip install pytest

WORKDIR /agavepy

COPY . /agavepy

CMD ["/bin/bash"]