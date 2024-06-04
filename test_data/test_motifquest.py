import unittest
import sys
import os

# Add the directory containing motifquest.py to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from motifquest import read_sequences, find_motifs

class TestMotifQuest(unittest.TestCase):
    def test_read_sequences(self):
        sequences = read_sequences("test_data/example.fasta")
        self.assertEqual(len(sequences), 2)
        self.assertEqual(sequences[0], "ATCGTACGATCG")

    def test_find_motifs(self):
        sequences = ["ATCGTACGATCG", "CGATCGTAGCTA"]
        pwm = find_motifs(sequences, motif_length=6)
        self.assertEqual(pwm.shape, (6, 4))

if __name__ == "__main__":
    unittest.main()


