import os

def renomear_arquivos_xml(diretorio):
    # Verifica se o diretório existe
    if not os.path.isdir(diretorio):
        print(f"O diretório {diretorio} não existe.")
        return

    # Itera sobre os arquivos no diretório
    for nome_arquivo in os.listdir(diretorio):
        if nome_arquivo.endswith('.xml'):
            caminho_antigo = os.path.join(diretorio, nome_arquivo)
            novo_nome = 'amanda+' + nome_arquivo
            caminho_novo = os.path.join(diretorio, novo_nome)
            
            # Renomeia o arquivo
            os.rename(caminho_antigo, caminho_novo)
            print(f"Renomeado: {nome_arquivo} -> {novo_nome}")

# Substitua 'seu_diretorio_aqui' pelo caminho do diretório onde estão os arquivos XML
diretorio = 'C:/Users/alexa/Pictures/muda nome arquivo xml/julho - 2024NFCe'
renomear_arquivos_xml(diretorio)
