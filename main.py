import matplotlib.pyplot as plt
from num2words import num2words
import syllables

if __name__ == "__main__":
    for t in ['length', 'syllables']:
        for limit in range(4, 11):
            limit = 10 ** limit
            result = []
            x = []

            for l_id, lang in enumerate(['de', 'fr', 'en']):
                result.append([])
                x.append([])

                increment = int(limit / 846)  # not using 10 multiple number to avoid biases

                for i in range(0, limit, increment):
                    x[l_id].append(i)

                    words = num2words(i, lang=lang)
                    if t == 'length':
                        result[l_id].append(len(words))
                    else:
                        sylls = sum(syllables.estimate(word) for word in words.split())
                        result[l_id].append(sylls + 0.25*l_id)

                plt.scatter(x[l_id], result[l_id], alpha=0.2, label=lang)

            if t == 'length':
                plt.ylim(0, 120)
            else:
                plt.ylim(0, 40)

            plt.legend()
            plt.title(f'{t}: [0, {limit}] (inc = {increment})')
            plt.savefig(f'{t}_{limit}.png')
            plt.clf()
