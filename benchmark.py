import subprocess
import time
from motifquest import read_sequences, find_motifs

def benchmark(input_file):
    sequences = read_sequences(input_file)

    start_time = time.time()
    pwm = find_motifs(sequences, motif_length=6)
    motifquest_time = time.time() - start_time

    # Run MEME command line tool for benchmarking
    meme_command = ["meme", input_file, "-oc", "meme_output"]
    start_time = time.time()
    subprocess.run(meme_command)
    meme_time = time.time() - start_time

    print(f"MotifQuest execution time: {motifquest_time:.2f} seconds")
    print(f"MEME execution time: {meme_time:.2f} seconds")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Benchmark MotifQuest against MEME")
    parser.add_argument("--input", required=True, help="Input file with sequences")
    args = parser.parse_args()

    benchmark(args.input)
