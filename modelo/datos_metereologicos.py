class DatosMetereologicos:
    def __init__(self,nombre_archivo:str):
        self.nombre_archivo=nombre_archivo

    def procesar_datos(self) ->tuple[float,float,float,float,str]:
        
        self.temperaturas = []
        self.humedades = []
        self.presiones = []
        self.direcciones_viento_grados=[]
        self.velocidades_viento=[]
        self.direcciones=["N","NNE","NE","ENE","E","ESE","SE","SSE","S","SSW","SW","WSW","W","WNW","NW","NNW"]
        self.direcciones_grados = {
            "N": 0,
            "NNE": 22.5,
            "NE": 45,
            "ENE": 67.5,
            "E": 90,
            "ESE": 112.5,
            "SE": 135,
            "SSE": 157.5,
            "S": 180,
            "SSW": 202.5,
            "SW": 225,
            "WSW": 247.5,
            "W": 270,
            "WNW": 292.5,
            "NW": 315,
            "NNW": 337.5
        }




        with open("datos.txt", 'r') as archivo:
            for linea in archivo:
                if linea.startswith("Temperatura:"):
                  temperatura=float(linea.split(":")[1].strip())
                  self.temperaturas.append(temperatura)            

                elif linea.startswith("Humedad:"):
                  humedad=float(linea.split(":")[1].strip())
                  self.humedades.append(humedad)
            
                elif linea.startswith("Presion:"):
                  presion=float(linea.split(":")[1].strip())
                  self.presiones.append(presion)
                  
                elif linea.startswith("Viento:"):
                    velocidad = linea.split(":")[1].strip().split(",")
                    v_viento = float(velocidad[0])
                    direccion_viento = velocidad[1].strip()
                    self.velocidades_viento.append(v_viento)
                    self.direcciones_viento_grados.append(direccion_viento)

    def __str__(self):

      resultado = f"Las temperaturas son : {self.temperaturas}\n"
      p_temp = sum(self.temperaturas) / len(self.temperaturas)
      resultado += f"El promedio de la temperatura es de : {p_temp}\n\n"

      resultado += f"Las presiones son : {self.presiones}\n"
      p_pre = sum(self.presiones) / len(self.presiones)
      resultado += f"El promedio de la presión es de : {p_pre}\n\n"

      resultado += f"Las humedades son : {self.humedades}\n"
      p_hum = sum(self.humedades) / len(self.humedades)
      resultado += f"El promedio de la humedad es de : {p_hum}\n\n"

      resultado += f"Las velocidades del viento son: {self.velocidades_viento}\n"
      p_viento = sum(self.velocidades_viento) / len(self.velocidades_viento)
      resultado += f"El promedio de la velocidad del viento es de : {p_viento}\n\n"

      resultado += f"Las direcciones del viento son: {self.direcciones}\n"
      suma_valores = sum(self.direcciones_grados.values())
      promedio = suma_valores / len(self.direcciones_grados)
      resultado += f"El promedio de las direcciones es de {promedio}\n"

      valor_mas_cercano = min(self.direcciones_grados, key=lambda x: abs(self.direcciones_grados[x] - promedio))
      resultado += f"La dirección que predomina es la de : {valor_mas_cercano}\n"

      return resultado 
      
      
        
    
          
        
        
    

