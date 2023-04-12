import pandas as pd

results = []
candidates = ['Baswedan', 'Subianto', 'Maharani', 'Ganjar']


def arrange(array, memory=[], results=None):
    if results is None:
        results = []
    for i in range(len(array)):
        current = [array[i]]
        remaining = array[:i] + array[i+1:]
        if not remaining:
            results.append(memory + current)
        results = arrange(remaining, memory + current, results)
    return results

chairs = arrange(candidates)
# mencetak dalam bentuk tabel
df = pd.DataFrame(chairs)
print(df)