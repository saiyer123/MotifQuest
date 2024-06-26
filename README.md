# MotifQuest

MotifQuest is a specialized software tool designed to identify motifs within DNA sequences, which are the specific sequences recognized by transcription factors (TFs). The project aims to compare the effectiveness of MotifQuest against MEME (Multiple EM for Motif Elicitation).

## Project Description

MotifQuest leverages efficient algorithms for pattern matching and statistical modeling to identify transcription factor binding sites within DNA sequences. The specific method to be implemented is motif finding through probabilistic models such as Position Weight Matrices (PWMs) and Expectation Maximization (EM). 

### Key Features:
- **Probabilistic Models:** Uses PWMs to model the frequency of each nucleotide at each position in the motif.
- **Iterative Refinement:** Employs EM to iteratively refine the PWM based on observed sequence data, improving the accuracy of motif detection.
- **Benchmarking:** Compares the performance of MotifQuest with MEME, a widely-used tool in bioinformatics.

### Implementation Details:
- **Programming Language:** Python
- **Libraries:** Utilizes Biopython for sequence data manipulation and NumPy for numerical computations.
- **Input Data:** Sequences derived from ChIP-seq data, providing peaks corresponding to binding sites where TFs are enriched.

# Installation

To install the necessary dependencies, run:
```bash
pip install -r requirements.txt
 ```
# Running MEME with Docker
Pull the MEME Suite Docker image:
```bash
docker pull memesuite/memesuite
```
Run MEME on your FASTA file:
```bash
docker run -v ~/meme_data:/data memesuite/memesuite meme /data/new_extracted_nucleotide_sequences_dataset0.fasta -o /data/meme_output_new
```
#### For macOS:
1. Download Docker Desktop for Mac from the [Docker website](https://www.docker.com/products/docker-desktop).
2. Open the downloaded `.dmg` file and drag the Docker icon to your Applications folder.
3. Open Docker from your Applications folder.
4. Follow the instructions in the Docker Desktop window to complete the setup.

To set up the environment and install the necessary dependencies, follow these steps:

1. **Create and activate a new Conda environment:**
   Using Miniconda or Anaconda
If you have Miniconda or Anaconda installed, you can create a new Conda environment and install the necessary dependencies as follows. If not download version 4.10.2 of Anocanda on their official website.

   ```bash
   conda create -n new_meme_env
   conda activate new_meme_env
Install MEME-suite: 
 ```bash
conda install -c bioconda meme
```
Verify the Installation: 
 ```bash
meme --version
```


# Usage

To run the tool, use the following command: 
```bash
python motifquest.py --input test_data/extracted_nucleotide_sequences_dataset0.txt --output output_file.txt
```
To Run MEME on the FASTA formatted file:
```bash
docker run -v ~/meme_data:/data memesuite/memesuite meme /data/new_extracted_nucleotide_sequences_dataset0.fasta -o /data/meme_output_new
```

# Running Benchmarking
To benchmark MotifQuest against MEME, use the following command:
```bash
python benchmark.py --input test_data/extracted_nucleotide_sequences_dataset0.txt
```
## Testing

Example test datasets are provided in the `test_data` directory. To run tests, use: python test_motifquest.py
Before running the tests, ensure you set the PYTHONPATH to your current directory:
```bash
export PYTHONPATH=$(pwd)
```
To run the tests, use the following command: 
 ```bash
python test_data/test_motifquest.py
```


# Contributors

- Dennis Chan (PID: A17009513)
- Sahil Iyer (PID: A16882413)




