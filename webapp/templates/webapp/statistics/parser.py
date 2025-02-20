import requests
from bs4 import BeautifulSoup

def fetch_invoices():
    url = "https://dchomefix.co/invoices/"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        items = soup.find_all('div', class_='box-content')

        extracted_data = []
        total_price = 0.0

        ceiling_count = 0  # Количество работ с потолком
        painting_count = 0  # Количество работ с покраской
        plaster_count = 0  # Количество работ со штукатуркой

        for item in items:
            title_element = item.find('h3')  # Заголовок
            title = title_element.get_text(strip=True) if title_element else 'Unknown'

            description_element = item.find_all('p')[1]  # Второй <p> содержит описание
            description = description_element.get_text(strip=True).lower() if description_element else ''

            # Извлекаем дату из первого <p> внутри <span>
            date_element = item.find('span').find('p')  # Находим первый тег <p> внутри первого <span>
            date_text = date_element.get_text(strip=True) if date_element else 'Unknown'  # Извлекаем текст из <p>

            price_element = item.find('span', class_='price')  # Находим элемент с ценой
            price_text = price_element.get_text(strip=True) if price_element else 'Unknown'
            price = float(price_text.replace('$', '').replace(',', '').strip()) if price_text != 'Unknown' else 0.0

            extracted_data.append({
                'title': title,
                'description': description,
                'price': price_text,
                'date': date_text  # Добавляем дату в извлекаемые данные
            })

            total_price += price

            # Проверяем наличие ключевых слов в описании
            if 'ceiling' in description or 'ceilings' in description or 'потолок' in description or 'потолки' in description:
                ceiling_count += 1
            if 'painting' in description or 'paint' in description or 'покраска' in description or 'краска' in description:
                painting_count += 1
            if 'plaster' in description or 'plastering' in description or 'штукатурка' in description:
                plaster_count += 1

        return extracted_data, total_price, ceiling_count, painting_count, plaster_count
    else:
        print(f"Ошибка при получении страницы: {response.status_code}")
        return [], 0.0, 0, 0, 0
