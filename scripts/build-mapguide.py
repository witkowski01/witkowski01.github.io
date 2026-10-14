#!/usr/bin/env python3
"""Build static MapGuide pages and privacy policies in nine languages. Python standard library only."""
import json
from html import escape
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1] / "mapguide"
ORIGIN = "https://witkowski01.github.io"
EMAIL = "witkompapp@gmail.com"
DATA = {
"en": {
"features":"How it works", "support":"Support", "policy":"Privacy policy", "skip":"Skip to content", "language":"Polski", "other":"pl",
"status":"For iPhone & iPad · In development", "title":"Your places.<br>A plan that<br><em>makes sense.</em>",
"description":"Turn your sightseeing ideas into an organized trip. Keep places and notes together, choose what to visit, and put your route in order.",
"explore":"Explore MapGuide", "contact":"Get support", "availability":"Preparing for beta testing. Public download coming later.",
"captions":["Save places","Arrange your day","Head out"],
"strip":["iPhone & iPad · iOS 18.4+","No account needed","Your lists, stored locally","9 app languages"],
"section_eyebrow":"Less scattered. More explored.", "section_title":"From “let’s go there”<br>to a day well planned.",
"section_text":"A café in your notes. A museum on a map. A whole list of recommendations. Bring them together and decide what comes next.",
"steps":[
("Keep the good finds.","Save places from the map, search, coordinates, or your current location. Group them into lists and add your own names, notes, and tags."),
("Make the day yours.","Choose up to 20 stops, set visit times, and arrange the order. Compare your route with a suggested order using travel times from Apple Maps."),
("Take the next step.","Open navigation in Apple Maps or Google Maps. Mark places as visited or skipped, and keep your trip history for another day.")],
"example":"A day, at your pace", "example_note":"Illustrative trip", "stops":["Coffee stop","Museum visit","Park walk"],
"privacy_eyebrow":"A little less to worry about", "privacy_title":"Your plans.<br>On your device.",
"privacy_text":"Your lists, notes, and saved trips live on your device. MapGuide has no account system, advertising, or analytics SDK. You choose when to export or share a plan.",
"privacy_detail":"Map searches and route comparisons use Apple services. Opening directions shares the necessary route details with the map provider you choose.",
"privacy_link":"Read the privacy policy", "tags":["No account","No ads","No background tracking"],
"faq_title":"Before you<br>head out.", "faq_intro":"A few things worth knowing about planning with MapGuide.",
"faqs":[
("Does MapGuide work offline?","Saved lists, notes, and trip plans are stored locally. Map search, resolving places, and travel-time comparisons require internet access. MapGuide does not download offline maps."),
("Can I walk, drive, cycle, or use public transit?","Yes. Choose a travel mode when comparing routes and opening navigation. Availability and estimates depend on your map provider and region. Longer routes may open in stages."),
("Can I bring in ideas from an AI assistant?","MapGuide can prepare a prompt for you to copy into an AI assistant of your choice. Import the resulting JSON list, review matched places, and confirm what to save. Your saved lists are not sent to an AI service automatically."),
("Will my plans sync across devices?","There is no cloud sync. You can export a JSON backup and import it on another device. Keep an export before deleting the app: its local data is excluded from automatic device backup.")],
"cta_title":"A question about your next trip?", "cta_text":"Find answers, report an issue, or get in touch.", "footer":"Made by Konrad Witkowski",
"support_intro":"Help with your places, plans, and routes. If something is not working as expected, we’re here to help.",
"email_title":"Let’s figure it out.", "email_intro":"For questions, feedback, or privacy requests, email:", "support_subject":"MapGuide support",
"report_title":"Reporting an issue", "report_intro":"A few details help us understand what happened:",
"report_items":["Your iPhone or iPad model and iOS version.","The MapGuide version and what you were trying to do.","Steps to reproduce the problem and any error message.","A screenshot, if useful. Remove private notes and precise locations you do not want to share."],
"help_title":"Common questions",
"help_faqs":[
("How do I back up my data?","Open Settings in MapGuide and export a JSON backup. Save it to a location you control. Use Import to restore a backup; review the confirmation carefully, because restoring replaces the current app data."),
("Why can’t I find a place or compare a route?","Check your internet connection and try a more specific place name or area. Apple Maps coverage and rate limits may affect results. You can also save a place manually using coordinates."),
("How do I use my current location?","Choose the current-location option when saving a place or setting your trip start. If permission is denied, review MapGuide’s location permission in iOS Settings. You can still enter a location manually."),
("How do I delete my data?","Delete lists and trips in the app, then use the option to remove unused places in Settings. Discard any saved import draft in the importer. Deleting the app removes its local data; exported backups remain wherever you saved them."),
("Where can I download MapGuide?","MapGuide is being prepared for beta testing. There is no public App Store or TestFlight download link yet. This page will be updated when one is available.")],
"support_privacy":"MapGuide does not require an account. Read our privacy policy for information about local data, map services, and this website.",
"policy_intro":"How MapGuide for iOS handles your information, and what happens when you visit this website or contact support.",
"updated":"Updated October 14, 2026", "contents":"On this page",
"policy_summary":"Your lists and notes are stored on your device. MapGuide has no accounts, ads, or analytics SDK. Map and navigation features can send queries and route details to the providers you choose.",
"sections":[
("publisher","Publisher and contact",[
"MapGuide is published by Konrad Witkowski, Poland. For privacy questions or requests concerning information you have sent us, contact <a href='mailto:{email}'>{email}</a>."]),
("local-data","Information stored on your device",[
"MapGuide stores your collections, saved places, custom names, notes, tags, coordinates, Apple Place identifiers, trip history, and preferences locally. An unfinished import may also be saved as a local draft. We do not operate a MapGuide server that receives copies of this data.",
"The app’s data directory uses iOS file protection and is excluded from automatic device backup. This is operating-system protection, not a separately encrypted SQLite database. Export a backup before deleting the app if you want to keep your plans."]),
("location","Location and map services",[
"MapGuide requests location access while you use the app, when you choose to use your current location as a trip start or save it as a place. It does not track your location in the background. You can manage permission in iOS Settings and enter places manually instead.",
"Searching for places, displaying maps, resolving Apple Place identifiers, and comparing routes use Apple’s MapKit services. Relevant queries, areas, and route points are sent to Apple; public-transit estimates may include a planned departure time. See <a href='https://www.apple.com/legal/privacy/data/en/apple-maps/'>Apple Maps &amp; Privacy</a>.",
"Coordinates resolved for an active trip may be cached locally until you explicitly finish or delete that trip. These temporary coordinates are not included in exported backups. Opening navigation or place information in Apple Maps or Google Maps sends the necessary place or route details to that service. See <a href='https://policies.google.com/privacy'>Google’s Privacy Policy</a>."]),
("sharing","Exports, imports, and AI assistants",[
"Exporting or sharing is an action you initiate. Backup files may contain personal notes and coordinates. The destination you choose, such as a file provider or messaging app, handles that file under its own terms. Temporary export files are removed after sharing finishes.",
"The optional AI-planning feature creates a prompt locally from the planning details you enter and copies it to your clipboard. You decide whether to paste it into an external assistant. MapGuide does not automatically send saved collections or notes to an AI provider. Imported proposals are reviewed before you confirm saving them; matching proposed places uses Apple Maps."]),
("deletion","Retention and deletion",[
"Local lists, places, notes, and trip history remain until you remove them in the app or delete the app. You can remove unused places in Settings and discard an import draft in the importer. Finishing or deleting a trip clears its temporary provider coordinates. Exported files are separate copies: delete them from the locations or services where you saved them.",
"We cannot access, export, or delete data that exists only on your device. Contact us if you need help using the app’s data controls."]),
("support","Support and beta feedback",[
"If you email us, we receive your email address, message, and any attachments you choose to send. We use them to respond to your request and investigate the issue. Avoid sending sensitive notes or precise locations unless they are necessary to explain your request. You may contact us to request access, correction, or deletion of support correspondence.",
"The app does not include advertising, tracking, analytics, or a third-party crash-reporting SDK. During TestFlight testing, Apple automatically collects crash logs and usage information and shares them with us, along with feedback you submit. This may include your name and email address, depending on how you joined the test. We use this information to investigate issues and improve MapGuide. See <a href='https://www.apple.com/legal/privacy/data/en/test-flight/'>TestFlight &amp; Privacy</a>."]),
("website","This website",[
"This static website is hosted on GitHub Pages. We do not add analytics, advertising, cookies, or tracking scripts. Images and styles are served from the same site; no external fonts or embedded maps are loaded.",
"GitHub logs visitors’ IP addresses for security purposes. See <a href='https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages#data-collection'>GitHub Pages data collection</a> and the <a href='https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement'>GitHub Privacy Statement</a>. External services have their own privacy practices."]),
("changes","Changes to this policy",["This policy may be updated as MapGuide changes. The date above identifies the current version. Material changes in data handling will be reflected here."])
]},
"pl": {
"features":"Jak to działa", "support":"Pomoc", "policy":"Polityka prywatności", "skip":"Przejdź do treści", "language":"English", "other":"en",
"status":"Na iPhone’a i iPada · W przygotowaniu", "title":"Twoje miejsca.<br>Plan, który<br><em>ma sens.</em>",
"description":"Zamień pomysły na zwiedzanie w uporządkowaną wycieczkę. Zbierz miejsca i notatki, wybierz, co chcesz odwiedzić, i ułóż kolejność trasy.",
"explore":"Poznaj MapGuide", "contact":"Potrzebujesz pomocy?", "availability":"Przygotowujemy testy beta. Publiczne pobieranie udostępnimy później.",
"captions":["Zapisz miejsca","Ułóż swój dzień","Ruszaj w drogę"],
"strip":["iPhone i iPad · iOS 18.4+","Bez zakładania konta","Listy zapisane lokalnie","9 języków aplikacji"],
"section_eyebrow":"Mniej chaosu. Więcej zwiedzania.", "section_title":"Od „chodźmy tam”<br>do dobrego planu dnia.",
"section_text":"Kawiarnia w notatkach. Muzeum na mapie. Cała lista poleceń. Zbierz je razem i zdecyduj, dokąd ruszyć w następnej kolejności.",
"steps":[
("Zachowaj dobre pomysły.","Dodawaj miejsca z mapy, wyszukiwarki, współrzędnych lub bieżącej lokalizacji. Grupuj je w listy i dopisuj własne nazwy, notatki oraz tagi."),
("Zaplanuj dzień po swojemu.","Wybierz do 20 przystanków, określ czas wizyt i ułóż kolejność. Porównaj swoją trasę z proponowanym wariantem na podstawie czasów Apple Maps."),
("Ruszaj do kolejnego miejsca.","Otwórz nawigację w Apple Maps lub Google Maps. Oznaczaj odwiedzone i pominięte punkty, a historię wycieczek zachowaj na kolejną okazję.")],
"example":"Dzień w Twoim tempie", "example_note":"Przykładowa wycieczka", "stops":["Przerwa na kawę","Wizyta w muzeum","Spacer w parku"],
"privacy_eyebrow":"O jedną rzecz mniej na głowie", "privacy_title":"Twoje plany.<br>Na Twoim urządzeniu.",
"privacy_text":"Listy, notatki i zapisane wycieczki pozostają na Twoim urządzeniu. MapGuide nie ma systemu kont, reklam ani modułu analitycznego. To Ty decydujesz o eksporcie lub udostępnieniu planu.",
"privacy_detail":"Wyszukiwanie miejsc i porównywanie tras korzystają z usług Apple. Otwarcie nawigacji przekazuje potrzebne dane trasy wybranemu dostawcy map.",
"privacy_link":"Przeczytaj politykę prywatności", "tags":["Bez konta","Bez reklam","Bez śledzenia w tle"],
"faq_title":"Zanim<br>wyruszysz.", "faq_intro":"Kilka rzeczy, które warto wiedzieć o planowaniu z MapGuide.",
"faqs":[
("Czy MapGuide działa bez internetu?","Zapisane listy, notatki i plany wycieczek są przechowywane lokalnie. Wyszukiwanie na mapie, pobieranie położenia miejsc i porównywanie czasów przejazdu wymagają internetu. MapGuide nie pobiera map offline."),
("Czy mogę wybrać spacer, samochód, rower lub komunikację miejską?","Tak. Te tryby są dostępne przy porównywaniu tras i otwieraniu nawigacji. Dostępność i szacowane czasy zależą od dostawcy map oraz regionu. Dłuższe trasy mogą być otwierane etapami."),
("Czy mogę wykorzystać pomysły od asystenta AI?","MapGuide przygotuje prompt, który możesz skopiować do wybranego asystenta AI. Zaimportuj otrzymaną listę JSON, sprawdź dopasowane miejsca i potwierdź zapis. Aplikacja nie wysyła automatycznie Twoich list do usług AI."),
("Czy plany synchronizują się między urządzeniami?","Nie ma synchronizacji w chmurze. Możesz wyeksportować kopię JSON i zaimportować ją na innym urządzeniu. Zrób eksport przed usunięciem aplikacji — jej dane lokalne są wyłączone z automatycznej kopii urządzenia.")],
"cta_title":"Pytanie przed kolejną wycieczką?", "cta_text":"Znajdź odpowiedź, zgłoś problem lub napisz do nas.", "footer":"Autor: Konrad Witkowski",
"support_intro":"Pomoc z miejscami, planami i trasami. Jeśli coś działa inaczej, niż oczekujesz, napisz do nas.",
"email_title":"Znajdźmy rozwiązanie.", "email_intro":"Pytania, uwagi i sprawy prywatności możesz kierować na:", "support_subject":"MapGuide — pomoc",
"report_title":"Jak zgłosić problem", "report_intro":"Te informacje pomogą nam zrozumieć, co się stało:",
"report_items":["Model iPhone’a lub iPada oraz wersja iOS.","Wersja MapGuide i czynność, którą próbujesz wykonać.","Kroki prowadzące do problemu i treść komunikatu błędu.","Zrzut ekranu, jeśli pomoże. Usuń prywatne notatki i dokładne lokalizacje, których nie chcesz udostępniać."],
"help_title":"Najczęstsze pytania",
"help_faqs":[
("Jak zrobić kopię danych?","Otwórz Ustawienia w MapGuide i wyeksportuj kopię JSON. Zapisz ją w wybranym przez siebie miejscu. Opcja importu przywraca kopię — przeczytaj podsumowanie, ponieważ przywrócenie zastępuje bieżące dane aplikacji."),
("Dlaczego nie mogę znaleźć miejsca lub porównać trasy?","Sprawdź połączenie z internetem i spróbuj dokładniejszej nazwy albo obszaru. Wyniki zależą od pokrycia Apple Maps i limitów zapytań. Miejsce możesz też dodać ręcznie, podając współrzędne."),
("Jak użyć bieżącej lokalizacji?","Wybierz bieżącą lokalizację podczas zapisywania miejsca lub ustawiania początku wycieczki. Jeśli dostęp jest zablokowany, sprawdź uprawnienia MapGuide w Ustawieniach iOS. Możesz też podać położenie ręcznie."),
("Jak usunąć swoje dane?","Usuń listy i wycieczki w aplikacji, a następnie skorzystaj z usuwania nieużywanych miejsc w Ustawieniach. Zapisany szkic importu odrzuć w importerze. Usunięcie aplikacji usuwa jej dane lokalne; wyeksportowane kopie pozostają w miejscach, w których je zapisano."),
("Skąd mogę pobrać MapGuide?","Przygotowujemy aplikację do testów beta. Publiczny link do App Store lub TestFlight nie jest jeszcze dostępny. Zaktualizujemy tę stronę, gdy będzie można pobrać aplikację.")],
"support_privacy":"MapGuide nie wymaga konta. Informacje o danych lokalnych, usługach mapowych i tej stronie znajdziesz w polityce prywatności.",
"policy_intro":"Jak MapGuide na iOS przetwarza informacje oraz co dzieje się podczas odwiedzania tej strony i kontaktu z pomocą.",
"updated":"Aktualizacja: 14 października 2026 r.", "contents":"Na tej stronie",
"policy_summary":"Listy i notatki są zapisane na Twoim urządzeniu. MapGuide nie ma kont, reklam ani modułu analitycznego. Funkcje map i nawigacji mogą przekazywać zapytania oraz dane trasy wybranym dostawcom.",
"sections":[
("publisher","Wydawca i kontakt",["Wydawcą MapGuide jest Konrad Witkowski, Polska. Pytania o prywatność i prośby dotyczące informacji przekazanych nam w korespondencji kieruj na <a href='mailto:{email}'>{email}</a>."]),
("local-data","Informacje na Twoim urządzeniu",[
"MapGuide zapisuje lokalnie kolekcje, miejsca, własne nazwy, notatki, tagi, współrzędne, identyfikatory Apple Places, historię wycieczek i ustawienia. Niedokończony import może być zapisany jako lokalny szkic. Nie prowadzimy serwera MapGuide, który otrzymywałby kopie tych danych.",
"Katalog danych korzysta z ochrony plików iOS i jest wyłączony z automatycznego backupu urządzenia. Jest to ochrona systemu operacyjnego, a nie osobno szyfrowana baza SQLite. Jeśli chcesz zachować plany, wyeksportuj kopię przed usunięciem aplikacji."]),
("location","Lokalizacja i usługi mapowe",[
"MapGuide prosi o dostęp do lokalizacji podczas używania aplikacji, gdy wybierzesz bieżące położenie jako początek wycieczki lub zapiszesz je jako miejsce. Nie śledzi lokalizacji w tle. Uprawnieniem możesz zarządzać w Ustawieniach iOS, a miejsca podawać ręcznie.",
"Wyszukiwanie miejsc, wyświetlanie map, pobieranie położenia na podstawie identyfikatora Apple Place oraz porównywanie tras korzystają z MapKit firmy Apple. Do Apple trafiają odpowiednie zapytania, obszary i punkty trasy; dla komunikacji miejskiej także planowana pora wyjazdu. Zobacz <a href='https://www.apple.com/legal/privacy/data/en/apple-maps/'>Apple Maps i prywatność</a>.",
"Współrzędne pobrane dla aktywnej wycieczki mogą być przechowywane tymczasowo na urządzeniu do jej jawnego zakończenia lub usunięcia. Nie trafiają do eksportowanych kopii. Otwarcie nawigacji lub informacji o miejscu w Apple Maps albo Google Maps przekazuje tej usłudze potrzebne dane miejsca lub trasy. Zobacz <a href='https://policies.google.com/privacy'>politykę prywatności Google</a>."]),
("sharing","Eksport, import i asystenci AI",[
"Eksport i udostępnianie odbywają się na Twoje polecenie. Pliki kopii mogą zawierać prywatne notatki i współrzędne. Wybrany dostawca plików lub komunikator przetwarza przekazaną kopię na własnych zasadach. Tymczasowe pliki eksportu są usuwane po zakończeniu udostępniania.",
"Opcjonalne planowanie z AI tworzy prompt lokalnie z wprowadzonych szczegółów planu i kopiuje go do schowka. To Ty decydujesz, czy wkleić go do zewnętrznego asystenta. MapGuide nie wysyła automatycznie zapisanych kolekcji i notatek do dostawcy AI. Importowaną propozycję przeglądasz przed zatwierdzeniem zapisu; dopasowanie proponowanych miejsc korzysta z Apple Maps."]),
("deletion","Przechowywanie i usuwanie",[
"Lokalne listy, miejsca, notatki i historia wycieczek pozostają do ich usunięcia w aplikacji lub usunięcia aplikacji. Nieużywane miejsca możesz usunąć w Ustawieniach, a szkic importu odrzucić w importerze. Zakończenie lub usunięcie wycieczki usuwa jej tymczasowe współrzędne dostawcy. Wyeksportowane pliki są osobnymi kopiami — usuń je z miejsc lub usług, w których je zapisano.",
"Nie mamy dostępu do danych istniejących wyłącznie na Twoim urządzeniu i nie możemy ich zdalnie wyeksportować ani usunąć. Napisz do nas, jeśli potrzebujesz pomocy w obsłudze funkcji zarządzania danymi."]),
("support","Kontakt i opinie z testów",[
"Gdy do nas napiszesz, otrzymamy Twój adres e-mail, treść wiadomości i wybrane załączniki. Używamy ich do odpowiedzi na zgłoszenie i zbadania problemu. Nie przesyłaj wrażliwych notatek ani dokładnych lokalizacji, jeśli nie są potrzebne do wyjaśnienia sprawy. Możesz poprosić o dostęp, sprostowanie lub usunięcie korespondencji z pomocą.",
"Aplikacja nie zawiera reklam, śledzenia, analityki ani zewnętrznego modułu raportowania awarii. Podczas testów przez TestFlight Apple automatycznie zbiera raporty awarii i informacje o użyciu oraz udostępnia je nam wraz z przesłanymi przez Ciebie opiniami. Zależnie od sposobu dołączenia do testu mogą obejmować Twoje imię, nazwisko i adres e-mail. Używamy tych informacji do badania problemów i ulepszania MapGuide. Zobacz <a href='https://www.apple.com/legal/privacy/data/en/test-flight/'>informację o prywatności TestFlight</a>."]),
("website","Ta strona internetowa",[
"Ta statyczna strona jest hostowana przez GitHub Pages. Nie dodajemy analityki, reklam, plików cookie ani skryptów śledzących. Grafiki i style pochodzą z tej samej witryny; nie wczytujemy zewnętrznych fontów ani osadzonych map.",
"GitHub zapisuje adresy IP odwiedzających w celach bezpieczeństwa. Zobacz <a href='https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages#data-collection'>informacje o zbieraniu danych przez GitHub Pages</a> oraz <a href='https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement'>politykę prywatności GitHub</a>. Zewnętrzne usługi mają własne zasady prywatności."]),
("changes","Zmiany polityki",["Polityka może być aktualizowana wraz ze zmianami MapGuide. Data powyżej wskazuje bieżącą wersję. Istotne zmiany w przetwarzaniu danych zostaną opisane na tej stronie."])
]}
}

POLICY_LANGUAGES = {"en":"English", "pl":"Polski", "de":"Deutsch", "es":"Español", "fr":"Français", "it":"Italiano", "uk":"Українська", "zh-Hans":"简体中文", "ja":"日本語"}
POLICY_DATA = {"en": DATA["en"], "pl": DATA["pl"], **json.loads(Path(__file__).with_name("privacy-translations.json").read_text(encoding="utf-8"))}


def url(lang, page=""):
    return "/mapguide/" + (lang + "/" if lang != "en" else "") + (page + "/" if page else "")

def faq(items):
    return '<div class="faq-list">' + ''.join(f'<details><summary>{escape(q)}</summary><p>{escape(a)}</p></details>' for q,a in items) + '</div>'

def layout(lang, page, body):
    d=DATA[lang]
    title = d["policy"] if page=="privacy" else d["support"] if page=="support" else "Your places. A plan that makes sense." if lang=="en" else "Twoje miejsca. Plan, który ma sens."
    description = d["policy_intro"] if page=="privacy" else d["support_intro"] if page=="support" else d["description"]
    current = ' aria-current="page"' if page=="support" else ''
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>MapGuide — {escape(title)}</title><meta name="description" content="{escape(description,quote=True)}">
<meta name="theme-color" content="#215d42"><link rel="canonical" href="{ORIGIN}{url(lang,page)}">
<link rel="alternate" hreflang="en-US" href="{ORIGIN}{url('en',page)}"><link rel="alternate" hreflang="pl" href="{ORIGIN}{url('pl',page)}"><link rel="alternate" hreflang="x-default" href="{ORIGIN}{url('en',page)}">
<meta property="og:type" content="website"><meta property="og:title" content="MapGuide — {escape(title,quote=True)}"><meta property="og:description" content="{escape(description,quote=True)}"><meta property="og:url" content="{ORIGIN}{url(lang,page)}"><meta property="og:image" content="{ORIGIN}/mapguide/assets/mapguide-icon.png">
<link rel="icon" type="image/png" href="/mapguide/assets/mapguide-icon.png"><link rel="apple-touch-icon" href="/mapguide/assets/mapguide-icon.png"><link rel="stylesheet" href="/mapguide/styles.css"></head><body>
<a class="skip" href="#main">{d['skip']}</a><header class="site-header"><div class="wrap header-inner"><a class="brand" href="{url(lang)}" aria-label="MapGuide"><img src="/mapguide/assets/mapguide-icon.png" width="46" height="46" alt="">MapGuide</a><nav class="site-nav" aria-label="{'Main navigation' if lang=='en' else 'Nawigacja główna'}"><a class="nav-features" href="{url(lang)}#how-it-works">{d['features']}</a><a href="{url(lang,'support')}"{current}>{d['support']}</a><a class="language" href="{url(d['other'],page)}" lang="{d['other']}" hreflang="{d['other']}">{d['language']}</a></nav></div></header>
{body}
<footer class="site-footer"><div class="wrap footer-inner"><div><div class="footer-brand">MapGuide</div><span>© 2026 · {d['footer']}</span></div><nav class="footer-nav" aria-label="{'Footer' if lang=='en' else 'Stopka'}"><a href="{url(lang,'support')}">{d['support']}</a><a href="{url(lang,'privacy')}">{d['policy']}</a><a href="mailto:{EMAIL}">{EMAIL}</a></nav></div></footer></body></html>'''

def home(lang):
    d=DATA[lang]
    strip=''.join(f'<span>{escape(t)}</span>' for t in d['strip'])
    steps=''.join(f'<article class="step"><span class="step-number">0{i}</span><h3>{escape(t)}</h3><p>{escape(p)}</p></article>' for i,(t,p) in enumerate(d['steps'],1))
    return f'''<main id="main"><div class="wrap"><section class="hero" aria-labelledby="hero-title"><div><p class="eyebrow"><span class="status-dot"></span>{d['status']}</p><h1 id="hero-title">{d['title']}</h1><p class="lede">{d['description']}</p><div class="actions"><a class="button" href="#how-it-works">{d['explore']} <span aria-hidden="true">↗</span></a><a class="text-link" href="{url(lang,'support')}">{d['contact']} <span aria-hidden="true">→</span></a></div><p class="small-note">{d['availability']}</p></div><div class="hero-art"><img class="hero-icon" src="/mapguide/assets/mapguide-icon.png" width="1280" height="1280" alt="{'MapGuide icon: a blue pin over a layered map and route' if lang=='en' else 'Ikona MapGuide: niebieska pinezka nad warstwową mapą i trasą'}" fetchpriority="high"><p class="art-caption">{''.join(f'<span>{t}</span>' for t in d['captions'])}</p></div></section><div class="platform-strip">{strip}</div>
<section class="section" id="how-it-works" aria-labelledby="how-title"><div class="section-intro"><div><p class="eyebrow">{d['section_eyebrow']}</p><h2 id="how-title">{d['section_title']}</h2></div><p>{d['section_text']}</p></div><div class="steps">{steps}</div><div class="example"><div class="example-label"><strong>{d['example']}</strong>{d['example_note']}</div><ol class="stops">{''.join(f'<li><span>{i}</span>{t}</li>' for i,t in enumerate(d['stops'],1))}</ol></div></section>
<section class="privacy-callout" aria-labelledby="privacy-title"><div><p class="eyebrow">{d['privacy_eyebrow']}</p><h2 id="privacy-title">{d['privacy_title']}</h2><div class="privacy-tags">{''.join(f'<span>{t}</span>' for t in d['tags'])}</div></div><div><p>{d['privacy_text']}</p><p>{d['privacy_detail']}</p><a href="{url(lang,'privacy')}">{d['privacy_link']} <span aria-hidden="true">↗</span></a></div></section>
<section class="section faq-layout" aria-labelledby="faq-title"><div class="faq-intro"><p class="eyebrow">FAQ</p><h2 id="faq-title">{d['faq_title']}</h2><p>{d['faq_intro']}</p></div>{faq(d['faqs'])}</section><section class="support-cta"><div><h2>{d['cta_title']}</h2><p>{d['cta_text']}</p></div><a class="button" href="{url(lang,'support')}">{d['support']} <span aria-hidden="true">↗</span></a></section></div></main>'''

def support(lang):
    d=DATA[lang]
    return f'''<main id="main" class="wrap"><div class="document-hero"><p class="eyebrow">MapGuide</p><h1>{d['support']}</h1><p class="lede">{d['support_intro']}</p></div><div class="support-main"><section class="contact-box"><h2>{d['email_title']}</h2><p>{d['email_intro']}</p><a class="contact-email" href="mailto:{EMAIL}?subject={quote(d['support_subject'])}">{EMAIL}</a></section><h2>{d['report_title']}</h2><p>{d['report_intro']}</p><ul class="report-list">{''.join(f'<li>{escape(t)}</li>' for t in d['report_items'])}</ul><h2>{d['help_title']}</h2>{faq(d['help_faqs'])}<p>{d['support_privacy']}</p><a class="text-link" href="{url(lang,'privacy')}">{d['policy']} →</a></div></main>'''

def privacy(lang):
    d=POLICY_DATA[lang]
    contents=''.join(f'<li><a href="#{id}">{escape(title)}</a></li>' for id,title,_ in d['sections'])
    sections=''.join(f'<section id="{id}"><h2>{i}. {escape(title)}</h2>'+''.join('<p>'+p.replace('{email}',EMAIL)+'</p>' for p in paragraphs)+'</section>' for i,(id,title,paragraphs) in enumerate(d['sections'],1))
    return f'''<main id="main" class="wrap"><div class="document-hero"><p class="eyebrow">MapGuide · iOS</p><h1>{d['policy']}</h1><p class="lede">{d['policy_intro']}</p><p class="meta"><time datetime="2026-10-14">{d['updated']}</time></p></div><div class="document-layout"><aside class="contents" aria-label="{d['contents']}"><strong>{d['contents']}</strong><ol>{contents}</ol></aside><article class="prose"><div class="notice"><p>{d['policy_summary']}</p></div>{sections}</article></div></main>'''


def policy_layout(lang):
    d=POLICY_DATA[lang]
    label=d.get("language_label", "Język" if lang=="pl" else "Language")
    support_label=d.get("support_label", DATA[lang]["support"] if lang in DATA else "Support · English")
    home_lang="pl" if lang=="pl" else "en"
    alternatives=''.join(f'<link rel="alternate" hreflang="{code if code!="en" else "en-US"}" href="{ORIGIN}{url(code,"privacy")}">' for code in POLICY_LANGUAGES)
    languages=''.join(f'<a href="{url(code,"privacy")}" lang="{code}" hreflang="{code}"'+(' aria-current="page"' if code==lang else '')+f'>{name}</a>' for code,name in POLICY_LANGUAGES.items())
    return f'''<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>MapGuide — {escape(d["policy"])}</title><meta name="description" content="{escape(d["policy_intro"],quote=True)}">
<meta name="theme-color" content="#215d42"><link rel="canonical" href="{ORIGIN}{url(lang,"privacy")}">{alternatives}
<link rel="alternate" hreflang="x-default" href="{ORIGIN}{url("en","privacy")}">
<meta property="og:type" content="website"><meta property="og:title" content="MapGuide — {escape(d["policy"],quote=True)}"><meta property="og:url" content="{ORIGIN}{url(lang,"privacy")}">
<link rel="icon" type="image/png" href="/mapguide/assets/mapguide-icon.png"><link rel="stylesheet" href="/mapguide/styles.css"></head>
<body class="policy-page"><header class="site-header"><div class="wrap header-inner"><a class="brand" href="{url(home_lang)}" aria-label="MapGuide"><img src="/mapguide/assets/mapguide-icon.png" width="46" height="46" alt="">MapGuide</a><a class="text-link" href="{url(home_lang,"support")}">{support_label}</a></div></header>
<nav class="wrap policy-languages" aria-label="{label}">{languages}</nav>
{privacy(lang)}
<footer class="site-footer"><div class="wrap footer-inner"><div><div class="footer-brand">MapGuide</div><span>© 2026 · {d["footer"]}</span></div><a href="mailto:{EMAIL}">{EMAIL}</a></div></footer></body></html>'''


for lang in DATA:
    for page,render in [("",home),("support",support)]:
        directory=ROOT / (lang if lang!="en" else "") / page
        directory.mkdir(parents=True,exist_ok=True)
        (directory/"index.html").write_text(layout(lang,page,render(lang)),encoding="utf-8")
for lang in POLICY_LANGUAGES:
    directory=ROOT / (lang if lang!="en" else "") / "privacy"
    directory.mkdir(parents=True,exist_ok=True)
    (directory/"index.html").write_text(policy_layout(lang),encoding="utf-8")
print("Built 13 MapGuide pages, including privacy policies in all 9 app languages.")
