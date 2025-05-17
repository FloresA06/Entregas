
from openpyxl import Workbook

libro=Workbook()
ws=libro.active

ws.title="Datos"
libro.save("mi_libro.xlsx")
