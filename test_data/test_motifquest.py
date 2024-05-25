import unittest
from motifquest import read_sequences

class TestMotifQuest(unittest.TestCase):
    def test_read_sequences(self):
        sequences = read_sequences("test_data/example.fasta")
        self.assertEqual(len(sequences), 2)
        self.assertEqual(sequences[0], "ATCGTACGATCG")

if __name__ == "__main__":
    unittest.main()
