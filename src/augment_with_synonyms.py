import random
import nltk
from nltk.corpus import wordnet
import os

nltk.download('wordnet', quiet=True)


def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)


def augment_with_synonyms(input_file, output_file):
    with open(input_file, 'r') as f:
        content = f.read()

    words = content.split()
    augmented_words = []

    for word in words:
        synonyms = get_synonyms(word)
        if synonyms and random.random() < 0.2:  # 20% chance to replace with a synonym
            augmented_words.append(random.choice(synonyms))
        else:
            augmented_words.append(word)

    augmented_content = ' '.join(augmented_words)

    with open(output_file, 'w') as f:
        f.write(augmented_content)


# Define the input and output file paths
input_file = os.path.join('data', 'model_response.txt')
output_file = os.path.join('data', 'synonym_augmented_model_response.txt')

# Call the function with the defined file paths
augment_with_synonyms(input_file, output_file)

print(f"Augmented content has been written to {output_file}")
