from PyQt5 import uic, QtWidgets, QtCore
import sqlite3


banco = sqlite3.connect('banco.db')
tipo_padrao = ("Padrão")

def exibir_erro_login(mensagem):
    QtWidgets.QMessageBox.about(pt1, 'Erro', mensagem)

def validar_campos(login, senha):
    if not login or not senha:
        exibir_erro_login('Por favor, preencha todos os campos para logar')
        return False
    return True

def verificar_dados_login(cursor, login, senha):
    cursor.execute("SELECT * FROM funcionarios WHERE login = %s AND senha = %s", (login, senha))
    return cursor.fetchone()

def atualizar_status_carros(cursor):
    cursor.execute("SELECT nome_carro, ocup FROM carros")
    result = cursor.fetchall()

    carros_status = {
        "Kwid": (pt3.kwid, pt3.devkwid),
        "Mobi": (pt3.mobi, pt3.devmobi),
        "Argo": (pt3.argo, pt3.devargo),
        "Gol": (pt3.gol, pt3.devgol),
        "Compass": (pt3.compass, pt3.devcompass),
        "Hrv": (pt3.hrv, pt3.devhrv)
    }

    for nome_carro, ocup in result:
        if nome_carro in carros_status:
            carro, devcarro = carros_status[nome_carro]
            carro.setEnabled(ocup != "1")
            devcarro.setEnabled(ocup == "1")

def tratar_tipo_usuario(tipo_usuario):
    pt1.close()
    pt2.show()
    pt2.funcionario.setEnabled(tipo_usuario != tipo_padrao)
    print(tipo_padrao if tipo_usuario == tipo_padrao else "gestor")

def logar():
    login = pt1.loginspace.text()
    senha = pt1.pinspace.text()

    if not validar_campos(login, senha):
        return

    try:
        cursor = banco.cursor()
        usuario = verificar_dados_login(cursor, login, senha)

        if usuario:
            atualizar_status_carros(cursor)
            tratar_tipo_usuario(usuario[3])
        else:
            pt1.infoname.setText("Dados incorretos")
            pt1.pinspace.setText("")
            pt1.loginspace.setText("")
    except Exception as e:
        print(f"Erro ao validar os dados: {e}")


#FUNCOES LOGOUT
def logout():
    pt2.close()
    pt1.infoname.setText("")
    pt1.pinspace.setText("")
    pt1.loginspace.setText("")
    pt1.show()

def logout3():
    pt3.close()

def logout4():
    pt4.close()

def logout41():
    pt41.close()

def logout42():
    pt42.close()

def logout5():
    pt5.close()

def logout51():
    pt51.close()

def logout52():
    pt52.close()

def logout6():
    pt6.close()

def logout61():
    pt61.close()

def logout62():
    pt62.close()

def logout7():
    pt7.close()

def logout71():
    pt71.close()

def logout72():
    pt72.close()

def logout8():
    pt8.close()

def logout81():
    pt81.close()

def logout82():
    pt82.close()

def logout9():
    pt9.close()

def logout91():
    pt91.close()

def logout92():
    pt92.close()

def logout10():
    pt10.close()
    pt2.show()

def logout11():
    pt11.close()
    pt2.show()

def logout12():
    pt12.label_info.setText("")
    pt12.close()

def logout13():
    pt13.label_info.setText("")
    pt13.close()

def buscar_dados_funcionarios():
    query = "SELECT nome_funcio, cargo_funcio, login_funcio, senha_funcio FROM funcionarios"
    cursor = banco.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def logout14():
    pt14.label.setText("")
    pt14.close()
    pt11.show()
    dados_lidos = buscar_dados_funcionarios()
    pt11.tabela_funcio.setRowCount(len(dados_lidos))

    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            pt11.tabela_funcio.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def buscar_dados_cliente():
    cursor = banco.cursor()
    cursor.execute("SELECT nome_cliente, cnh_cliente, nasc_cliente, end_cliente, tel_cliente FROM cliente")
    return cursor.fetchall()

def preencher_tabela_cliente(tabela, dados_lidos):
    tabela.setRowCount(len(dados_lidos))
    for i in range(len(dados_lidos)):
        for j in range(5):
            tabela.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def logout15():
    pt15.label.setText("")
    pt15.close()
    pt10.show()
    dados_lidos = buscar_dados_cliente()
    preencher_tabela_cliente(pt10.tabelacliente, dados_lidos)

def logout16():
    pt16.close()

def logout17():
    pt17.close()

#FUNCOES CHAMAR TELA

def chamar_tela_alugar():
    pt3.show()


def chamar_tela_kwid():
    pt4.show()


def chamar_tela_mobi():
    pt5.show()


def chamar_tela_argo():
    pt6.show()


def chamar_tela_gol():
    pt7.show()


def chamar_tela_compass():
    pt8.show()


def chamar_tela_hrv():
    pt9.show()

def chamar_tela_cliente():
    pt2.close()
    pt10.show()
    dados_lidos = buscar_dados_cliente()
    preencher_tabela_cliente(pt10.tabelacliente, dados_lidos)

def chamar_tela_funcio():
    pt2.close()
    pt11.show()
    dados_lidos = buscar_dados_funcionarios()
    pt11.tabela_funcio.setRowCount(len(dados_lidos))

    for i in range(0, len(dados_lidos)):
        for j in range(0, 4):
            pt11.tabela_funcio.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def chamar_tela_editar_cliente():
    row = pt10.tabelacliente.currentRow()
    nome = pt10.tabelacliente.item(row, 0).text()
    cnh = pt10.tabelacliente.item(row, 1).text()
    end = pt10.tabelacliente.item(row, 3).text()
    tel = pt10.tabelacliente.item(row, 4).text()
    
    pt15.clientes_name_2.setPlaceholderText(nome)
    pt15.clientes_cnh_2.setPlaceholderText(cnh)
    pt15.clientes_end_2.setPlaceholderText(end)
    pt15.clientes_tel_2.setPlaceholderText(tel)

    pt10.close()
    pt15.show()


def chamar_tela_cadastrar_cliente():
    pt12.show()

def chamar_tela_cadastrar_funcio():
    pt13.show()

def chamar_tela_clienteselect():
    pt101.show()
    dados_lidos = buscar_dados_cliente()
    preencher_tabela_cliente(pt10.tabelacliente, dados_lidos)

def chamar_tela_editar_funcio():
    row = pt11.tabela_funcio.currentRow()
    nome = pt11.tabela_funcio.item(row, 0).text()
    cargo = pt11.tabela_funcio.item(row, 1).text()
    login = pt11.tabela_funcio.item(row, 2).text()
    senha = pt11.tabela_funcio.item(row, 3).text()

    pt14.funci_name_2.setPlaceholderText(nome)
    pt14.funci_login_3.setPlaceholderText(login)
    pt14.funci_senha_2.setPlaceholderText(senha)
    pt14.funci_senha_3.setPlaceholderText(senha)

    if (cargo == "Gestor"):
        pt14.radio_gestor.setChecked(True)
    else:
        pt14.radio_padrao.setChecked(True)

    pt11.close()
    pt14.show()

def chamar_tela_infocar():
    pt16.show()

def chamar_tela_tabela():
    pt17.show()

def chamar_tela_dev_carro(nome_carro, tela):
    tela.show()
    try:
        cursor = banco.cursor()
        cursor.execute("SELECT * FROM carros")
        resultado = cursor.fetchall()
        for check in resultado:
            if nome_carro == check[0]:
                tela.nome_cliente.setText(check[1])
                tela.diariaspace6.setText(check[3])
                tela.data_retirada.setText(check[4])
                break
    except Exception as e:
        print(f"Erro ao validar os dados: {e}")

def chamar_tela_devkwid():
    chamar_tela_dev_carro("Kwid", pt41)

def chamar_tela_devmobi():
    chamar_tela_dev_carro("Mobi", pt51)

def chamar_tela_devargo():
    chamar_tela_dev_carro("Argo", pt61)

def chamar_tela_devgol():
    chamar_tela_dev_carro("Gol", pt71)

def chamar_tela_devcompass():
    chamar_tela_dev_carro("Compass", pt81)

def chamar_tela_devhrv():
    chamar_tela_dev_carro("HRV", pt91)

#FUNCOES CADASTRAR

def verificar_caracteres_especiais(campo, nome_campo):
    caracteres = "!@#$%¨&*()-=+[]"
    for j in caracteres:
        if j in campo:
            QtWidgets.QMessageBox.about(pt1, 'Erro', f'Por favor não use caracteres especiais para registrar {nome_campo}!')
            return True
    return False

def limpar_campos_cliente():
    pt12.clientes_name_2.setText("")
    pt12.clientes_cnh_2.setText("")
    pt12.clientes_tel_2.setText("")
    pt12.clientes_end_2.setText("")

def limpar_campos_funcionario():
    pt14.funci_name_2.setText("")
    pt14.funci_name_2.setPlaceholderText("")
    pt14.funci_login_3.setText("")
    pt14.funci_login_3.setPlaceholderText("")
    pt14.funci_senha_2.setText("")
    pt14.funci_senha_2.setPlaceholderText("")
    pt14.funci_senha_3.setText("")
    pt14.funci_senha_3.setPlaceholderText("")

def atualizar_tabela_funcionarios():
    dados_lidos = buscar_dados_funcionarios()
    pt11.tabela_funcio.setRowCount(len(dados_lidos))
    for i in range(len(dados_lidos)):
        for j in range(4):
            pt11.tabela_funcio.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados_lidos[i][j])))

def cadastrar_funcionario():
    nome = pt13.funci_name_2.text()
    login = pt13.funci_login_3.text()
    senha = pt13.funci_senha_2.text()
    senha2 = pt13.funci_senha_3.text()

    if not nome or not login or not senha or not senha2:
        QtWidgets.QMessageBox.about(pt1, 'Erro', 'Por favor preencha todos os campos antes de inserir')
        return

    if verificar_caracteres_especiais(nome, 'nome') or verificar_caracteres_especiais(login, 'login') or \
       verificar_caracteres_especiais(senha, 'senha') or verificar_caracteres_especiais(senha2, 'confirmação de senha'):
        return

    opcao = "Gestor" if pt13.radio_gestor.isChecked() else tipo_padrao

    if senha == senha2:
        try:
            cursor = banco.cursor()
            cursor.execute(f"INSERT INTO funcionarios(nome_funcio, login_funcio, cargo_funcio, senha_funcio) VALUES ('{nome}', '{login}', '{opcao}', '{senha}')")
            banco.commit()
            pt13.label_info.setText("Usuário cadastrado com sucesso")
            limpar_campos()
        except Exception as e:
            print(f"Erro ao inserir os dados: {e}")
    else:
        pt13.label_info.setText("As duas senhas não coincidem")

    atualizar_tabela_funcionarios()

def cadastrar_cliente():
    nome = pt12.clientes_name_2.text()
    cnh = pt12.clientes_cnh_2.text()
    nasc = pt12.clientes_nasc_2.text()
    end = pt12.clientes_end_2.text()
    tel = pt12.clientes_tel_2.text()

    if not nome or not cnh or not nasc or not end or not tel:
        QtWidgets.QMessageBox.about(pt1, 'Erro', 'Por favor preencha todos os campos antes de inserir')
        return

    if any(verificar_caracteres_especiais(campo, nome_campo) for campo, nome_campo in [
        (nome, 'nome'), (cnh, 'CNH'), (nasc, 'data de nascimento'), (tel, 'telefone')]):
        return

    try:
        cursor = banco.cursor()
        cursor.execute(f"INSERT INTO cliente(nome_cliente, cnh_cliente, nasc_cliente, end_cliente, tel_cliente) VALUES ('{nome}', '{cnh}', '{nasc}', '{end}', '{tel}')")
        banco.commit()
        pt12.label_info.setText("Usuário cadastrado com sucesso")
        limpar_campos_cliente()
    except:
        print("Erro ao inserir os dados")
        
#FUNCOES EDITAR
def editar_cliente():
    nome = pt15.clientes_name_2.placeholderText()
    cnh = pt15.clientes_cnh_2.placeholderText()
    nasc = pt15.clientes_nasc_2.placeholderText()
    end = pt15.clientes_end_2.placeholderText()
    tel = pt15.clientes_tel_2.placeholderText()

    nome_novo = pt15.clientes_name_2.text() or nome
    cnh_novo = pt15.clientes_cnh_2.text() or cnh
    nasc_novo = pt15.clientes_nasc_2.text() or nasc
    end_novo = pt15.clientes_end_2.text() or end
    tel_novo = pt15.clientes_tel_2.text() or tel

    if any(verificar_caracteres_especiais(campo, nome_campo) for campo, nome_campo in [
        (nome_novo, 'nome'), (cnh_novo, 'CNH'), (nasc_novo, 'data de nascimento'), (tel_novo, 'telefone')]):
        return

    try:
        cursor = banco.cursor()
        cursor.execute("UPDATE cliente SET nome_cliente=?, cnh_cliente=?, nasc_cliente=?, end_cliente=?, tel_cliente=? WHERE nome_cliente=? AND cnh_cliente=? AND end_cliente=? AND tel_cliente=?",
                       (nome_novo, cnh_novo, nasc_novo, end_novo, tel_novo, nome, cnh, end, tel))
        banco.commit()
        pt15.label.setText("Usuário atualizado com sucesso")
        limpar_campos_cliente()
    except:
        print("Erro ao inserir os dados")

def editar_funcionario():
    nome = pt14.funci_name_2.placeholderText()
    login = pt14.funci_login_3.placeholderText()
    senha = pt14.funci_senha_2.placeholderText()
    senha2 = pt14.funci_senha_3.placeholderText()

    nome_novo = pt14.funci_name_2.text() or nome
    login_novo = pt14.funci_login_3.text() or login
    senha_novo = pt14.funci_senha_2.text() or senha
    senha2_novo = pt14.funci_senha_3.text() or senha2

    if any(verificar_caracteres_especiais(campo, nome_campo) for campo, nome_campo in [
        (nome_novo, 'nome'), (login_novo, 'login'), (senha_novo, 'senha'), (senha2_novo, 'confirmação de senha')]):
        return

    cargo = "Gestor" if pt14.radio_gestor.isChecked() else tipo_padrao

    if senha_novo == senha2_novo:
        try:
            cursor = banco.cursor()
            cursor.execute("UPDATE funcionarios SET nome_funcio=?, login_funcio=?, cargo_funcio=?, senha_funcio=? WHERE nome_funcio=? AND login_funcio=? AND cargo_funcio=? AND senha_funcio=?", 
                           (nome_novo, login_novo, cargo, senha_novo, nome, login, cargo, senha))
            banco.commit()
            pt14.label.setText("Funcionário atualizado com sucesso")
            limpar_campos_funcionario()
        except:
            print("Erro ao inserir os dados")
    else:
        pt14.label.setText("As duas senhas não coincidem")
    
#FUNCOES EXCLUIR
def excluir_funcionario():
    try:
        row = pt11.tabela_funcio.currentRow()
        
        nome = pt11.tabela_funcio.item(row, 0).text()
        cargo = pt11.tabela_funcio.item(row, 1).text()
        login = pt11.tabela_funcio.item(row, 2).text()
        senha = pt11.tabela_funcio.item(row, 3).text()

        cursor = banco.cursor()
        cursor.execute("DELETE FROM funcionarios WHERE nome_funcio = ? AND cargo_funcio = ? AND login_funcio = ? AND senha_funcio = ?", (nome, cargo, login, senha,))
        banco.commit()
        pt11.tabela_funcio.removeRow(row)

        print("Funcionário deletado")
    except:
        print("Um erro ocorreu ao deletar o funcionário")

def excluir_cliente():
    try:
        row = pt10.tabelacliente.currentRow()
        
        nome = pt10.tabelacliente.item(row, 0).text()
        cnh = pt10.tabelacliente.item(row, 1).text()
        cursor = banco.cursor()
        cursor.execute("DELETE FROM cliente WHERE nome_cliente = ? AND cnh_cliente = ? ", (nome, cnh))
        banco.commit()
        pt10.tabelacliente.removeRow(row)

        print("Cliente deletado")
    except:
        print("Um erro ocorreu ao deletar o cliente")

def setarnomekwid():
    row = pt101.tabelacliente.currentRow()
    nome = pt101.tabelacliente.item(row, 0).text()
    pt4.nome_cliente.setText(nome)
    pt101.close()

def setarnomemobi():
    row = pt101.tabelacliente.currentRow()
    nome = pt101.tabelacliente.item(row, 0).text()
    pt5.nome_cliente.setText(nome)
    pt101.close()

def setarnomeargo():
    row = pt101.tabelacliente.currentRow()
    nome = pt101.tabelacliente.item(row, 0).text()
    pt6.nome_cliente.setText(nome)
    pt101.close()

def setarnomegol():
    row = pt101.tabelacliente.currentRow()
    nome = pt101.tabelacliente.item(row, 0).text()
    pt7.nome_cliente.setText(nome)
    pt101.close()

def setarnomecompass():
    row = pt101.tabelacliente.currentRow()
    nome = pt101.tabelacliente.item(row, 0).text()
    pt8.nome_cliente.setText(nome)
    pt101.close()

def setarnomehrv():
    row = pt101.tabelacliente.currentRow()
    nome = pt101.tabelacliente.item(row, 0).text()
    pt9.nome_cliente.setText(nome)
    pt101.close()

def setaralugkwid():
    cliente = pt4.nome_cliente.text()
    dataalug = pt4.data_retirada.text()
    datadev = pt4.data_devolucao.text()
    ocup="1"
    try:
        cursor = banco.cursor()
        cursor.execute(
            "UPDATE carros SET cliente=?, data_alug=?, data_dev=?, ocup=? WHERE nome_carro='Kwid'",
            (cliente, dataalug, datadev, ocup))
        banco.commit()
    except:
        print("Um erro ocorreu ao atualizar carro")
    pt4.close()
    pt3.kwid.setEnabled(False)
    pt3.devkwid.setEnabled(True)
    pt4.nome_cliente.setText("")

def setaralugmobi():
    cliente = pt5.nome_cliente.text()
    dataalug = pt5.data_retirada.text()
    datadev = pt5.data_devolucao.text()
    ocup="1"
    try:
        cursor = banco.cursor()
        cursor.execute(
            "UPDATE carros SET cliente=?, data_alug=?, data_dev=?, ocup=? WHERE nome_carro='Mobi'",
            (cliente, dataalug, datadev, ocup))
        banco.commit()
    except:
        print("Um erro ocorreu ao atualizar carro")
    pt5.close()
    pt3.mobi.setEnabled(False)
    pt3.devmobi.setEnabled(True)
    pt5.nome_cliente.setText("")

def setaralugargo():
    cliente = pt6.nome_cliente.text()
    dataalug = pt6.data_retirada.text()
    datadev = pt6.data_devolucao.text()
    ocup="1"
    try:
        cursor = banco.cursor()
        cursor.execute(
            "UPDATE carros SET cliente=?, data_alug=?, data_dev=?, ocup=? WHERE nome_carro='Argo'",
            (cliente, dataalug, datadev, ocup))
        banco.commit()
    except:
        print("Um erro ocorreu ao atualizar carro")
    pt6.close()
    pt3.argo.setEnabled(False)
    pt3.devargo.setEnabled(True)
    pt6.nome_cliente.setText("")

def setaraluggol():
    cliente = pt7.nome_cliente.text()
    dataalug = pt7.data_retirada.text()
    datadev = pt7.data_devolucao.text()
    ocup="1"
    try:
        cursor = banco.cursor()
        cursor.execute(
            "UPDATE carros SET cliente=?, data_alug=?, data_dev=?, ocup=? WHERE nome_carro='Gol'",
            (cliente, dataalug, datadev, ocup))
        banco.commit()
    except:
        print("Um erro ocorreu ao atualizar carro")
    pt7.close()
    pt3.gol.setEnabled(False)
    pt3.devgol.setEnabled(True)
    pt7.nome_cliente.setText("")

def setaralugcompass():
    cliente = pt8.nome_cliente.text()
    dataalug = pt8.data_retirada.text()
    datadev = pt8.data_devolucao.text()
    ocup="1"
    try:
        cursor = banco.cursor()
        cursor.execute(
            "UPDATE carros SET cliente=?, data_alug=?, data_dev=?, ocup=? WHERE nome_carro='Compass'",
            (cliente, dataalug, datadev, ocup))
        banco.commit()
    except:
        print("Um erro ocorreu ao atualizar carro")
    pt8.close()
    pt3.compass.setEnabled(False)
    pt3.devcompass.setEnabled(True)
    pt8.nome_cliente.setText("")

def setaralughrv():
    cliente = pt9.nome_cliente.text()
    dataalug = pt9.data_retirada.text()
    datadev = pt9.data_devolucao.text()
    ocup="1"
    try:
        cursor = banco.cursor()
        cursor.execute(
            "UPDATE carros SET cliente=?, data_alug=?, data_dev=?, ocup=? WHERE nome_carro='HRV'",
            (cliente, dataalug, datadev, ocup))
        banco.commit()
    except:
        print("Um erro ocorreu ao atualizar carro")
    pt9.close()
    pt3.hrv.setEnabled(False)
    pt3.devhrv.setEnabled(True)
    pt9.nome_cliente.setText("")

def devkwid():
    ocup="0"
    pt41.close()
    pt42.show()
    diaria= int(pt41.diariaspace6.text())
    total=(diaria*61)+104
    pt42.total.setText(str(total))
    pt3.kwid.setEnabled(True)
    pt3.devkwid.setEnabled(False)
    try:
        cursor = banco.cursor()
        cursor.execute("UPDATE carros SET ocup=? WHERE nome_carro='Kwid'",(ocup))
        banco.commit()

    except:
        print("Um erro ocorreu ao atualizar carro")

def devmobi():
    ocup="0"
    pt51.close()
    pt52.show()
    diaria= int(pt51.diariaspace6.text())
    total=(diaria*66)+104
    pt52.total.setText(str(total))
    pt3.mobi.setEnabled(True)
    pt3.devmobi.setEnabled(False)
    try:
        cursor = banco.cursor()
        cursor.execute("UPDATE carros SET ocup=? WHERE nome_carro='Mobi'",(ocup))
        banco.commit()

    except:
        print("Um erro ocorreu ao atualizar carro")

def devargo():
    ocup="0"
    pt61.close()
    pt62.show()
    diaria= int(pt61.diariaspace6.text())
    kmtotal= int(pt61.kmspace.text())
    total= (diaria*82)+(kmtotal*0.50)+143
    pt62.total.setText(str(total))
    pt3.argo.setEnabled(True)
    pt3.devargo.setEnabled(False)
    try:
        cursor = banco.cursor()
        cursor.execute("UPDATE carros SET ocup=? WHERE nome_carro='Argo'",(ocup))
        banco.commit()

    except:
        print("Um erro ocorreu ao atualizar carro")

def devgol():
    ocup="0"
    pt71.close()
    pt72.show()
    diaria= int(pt71.diariaspace6.text())
    kmtotal= int(pt71.kmspace.text())
    total= (diaria*86)+(kmtotal*0.60)+143
    pt72.total.setText(str(total))
    pt3.gol.setEnabled(True)
    pt3.devgol.setEnabled(False)
    try:
        cursor = banco.cursor()
        cursor.execute("UPDATE carros SET ocup=? WHERE nome_carro='Gol'",(ocup))
        banco.commit()

    except:
        print("Um erro ocorreu ao atualizar carro")

def devcompass():
    ocup="0"
    pt81.close()
    pt82.show()
    diaria= int(pt81.diariaspace6.text())
    kmtotal= int(pt81.kmspace.text())
    total= (diaria*198)+(kmtotal*2.50)+207
    pt82.total.setText(str(total))
    pt3.compass.setEnabled(True)
    pt3.devcompass.setEnabled(False)
    try:
        cursor = banco.cursor()
        cursor.execute("UPDATE carros SET ocup=? WHERE nome_carro='Compass'",(ocup))
        banco.commit()

    except:
        print("Um erro ocorreu ao atualizar carro")

def devhrv():
    ocup = "0"
    pt91.close()
    pt92.show()
    diaria = int(pt91.diariaspace6.text())
    kmtotal = int(pt91.kmspace.text())
    total = (diaria * 175) + (kmtotal * 1.80) + 207
    pt92.total.setText(str(total))
    pt3.hrv.setEnabled(True)
    pt3.devhrv.setEnabled(False)

    try:
        cursor = banco.cursor()
        cursor.execute("UPDATE carros SET ocup=? WHERE nome_carro='Hrv'", (ocup,))
        banco.commit()

    except Exception as e:
        print(f"Um erro ocorreu ao atualizar carro: {e}")


app = QtWidgets.QApplication([])
#CRIAR TELAS
pt1 = uic.loadUi("tela/pt1(login).ui")
pt2 = uic.loadUi("tela/pt2(inicial).ui")
pt3 = uic.loadUi("tela/pt3(carros).ui")
pt4 = uic.loadUi("tela/pt4(kwid).ui")
pt41 = uic.loadUi("tela/pt4-1(kwid).ui")
pt42 = uic.loadUi("tela/pt4-2(kwid).ui")
pt5 = uic.loadUi("tela/pt5(mobi).ui")
pt51 = uic.loadUi("tela/pt5-1(mobi).ui")
pt52 = uic.loadUi("tela/pt5-2(mobi).ui")
pt6 = uic.loadUi("tela/pt6(argo).ui")
pt61 = uic.loadUi("tela/pt6-1(argo).ui")
pt62 = uic.loadUi("tela/pt6-2(argo).ui")
pt7 = uic.loadUi("tela/pt7(gol).ui")
pt71 = uic.loadUi("tela/pt7-1(gol).ui")
pt72 = uic.loadUi("tela/pt7-2(gol).ui")
pt8 = uic.loadUi("tela/pt8(compass).ui")
pt81 = uic.loadUi("tela/pt8-1(compass).ui")
pt82 = uic.loadUi("tela/pt8-2(compass).ui")
pt9 = uic.loadUi("tela/pt9(hrv).ui")
pt91 = uic.loadUi("tela/pt9-1(hrv).ui")
pt92 = uic.loadUi("tela/pt9-2(hrv).ui")
pt10 = uic.loadUi("tela/pt10(clientes).ui")
pt101 = uic.loadUi("tela/pt10-1(clientes).ui")
pt11 = uic.loadUi("tela/pt11(func).ui")
pt12 = uic.loadUi("tela/pt12(clientes_cadastro).ui")
pt13 = uic.loadUi("tela/pt13(func_cadastro).ui")
pt14 = uic.loadUi("tela/pt14(func_editar).ui")
pt15 = uic.loadUi("tela/pt15(clientes_editar).ui")
pt16 = uic.loadUi("tela/pt16(info_car).ui")
pt17 = uic.loadUi("tela/pt17(tabela).ui")


#BOTAO LOGIN
pt1.open.clicked.connect(logar)

#BOTOES CADASTRAR
pt4.salvar.clicked.connect(setaralugkwid)
pt41.devolver.clicked.connect(devkwid)
pt101.cadastrarcliente.clicked.connect(setarnomekwid)
pt5.salvar.clicked.connect(setaralugmobi)
pt51.devolver.clicked.connect(devmobi)
pt101.cadastrarcliente.clicked.connect(setarnomemobi)
pt6.salvar.clicked.connect(setaralugargo)
pt61.devolver.clicked.connect(devargo)
pt101.cadastrarcliente.clicked.connect(setarnomeargo)
pt7.salvar.clicked.connect(setaraluggol)
pt71.devolver.clicked.connect(devgol)
pt101.cadastrarcliente.clicked.connect(setarnomegol)
pt8.salvar.clicked.connect(setaralugcompass)
pt81.devolver.clicked.connect(devcompass)
pt101.cadastrarcliente.clicked.connect(setarnomecompass)
pt9.salvar.clicked.connect(setaralughrv)
pt91.devolver.clicked.connect(devhrv)
pt101.cadastrarcliente.clicked.connect(setarnomehrv)
pt12.salvar_cliente.clicked.connect(cadastrar_cliente)
pt13.salvar_funcio.clicked.connect(cadastrar_funcionario)

#BOTOES DELETAR
pt10.excluircliente.clicked.connect(excluir_cliente)
pt11.excluirfuncionario_3.clicked.connect(excluir_funcionario)

#BOTOES EDITAR
pt15.salvar_cliente.clicked.connect(editar_cliente)
pt14.salvar_funcio.clicked.connect(editar_funcionario)

#BOTOES CHAMAR TELA
pt2.funcionario.clicked.connect(chamar_tela_funcio)
pt2.cliente.clicked.connect(chamar_tela_cliente)
pt2.alugar.clicked.connect(chamar_tela_alugar)
pt2.carsinfos.clicked.connect(chamar_tela_infocar)
pt3.kwid.clicked.connect(chamar_tela_kwid)
pt3.devkwid.clicked.connect(chamar_tela_devkwid)
pt3.mobi.clicked.connect(chamar_tela_mobi)
pt3.devmobi.clicked.connect(chamar_tela_devmobi)
pt3.argo.clicked.connect(chamar_tela_argo)
pt3.devargo.clicked.connect(chamar_tela_devargo)
pt3.gol.clicked.connect(chamar_tela_gol)
pt3.devgol.clicked.connect(chamar_tela_devgol)
pt3.compass.clicked.connect(chamar_tela_compass)
pt3.devcompass.clicked.connect(chamar_tela_devcompass)
pt3.hrv.clicked.connect(chamar_tela_hrv)
pt3.devhrv.clicked.connect(chamar_tela_devhrv)
pt4.botaocliente.clicked.connect(chamar_tela_clienteselect)
pt5.botaocliente.clicked.connect(chamar_tela_clienteselect)
pt6.botaocliente.clicked.connect(chamar_tela_clienteselect)
pt7.botaocliente.clicked.connect(chamar_tela_clienteselect)
pt8.botaocliente.clicked.connect(chamar_tela_clienteselect)
pt9.botaocliente.clicked.connect(chamar_tela_clienteselect)
pt10.cadastrarcliente.clicked.connect(chamar_tela_cadastrar_cliente)
pt10.editarcliente.clicked.connect(chamar_tela_editar_cliente)
pt11.cadastrarfuncionario_2.clicked.connect(chamar_tela_cadastrar_funcio)
pt11.editar_funcio.clicked.connect(chamar_tela_editar_funcio)
pt16.tabelabotao.clicked.connect(chamar_tela_tabela)


#BOTOES LOGOUT
pt2.exitbutton.clicked.connect(logout)
pt3.exitbutton.clicked.connect(logout3)
pt4.voltar_10.clicked.connect(logout4)
pt41.voltar_10.clicked.connect(logout41)
pt42.devolver.clicked.connect(logout42)
pt42.voltar_10.clicked.connect(logout42)
pt5.voltar_10.clicked.connect(logout5)
pt51.voltar_10.clicked.connect(logout51)
pt52.devolver.clicked.connect(logout52)
pt52.voltar_10.clicked.connect(logout52)
pt6.voltar_10.clicked.connect(logout6)
pt61.voltar_10.clicked.connect(logout61)
pt62.devolver.clicked.connect(logout62)
pt62.voltar_10.clicked.connect(logout62)
pt7.voltar_10.clicked.connect(logout7)
pt71.voltar_10.clicked.connect(logout71)
pt72.devolver.clicked.connect(logout72)
pt72.voltar_10.clicked.connect(logout72)
pt8.voltar_10.clicked.connect(logout8)
pt81.voltar_10.clicked.connect(logout81)
pt82.devolver.clicked.connect(logout82)
pt82.voltar_10.clicked.connect(logout82)
pt9.voltar_10.clicked.connect(logout9)
pt91.voltar_10.clicked.connect(logout91)
pt92.devolver.clicked.connect(logout92)
pt92.voltar_10.clicked.connect(logout92)
pt10.saircliente.clicked.connect(logout10)
pt11.sairfunc.clicked.connect(logout11)
pt12.voltar_10.clicked.connect(logout12)
pt13.voltar_10.clicked.connect(logout13)
pt14.voltar_10.clicked.connect(logout14)
pt15.voltar_10.clicked.connect(logout15)
pt16.voltar_10.clicked.connect(logout16)
pt17.voltar_10.clicked.connect(logout17)


pt1.show()
app.exec()
