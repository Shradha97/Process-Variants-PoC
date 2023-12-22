from collections import defaultdict


def get_seq_dict(df, col):
    entities = df[col].unique()

    # assign each task a unique alphabet id
    seq = defaultdict()
    for i, task in enumerate(entities):
        seq[task] = chr(i + 65)
    return seq


def get_fasta(
    df,
    seq_dict,
    col,
    label_col,
    label_prefix="",
    excludeConsecutive=False,
    align=True,
):
    fasta = []
    sequences = []
    for row in df.iterrows():
        sequence = ""
        x = f"> {label_prefix + str(row[1][label_col])} \n"
        fasta.append(x)
        prev = None
        for e in row[1][col]:
            if excludeConsecutive:
                if prev != e:
                    fasta.append(seq_dict[e])
                    prev = e
            else:
                fasta.append(seq_dict[e])
            if align:
                sequence += seq_dict[e]
        fasta.append("\n")
        sequences.append(sequence)
    return "".join(fasta), sequences


def get_aligned_fasta(
    df,
    col,
    label_col,
    label_prefix="",
    excludeConsecutive=False,
):
    fasta = []
    for row in df.iterrows():
        x = f"> {label_prefix + str(row[1][label_col])} \n"
        fasta.append(x)
        prev = None
        for e in row[1][col]:
            if excludeConsecutive:
                if prev != e:
                    fasta.append(e)
                    prev = e
            else:
                fasta.append(e)
        fasta.append("\n")
    return "".join(fasta)


def read_fasta_file(fasta_file):
    with open(fasta_file, "r") as f:
        lines = f.readlines()
    return lines


def save_fasta(fasta, path):
    with open(path, "w") as f:
        f.write(fasta)
