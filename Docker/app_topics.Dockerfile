# #FROM python:3.8-alpine
# FROM huggingface/transformers-tensorflow-cpu
# RUN pip3 install --upgrade pip
#
# RUN pip3 install --upgrade setuptools wheel
# RUN pip3 install pybind11
#
# COPY requirements.txt /tmp/requirements.txt
#
# RUN pip3 install -r /tmp/requirements.txt
#
# RUN pip3 install gunicorn
# COPY . /app
# WORKDIR /app
#
# CMD ["gunicorn", "-w", "1", "--threads", "4", "--bind", ":5013", "run_topics:app"]