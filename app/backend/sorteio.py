from flask import render_template, request, redirect, url_for, flash
from app import app
from app.Random_name import Random_name

listadenomes = []


@app.route('/', methods=['GET', 'POST'])
def SorteioComNomes():
    action = request.form.get('action')  # variável para idêntificar as ações dos botões do front-and
    if request.method == 'POST':
        nome = request.form.get('nome')
        # lógica para adicionar nome a lista
        if action == 'Adicionar':
            for indice, item in enumerate(listadenomes):
                if item['nome'] == nome:
                    listadenomes.remove(listadenomes[indice])
                    break
                    listadenomes.append(item)
                    return redirect(url_for('SorteioComNomes'))
        if nome:
            dicionario = {'nome': nome}
            listadenomes.append(dicionario)

        # Lógica para limpar a lista
        if action == 'limpar lista':
            listadenomes.clear()

        # Lógica para sortear o nome
        if action == 'Sortear':
            for item in range(len(listadenomes)):
                # Variável que recebe o retorno da função de sorteio de nome
                nome_sorteado = Random_name.Sorteio.random_name(listadenomes, "nome")
                return render_template('sorteio.html', nome_sorteado=nome_sorteado,
                                       listadenomes=listadenomes, LenLista=len(listadenomes),
                                       Duplo=False)

    return render_template('sorteio.html', listadenomes=listadenomes, LenLista=len(listadenomes),
                           Duplo=False)


nome_sorteado = []  # Lista que recebe os nomes sorteados
ListaTodosNomes = []  # Lista que recebe a lista acima para ser passada para o front


@app.route('/SortearDupla', methods=['GET', 'POST'])
def SorteioDoisNomes():
    action = request.form.get('action')
    if request.method == 'POST':
        nome = request.form.get('nome')
        if action == 'adicionar':
            for indice, item in enumerate(listadenomes):
                if item['nome'] == nome:
                    listadenomes.remove(listadenomes[indice])
                    break
                    listadenomes.append(item)
                    return redirect(url_for('SorteioDoisNomes'))
        if nome:
            dicionario = {'nome': nome}
            listadenomes.append(dicionario)

        if action == 'limpar lista':
            listadenomes.clear()
            nome_sorteado.clear()
            ListaTodosNomes.clear()

        if action == 'Sortear':
            if listadenomes:
                for i in range(0, 2):
                    nomes = Random_name.Sorteio.Two_random_name(listadenomes, "nome")
                    nome_sorteado.append(nomes['nome'])
                    if len(nome_sorteado) == 2:
                        ListaTodosNomes.append(nome_sorteado)
                        break
                return render_template('sorteio.html', ListaTodosNomes=ListaTodosNomes,
                                       listadenomes=listadenomes, LenLista=len(listadenomes),
                                       Duplo=True)
    return render_template('sorteio.html', listadenomes=listadenomes, LenLista=len(listadenomes),
                           Duplo=True)
