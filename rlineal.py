class Regresion:

    def __init__(self, lista_t):
        self.lista=[elemento for elemento in lista_t]
        self.x= [elemento[0] for elemento in lista_t]
        self.y= [elemento[1] for elemento in lista_t]
        self.sumx=sum(self.x)
        self.sumy=sum(self.y)
        self.largox=len(self.x)
        self.largoy=len(self.y)
        self.promx= self.sumx/self.largox
        self.promy= self.sumy/self.largoy


    def pendiente(self):
        suma_xy=0
        suma_xx=0
        for i in range(self.largox):
            suma_xy= suma_xy+(self.x[i]-self.promx)*(self.y[i]-self.promy)
            suma_xx= suma_xx+(self.x[i]-self.promx)*(self.x[i]-self.promx)
            
        m= suma_xy/suma_xx
        return m

    def intercepto(self):
        huea= Regresion(self.lista)
        pend1= huea.pendiente()
        var_mx= self.promx*pend1
        b= self.promy - var_mx
        return b

    def maximo_x(self):
        mayor= float('-inf')
        for k in range(self.largox):
            if self.x[k]>mayor:
                mayor= self.x[k]

        return mayor

    def minimo_x(self):
        minimo= float('inf')
        for k in range(self.largox):
            if self.x[k]<minimo:
                minimo= self.x[k]

        return minimo
            

    def __repr__(self):
        nueva_huea= Regresion(self.lista)
        pend2= nueva_huea.pendiente()
        inter2=nueva_huea.intercepto()
        return str('y(x) = ')+str(pend2)+str('*x')+str(' + ')+str(inter2)
        
    
