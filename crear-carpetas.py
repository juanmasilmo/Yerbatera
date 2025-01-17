# Este proyecto estará estructurado siguiendo el árbol mencionado.
# Comenzaremos con la creación de la base de datos y la estructura básica del sistema.

import os

def create_project_structure():
    # Definición del árbol de directorios
    base_path = "SistemaStockVentas"
    structure = [
        "config/translations",
        "database",
        "models",
        "views/abm_views",
        "controllers/abm_controllers",
        "static/css",
        "static/images",
        "tests"
    ]

    # Crear directorios
    for folder in structure:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)

    # Archivos base
    files = {
        "config/config.ini": "[database]\nhost=localhost\nport=5432\ndatabase=sistema_stock_ventas\nuser=postgres\npassword=postgres\n",
        "database/db_init.sql": """-- Script para inicializar la base de datos\nCREATE TABLE IF NOT EXISTS usuarios (\n    id SERIAL PRIMARY KEY,\n    nombre_usuario VARCHAR(50) UNIQUE NOT NULL,\n    contrasena VARCHAR(255) NOT NULL,\n    rol VARCHAR(20) NOT NULL\n);\n\nINSERT INTO usuarios (nombre_usuario, contrasena, rol)\nVALUES ('admin', 'admin', 'admin')\nON CONFLICT (nombre_usuario) DO NOTHING;\n\n-- Más tablas pueden ser añadidas aquí\n""",
        "models/abm_models.py": "# Lógica de los ABMs\n",
        "models/user_model.py": "# Lógica de autenticación y roles\n",
        "views/main_window.ui": "<!-- UI del dashboard -->\n",
        "views/login_window.ui": "<!-- UI del login -->\n",
        "controllers/main_controller.py": "# Controlador principal\n",
        "controllers/login_controller.py": "# Controlador de login\n",
        "README.md": "# Sistema de Gestión de Stock y Ventas\n\nEste sistema maneja inventario, ventas, y cuenta con un sistema de login.\n",
        "main.py": """# Punto de entrada del sistema\nimport sys\nfrom PyQt6.QtWidgets import QApplication\n\ndef main():\n    app = QApplication(sys.argv)\n    # Aquí cargaríamos la ventana principal del sistema\n    sys.exit(app.exec())\n\nif __name__ == '__main__':\n    main()\n"""
    }

    # Crear archivos base con contenido
    for filepath, content in files.items():
        full_path = os.path.join(base_path, filepath)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

# Ejecutar función para crear la estructura del proyecto
create_project_structure()

print("Estructura del proyecto creada correctamente en la carpeta 'SistemaStockVentas'.")
