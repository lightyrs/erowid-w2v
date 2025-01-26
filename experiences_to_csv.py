import os
import pandas as pd

def collect_text_files(root_dir):
    texts = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read().strip()
                    texts.append([text])

    df = pd.DataFrame(texts, columns=['text'])
    df.to_csv('output.csv', index=False)

if __name__ == '__main__':
    root_directory = './core-experiences/'  # Change this to your root directory
    collect_text_files(root_directory)
