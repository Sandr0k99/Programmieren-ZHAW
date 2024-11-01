import re


def count_singular_pronouns(text):
    text = text.lower()
    first_person_pronouns = ['i', 'me', 'my']
    count = sum(text.split().count(pronoun) for pronoun in first_person_pronouns)
    return count


def count_number_of_words(text):
    text = text.lower()
    count = len(text.split())
    return count


def count_average_words_per_sentence(text):
    text = text.lower()
    sentences = list(filter(None, re.split(r'[.!?]+', text)))
    average_words = len(text.split()) / len(sentences)
    return average_words


def gender_detection(text, pronoun_threshold=4, word_count_threshold=10):
    word_count = len(text.split())
    pronoun_count = count_singular_pronouns(text)

    if word_count < word_count_threshold:
        return "male"
    elif pronoun_count >= pronoun_threshold:
        return "female"
    else:
        return "unknown"


sample_text = "I think that my opinion is important. I believe in myself, and I know what I want."
print(f"Sample text: {sample_text}")
print("Number of first-person singular pronouns:", count_singular_pronouns(sample_text))
print("Number of words:", count_number_of_words(sample_text))
print("Average words per sentence:", count_average_words_per_sentence(sample_text))
print("Detected gender:", gender_detection(sample_text))
