import openai
import os
import re
from dotenv import load_dotenv

ARTICLE_PATH = "./data/artykul.txt"
OUTPUT_FILE = "./output/artykul.html"
TEMPLATE_FILE = "./output/szablon.html"
PREVIEW_FILE = "./output/podglad.html"

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Nie znalexiono pliku: {file_path}")
        return None
    except Exception as e:
        print(f"Błąd podczas odczytu pliku {file_path}: {e}")
        return None
    
def save_html(content, file_destination):
    try:
        with open(file_destination, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"Plik {file_destination} został wygenerowany.")
    except Exception as e:
        print(f"Błąd podczas odczytu pliku {file_destination}: {e}")
        
def generate_html_from_openai(messages, model="gpt-4o-mini", max_tokens=1500):
    try:
        response = openai.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=0.5
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Błąd podczas generowania treści przez OpenAI API: {e}")
        return None
    
def create_preview_file(template_path, article_path, output_path):
    template_content = read_file(template_path)
    if not template_content:
        print("Szablon jest pusty lub nie został poprawnie wczytany.")
        return
    
    article_content = read_file(article_path)
    if not article_content:
        print("Artykuł jest pusty lub nie został poprawnie wczytany.")
        return
    
    preview_content = re.sub(
        r"(<body\s*>\s*)(.*?)(\s*</body>)", 
        rf"\1{article_content}\3", 
        template_content, 
        flags=re.DOTALL
    )
    save_html(preview_content, output_path)
            
def main():
    article_content = read_file(ARTICLE_PATH)
    if not article_content:
        return
    
    aritcle_messages = [
        {"role": "system", "content": "Jesteś asystentem AI specjalizującym się w generowaniu kodu HTML."},
        {"role": "user", "content": (
                f"Przetwórz poniższy artykuł na kod HTML zgodnie z poniższymi wymaganiami:\n"
                f"- Użyj odpowiednich tagów HTML: <h1> dla tytułu artykułu, <h2> dla nagłówków sekcji, <p> dla paragrafów.\n"
                f"- Dla każdego paragrafu <p> i przypisanego do niego obrazka utwórz wspólny kontener <section>, wewnątrz którego znajdzie się <p> i poniżej niego <figure>.\n"
                f"- W każdym <figure> dodaj tag <img> z atrybutem src='image_placeholder.jpg' oraz atrybutem alt opisującym grafikę w kontekście artykułu.\n"
                f"- Elementy <h2> nie powinne znajdywać się w częściach <section>, tylko poza nimi.\n"
                f"- Dodaj podpis pod każdą grafiką za pomocą <figcaption> i zamknij go w <figure> razem z <img>.\n"
                f"- Nie dodawaj żadnych bloków kodu, takich jak ``` lub formatowania blokowego.\n"
                f"- Nie dodawaj CSS ani JavaScript; kod powinien obejmować wyłącznie treść między tagami <body> i </body>.\n\n"
                f"Plik HTML:\n{article_content}"
            )
        }
    ]
    
    article_html = generate_html_from_openai(aritcle_messages)
    if article_html:
        save_html(article_html, OUTPUT_FILE)
    else:
        print("Nie udało się wygenerować artykułu HTML.")
        return
    
    template_messages = [
        {"role": "system", "content": "Jesteś asystentem AI specjalizującym się w generowaniu kodu HTML."},
        {"role": "user", "content": (
                f"Przetwórz poniższy artykuł na kod HTML zgodnie z poniższymi wymaganiami:\n"
                f"- Ostyluj każdy element strony w sekcji <style>.\n"
                f"- Sekcję <section> ustaw wartość display na flex.\n"
                f"- Napisz skrypt, który będzie ustawiał flex-direction poszczególnym sekcjom <section> parzystym na row, nieparzystym reverse-row.\n"
                f"- Nie dodawaj żadnych bloków kodu, takich jak ``` lub formatowania blokowego.\n"
                f"- Kod nie ma zawierać żadnej zawartości w sekcji <body>, ustaw te sekcje tak: <body></body>.\n\n"
                f"Artykuł:\n{article_html}"
            )
        }
    ]
    
    template_html = generate_html_from_openai(template_messages)
    if template_html:
        save_html(template_html, TEMPLATE_FILE)
        create_preview_file(TEMPLATE_FILE, OUTPUT_FILE, PREVIEW_FILE)
    else:
        print("Nie udało się wygenerować szablonu HTML.")
        return

if __name__ == "__main__":
    main()