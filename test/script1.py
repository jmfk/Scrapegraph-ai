import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://schultzbergagency.com/emil-raste-karlsen/'
    response = requests.get(url)
    page_content = response.content

    soup = BeautifulSoup(page_content, 'html.parser')
    
    actor_info = {}
    
    # Extracting actor's name
    actor_info['name'] = soup.find('h2', class_='elementor-heading-title elementor-size-default').text.strip()
    
    # Extracting actor's profile details
    profile_section = soup.find('div', class_='elementor-element elementor-element-ec3227d elementor-widget elementor-widget-text-editor')
    profile_details = profile_section.find_all('p')
    
    for detail in profile_details:
        text = detail.text.strip()
        if text:
            key, value = text.split(':', 1)
            actor_info[key.strip().lower().replace(' ', '_')] = value.strip()
    
    print(actor_info)

if __name__ == "__main__":
    main()