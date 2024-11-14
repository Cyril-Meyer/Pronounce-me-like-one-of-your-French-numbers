import matplotlib.pyplot as plt
from num2words import num2words
import syllables

if __name__ == "__main__":
    for limit in range(4, 10):
        limit = 10 ** limit
        result = []
        x = []

        for l_id, lang in enumerate(['de', 'fr', 'en']):
            result.append([])
            x.append([])

            increment = int(limit / 846)  # not using 10 multiple number to avoid biases

            for i in range(0, limit, increment):
                words = num2words(i, lang=lang)
                # result[l_id].append(len(words))

                sylls = sum(syllables.estimate(word) for word in words.split())
                result[l_id].append(sylls + 0.25*l_id)
                x[l_id].append(i)

            plt.scatter(x[l_id], result[l_id], label=lang)

        plt.legend()
        plt.title(f'[0, {limit}] (inc = {increment})')
        plt.savefig(f'{limit}.png')
        plt.clf()
