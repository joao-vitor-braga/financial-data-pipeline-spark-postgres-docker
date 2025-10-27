FROM apache/spark-py:v3.3.1
WORKDIR /opt/spark
COPY . .
CMD ["/opt/spark/bin/spark-submit", "--master", "local[*]", "--jars", "/opt/spark/jars/postgresql-42.2.18.jar", "/opt/spark/tratamento/tratamento_movimentoflat.py"]