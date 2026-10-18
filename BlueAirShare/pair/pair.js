'use strict';
(() => {
  // Inspect only in memory, then remove the fragment from this history entry. Keep
  // only status/expiry, not the secret. Native installed-app links are handled by
  // the OS before this page; browser fallback asks for an in-app scan.
  let invitation;
  function readFragment() {
    invitation = BlueAirShareInvitation.inspect(BlueAirShareInvitation.base + location.hash);
    if (location.hash) history.replaceState(null, '', location.pathname);
  }
  readFragment();
  let language = navigator.language.toLowerCase().startsWith('pl') ? 'pl' : 'en';
  const messages = {
    en: {
      valid: 'The code has not expired. After installing, scan it again in BlueAirShare; the receiver also checks that it is unused.',
      expired: 'This invitation has expired. Ask the receiver to generate a new QR and scan it again.',
      invalid: 'This invitation is missing or damaged, or device clocks disagree. Check the time and scan a new receiver QR.'
    },
    pl: {
      valid: 'Kod nie wygasł. Po instalacji zeskanuj go ponownie w BlueAirShare; odbiorca sprawdzi też, czy nie został już użyty.',
      expired: 'To zaproszenie wygasło. Poproś odbiorcę o nowy QR i zeskanuj go ponownie.',
      invalid: 'Brak zaproszenia, uszkodzony kod lub niezgodny czas urządzeń. Sprawdź zegary i zeskanuj nowy QR odbiorcy.'
    }
  };
  function render() {
    document.documentElement.lang = language;
    document.querySelectorAll('[data-en]').forEach(element => {
      if (element.textContent !== element.dataset[language]) element.textContent = element.dataset[language];
    });
    const toggle = document.getElementById('language');
    toggle.textContent = language === 'en' ? 'Polski' : 'English';
    toggle.setAttribute('aria-label', language === 'en' ? 'Zmień język na polski' : 'Switch to English');
    if (invitation.state === 'valid' && invitation.expires <= Math.floor(Date.now() / 1000)) invitation = { state: 'expired' };
    const status = document.getElementById('status');
    if (status.textContent !== messages[language][invitation.state]) status.textContent = messages[language][invitation.state];
  }
  document.getElementById('language').addEventListener('click', () => { language = language === 'en' ? 'pl' : 'en'; render(); });
  window.addEventListener('pageshow', render);
  window.addEventListener('hashchange', () => { readFragment(); render(); });
  document.addEventListener('visibilitychange', render);
  setInterval(render, 1000);
  render();
})();
