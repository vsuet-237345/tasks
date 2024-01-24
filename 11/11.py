import tkinter as tk
import requests
import json

url = f'https://api.github.com/repos/rust-lang/rust'
response = requests.get(url)
repository_info = response.json()

def write_repository_info():
    output_json = {
        'company': repository_info.get('company', None),
        'created_at': repository_info.get('created_at', None),
        'email': repository_info.get('email', None),
        'id': repository_info.get('id', None),
        'name': repository_info.get('name', None),
        'url': repository_info.get('url', None)
    }
    with open('repository_info.txt', 'w') as file:
        file.write(json.dumps(output_json, indent=4))
    result_label.config(text="Результат получен и записан в файл 'repository_info.txt'")

app = tk.Tk()
app.title("Получение информации о репозитории")

repository_label = tk.Label(app, text="Имя репозитория:")
repository_label.pack()

repository_name = tk.Label(app, text=repository_info['full_name'])
repository_name.pack()

get_info_button = tk.Button(app, text="Получить информацию", command=write_repository_info)
get_info_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()