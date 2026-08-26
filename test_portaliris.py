# test_portaliris.py
"""
Tests for PortalIris module.
"""

import unittest
from portaliris import PortalIris

class TestPortalIris(unittest.TestCase):
    """Test cases for PortalIris class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PortalIris()
        self.assertIsInstance(instance, PortalIris)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PortalIris()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
