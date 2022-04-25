import conexao as con

try:
    conexao, cur = con.create_database()
    cur.execute("CREATE TABLE IF NOT EXISTS cep_table(id INTEGER PRIMARY KEY AUTOINCREMENT,cidade  VARCHAR, distrito VARCHAR, "
                "bairro VARCHAR, cep VARCHAR)")
    cur.execute("CREATE TABLE IF NOT EXISTS cep_table2(id INTEGER PRIMARY KEY AUTOINCREMENT,provincia  VARCHAR, distrito VARCHAR, "
                "postoAdministrativo VARCHAR, cep VARCHAR)")
except:
    pass


def insert(provincia, distrito, postoadmin, cep):
    cur.execute(f"INSERT INTO cep_table2 ('provincia','distrito','postoadministrativo','cep') VALUES ('{provincia}','{distrito}','{postoadmin}'"
                f",'{cep}')")
    conexao.commit()


def show():
    data = cur.execute("SELECT * FROM cep_table")
    return data


def show2():
    data = cur.execute("SELECT * FROM cep_table2")
    return data

def busca(nome):
    data = cur.execute(f"SELECT * FROM cep_table WHERE  bairro = '{nome}'")
    conexao.commit()
    lista = []
    if data.fetchone() != None:
        data = cur.execute(f"SELECT * FROM cep_table WHERE  bairro = '{nome}'")
        conexao.commit()
        for x in data.fetchone():
            lista.append(x)
        cidade = lista[1]
        distrito = lista[2]
        bairro = lista[3]
        cep = lista[4]
        bairroJson = {
            bairro: {
                "cidade": cidade,
                "distrito": distrito,
                "bairro": bairro,
                "cep": cep
            }
        }
        return bairroJson


def busca2(nome):
    data = cur.execute(f"SELECT * FROM cep_table2 WHERE  postoAdministrativo = '{nome}'")
    conexao.commit()
    lista = []
    if data.fetchone() != None:
        data = cur.execute(f"SELECT * FROM cep_table2 WHERE  postoAdministrativo = '{nome}'")
        conexao.commit()
        for x in data.fetchone():
            lista.append(x)
        cidade = lista[1]
        distrito = lista[2]
        bairro = lista[3]
        cep = lista[4]
        bairroJson = {
            bairro: {
                "provincia": cidade,
                "distrito": distrito,
                "posto administrativo": bairro,
                "cep": cep
            }
        }
        return bairroJson