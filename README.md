# love-sim

Brauzerda ishlaydigan 3D "real life" simulyator: kinoteatr zali, ikki personaj, PUBG uslubidagi boshqaruv
(kompyuter va telefon), animatsiyalar, quchoqlash va o'pish, ekranga PC videosini chiqarish.

## Lokal ishga tushirish
```
python -m http.server 8000 --directory web
```
so'ng http://localhost:8000 ni oching (fayl sifatida ochib bo'lmaydi, server kerak).

## Boshqaruv
| | Kompyuter | Telefon |
|---|---|---|
| Yurish / qarash | W A S D / sichqoncha | chap joystick / o'ng tomonni surish |
| Yugurish, sakrash | Shift, Space | tugmalar |
| Quchoqlash, o'pish | H, K | "Quchoq", "O'pish" |
| O'tirish, raqs, chiroq | E, G, L | tugmalar |
| Kamera (yuzdan / 3-shaxs) | V | "Kamera" |
| Menyu (animatsiyalar, ekran ulashish) | Esc | "Animatsiyalar" |

## Tuzilma
- `web/` sayt (Vercel'ga shu papka joylanadi). `index.html` o'yin kodi, `assets/` model, tekstura va animatsiyalar.
- `tools/` animatsiya va modellarni tayyorlash skriptlari (Rocketbox'dan yuklash, siqish).

## Joylash (Vercel)
Vercel'da Root Directory = `web`. `main` ga push qilinsa sayt o'zi yangilanadi.

## Rejalar
Onlayn rejim: xona kodi, ikki uzoq foydalanuvchi, PC ekranini WebRTC orqali uzatish.

## Manbalar
Personajlar va animatsiyalar: [Microsoft Rocketbox Avatar Library](https://github.com/microsoft/Microsoft-Rocketbox) (MIT).
Litsenziya matni: `THIRD_PARTY_LICENSES/`. 3D dvigatel: [three.js](https://threejs.org) (MIT).

## Asset tayyorlash (ixtiyoriy)
`tools/` ichida: `dl_*.py` Rocketbox animatsiyalarini yuklaydi, `pack_anims.mjs` ularni siqadi.
Tayyor natija `web/assets/` da allaqachon bor, bu skriptlar faqat qayta yaratish uchun.
