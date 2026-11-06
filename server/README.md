# Signal serveri (ixtiyoriy)

Standart holda sayt ommaviy PeerJS bulutidan (`0.peerjs.com`) foydalanadi. Ba'zi tarmoqlarda u bloklangan
yoki beqaror bo'ladi ("network" xatosi). Shunda o'zingizning serveringizni qo'yish mumkin:

1. Render.com (yoki Railway) da **Web Service** yarating, repo: `love-sim`, Root Directory: `server`.
2. Build: `npm install`, Start: `npm start`.
3. Tayyor manzil, masalan `lovesim-signal.onrender.com`. Saytni shunday oching:
   `https://love-sim-web.vercel.app/#sig=lovesim-signal.onrender.com`
   (yoki kodda `SIG` ni doimiy qilib qo'yamiz).

Video, ovoz va harakat ma'lumoti baribir to'g'ridan-to'g'ri (WebRTC) o'tadi, server faqat ulanishni boshlaydi.
