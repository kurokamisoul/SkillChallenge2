
def crear_contacto(id ,nombre_contacto, telefono, email, fecha_creacion):
    return{
        "id":id,
        "nombre_contacto" :  nombre_contacto,
        "telefono": telefono,
        "email": email,
        "activo": True,
        "fecha_creacion" : fecha_creacion,

    }

