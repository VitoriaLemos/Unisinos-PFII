from pathlib import Path

def content_analysis(file):
    text = open(file, encoding='utf8').read().lower().split('.')
    return [x for x in text if contains_keyword(x)]


def contains_keyword(text):
    keywords = ['tim']
    for word in keywords:
        if word in text: return True
    return False

# load the files from a folder
txt_folder = Path([path to files]).rglob('*.txt')
files = [x for x in txt_folder]

for file in files:
    for x in content_analysis(file):
        print(file)
        print(x)