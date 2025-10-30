def comparisons(seq: list[int]):
    return [b - a for a, b in zip(seq, seq[1:])]


with open("Data/_9_1.txt") as f:
    sequences = []
    predicted_numbers = []

    for line in f.readlines():
        sub_seqs = []
        sequence = list(map(int, line.split()))

        sub_seq = sequence.copy()
        while any(sub_seq):
            sub_seq = comparisons(sub_seq)
            sub_seqs.append(sub_seq)

        sub_seqs.pop()
        previous_last_number = 0

        for sub_seq in reversed(sub_seqs):
            sub_seq.append(previous_last_number + sub_seq[-1])
            previous_last_number = sub_seq[-1]
        predicted_numbers.append(previous_last_number + sequence[-1])

    print(f"Sum of all predicted numbers : {sum(predicted_numbers)}")
