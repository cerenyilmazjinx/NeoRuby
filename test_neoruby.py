# test_neoruby.py
"""
Tests for NeoRuby module.
"""

import unittest
from neoruby import NeoRuby

class TestNeoRuby(unittest.TestCase):
    """Test cases for NeoRuby class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NeoRuby()
        self.assertIsInstance(instance, NeoRuby)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NeoRuby()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
