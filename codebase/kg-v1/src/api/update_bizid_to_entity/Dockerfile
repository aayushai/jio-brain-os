FROM python:3.9

ENV APP /app

RUN mkdir $APP
WORKDIR $APP

EXPOSE 31034

COPY . .
RUN python -m pip install --upgrade pip
RUN pip3 install -r api/update_bizid_to_entity/requirements.txt --no-cache-dir --trusted-host 10.141.51.157 --trusted-host nexus.rjil.ril.com --index-url http://Brain_os:Brain_os@nexus.rjil.ril.com:9081/repository/Brain_os-py-group/simple/

CMD [ "make", "server_update_bizid_to_entity" ]
