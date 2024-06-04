import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://schultzbergagency.com/johanna-hedberg/'
    response = requests.get(url)
    page_content = response.content
    soup = BeautifulSoup(page_content, 'html.parser')
    
    actor_info = {}
    
    # Extracting actor's name
    actor_info['name'] = soup.find('h2', class_='elementor-heading-title elementor-size-default').text.strip()
    
    # Extracting actor's profile details
    profile_details = soup.find('div', class_='elementor-widget-container').find_all('p')
    for detail in profile_details:
        text = detail.text.strip()
        if text.startswith('Based in:'):
            actor_info['based_in'] = text.replace('Based in:', '').strip()
        elif text.startswith('BORN'):
            actor_info['born'] = text.replace('BORN:', '').strip()
        elif text.startswith('EDUCATION'):
            actor_info['education'] = text.replace('EDUCATION:', '').strip()
        elif text.startswith('Height:'):
            actor_info['height'] = text.replace('Height:', '').strip()
        elif text.startswith('Hair color:'):
            actor_info['hair_color'] = text.replace('Hair color:', '').strip()
        elif text.startswith('Eye color:'):
            actor_info['eye_color'] = text.replace('Eye color:', '').strip()
        elif text.startswith('DRIVER’S LICENCE:'):
            actor_info['drivers_licence'] = text.replace('DRIVER’S LICENCE:', '').strip()
        elif text.startswith('Languages:'):
            actor_info['languages'] = text.replace('Languages:', '').strip()
        elif text.startswith('Swedish dialects:'):
            actor_info['swedish_dialects'] = text.replace('Swedish dialects:', '').strip()
        elif text.startswith('Skills:'):
            actor_info['skills'] = text.replace('Skills:', '').strip()
    
    # Extracting film and TV productions
    film_tv_productions = []
    film_tv_section = soup.find('h2', text='FILM- AND TV PRODUCTIONS (selected)').find_next('div', class_='elementor-widget-container')
    productions = film_tv_section.find_all('span', style="color: #ceb475;")
    for production in productions:
        year = production.text.strip()
        title = production.find_next_sibling(text=True).strip()
        film_tv_productions.append(f"{year} {title}")
    actor_info['film_tv_productions'] = film_tv_productions
    
    # Extracting theatre productions
    theatre_productions = []
    theatre_section = soup.find('h2', text='Theatre PRODUCTIONS (SELECted)').find_next('div', class_='elementor-widget-container')
    productions = theatre_section.find_all('span', style="color: #ceb475;")
    for production in productions:
        year = production.text.strip()
        title = production.find_next_sibling(text=True).strip()
        theatre_productions.append(f"{year} {title}")
    actor_info['theatre_productions'] = theatre_productions
    
    print(actor_info)

if __name__ == "__main__":
    main()