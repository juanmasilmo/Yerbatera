# Crearemos datos ficticios para insertar en cada tabla y generaremos un archivo SQL separado.

import random
from faker import Faker

fake = Faker()

# Datos iniciales
data = []

# Generar registros para la tabla `pais`
for i in range(20):
    data.append(f"INSERT INTO pais (nombre) VALUES ('{fake.country()}');")

# Generar registros para la tabla `provincias`
for i in range(20):
    id_pais = random.randint(1, 20)  # Suponiendo que ya hay 20 países creados
    data.append(f"INSERT INTO provincias (id_pais, nombre) VALUES ({id_pais}, '{fake.state()}');")

# Generar registros para la tabla `localidades`
for i in range(20):
    id_provincias = random.randint(1, 20)  # Suponiendo que ya hay 20 provincias creadas
    data.append(f"INSERT INTO localidades (id_provincias, nombre, cp) VALUES ({id_provincias}, '{fake.city()}', '{fake.zipcode()}');")

# Generar registros para la tabla `direcciones`
for i in range(20):
    id_localidad = random.randint(1, 20)  # Suponiendo que ya hay 20 localidades creadas
    data.append(f"INSERT INTO direcciones (id_localidad, calle, altura, piso, departamento, observaciones) VALUES ({id_localidad}, '{fake.street_name()}', {random.randint(1, 9999)}, {random.randint(0, 10)}, '{random.choice(['A', 'B', 'C'])}', '{fake.sentence()}');")

# Generar registros para la tabla `vendedores`
for i in range(20):
    id_direcciones = random.randint(1, 20)  # Suponiendo que ya hay 20 direcciones creadas
    data.append(f"INSERT INTO vendedores (nombre, apellido, id_direcciones, tel, observaciones) VALUES ('{fake.first_name()}', '{fake.last_name()}', {id_direcciones}, '{fake.phone_number()}', '{fake.sentence()}');")

# Guardar en archivo SQL
file_path = "D:\\Sistemas\\Yerbatera"
with open(file_path, "w") as file:
    file.write("\n".join(data))

file_path
