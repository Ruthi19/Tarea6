def introducir_puntuacion_y_comentarios():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        if point.isdecimal():
            point = int(point)
            if point <= 0 or point > 5:
                print('Indíquelo en una escala de 1 a 5')
            else:
                print('Introduzca sus comentarios.')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                with open("data.txt", 'a') as file_pc:
                    file_pc.write(f'{post}\n')
                break
        else:
            print('Introduzca los puntos de valoración como números')

def comprobar_resultados():
    print('Resultados hasta la fecha.')
    with open("data.txt", "r") as read_file:
        print(read_file.read())

def terminar():
    print('Terminación.')
    return True

def menu_principal():
    while True:
        print('Seleccione el proceso que desea aplicar')
        print('1: Introducir puntos de evaluación y comentarios')
        print('2: Comprueba los resultados hasta ahora.')
        print('3: Terminar.')
        num = input()

        if num.isdecimal():
            num = int(num)
            if num == 1:
                introducir_puntuacion_y_comentarios()
            elif num == 2:
                comprobar_resultados()
            elif num == 3:
                if terminar():
                    break
            else:
                print('Introduzca de 1 a 3')
        else:
            print('Introduzca de 1 a 3')

if __name__ == "__main__":
    menu_principal()