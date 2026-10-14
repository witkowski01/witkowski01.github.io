# witkowski01.github.io
Friendly Note — polityka prywatności, usuwanie konta i app-ads.txt

## MapGuide

- Strona aplikacji: https://witkowski01.github.io/mapguide/
- Pomoc: https://witkowski01.github.io/mapguide/support/
- Prywatność: https://witkowski01.github.io/mapguide/privacy/
- Wersja polska: https://witkowski01.github.io/mapguide/pl/

Statyczne strony HTML, lokalne grafiki i CSS, bez analityki i zewnętrznych fontów.
Treści w obu językach można zaktualizować w `scripts/build-mapguide.py`, a następnie uruchomić `python3 scripts/build-mapguide.py`.
Workflow publikuje tylko jawnie wskazane pliki stron; skrypt generujący nie trafia do witryny.
Podgląd ikony jest przygotowany z grafiki koncepcyjnej; można zastąpić `mapguide/assets/mapguide-icon.png` docelowym plikiem.

Pełna polityka prywatności jest dostępna we wszystkich 9 językach aplikacji. Wersja angielska znajduje się pod `/mapguide/privacy/`, pozostałe pod `/mapguide/<kod>/privacy/` (`pl`, `de`, `es`, `fr`, `it`, `uk`, `zh-Hans`, `ja`). Dodatkowe tłumaczenia polityki są w `scripts/privacy-translations.json`; `scripts/build-mapguide.py` generuje łącznie 13 stron.
