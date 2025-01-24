import logging as log

log.basicConfig(level=log.DEBUG,
                format = '%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt = "%I:%M:%S %p",
                handlers=[
                    log.FileHandler("./Seccion 23 Capa de Datos/Capa_Datos_Persona/capa_datos.log"),
                    log.StreamHandler()
                ]
)

if __name__ == "__main__":
    log.debug("Mensaje")
    log.info("Mensaje")
    log.warning("Mensaje")
    log.error("Mensaje")
    log.critical("Mensaje")