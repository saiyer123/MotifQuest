def calculate_pwm(sequences):
    import numpy as np
    
    # Create a dictionary to map nucleotides to indices
    base_to_index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    
    # Initialize the counts array
    counts = np.zeros((len(sequences[0]), len(base_to_index)))
    
    # Debug: Print sequences
    print("Sequences:")
    for seq in sequences:
        print(seq)
    
    # Count the occurrences of each nucleotide at each position
    for seq in sequences:
        for i, base in enumerate(seq):
            if base in base_to_index:
                counts[i, base_to_index[base]] += 1
    
    # Debug: Print counts before normalization
    print("Counts before normalization:")
    print(counts)
    
    # Convert counts to probabilities (PWM)
    pwm = counts / counts.sum(axis=1, keepdims=True)
    
    # Debug: Print PWM
    print("PWM:")
    print(pwm)
    
    return pwm

def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Calculate PWM from FASTQ sequences.')
    parser.add_argument('--input', required=True, help='Input FASTQ file')
    parser.add_argument('--output', required=True, help='Output file for PWM')
    args = parser.parse_args()
    
    # Read sequences from the input FASTQ file
    sequences = read_sequences(args.input)
    
    # Calculate the PWM
    pwm = calculate_pwm(sequences)
    
    # Write the PWM to the output file
    with open(args.output, 'w') as f:
        f.write("PWM:\n")
        f.write(str(pwm))

def read_sequences(input_file):
    sequences = []
    with open(input_file) as f:
        count = 0
        for line in f:
            count += 1
            if count % 4 == 2:  # Only read the sequence lines
                sequences.append(line.strip())
    return sequences

if __name__ == '__main__':
    main()
