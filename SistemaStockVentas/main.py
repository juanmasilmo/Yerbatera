# Punto de entrada del sistema
import sys
from PyQt6.QtWidgets import QApplication

def main():
    app = QApplication(sys.argv)
    # Aquí cargaríamos la ventana principal del sistema
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
