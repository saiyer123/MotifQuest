import numpy as np
from Bio import SeqIO

def read_sequences(input_file):
# Function to read sequences from FASTQ file
    def read_sequences(file_path):
        sequences = []
        for record in SeqIO.parse(input_file, "fasta"):
            sequences.append(str(record.seq))
        with open(file_path, 'r') as f:
            for i, line in enumerate(f):
                if i % 4 == 1:  # The sequence lines in a FASTQ file are every 4th line, starting from the second line
                    sequences.append(line.strip())
        return sequences

def initialize_pwm(sequences, motif_length):
    # Initialize PWM with random values
    pwm = np.random.rand(motif_length, 4)
    pwm /= pwm.sum(axis=1, keepdims=True)
    return pwm
# Function to calculate PWM
def calculate_pwm(sequences):
    sequence_length = len(sequences[0])
    counts = np.zeros((sequence_length, 4))  # Initialize count matrix

    # Dictionary to map nucleotides to indices
    base_to_index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

    # Fill the count matrix
    for seq in sequences:
        for i, base in enumerate(seq):
            if base in base_to_index:
                counts[i, base_to_index[base]] += 1

def expectation_maximization(sequences, pwm, iterations=100):
    for _ in range(iterations):
        # E-step: Calculate expected counts
        counts = np.zeros_like(pwm)
        for seq in sequences:
            for i in range(len(seq) - pwm.shape[0] + 1):
                subseq = seq[i:i + pwm.shape[0]]
                prob = np.prod([pwm[j, 'ACGT'.index(base)] for j, base in enumerate(subseq)])
                counts += prob
        # M-step: Update PWM with normalized counts
        pwm = counts / counts.sum(axis=1, keepdims=True)
    # Avoid division by zero by adding a small epsilon value
    pwm = counts / (counts.sum(axis=1, keepdims=True) + 1e-6)
    return pwm

def find_motifs(sequences, motif_length):
    pwm = initialize_pwm(sequences, motif_length)
    pwm = expectation_maximization(sequences, pwm)
    return pwm
# Read sequences from the input FASTQ file
input_file = "test_data/cse185proj.fastq"
sequences = read_sequences(input_file)

# Check if sequences were read correctly
if len(sequences) == 0:
    print("No sequences read from the file.")
else:
    print(f"Read {len(sequences)} sequences.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="MotifQuest: Motif Finding Tool")
    parser.add_argument("--input", required=True, help="Input file with sequences")
    parser.add_argument("--output", required=True, help="Output file for results")
    args = parser.parse_args()
# Calculate the PWM
pwm = calculate_pwm(sequences)

    sequences = read_sequences(args.input)
    motif_length = 6  # Example motif length
    pwm = find_motifs(sequences, motif_length)
# Print the PWM
print("PWM:")
print(pwm)

    with open(args.output, 'w') as f:
        f.write("PWM:\n")
        f.write(str(pwm))
# Save the PWM to an output file
output_file = "test_data/cse185_output.txt"
with open(output_file, 'w') as f:
    f.write("PWM:\n")
    np.savetxt(f, pwm)
