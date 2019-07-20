from design import *
from metodos import *

###################################################
##                                               ##                        
##   @author Victor jx                           ##
##   calculadora basica con Qt5 and python 3.7   ##
##                                               ##
###################################################

class Mainwindow(QtWidgets.QMainWindow, Ui_MainWindow):
    captura = ""
    def __init__(self, *args,**kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)
        self.numeros()


    def numeros(self):
        self.btnCero.clicked.connect(self.cero)
        self.btnUno.clicked.connect(self.uno)
        self.btnDos.clicked.connect(self.dos)
        self.btnTres.clicked.connect(self.tres)
        self.btnCuatro.clicked.connect(self.cuatro)
        self.btnCinco.clicked.connect(self.cinco)
        self.btnSeis.clicked.connect(self.seis)
        self.btnSiete.clicked.connect(self.siete)
        self.btnOcho.clicked.connect(self.ocho)
        self.btnNueve.clicked.connect(self.nueve)
        
        self.btnPunto.clicked.connect(self.punto)
        self.btnMas.clicked.connect(self.mas)
        self.btnMenos.clicked.connect(self.menos)
        self.btnDivi.clicked.connect(self.divi)
        self.btnMulti.clicked.connect(self.multi)
        self.btnIgual.clicked.connect(self.igual)

    
    def cero(self):
        self.captura +="0"
        self.MostrarDatos.setText(self.captura)   
    def uno(self):
        self.captura +="1"
        self.MostrarDatos.setText(self.captura)
    def dos(self):
        self.captura +="2"
        self.MostrarDatos.setText(self.captura)
    def tres(self):
        self.captura +="3"
        self.MostrarDatos.setText(self.captura)
    def cuatro(self):
        self.captura +="4"
        self.MostrarDatos.setText(self.captura)
    def cinco(self):
        self.captura +="5"
        self.MostrarDatos.setText(self.captura)
    def seis(self):
        self.captura +="6"
        self.MostrarDatos.setText(self.captura)
    def siete(self):
        self.captura +="7"
        self.MostrarDatos.setText(self.captura)
    def ocho(self):
        self.captura +="8"
        self.MostrarDatos.setText(self.captura)
    def nueve(self):
        self.captura +="9"
        self.MostrarDatos.setText(self.captura)

    def punto(self):
        self.captura +="."
        self.MostrarDatos.setText(self.captura)

    def mas(self):
        self.captura +="+"
        self.MostrarDatos.setText(self.captura)

    def menos(self):
        self.captura +="-"
        self.MostrarDatos.setText(self.captura)
    
    def multi(self):
        self.captura +="*"
        self.MostrarDatos.setText(self.captura)

    def divi(self):
        self.captura +="/"
        self.MostrarDatos.setText(self.captura)

    def igual(self):
        print(self.captura)
        print(type(self.captura))
        
        
        #self.variable = self.captura
        self.var =","        
        self.new = self.var.join(self.captura)
        self.lista = self.new.split(",")
        print(self.lista)
        
        self.signo =""
        self.num1 =""
        self.num2 =""
        
        # identificar signo y numeros
        for a in self.lista:
            if ord(a) == 43 or ord(a) == 42 or ord(a) == 45:
                self.signo += a
            else:
                if self.signo == "":
                    self.num1 += a
                else:
                    self.num2 +=a
                    
        self.MostrarDatos.setText(self.captura+" = "+str(operacion(self.signo,float(self.num1),float(self.num2))))
        self.captura="0"





    


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Mainwindow()
    window.show()
    app.exec_()