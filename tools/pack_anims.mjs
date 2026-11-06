// Rocketbox FBX animatsiyalarini ixcham JSON'ga siqadi (20 fps, Int16, delta + gzip).
// Ishlatish:  npm i three@0.160.0  &&  node pack_anims.mjs <fbx-papka> <chiqish.json>
import fs from 'fs';
import zlib from 'zlib';
globalThis.self = globalThis;
const {FBXLoader} = await import('three/examples/jsm/loaders/FBXLoader.js');
const L = new FBXLoader();
const dir = (process.argv[2] || 'anim2').replace(/\/?$/, '/');
const outFile = process.argv[3] || 'anims.json';
const FPS = 20;
const out = {};
let total = 0;
for (const f of fs.readdirSync(dir).filter(x => x.endsWith('.fbx')).sort()) {
  const buf = fs.readFileSync(dir + f);
  let a;
  try { a = L.parse(buf.buffer.slice(buf.byteOffset, buf.byteOffset + buf.byteLength), '').animations[0]; } catch (e) { console.log('SKIP', f, e.message); continue; }
  const dur = a.duration, N = Math.max(2, Math.ceil(dur * FPS) + 1);
  const times = Array.from({length: N}, (_, i) => Math.min(i / FPS, dur));
  const qt = a.tracks.filter(t => t.name.endsWith('.quaternion') && !/Footsteps/.test(t.name));
  const pt = a.tracks.find(t => t.name === 'Bip01.position');
  const names = qt.map(t => t.name);
  const arr = new Int16Array(N * (qt.length * 4 + 3));
  let off = 0;
  for (const t of qt) {
    const it = t.createInterpolant(); let prev = null;
    for (let i = 0; i < N; i++) {
      const r = it.evaluate(times[i]);
      let q = [r[0], r[1], r[2], r[3]];
      const n = Math.hypot(...q) || 1; q = q.map(x => x / n);
      if (prev && prev[0]*q[0] + prev[1]*q[1] + prev[2]*q[2] + prev[3]*q[3] < 0) q = q.map(x => -x);
      prev = q;
      for (let j = 0; j < 4; j++) arr[off++] = Math.round(q[j] * 32767);
    }
  }
  // Bip01 pozitsiyasi: oldinga siljish olib tashlanadi (sikl yopiladi), siljish `drift` sifatida saqlanadi
  const it = pt.createInterpolant(); const P = [];
  for (let i = 0; i < N; i++) { const r = it.evaluate(times[i]); P.push([r[0], r[1], r[2]]); }
  for (let i = 0; i < N; i++) for (let j = 0; j < 3; j++) {
    const d = (P[N - 1][j] - P[0][j]) * (i / (N - 1));
    arr[off++] = Math.round((P[i][j] - d) * 100);
  }
  const drift = [P[N-1][0]-P[0][0], P[N-1][1]-P[0][1], P[N-1][2]-P[0][2]];
  for (let j = 0; j < qt.length; j++) { const b = j * N * 4; for (let i = N - 1; i >= 1; i--) for (let c = 0; c < 4; c++) arr[b + i*4 + c] -= arr[b + (i-1)*4 + c]; }
  { const b = qt.length * N * 4; for (let i = N - 1; i >= 1; i--) for (let c = 0; c < 3; c++) arr[b + i*3 + c] -= arr[b + (i-1)*3 + c]; }
  const gz = zlib.gzipSync(Buffer.from(arr.buffer), {level: 9});
  out[f.replace('.fbx', '')] = {dur, n: N, names, drift, data: gz.toString('base64')};
  total += gz.length;
}
fs.writeFileSync(outFile, JSON.stringify(out));
console.log('TOTAL', (total / 1048576).toFixed(2) + 'MB', Object.keys(out).length, 'ta klip');
