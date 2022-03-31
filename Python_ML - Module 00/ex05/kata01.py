if __name__ == '__main__':

    languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihiro Matsumoto',
        'PHP': 'Rasmus Lerdorf',
        }

    for key, val in languages.items():
        print(f"{key} was created by {val}")