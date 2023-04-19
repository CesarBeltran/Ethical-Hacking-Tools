#Laboratorio 1 – Ataque a red WIFI.

## Uso de herramientas Aircrack-ng, Airdecap-ng y Wireshark.
El presente laboratorio tiene como objetivo realizar el análisis de una red WiFi bajo el protocolo WPA utilizando diferentes herramientas de seguridad como Aircrack-ng, Airdecap-ng y Wireshark.  En el informe se detalla la forma en que por medio de un ataque de diccionario se consigue la clave de la red, se desencripta la captura de paquetes de red y su posterior análisis.

Con ayuda de la herramienta aircrack-ng se realiza ataque de fuerza bruta usando el diccionario proporcionado para la actividad y el siguiente comando: 
 
    aircrack-ng CapturaWIFIActividad.pcap -w diccionario.txt

Se seleccionó la red objetivo (BSSID: 00:0C:41:82:B2:55) cuyo protocolo de seguridad es WPA. Luego de 9 minutos se pudo romper la contraseña de la red, la cual es "Induction"


El ultimo parámetro es el nombre del archivo de captura que se quiere desencriptar.
Se usó el siguiente comando donde:
-e especifica el nombre de la red ESSID, en este caso es Coherer
-p Especifica la contraseña de la red Wifi que es la misma con la que se desencriptará el tráfico capturado.
 
    airdecap-ng -e Coherer -p Induction CapturaWIFIActividad.pcap

Luego de la ejecución del comando se observa en el resultado que el número total de dispositivos inalámbricos encontrados son 11.

Un total de 1093 paquetes leídos y 268 paquetes de datos encriptados con el protocolo WPA y que 190 paquetes WPA han sido desencriptados correctamente.
Adicional se observa que en la ruta donde se encontraba el archivo de captura, se ha creado un nuevo archivo desencriptado.


Después de tener el archivo decodificado previamente se procede a abrir con Wireshark y de este modo tener información más detallada sobre la actividad de la red capturada.
