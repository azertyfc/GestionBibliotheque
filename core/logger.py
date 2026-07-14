import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("Bibliotheque")

logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

# Affichage console
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Fichier logs/app.log
file_handler = logging.FileHandler(
    "logs/app.log",
    encoding="utf-8"
)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)