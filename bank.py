# bank 

from typing import Dict, List, Optional, Type
from datetime import datetime
class Bank:

    def __init__(self, name: str = "Python Bank", storage_path: str = ""):
        self.name = name
        self.account = ""
        self.storage = ""