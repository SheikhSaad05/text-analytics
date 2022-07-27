#FROM python:3.8-alpine

FROM python:3.9


RUN pip3 install --upgrade pip
#RUN apt-get install --no-cache gcc make musl-dev python3-dev libffi-dev openssl-dev libxslt-dev && pip3 install --upgrade pip
#RUN apt-get install  libsodium-dev libxml2-dev libxslt-dev libffi-dev gcc musl-dev libgcc openssl-dev curl
#RUN apt-get install jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev cargo

RUN pip3 install --upgrade setuptools wheel
RUN pip3 install pybind11

# RUN apt-get update \
# 	&&  pip install numpy==1.17.3 \
# 	&&  pip install scipy
RUN apt-get update

#RUN (curl -Ls https://cli.doppler.com/install.sh || wget -qO- https://cli.doppler.com/install.sh) | sh
COPY requirements.txt /requirements.txt
#RUN pip3 install poetry && pip3 install --no-build-isolation pendulum==2.1.0
#RUN SODIUM_INSTALL=system pip install pynacl
RUN pip install -r requirements.txt
RUN pip install transformers==4.11.3
RUN pip install gunicorn
COPY . /app
WORKDIR /app
#ARG DOPPLER_SECRET
#RUN doppler secrets download -t $DOPPLER_SECRET --format=env-no-quotes --no-file > .env
#RUN pip3 freeze
CMD ["gunicorn", "-w", "1", "--threads", "4", "--bind", ":5014", "run_keywords:app"]
