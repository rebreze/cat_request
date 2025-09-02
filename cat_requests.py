import requests

# получение первой страницы
response = requests.get("https://catfact.ninja/facts")
data = response.json()

# общее количество и на странице
total_facts = data['total']
facts_per_page = data['per_page']

# последняя страница
last_page_number = (total_facts + facts_per_page - 1) // facts_per_page  # округление верха

# факты с последней страницы
last_page_response = requests.get(f"https://catfact.ninja/facts?page={last_page_number}")
last_page_data = last_page_response.json()
facts_list = last_page_data['data']

# поиск самого короткого
shortest = facts_list[0]['fact']
for fact in facts_list:
    if len(fact['fact']) < len(shortest):
        shortest = fact['fact']

print("Самый короткий факт на последней странице:", shortest)
