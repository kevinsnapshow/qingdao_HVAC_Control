FROM daocloud.io/ncity/gunicorn_flask_latest
ADD . /app
WORKDIR /app
RUN \
&&apt-get update \
&&pip install -i http://pypi.tuna.tsinghua.edu.cn.simple --upgrade pip \
&&pip install -i http://pypi.tuna.tsinghua.edu.cn.simple -r requirements.txt

EXPOSE 6500
ENTRYPOINT ["python"]

CMD ["app.py"]