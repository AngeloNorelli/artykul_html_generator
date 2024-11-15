# Generator Artykułów HTML
## Opis projektu
Aplikacja generuje pliki HTML na podstawie treści artykułu dostarczonego w formie pliku tekstowego, korzystając z OpenAI API.
Projekt zawiera trzy główne pliki wyjściowe:

1. `artykul.html` – HTML wygenerowany z treści artykułu, z poprawnie sformatowanymi nagłówkami, paragrafami i miejscami na obrazy.
2. `szablon.html` – szablon HTML wygenerowany na podstawie `artykul.html`, gotowy do osadzenia artykułu.
3. `podglad.html` - podglad na otrzymanu kod, połączony `szablon.html` z `artykul.html`.

## Struktura projektu
```bash
artykul_html_generator/
│
├── src/               # Katalog na kod źródłowy
│   └── main.py        # Główny plik aplikacji
│
├── data/              # Katalog na pliki z artykułami
│   └── artykul.txt    # Przykładowy plik z artykułem
│
├── output/            # Katalog na wygenerowane pliki HTML
│   ├── artykul.html   # Wygenerowany kod HTML artykułu
│   ├── szablon.html   # Szablon HTML do podglądu artykułu z CSS i JavaScript
│   └── podglad.html   # Plik podglądu artykułu
│
├── .env               # Plik z kluczem API (należy dodać przed uruchomieniem)
├── .gitignore         # Ignorowanie pliku `.env
└── README.md          # Ten właśnie plik
```

## Wymagania
* Python 3.7+
* Konto OpenAI z kluczem API
* Biblioteka openai (do zainstalowania przez pip)

## Instalacja
1. Sklonuj repozytorium:
    ```bash
    git clone https://github.com/AngeloNorelli/artykul_html_generator
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
   * Sprawdź, czy nazwa pliku zgadza się z nazwą w pliku `main.py` (na szczycie kodu jest zmienna zawierajacą ścieżkę do artykułu `ARTICLE_PATH`).

2. Uruchom główny skrypt aplikacji:
    ```bash
    python src/main.py
    ```

3. Sprawdź wygenerowane pliki HTML – `artykul.html` oraz `szablon.html` i `podglad.html` zostaną zapisane w katalogu output/.

4. Podgląd artykułu:
   * Aby zobaczyć podgląd wygenerowanego artykułu, otwórz plik `podglad.html`.