import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logging():
    log_dir = "logs"  # Nome do diretório para os logs
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "api.log")  # Arquivo de log principal
    
    # Configuração do formato do log
    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Configuração do handler para arquivo
    file_handler = RotatingFileHandler(
        log_file,
        maxBytes=10 * 1024 * 1024,  # 10 MB por arquivo
        backupCount=5  # Mantém 5 arquivos de backup
    )
    file_handler.setFormatter(log_format)

    # Configuração do logger principal
    logger = logging.getLogger("api_logger")
    logger.setLevel(logging.DEBUG)  # Define o nível de log mais baixo a ser capturado
    logger.addHandler(file_handler)

    # Logger para usar no código
    return logger