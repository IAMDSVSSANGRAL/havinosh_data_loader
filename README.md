### **📦 `havinosh_data_loader`: CSV to PostgreSQL Ingestion**  
**Seamlessly load CSV files into PostgreSQL dynamically.**  

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)  
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supported-green)  
![License](https://img.shields.io/badge/License-MIT-yellowgreen)  
![Status](https://img.shields.io/badge/Status-Active-brightgreen)  

---

## 🚀 **Overview**  
`havinosh_data_loader` is a Python package designed to automatically **detect CSV structure**, **create tables**, and **insert data into PostgreSQL** with minimal effort. Just drop your CSV files into a folder, and `havinosh_data_loader` will handle everything dynamically.  

---

## 📌 **Features**  
✅ **Automatic Table Creation** – Reads CSV headers and maps them to PostgreSQL columns  
✅ **Dynamic Schema Detection** – Infers data types automatically  
✅ **Batch Data Insertion** – Efficiently loads large datasets  
✅ **Error Handling** – Logs errors and provides detailed debugging  
✅ **Environment & CLI Configurations** – Supports `.env` file & CLI args for database credentials  
✅ **Modular & Extensible** – Well-structured for easy modifications  

---

## 📂 **Project Structure**  
```
havinosh_data_loader/
│── havinosh_data_loader/                   # Main package directory
│   ├── __init__.py           # Package initialization
│   ├── config.py             # Database configuration
│   ├── process_csv.py        # CSV processing logic (OOP-based)
│   ├── db_utils.py           # PostgreSQL connection utilities
│   ├── exception.py          # Custom exception handling
│   ├── logger.py             # Logging setup
│── scripts/                  # Command-line scripts
│   ├── ingest.py             # Main ingestion script (CLI)
│── tests/                    # Unit tests
│   ├── test_process_csv.py
│── csv_files/                # CSV storage (ignored in production)
│── setup.py                  # Package setup script
│── requirements.txt          # Dependencies
│── README.md                 # Documentation
│── .gitignore                # Ignore unnecessary files
│── LICENSE                   # License details
```

---

## 🛠 **Installation**  

### **1️⃣ Install via pip**  
Once published to PyPI, you can install `havinosh_data_loader` using:  
```sh
pip install havinosh_data_loader
```

### **2️⃣ Install from Source**  
Clone the repository and install dependencies:  
```sh
git clone https://github.com/IAMDSVSSANGRAL/havinosh_data_loader.git  
cd havinosh_data_loader  
pip install -r requirements.txt  
```

---

## ⚙ **Usage**  

### **1️⃣ Set Up Your Environment**  
#### 🔹 **Option 1: Using a `.env` File**  
Create a **`.env`** file in the root directory and add:  
```ini
DB_NAME=your_database
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

#### 🔹 **Option 2: Providing Credentials via CLI**  
No need for `.env` if you pass credentials directly via CLI.

---

### **2️⃣ Using the CLI**  
#### **Basic Ingestion (Uses `.env` for DB credentials)**  
```sh
python scripts/ingest.py --folder csv_files
```

#### **Ingest with Custom Database Credentials**  
```sh
python scripts/ingest.py --db_name mydb --user admin --password mypass --folder csv_files
```

---

### **3️⃣ Using the Python Package in Your Script**  
You can also use `havinosh_data_loader` programmatically within a Python script:

```python
from havinosh_data_loader.db_utils import Database
from havinosh_data_loader.process_csv import CSVProcessor
from havinosh_data_loader.config import Config

# Load database configuration from .env
config = Config()
db = Database(config.get_config())

# Define the folder where CSV files are stored
csv_folder = "csv_files/"

# Initialize the processor
processor = CSVProcessor(db_instance=db, csv_folder=csv_folder)

# Start the ingestion process
processor.process_csv()
```

---

## 🧪 **Testing**  
Run unit tests using:  
```sh
pytest tests/
```

---

## 📜 **License**  
This project is licensed under the **MIT License** – see the [`LICENSE`](LICENSE) file for details.  

---

## 🤝 **Contributing**  
Contributions are welcome! Please follow these steps:  
1. **Fork** the repository  
2. **Create a branch** (`feature-xyz`)  
3. **Commit your changes**  
4. **Push** and submit a **Pull Request**  

---

## 📬 **Contact**  
📧 Email: support@havinosh.com  
🌐 GitHub: [VISHAL SINGH SANGRAL](https://github.com/IAMDSVSSANGRAL)  

---

### **🚀 Happy Data Ingestion!** 🎉  

---

### **🔹 Key Updates in This README**
✅ Updated to reflect **OOP-based refactoring** (`CSVProcessor`, `Database`).  
✅ Improved **CLI usage** with direct DB credentials support.  
✅ Added **Python package usage example** for developers.  
✅ Enhanced **project structure** and **testing details**. 