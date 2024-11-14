import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

def read_article(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def generate_article(article_content):
    messages = [
        {"role": "system", "content": "Jesteś asystentem AI specjalizującym się w generowaniu kodu HTML."},
        {"role": "user", "content": (
                f"Przetwórz poniższy artykuł na kod HTML zgodnie z poniższymi wymaganiami:\n"
                f"- Użyj odpowiednich tagów HTML: <h1> dla tytułu artykułu, <h2> dla nagłówków sekcji, <p> dla paragrafów.\n"
                f"- Dla każdego paragrafu <p> i przypisanego do niego obrazka utwórz wspólny kontener <div>, wewnątrz którego znajdzie się <p> i poniżej niego <figure>.\n"
                f"- W każdym <figure> dodaj tag <img> z atrybutem src='image_placeholder.jpg' oraz atrybutem alt opisującym grafikę w kontekście artykułu.\n"
                f"- Dodaj podpis pod każdą grafiką za pomocą <figcaption> i zamknij go w <figure> razem z <img>.\n"
                f"- Nie dodawaj żadnych bloków kodu, takich jak ``` lub formatowania blokowego.\n"
                f"- Nie dodawaj CSS ani JavaScript; kod powinien obejmować wyłącznie treść między tagami <body> i </body>.\n\n"
                f"Artykuł:\n{article_content}"
            )
        }
    ]

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=1500,
        temperature=0.5
    )
    
    return response.choices[0].message.content

def save_html(html_content, output_file):
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_content)
        
def main():
    article_path = "./data/Zadanie dla JJunior AI Developera - tresc artykulu.txt"
    output_file = "./output/artykul.html"
    
    try:
        article_content = read_article(article_path)
        html_content = generate_article(article_content)
        save_html(html_content, output_file)
        print(f"Plik {output_file} został wygenerowany.")
    except FileNotFoundError:
        print(f"Nie znaleziono pliku: {article_path}")
        return
    except Exception as e:
        print(f"Wystąpił błąd podczas generowania artykulu: {e}")
        return    

if __name__ == "__main__":
    main()