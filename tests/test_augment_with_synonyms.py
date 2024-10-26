import unittest
import os
import sys
from src.augment_with_synonyms import augment_with_synonyms

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestAugmentation(unittest.TestCase):
    def setUp(self):
        self.model_response_path = 'data/model_response.txt'
        self.augmented_response_path = 'data/synonym_augmented_model_response.txt'
        self._check_file_exists(self.model_response_path, "Model response")

    def _check_file_exists(self, file_path, file_description):
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The {file_description} file '{
                                    file_path}' does not exist")

    def test_model_response_text_exists(self):
        self.assertTrue(os.path.exists(self.model_response_path),
                        f"The Model response file '{self.model_response_path}' does not exist")

    def test_synonym_augmentation(self):
        # Perform synonym augmentation
        augment_with_synonyms(self.model_response_path,
                              self.augmented_response_path)

        # Check if the augmented file was created
        self.assertTrue(os.path.exists(self.augmented_response_path),
                        f"The augmented response file '{self.augmented_response_path}' was not created")

        # Check if the augmented file is different from the original
        with open(self.model_response_path, 'r') as original, open(self.augmented_response_path, 'r') as augmented:
            original_content = original.read()
            augmented_content = augmented.read()
            self.assertNotEqual(original_content, augmented_content,
                                "The augmented content should be different from the original")

    def tearDown(self):
        # Clean up the augmented file after the test
        if os.path.exists(self.augmented_response_path):
            os.remove(self.augmented_response_path)


if __name__ == '__main__':
    unittest.main()
