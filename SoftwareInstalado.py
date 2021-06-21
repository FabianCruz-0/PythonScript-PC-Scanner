import cpuinfo
import subprocess
import platform
import psutil
import socket

from fpdf import FPDF
from getmac import get_mac_address as gma
from datetime import datetime

today = datetime.now().strftime('%d/%m/%Y - %I:%M %p.')

sistema = platform.platform()
procesador = cpuinfo.get_cpu_info()['brand_raw']
mac =  gma()
nombrePC = platform.node()
ram=psutil.virtual_memory().total / (1024.0 **3)
ip=socket.gethostbyname(socket.gethostname())
hdd = psutil.disk_usage('/')

memTotal = hdd.total / (2**30)
memUsada = hdd.used / (2**30)
memLibre =  hdd.free / (2**30)

print("Analizando el sistema, por favor, espera...")

Data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
a = Data.decode("latin-1")
programas = list(a.split("\r\r\n"))

my_pdf = FPDF()
my_pdf.add_page()
my_pdf.set_font("Arial", size=12)
my_pdf.cell(0,10, txt="---------------------------------------------------------------------------------------------------------------------------------------", ln=1, align="C")
my_pdf.set_font("Arial", style="B", size=20)
my_pdf.cell(200,10, txt="CONSTANCIA DE SOFTWARE INSTALADO", ln=1, align="C")
my_pdf.set_font("Arial", size=12)
my_pdf.cell(200,10, txt="Fecha y hora: "+ today, ln=1, align="L")
my_pdf.cell(0,10, txt="---------------------------------------------------------------------------------------------------------------------------------------", ln=1, align="C")

my_pdf.set_font("Arial", style="B", size=15)
my_pdf.cell(200,10, txt="NOMBRE DEL PC", ln=1, align="L")
my_pdf.set_font("Arial", size=12)
my_pdf.cell(200,10, txt=nombrePC, ln=1, align="L")

my_pdf.set_font("Arial", style="B", size=15)
my_pdf.cell(200,10, txt="DIRECCIÓN MAC", ln=1, align="L")
my_pdf.set_font("Arial", size=12)
my_pdf.cell(200,10, txt=mac, ln=1, align="L")

my_pdf.set_font("Arial", style="B", size=15)
my_pdf.cell(200,10, txt="DIRECCIÓN IPV4", ln=1, align="L")
my_pdf.set_font("Arial", size=12)
my_pdf.cell(200,10, txt=ip, ln=1, align="L")

my_pdf.set_font("Arial", style="B", size=15)
my_pdf.cell(200,10, txt="MODELO DEL PROCESADOR", ln=1, align="L")
my_pdf.set_font("Arial", size=12)
my_pdf.cell(200,10, txt=procesador, ln=1, align="L")

my_pdf.set_font("Arial", style="B", size=15)
my_pdf.cell(200,10, txt="SISTEMA OPERATIVO", ln=1, align="L")
my_pdf.set_font("Arial", size=12)
my_pdf.cell(200,10, txt=sistema, ln=1, align="L")

my_pdf.set_font("Arial", style="B", size=15)
my_pdf.cell(200,10, txt="MEMORIA RAM", ln=1, align="L")
my_pdf.set_font("Arial", size=12)
my_pdf.cell(200,10, txt="%.2f GB" %ram, ln=1, align="L")

my_pdf.set_font("Arial", style="B", size=15)
my_pdf.cell(200,10, txt="MEMORIA ROM", ln=1, align="L")
my_pdf.set_font("Arial", size=12)
my_pdf.cell(200,7, txt="Total: %.2f GB" % memTotal, ln=1, align="L")
my_pdf.cell(200,7, txt="Usada: %.2f GB" % memUsada, ln=1, align="L")
my_pdf.cell(200,7, txt="Libre: %.2f GB" % memLibre, ln=1, align="L")
my_pdf.ln()
my_pdf.set_font("Arial", style="B", size=15)
my_pdf.cell(200,10, txt="LISTADO DE SOFTWARE INSTALADO:", ln=1, align="C")
my_pdf.set_font("Arial", size=10)

for i in range(1,len(programas)):
    my_pdf.cell(200,5, txt=programas[i], ln=1, align="L")

my_pdf.set_font("Arial", size=12)
my_pdf.cell(0,10, txt="---------------------------------------------------------------------------------------------------------------------------------------", ln=1, align="C")
my_pdf.set_font("Arial", style="B", size=12)
my_pdf.cell(200,10, txt="FIRMA:_____________________", ln=1, align="L")
my_pdf.cell(200,10, txt="NOMBRE COMPLETO:_________________________________________________", ln=1, align="L")
my_pdf.cell(200,10, txt="CURP:_________________________________________________", ln=1, align="L")
my_pdf.cell(200,10, txt="FECHA Y HORA DE LA FIRMA: " + today, ln=1, align="L")
my_pdf.set_font("Arial", size=12)
my_pdf.cell(0,10, txt="---------------------------------------------------------------------------------------------------------------------------------------", ln=1, align="C")

my_pdf.output("Constancia-PC-" + nombrePC +".pdf")

print("archivo PDF generado exitosamente.")
print("Nombre del archivo: Constancia-PC-" + nombrePC + ".pdf")
input("Ya puedes cerrar esta ventana.")