# Generator Artykułów HTML
## Opis projektu
Aplikacja generuje plik HTML na podstawie treści artykułu dostarczonego w formie pliku tekstowego. Program łączy się z OpenAI API, aby przetworzyć treść artykułu i wygenerować kod HTML zgodnie ze zdefiniowanymi wytycznymi. Generowany kod HTML zawiera samą sekcję `<body>` nagłówki, paragrafy i obrazy z naprzemiennym wyrównaniem (lewo-prawo), zamknięte w kontenerach `<div>`, co ułatwia stylizację.

Aplikacja tworzy dwa pliki:

1. `artykul.html` – HTML wygenerowany z treści artykułu.
2. `podglad.html` – plik do wizualizacji wygenerowanego artykułu na podstawie 
`szablon.html`, który zawiera style i skrypty JavaScript.

## Struktura projektu
```bash
artykul_html_generator/
│
├── src/               # Katalog na kod źródłowy
│   ├── main.py        # Główny plik aplikacji
│   ├── szablon.html   # Szablon HTML do podglądu artykułu z CSS i JavaScript
│   └── podglad.html   # Plik podglądu artykułu
│
├── data/              # Katalog na pliki z artykułami
│   └── artykul.txt    # Przykładowy plik z artykułem
│
├── output/            # Katalog na wygenerowane pliki HTML
│   └── artykul.html   # Wygenerowany kod HTML (po uruchomieniu aplikacji)
│
├── .env               # Plik z kluczem API (należy dodać przed uruchomieniem)
├── .gitignore         # Ignorowanie pliku `.env
└── README.md          # Ten właśnie plik
```

## Wymagania
* Python 3.x
* Konto OpenAI z kluczem API
* Biblioteka openai (do zainstalowania przez pip)

## Instalacja
1. Sklonuj repozytorium:
```bash
git clone https://github.com/twoje-repozytorium/artykul_html_generator.git
cd artykul_html_generator
```

2. Zainstaluj wymagane biblioteki:
```bash
pip install openai
```

3. Utwórz plik `.env` w katalogu głównym projektu i dodaj do niego klucz API OpenAI:
```plaintext
OPENAI_API_KEY=twoj_klucz_api
```

## Instrukcja uruchomienia
1. Umieść plik artykułu w katalogu `data/`, np. `artykul.txt`. Upewnij się, że tekst artykułu jest czytelny i odpowiednio sformatowany.

2. Uruchom główny skrypt aplikacji:
```bash
python src/main.py
```

3. Sprawdź wygenerowany plik HTML – artykul.html zostanie zapisany w katalogu output/.

4. Podgląd artykułu:
   * Aby zobaczyć podgląd wygenerowanego artykułu, otwórz plik skopiuj zawartość pliku `artykul.html`. 
   * Wklej jego zawartość do sekcji `<body>` pliku `podglad.html`.
   * Otwórz plik `podglad.html` w przeglądarce
   * Plik ten korzysta z szablonu `szablon.html`, który zawiera style CSS i JavaScript do wyświetlania obrazków naprzemiennie po lewej i prawej stronie paragrafów.