from fastapi import FastAPI
import controller

app = FastAPI()


@app.get("/buscar-por-nome/{nome}")
def get_cep_nome(nome: str):
    retorno = controller.busca(nome.title())
    if retorno == None:
        retorno = controller.busca2(nome.title())
        if retorno == None:
            return {f"mensage":f"nome { {nome} } inexistente"}
        return retorno
    else:
        return retorno



@app.get("/buscar-todos/")
def get_datas():
    data = controller.show()
    lista = []
    for x in data.fetchall():
        cidade = x[1]
        distrito = x[2]
        bairro = x[3]
        cep = x[4]
        distritosJson = {
                    distrito: {
                        "cidade": cidade,
                        "distrito": distrito,
                        "bairro": bairro,
                        "cep": cep
                    }
                }
        lista.append(distritosJson)

    data2 = controller.show2()
    lista2 = []
    for x in data.fetchall():
        provincia = x[1]
        distrito = x[2]
        postoadmin = x[3]
        cep = x[4]
        distritosJson2 = {
                    distrito: {
                        "provincia": provincia,
                        "distrito": distrito,
                        "posto administrativo": bairro,
                        "cep": cep
                    }
                }
        lista2.append(distritosJson2)
    return lista, lista2
