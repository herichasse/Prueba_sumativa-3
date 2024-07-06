import json

def cargar_usuarios_desde_json(archivo, nombre):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            usuarios = json.load(f)
            usuarios_filtrados = [usr for usr in usuarios if usr.get("nombre", " ").lower() == nombre.lower()]
            return usuarios_filtrados if usuarios_filtrados else None
    except FileNotFoundError:
        print(f"No se encontró el archivo {archivo}.")
        return None
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo {archivo}.")
        return None

def buscar_usuario_por_nombre(lista_usuarios, nombre):
    for usuario in lista_usuarios:
        if usuario.get("nombre", " ").lower() == nombre.lower():
            return usuario
    return None

def guardar_usuario_en_txt(usuario, archivo):
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(f"Nombre: {usuario.get('nombre', 'N/A')}\n")
            f.write(f"Edad: {usuario.get('edad', 'N/A')}\n")
            f.write(f"Email: {usuario.get('email', 'N/A')}\n")
            print(f"Usuario guardado en {archivo}.")
    except IOError:
        print(f"No se pudo guardar el usuario en {archivo}.")

def main():
    archivo_json = 'C:\\archivos_python\\usuarios.json'
    archivo_txt = 'C:\\archivos_python\\usuarios.txt'

    nombre_usuario = input("Ingrese el nombre del usuario a buscar: ")
    lista_usuarios = cargar_usuarios_desde_json(archivo_json, nombre_usuario)

    if lista_usuarios is None:
        print("No se encontro ningun usuario con el nombre",nombre_usuario)
        return

    usuario = buscar_usuario_por_nombre(lista_usuarios, nombre_usuario)

    if usuario:
        print("Usuario encontrado:")
        print(usuario)
        guardar_usuario_en_txt(usuario, archivo_txt)
    else:
        print(f"Usuario con nombre '{nombre_usuario}' no encontrado.")

if __name__ == "__main__":
    main()