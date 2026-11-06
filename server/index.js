import { PeerServer } from 'peer';

// Faqat "tanishtiruvchi": kod orqali ikki brauzerni bir-biriga ulaydi.
PeerServer({
  port: Number(process.env.PORT) || 9000,
  path: '/',
  proxied: true,          // Render/Railway kabi proxy ortida
  allow_discovery: false,
  alive_timeout: 60000,
});
console.log('Signal serveri ishga tushdi');
