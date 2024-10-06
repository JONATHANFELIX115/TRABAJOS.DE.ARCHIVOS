# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# main.py

# Abre el archivo my_notes.txt en modo escritura ('w')
with open("my_notes.txt", "w") as file:
    # Escribe tres líneas de notas personales
    file.write("Nombre: Jonathan Felix\n")
    file.write("Edad: 33 años\n")
    file.write("Ciudad de Residencia: Quito\n")
    file.write("Número Telefónico: 0997011051\n")
    file.write("Universidad: UEA\n")
    file.write("Carrera: Tecnologías de la Información\n")

print("Archivo 'my_notes.txt' escrito exitosamente.")
# main.py

# Abre el archivo my_notes.txt en modo lectura ('r')
with open("my_notes.txt", "r") as file:
    print("\nContenido de 'my_notes.txt':")
    # Lee el archivo línea por línea y las muestra en la consola
    for line in file:
        print(line.strip())  # strip() elimina los saltos de línea adicionales

print("Lectura del archivo 'my_notes.txt' completada.")


