# Jonibek's Blog

Zamonaviy va soddalashtirilgan Django blog/news sayti. Loyiha foydalanuvchiga maqolalarni o'qish, bo'limlar bo'yicha ko'rish, qidirish va izoh qoldirish imkonini beradi. Interfeys real kontentga yo'naltirilgan bo'lib, bosh sahifa va maqola sahifalari yangiliklar sayti uslubida qurilgan.

## Loyiha haqida

Bu loyiha Django asosida yozilgan kontent saytidir. Asosiy vazifasi:

- maqolalarni bosh sahifada tartibli va tushunarli ko'rsatish
- maqolalarni kategoriya bo'yicha ajratish
- foydalanuvchiga maqolalarni o'qish va izoh yozish imkonini berish
- administratorga yangi post yaratish, tahrirlash va o'chirish imkonini berish

Sayt tuzilmasi klassik blog va news-platforma o'rtasidagi formatda ishlaydi: bosh sahifada asosiy maqola, so'nggi yozuvlar va kategoriyalar bloklari; ichki sahifalarda esa to'liq maqola, yon panel va izohlar mavjud.

## Asosiy imkoniyatlar

- `Bosh sahifa`:
  asosiy maqola, so'nggi maqolalar va kategoriyalar kesimida bloklar
- `Maqolalar sahifasi`:
  barcha postlarni list ko'rinishida chiqaradi
- `Kategoriya filteri`:
  `O'zbekiston`, `Jahon`, `Iqtisodiyot`, `Sport`, `Texnologiya`
- `Qidiruv`:
  header ichidagi ixcham qidiruv orqali maqolalarni tez topish
- `Maqola detail sahifasi`:
  to'liq matn, cover rasm, qisqacha tavsif va yon tomonda boshqa maqolalar
- `Izohlar tizimi`:
  login qilgan foydalanuvchi maqolaga izoh qoldira oladi
- `Autentifikatsiya`:
  ro'yxatdan o'tish, login, logout, parolni tiklash va parolni almashtirish
- `Admin uchun post boshqaruvi`:
  superuser yangi maqola yaratishi, muallif esa o'z maqolasini tahrirlashi va o'chirishi mumkin
- `CKEditor 5`:
  maqola matnini boy formatda yozish uchun
- `Responsive UI`:
  yagona `base.html` asosida barcha sahifalarda bir xil uslub

## Texnologiyalar

- Python
- Django 6
- SQLite
- Django Crispy Forms
- Crispy Bootstrap 5
- Django CKEditor 5
- HTML templates
- Custom CSS
- Vanilla JavaScript

## Tuzilma

```text
Pages/
|-- accounts/         # foydalanuvchi modeli, signup form va auth oqimi
|-- articles/         # maqola modeli, izohlar, CRUD view'lar
|-- config/           # global settings va URL configuration
|-- pages/            # bosh sahifa view'lari
|-- media/            # yuklangan rasmlar
|-- static/           # global CSS va JS
|-- templates/        # barcha HTML template'lar
|-- db.sqlite3        # lokal baza
|-- manage.py
```

## Foydalanuvchi oqimi

1. Foydalanuvchi bosh sahifaga kiradi va asosiy yoki so'nggi maqolalarni ko'radi.
2. Kerakli bo'limni category chip orqali tanlaydi yoki qidiruvdan foydalanadi.
3. Maqola detail sahifasiga o'tib, to'liq matnni o'qiydi.
4. Tizimga kirgan bo'lsa, izoh qoldira oladi.
5. Administrator bo'lsa, yangi post yaratadi yoki mavjud postni yangilaydi.

## URL'lar

- `/` - bosh sahifa
- `/articles/` - barcha maqolalar
- `/articles/create/` - yangi maqola yaratish
- `/articles/<id>/detail/` - maqola detail sahifasi
- `/articles/<id>/edit/` - maqola tahrirlash
- `/articles/<id>/delete/` - maqola o'chirish
- `/accounts/login/` - kirish
- `/accounts/signup/` - ro'yxatdan o'tish
- `/admin/` - Django admin panel

## O'rnatish va ishga tushirish

### 1. Virtual environment yaratish

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 2. Kerakli paketlarni o'rnatish

Loyihada alohida `requirements.txt` yo'q, shuning uchun minimal paketlarni qo'lda o'rnatish mumkin:

```powershell
pip install django crispy-bootstrap5 django-crispy-forms django-ckeditor-5 pillow
```

### 3. Migratsiyalarni qo'llash

```powershell
python manage.py migrate
```

### 4. Superuser yaratish

```powershell
python manage.py createsuperuser
```

### 5. Serverni ishga tushirish

```powershell
python manage.py runserver
```

Shundan keyin sayt odatda `http://127.0.0.1:8000/` da ochiladi.

## Muhim modullar

- `accounts`
  custom user modeli va signup form
- `articles`
  maqola modeli, kategoriyalar, izohlar va CRUD sahifalari
- `pages`
  bosh sahifa kontentini yig'uvchi view
- `templates/base.html`
  barcha sahifalar uchun umumiy layout
- `static/css/app.css`
  saytning asosiy dizayn tizimi
- `static/js/app.js`
  mobile nav, alert yopish va qidiruv filter logikasi

## Kontent modeli

### `Article`

- `title`
- `category`
- `summary`
- `body`
- `photo`
- `date`
- `author`

### `Comments`

- `article`
- `comments`
- `author`

## Dizayn yondashuvi

README uchun loyiha vazifasini qisqa aytganda: bu dekorativ demo emas, balki real blog/news saytiga yaqin tuzilgan Django web ilova. Dizayn kontentni oldinga chiqaradi, sahifalar bir xil uslubda ishlaydi va foydalanuvchi minimal harakat bilan maqolaga kirib o'qib chiqishi mumkin.

## Kelajakda yaxshilash mumkin bo'lgan joylar

- `requirements.txt` qo'shish
- production uchun `DEBUG=False` va `ALLOWED_HOSTS` sozlash
- pagination qo'shish
- qidiruvni server-side qilish
- testlarni kengaytirish
- kategoriya va taglar uchun alohida sahifalar ochish

## Muallif

Ushbu loyiha Django o'rganish va real blog/news uslubidagi sayt yaratish maqsadida tayyorlangan.
