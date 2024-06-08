import numpy as np

# Function to read sequences from FASTQ file
def read_sequences(file_path):
    sequences = []
    with open(file_path, 'r') as f:
        for i, line in enumerate(f):
            if i % 4 == 1:  # The sequence lines in a FASTQ file are every 4th line, starting from the second line
                sequences.append(line.strip())
    return sequences

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

    # Avoid division by zero by adding a small epsilon value
    pwm = counts / (counts.sum(axis=1, keepdims=True) + 1e-6)
    return pwm

# Read sequences from the input FASTQ file
input_file = "test_data/cse185proj.fastq"
sequences = read_sequences(input_file)

# Check if sequences were read correctly
if len(sequences) == 0:
    print("No sequences read from the file.")
else:
    print(f"Read {len(sequences)} sequences.")

# Calculate the PWM
pwm = calculate_pwm(sequences)

# Print the PWM
print("PWM:")
print(pwm)

# Save the PWM to an output file
output_file = "test_data/cse185_output.txt"
with open(output_file, 'w') as f:
    f.write("PWM:\n")
    np.savetxt(f, pwm)
