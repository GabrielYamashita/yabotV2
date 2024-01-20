
def process_command(command):
    # Define Geração de Imagem = False
    imgGen = False

    # Comando para Gerar QR Code para um Link
    if 'qr' in command.lower():
        link = command.split(' ')[1]

        resp = f'QR Code Generated for {link}'
        imgGen = f'https://api.qrserver.com/v1/create-qr-code/?size=250x250&data=%3C{link}%3E'



    # Sem Comando
    else:
        resp = 'Command not Found!'

    return resp, imgGen # retorno texto, img


