import numpy as np
import matplotlib.pyplot as plt
import argparse

def read_sequences(input_file):
    sequences = []
    with open(input_file, 'r') as f:
        for line in f:
            sequence = line.strip()
            if sequence:  # Check if the line is not empty
                sequences.append(sequence)
    return sequences

def initialize_pwm(sequences, motif_length):
    pwm = np.random.rand(motif_length, 4)
    pwm /= pwm.sum(axis=1, keepdims=True)
    return pwm

def expectation_maximization(sequences, pwm, iterations=100):
    for _ in range(iterations):
        counts = np.zeros_like(pwm)
        for seq in sequences:
            for i in range(len(seq) - pwm.shape[0] + 1):
                subseq = seq[i:i + pwm.shape[0]]
                for j, base in enumerate(subseq):
                    if base in 'ACGT':
                        counts[j, 'ACGT'.index(base)] += 1
        pwm = counts / counts.sum(axis=1, keepdims=True)
    return pwm

def find_motifs(sequences, motif_length):
    pwm = initialize_pwm(sequences, motif_length)
    pwm = expectation_maximization(sequences, pwm)
    return pwm

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MotifQuest: Motif Finding Tool")
    parser.add_argument("--input", required=True, help="Input file with sequences")
    parser.add_argument("--output", required=True, help="Output file for PWM results")
    args = parser.parse_args()

    # Read sequences from the input file
    sequences = read_sequences(args.input)

    # Check if sequences were read correctly
    if len(sequences) == 0:
        print("No sequences read from the file.")
    else:
        print(f"Read {len(sequences)} sequences.")

    # Plot histogram of nucleotide frequencies
    nucleotide_counts = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for sequence in sequences:
        for nucleotide in sequence:
            if nucleotide in nucleotide_counts:
                nucleotide_counts[nucleotide] += 1

    plt.bar(nucleotide_counts.keys(), nucleotide_counts.values())
    plt.xlabel('Nucleotide')
    plt.ylabel('Frequency')
    plt.title('Nucleotide Frequency Histogram')

    # Save the histogram plot if an output file is specified
    if args.output:
        output_histogram_filename = args.output.replace(".txt", "_histogram.png")
        plt.savefig(output_histogram_filename)
        print(f"Histogram plot saved as {output_histogram_filename}")

        # Display the histogram plot
        plt.show()

    # Calculate the PWM
    motif_length = 6  # Example motif length
    pwm = find_motifs(sequences, motif_length)

    # Save the PWM to an output file
    with open(args.output, 'w') as f:
        f.write("PWM:\n")
        np.savetxt(f, pwm)




