/* Shared by the landing page and Node tests. Never log or persist invitation data. */
(function (root) {
  'use strict';
  const base = 'https://witkowski01.github.io/BlueAirShare/pair/';
  const uuid = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/;
  const hex = /^[0-9a-f]{64}$/;
  function privateIPv4(value) {
    if (!/^(0|[1-9][0-9]{0,2})(\.(0|[1-9][0-9]{0,2})){3}$/.test(value)) return false;
    const p = value.split('.').map(Number);
    return p.every(n => n <= 255) && (p[0] === 10 ||
      (p[0] === 172 && p[1] >= 16 && p[1] <= 31) || (p[0] === 192 && p[1] === 168));
  }
  function inspect(value, now = Math.floor(Date.now() / 1000)) {
    if (typeof value !== 'string' || value.length > 600 || /[^\x21-\x7e]/.test(value) || !value.startsWith(base + '#')) return { state: 'invalid' };
    const fields = value.slice(base.length + 1).split('~');
    if (fields.length !== 10) return { state: 'invalid' };
    const [v, invitationID, deviceID, fingerprint, platform, address, port, issued, expires, secret] = fields;
    if (v !== 'v1' || !uuid.test(invitationID) || !uuid.test(deviceID) || !hex.test(fingerprint) ||
      !['iOS', 'iPadOS', 'android'].includes(platform) || !privateIPv4(address) || port !== '52840' ||
      !/^[1-9][0-9]{0,11}$/.test(issued) || !/^[1-9][0-9]{0,11}$/.test(expires) || !hex.test(secret)) return { state: 'invalid' };
    const start = Number(issued), end = Number(expires);
    if (!Number.isSafeInteger(start) || !Number.isSafeInteger(end) || end <= start || end - start > 1800 || start > now + 60) return { state: 'invalid' };
    if (end <= now) return { state: 'expired' };
    return { state: 'valid', expires: end };
  }
  const api = Object.freeze({ base, inspect });
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.BlueAirShareInvitation = api;
})(typeof globalThis === 'undefined' ? this : globalThis);
