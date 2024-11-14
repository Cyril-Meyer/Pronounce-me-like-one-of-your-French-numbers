import matplotlib.pyplot as plt
from num2words import num2words
import syllables

limit = 1000

if __name__ == "__main__":
    result = []

    for l_id, lang in enumerate(['en', 'fr', 'de']):
        result.append([])

        for i in range(limit):
            words = num2words(i, lang=lang)
            # result[l_id].append(len(words))

            sylls = sum(syllables.estimate(word) for word in words.split())
            result[l_id].append(sylls)

        plt.plot(result[l_id], label=lang)

    plt.legend()
    plt.show()
