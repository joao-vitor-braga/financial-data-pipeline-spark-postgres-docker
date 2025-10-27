from pyspark.sql import SparkSession
import os

spark = (SparkSession.builder.appName("processa_movimento_flat").getOrCreate())

####postgreSQL - conexão com feita c/ o banco
pg_host = os.getenv("POSTGRES_HOST")
pg_port = os.getenv("POSTGRES_PORT")
pg_db = os.getenv("POSTGRES_DB")
pg_user = os.getenv("POSTGRES_USER")
pg_password = os.getenv("POSTGRES_PASSWORD")

jdbc_url = f"jdbc:postgresql://{pg_host}:{pg_port}/{pg_db}"

conn_props = {
    "user": pg_user,
    "password": pg_password,
    "driver": "org.postgresql.Driver"
}

####caminho de saída para o arquivo csv que será gerado, através da variavel exposta no .env.
output_caminho = os.getenv("CSV_OUTPUT_PATH", "/opt/spark/data/output/movimento_flat")

####lendo as tabelas do PostgreSQL.
tabelas = ["associado", "conta", "cartao", "movimento"]
dfs = {t: spark.read.jdbc(jdbc_url, t, properties=conn_props) for t in tabelas}

####criando as tempviews para poder trabalhar dentro do spark.sql.
for nome, df in dfs.items():
    df.createOrReplaceTempView(nome)

#####iniciando a construção da tabela final movimento_flat:

####como eu não encontrei no diagrama inicial a coluna data_criacao_cartao, eu acabei não colocando na tabela movimento_flat final.

movimento_flat = """
    SELECT 
        a.nome                AS nome_associado,
        a.sobrenome           AS sobrenome_associado,
        a.idade               AS idade_associado,
        m.vlr_transacao       AS valor_transacao,
        m.des_transacao       AS descricao_transacao,
        m.data_movimento      AS data_movimento,
        ctao.num_cartao       AS numero_cartao,
        ctao.nom_impresso     AS nome_impresso_cartao,
        c.tipo                AS tipo_conta,
        c.data_criacao        AS data_criacao_conta
       
    FROM associado a
    LEFT JOIN conta c         ON a.id = c.id_associado
    LEFT JOIN cartao ctao     ON ctao.id_associado = a.id
    LEFT JOIN movimento m     ON m.id_cartao = ctao.id """

df_mov_flat = spark.sql(movimento_flat)

####tabela final em CSV
os.makedirs(output_caminho, exist_ok=True)

(
    df_mov_flat
    .write
    .mode("overwrite")
    .option("header", True)
    .csv(output_caminho)
)