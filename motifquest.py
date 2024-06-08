def read_sequences(input_file):
    sequences = []
    with open(input_file) as f:
        count = 0
        for line in f:
            count += 1
            if count % 4 == 2:  # Only read the sequence lines
                sequences.append(line.strip())
    return sequences

def calculate_pwm(sequences):
    import numpy as np

    # Print the number of sequences read
    print(f"Total sequences read: {len(sequences)}")
    print(f"First 10 sequences: {sequences[:10]}")  # Print first 10 sequences for debugging
    
    # Determine the most common sequence length
    lengths = [len(seq) for seq in sequences]
    most_common_length = max(set(lengths), key=lengths.count)
    print(f"Most common sequence length: {most_common_length}")
    
    # Filter sequences to only include those of the most common length
    filtered_sequences = [seq for seq in sequences if len(seq) == most_common_length]
    print(f"Filtered sequences count: {len(filtered_sequences)}")
    print(f"First 10 filtered sequences: {filtered_sequences[:10]}")  # Print first 10 filtered sequences for debugging
    
    if len(filtered_sequences) == 0:
        raise ValueError("No sequences of the most common length found")
    
    # Initialize the count matrix
    counts = np.zeros((most_common_length, 4))
    base_to_index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    
    for seq in filtered_sequences:
        for i, base in enumerate(seq):
            if base in base_to_index:
                counts[i, base_to_index[base]] += 1
            else:
                print(f"Unexpected base '{base}' found in sequence '{seq}'")  # Debugging unexpected bases
    
    print("Counts matrix before normalization:\n", counts)  # Debugging the counts matrix
    
    # Calculate the PWM
    pwm = counts / counts.sum(axis=1, keepdims=True)
    print("PWM matrix:\n", pwm)  # Debugging the PWM matrix
    
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
    try:
        pwm = calculate_pwm(sequences)
        
        # Write the PWM to the output file
        with open(args.output, 'w') as f:
            f.write("PWM:\n")
            f.write(str(pwm))
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()


