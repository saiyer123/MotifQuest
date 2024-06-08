import sys
import numpy as np
from Bio import SeqIO

def read_sequences(input_file):
    sequences = []
    for record in SeqIO.parse(input_file, "fastq"):
        sequences.append(str(record.seq).upper())
    return sequences

def calculate_pwm(sequences):
    # Define the bases and their corresponding indices
    bases = ['A', 'C', 'G', 'T']
    base_to_index = {base: idx for idx, base in enumerate(bases)}
    
    # Initialize the counts matrix
    counts = np.zeros((len(sequences[0]), len(bases)))
    
    for seq in sequences:
        for i, base in enumerate(seq):
            if base in base_to_index:
                counts[i, base_to_index[base]] += 1
            else:
                print(f"Unexpected character '{base}' at position {i} in sequence {seq}")
    
    # Calculate the position weight matrix (PWM)
    pwm = counts / counts.sum(axis=1, keepdims=True)
    return pwm

def main(input_file, output_file):
    sequences = read_sequences(input_file)
    print(f"Read {len(sequences)} sequences.")
    pwm = calculate_pwm(sequences)
    with open(output_file, 'w') as f:
        f.write("PWM:\n")
        f.write(str(pwm))
    print(f"Saved PWM to {output_file}.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python motifquest.py --input <input_file> --output <output_file>")
        sys.exit(1)
    
    input_file = sys.argv[sys.argv.index("--input") + 1]
    output_file = sys.argv[sys.argv.index("--output") + 1]
    main(input_file, output_file)
