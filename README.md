# Stock Alert 🚨

Este proyecto envía un resumen diario del cierre del mercado de acciones seleccionadas utilizando la API de **Twilio** para enviar mensajes SMS. Ideal para mantenerte al tanto del rendimiento de tus inversiones.

## Características ✨

- Recupera datos de cierre del mercado de acciones seleccionadas mediante la biblioteca `yfinance`.
- Envía resúmenes de precios de cierre directamente a tu teléfono vía **Twilio**.
- Configuración personalizable para seleccionar las acciones que deseas monitorear.

---

## Requisitos 📋

- **Python 3.12 o superior**
- Dependencias especificadas en `requirementsx.txt`.

### Librerías utilizadas:
- `twilio` (Para enviar SMS)
- `pandas` (Manejo de datos)
- `requests` (Manejo de solicitudes HTTP)
- `yfinance` (Obtención de datos del mercado de acciones)

---

## Instalación ⚙️

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/andresAc99/Stock_alert.git
   cd Stock_alert


## Estructura del Proyecto 🗂️
Stock_alert/
│
├── stock_alert.py          # Código principal para enviar las alertas
├── twilio_config.py        # Configuración de Twilio (privada)
├── requirementsx.txt       # Lista de dependencias
└── README.md               # Documentación del proyecto


   
