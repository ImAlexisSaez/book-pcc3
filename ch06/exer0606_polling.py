favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

office_workers = ['jen', 'sarah', 'john', 'andrew', 'edward', 'phil', 'erin']

for office_worker in office_workers:
    if office_worker in favorite_languages.keys():
        print(f"{office_worker.title()}, thank you for taking the poll!")
    else:
        print(f"{office_worker.title()}, please take the poll!")