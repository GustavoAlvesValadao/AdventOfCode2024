
def calcular_checksum(mapa):
    checksum = 0
    mapa = mapa.split() 
    for i, bloco in enumerate(mapa):
        if bloco != '.':
            id_arquivo = int(bloco)
            checksum += i * id_arquivo
    return checksum


def mover_blocos_para_compactar(mapa_com_ids):
    mapa = mapa_com_ids.split()

    def encontrar_espaco_livre():
        try:
            return mapa.index('.')
        except ValueError:
            return -1 

    def mover_bloco_para_espaco_livre():
        espaco_livre = encontrar_espaco_livre()
        if espaco_livre == -1:
            return False  

        ultimo_bloco = -1
        for i in range(len(mapa) - 1, -1, -1):
            if mapa[i] != '.':
                ultimo_bloco = i
                break

        if ultimo_bloco == -1 or espaco_livre >= ultimo_bloco:
            return False  

        mapa[espaco_livre] = mapa[ultimo_bloco]
        mapa[ultimo_bloco] = '.'
        return True

    while mover_bloco_para_espaco_livre():
        pass 

    return ' '.join(mapa)


def gerar_mapa_com_ids(mapa):
    mapa_com_ids = []
    arquivo_id = 0
    for i in range(0, len(mapa), 2):
        tamanho_arquivo = int(mapa[i])
        mapa_com_ids.extend([str(arquivo_id)] * tamanho_arquivo)
        arquivo_id += 1

        if i + 1 < len(mapa):
            tamanho_espaco = int(mapa[i + 1])
            mapa_com_ids.extend(['.'] * tamanho_espaco)

    return ' '.join(mapa_com_ids) 

mapa_exemplo = "2333133121414131402"
mapa_com_ids = gerar_mapa_com_ids(mapa_exemplo) 

mapa_compactado = mover_blocos_para_compactar(mapa_com_ids)

checksum_final = calcular_checksum(mapa_compactado)

print("Checksum final do sistema de arquivos:", checksum_final)
print("Mapa compactado:", mapa_compactado)
