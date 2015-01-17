from datetime import datetime, timedelta

class Tarifa:
    tarifaDia = 0
    tarifaNoche = 0
    def __init__(self,tarifaD,tarifaN):
            assert(tarifaD > 0 and tarifaN > 0)
            self.tarifaDia = tarifaD
            self.tarifaNoche = tarifaN
        
    def calcularMonto(self,fi,ff):
        reserva = ff-fi
        
        # Assert para verificar que las fechas son validas
        assert(259200 >= reserva.days*24*60*60 + reserva.seconds >= 900)
        
        totalHoras = reserva.days*24+reserva.seconds/3600
        minutos = (reserva.seconds%3600)/60
        print(reserva.days, reserva.seconds)
        horasNoche = 0
        horasDia   = 0
        while(totalHoras > 0):
            if(fi.hour >= 6 and fi.hour < 18):
                diferencia = 18 - fi.hour if 18 - fi.hour < totalHoras else totalHoras
                horasDia += diferencia
            elif (fi.hour >= 18):
                diferencia = 24 - fi.hour if 24 - fi.hour < totalHoras else totalHoras 
                horasNoche += diferencia
            else:    
                diferencia = 6 - fi.hour if 6 - fi.hour < totalHoras else totalHoras
                horasNoche += diferencia
            
            totalHoras -= diferencia
            fi = fi + timedelta(hours = (diferencia))
            
        monto = horasDia*self.tarifaDia + horasNoche*self.tarifaNoche    
        if((fi.hour == 5 and fi.minute + minutos > 59) or
            (fi.hour == 17 and fi.minute + minutos > 59)):
            monto += self.tarifaDia if self.tarifaDia > self.tarifaNoche else self.tarifaNoche
        elif(fi.minute + minutos > 0) :
             monto += self.tarifaDia if self.tarifaDia < self.tarifaNoche else self.tarifaNoche
        print(horasDia,"dia")
        print(horasNoche,"noche")
        return monto
                     

td = input("Introduzca la tarifa de dia: ")
tn = input("Introduzca la tarifa de noche: ")                     
tar = Tarifa(td,tn)
y,m,d,h,min = [int(x) for x in raw_input("Introduzca la fecha de inicio con el formato: anio mes dia hora minuto ").split(' ')]
fi = datetime(y,m,d,h,min)
y,m,d,h,min =[ int(x) for x in raw_input("Introduzca la fecha de fin con el formato: anio mes dia hora minuto: ").split(' ')]
ff = datetime(y,m,d,h,min)
print "Monto a pagar: %d" % tar.calcularMonto(fi, ff)