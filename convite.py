from PIL import Image, ImageDraw, ImageFont
import shutil
import os
import pandas as pd
import uuid

# Classe do gerador ID
class GeradorID:
    def gerar_codigo():
        # Gerar um UUID
        uuid_aleatorio = uuid.uuid1()

        # Extrair os primeiros 5 caracteres do UUID
        codigo = str(uuid_aleatorio)[:5]
        return codigo

# Classe do Sistema
class Sistema:
    def apagar_conteudo_diretorio(diretorio):
        if os.path.exists(diretorio):
            for item in os.listdir(diretorio):
                item_path = os.path.join(diretorio, item)
                try:
                    if os.path.isfile(item_path) or os.path.islink(item_path):
                        os.unlink(item_path)  # Remove arquivos ou links simbólicos
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path)  # Remove diretórios recursivamente
                except Exception as e:
                    print(f'Erro ao apagar {item_path}: {e}')
            print(f'Todo o conteúdo do diretório {diretorio} foi apagado com sucesso.')
        else:
            print(f'O diretório {diretorio} não existe.')

# Exemplo de uso
diretorio_para_limpar = 'convites_gerados'
Sistema.apagar_conteudo_diretorio(diretorio_para_limpar)



CONVIDADOS = pd.read_csv(r"convidados\convidados.csv")
LEFT_BORDER = 100


font1 = ImageFont.truetype(r"font\font.otf", size=50)
font2 = ImageFont.truetype(r"font\font.otf", size=30)


for convidado in CONVIDADOS[CONVIDADOS.columns[0]].values:
    imagem = Image.open(r"template\template.jpeg").convert("RGBA")

    lapis = ImageDraw.Draw(imagem)

    
    dados_imagem=imagem.size
    dados_texto=len(convidado)
    
    print(f"Pessoa: {convidado},  Tamanho do texto: {dados_texto}")
    # Calcular a posição x para centralizar o texto
    if dados_texto > 0 and dados_texto < 10:
        posicao_x = 650
    elif dados_texto >= 10 and dados_texto < 20:
        posicao_x = 600
    elif dados_texto >= 20 and dados_texto < 30:
        posicao_x = 550
    elif dados_texto >= 30 and dados_texto < 40:
        posicao_x = 450
    else:
        posicao_x=0


    # Nome do Convidado.
    lapis.text((posicao_x, 900), text=f"     {convidado}     ", fill="#000", font=font1)




    # Código do Convite.
    codigo=GeradorID.gerar_codigo()
    lapis.text((123, 1000), text=f"código: {codigo}", fill="#000", font=font2)
    


    imagem.save(f"convites_gerados\CONVITE - {convidado}.png")
