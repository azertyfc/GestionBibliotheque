from database.base import Base
from database.connexion import engine

import models.__init__

Base.metadata.create_all(bind=engine)

print("✅ Base créée")