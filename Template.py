import os 
import logging 
from pathlib import Path 

logging.basicConfig(level=logging.INFO,format="[%(asctime)s : %(message)s]")

list_of_files=[ 
    "src/helper.py", 
    "src/store_index.py", 
    "src/__init__.py",
    "requirements.txt", 
    "static/style.css", 
    "templates/index.html",
    "app.py", 
    "setup.py"
]


for file_path in list_of_files: 
    file_path=Path(file_path)
    file_dir,file_name=os.path.split(file_path)

    if file_dir != "": 
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"create {file_dir} for {file_name}")
    
    if(not os.path.exists(file_path)) or (os.path.getsize(file_path)==0): 
        with open(file_path,"w")as file: 
            pass 
            logging.info(f"create empty {file_name}")
    
    else: 
        logging.info(f"file is already exsits....")
