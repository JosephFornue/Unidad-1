import sys
from PyQt5 import uic, QtWidgets
import statistics
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QMovie

qtCreatorFile = "ProyectoUnidad1.ui"
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Configurar y mostrar el GIF animado
        self.mostrar_gif()

    def mostrar_gif(self):
        # Ruta de nuestro archivo GIF
        ruta_gif = r"C:\Users\Hp\Downloads\pinguim-penguin.gif"

        # Creamos un objeto de tipo QMovie con el GIF
        movie = QMovie(ruta_gif)
        self.label_5.setMovie(movie)

        # Reproduccion del GIF
        movie.start()

        # Configuración de la ventana, para evitar que el usuario altere las dimensiones
        self.setFixedSize(720, 405)  # Establecimos el tamaño fijo de la ventana
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)  # Deshabilitamos el botón de maximizar
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMinimizeButtonHint)  # Deshabilitamos el botón de minimizar

        # Área de los Signals
        self.btn_promedio.clicked.connect(self.calcular_promedio)
        self.btn_mediana.clicked.connect(self.calcular_mediana)
        self.btn_moda.clicked.connect(self.calcular_moda)
        self.btn_desvestandar.clicked.connect(self.calcular_desviacion)
        self.btn_valormayor.clicked.connect(self.calcular_valor_mayor)
        self.btn_valormenor.clicked.connect(self.calcular_valor_menor)

    # Área de los Slots
    def obtener_lista_numeros(self):
        numeros = self.txt_numeros.text().strip()

        if not numeros:
            # Manejar el caso de entrada vacía
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Por favor, ingresa al menos un número.")
            return []

        try:
            lista = numeros.split(",")
            lista_en_numeros = [int(i) for i in lista]
            return lista_en_numeros
        except ValueError:
            # Manejar el caso de entrada no válida
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Ingresa números válidos separados por comas.")
            return []

    def calcular_promedio(self):
        valores = self.obtener_lista_numeros()
        promedio = statistics.mean(valores)
        promedio_redondeado = round(promedio,2)
        self.txt_resultado.setText(str(promedio_redondeado))

    def calcular_mediana(self):
        valores = self.obtener_lista_numeros()
        mediana = statistics.median(valores)
        self.txt_resultado.setText(str(mediana))

    def calcular_moda(self):
        valores = self.obtener_lista_numeros()
        moda = statistics.mode(valores)
        self.txt_resultado.setText(str(moda))

    def calcular_desviacion(self):
        valores = self.obtener_lista_numeros()
        desviacion_estandar = statistics.stdev(valores)
        desviacion_estandar_redondeada = round(desviacion_estandar,2)
        self.txt_resultado.setText(str(desviacion_estandar_redondeada))

    def calcular_valor_mayor(self):
        valores = self.obtener_lista_numeros()
        valor_mayor = max(valores)
        self.txt_resultado.setText(str(valor_mayor))

    def calcular_valor_menor(self):
        valores = self.obtener_lista_numeros()
        valor_menor = min(valores)
        self.txt_resultado.setText(str(valor_menor))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
