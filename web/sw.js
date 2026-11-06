// Oddiy kesh: assets/ ni bir marta yuklab, keyingi safar bir zumda beradi.
const V = 'lovesim-6';
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', e => e.waitUntil((async () => {
  for (const k of await caches.keys()) if (k !== V) await caches.delete(k);
  await self.clients.claim();
})()));
self.addEventListener('fetch', e => {
  const req = e.request, u = new URL(req.url);
  if (req.method !== 'GET' || u.origin !== location.origin) return;
  if (u.pathname.includes('/assets/')) {
    // katta fayllar: avval keshdan
    e.respondWith(caches.open(V).then(async c => {
      const hit = await c.match(req);
      if (hit) return hit;
      const r = await fetch(req);
      if (r.ok) c.put(req, r.clone());
      return r;
    }));
  } else {
    // sahifa va kod: avval tarmoqdan (yangilanish darhol ko'rinsin), tarmoq yo'q bo'lsa keshdan
    e.respondWith(fetch(req).then(r => { if (r.ok) caches.open(V).then(c => c.put(req, r.clone())); return r; })
      .catch(() => caches.match(req)));
  }
});
