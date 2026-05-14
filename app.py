"""
Copa do Mundo 2026 - Flask
Dados armazenados apenas em memória
"""

from flask import Flask, render_template, request, redirect, url_for
from seunome import config

app = Flask(__name__)

dados = [[config['username']]]
lista = []


@app.get("/")
def home():
    return render_template(
        "base.html",
        lista_front=lista,
        lista_dados=dados
    )


@app.post("/add")
def add():

    selecao = request.form.get("selecao")
    continente = request.form.get("continente")
    titulos = request.form.get("titulos")

    if selecao != '' and continente != '' and titulos != '':

        time = []

        time.append(selecao.strip())
        time.append(continente.strip())
        time.append(titulos.strip())

        lista.append(time)

        print(f'Add: {lista}')

    else:
        print('** Todos os campos devem ser preenchidos **')

    return redirect(url_for("home"))


@app.post("/sort")
def sort():

    if lista != []:
        print('** Ordenando lista alfabeticamente **')
        lista.sort()

    return redirect(url_for("home"))


@app.post("/reverse")
def reverse():

    global lista

    if lista != []:

        print('** Ordem reversa da lista **')

        lista = sorted(
            lista,
            reverse=True,
            key=lambda x: x[0]
        )

    return redirect(url_for("home"))


@app.post("/clear")
def clear():

    global lista

    print('==> Apagando lista completa <==')

    lista = []

    return redirect(url_for("home"))


@app.get("/delete/<selecao_nome>")
def delete(selecao_nome):

    print(f'==> Removendo seleção: {selecao_nome}')

    for i in range(len(lista)):

        if selecao_nome in lista[i]:

            del lista[i]
            break

    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )