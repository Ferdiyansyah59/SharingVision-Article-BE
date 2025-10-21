# 1. Install dependencies
pip install -r requirements.txt

# 2. Buat database MySQL
CREATE DATABASE CDatabase;

# 3. Update .env dengan kredensial database Anda

# 4. Apply migration
flask db upgrade

# 5. Jalankan aplikasi
python run.py
