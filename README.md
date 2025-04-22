Penjelasan kode ini:

from app.routes.task_routes import task_bp
app.register_blueprint(task_bp)

Fungsi: Ini untuk mendaftarkan blueprint ke aplikasi Flask.
task_bp adalah Blueprint dari file task_routes.py yang berisi rute (@app.route).
register_blueprint membuat rute dari file itu bisa dikenali oleh Flask.
➡️ Gunanya: supaya kamu bisa pisahkan rute ke file lain dan tetap bisa dipakai oleh aplikasi utama.

with app.app_context():
    from app.models.task_model import MyTask
    db.create_all()

with app.app_context(): artinya kita lagi membuat konteks aplikasi Flask aktif.
Tanpa konteks ini, Flask gak tahu "aplikasi apa yang sedang aktif", sehingga operasi seperti db.create_all() tidak bisa jalan.
➡️ Gunanya: agar db.create_all() bisa berjalan di luar request/route (karena ini terjadi saat inisialisasi aplikasi).

db.create_all()

Ini akan membuat semua tabel berdasarkan model yang sudah kamu definisikan di SQLAlchemy (misalnya MyTask) jika belum ada di database.
Tapi...
Kamu perlu meng-import model barunya agar dikenali oleh create_all(). Misalnya kamu tambahkan model User, kamu perlu pastikan modelnya di-import:

with app.app_context():
    from app.models.task_model import MyTask
    from app.models.user_model import User  # tambahkan ini jika kamu punya model baru
    db.create_all()

Atau, supaya lebih rapi, kamu bisa bikin semua model kamu di satu tempat dan tinggal import semuanya dari models/__init__.py.
