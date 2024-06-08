import subprocess
import time
import os
from motifquest import read_sequences, find_motifs

def benchmark(input_file):
    # Read sequences from input file
    sequences = read_sequences(input_file)

    # Benchmark MotifQuest
    start_time = time.time()
    pwm = find_motifs(sequences, motif_length=6)
    motifquest_time = time.time() - start_time

    # Benchmark MEME
    meme_output_dir = "meme_output"
    if not os.path.exists(meme_output_dir):
        os.makedirs(meme_output_dir)
    
    meme_command = ["meme", input_file, "-oc", meme_output_dir]
    start_time = time.time()
    subprocess.run(meme_command)
    meme_time = time.time() - start_time

    # Print benchmarking results
    print(f"MotifQuest execution time: {motifquest_time:.2f} seconds")
    print(f"MEME execution time: {meme_time:.2f} seconds")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Benchmark MotifQuest against MEME")
    parser.add_argument("--input", required=True, help="Input file with sequences")
    args = parser.parse_args()

    benchmark(args.input)
