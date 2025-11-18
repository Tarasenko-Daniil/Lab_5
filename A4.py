import sys
from contextlib import redirect_stdout

with open('genedata.0.txt', 'w', encoding='utf-8') as f:
    sys.stdout = f

    def rle(string):
        code = []
        count = 1
        for i in range(1, len(string)+1):
            if i < len(string) and string[i] == string[i-1]:
                count += 1
            else:
                if count <= 2:
                    code.append(string[i-1] * count)
                else:
                    code.append(str(count) + string[i-1])
                count = 1
        c = ''.join(code)
        return c
  protein = []
    creature = []
    chains = []

    with open("sequences.0.txt", "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split("\t")
            protein.append(parts[0])
            creature.append(parts[1])
            chains.append(parts[2])

    proteins_chains = dict(zip(protein, chains))

    def search(seq, encoded_seq):
        decoded = rle(encoded_seq)
        if seq in decoded:
            return True
        else:
            return False
            
    def diff(first_chain, second_chain):
        decoded_first = rle(first_chain)
        decoded_second = rle(second_chain)

        difference_count = abs(len(decoded_first) - len(decoded_second))

        max_len = max(len(decoded_first), len(decoded_second))
        for i in range(max_len):
            char_first = decoded_first[i] if i < len(decoded_first) else None
            char_second = decoded_second[i] if i < len(decoded_second) else None
            if char_first != char_second:
                difference_count += 1

        return difference_count



