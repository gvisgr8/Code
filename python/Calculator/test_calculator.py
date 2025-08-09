import pytest
from python.Calculator.Calculator import *

class TestCalculator:
    @pytest.fixture
    def calculator(self):
        """Fixture that creates a Calculator instance for each test."""
        return Calculator()
    
    def test_add(self, calculator):
        """Test the add method with positive numbers."""
        assert calculator.add(3, 5) == 8
        assert calculator.add(-1, 1) == 0
        assert calculator.add(-1, -1) == -2
        assert calculator.add(0, 0) == 0
    
    def test_multiply(self, calculator):
        """Test the multiply method."""
        assert calculator.multiply(3, 5) == 15
        assert calculator.multiply(-2, 6) == -12
        assert calculator.multiply(-2, -2) == 4
        assert calculator.multiply(0, 5) == 0
    
    def test_subtract(self, calculator):
        """Test the subtract method."""
        assert calculator.subtract(5, 3) == 2
        assert calculator.subtract(1, 5) == -4
        assert calculator.subtract(-1, -1) == 0
        assert calculator.subtract(0, 0) == 0
    
    def test_divide(self, calculator):
        """Test the divide method with valid inputs."""
        assert calculator.divide(6, 2) == 3
        assert calculator.divide(-6, 2) == -3
        assert calculator.divide(0, 5) == 0
        assert calculator.divide(5, 2) == 2.5
    
    def test_divide_by_zero(self, calculator):
        """Test that division by zero raises a ValueError."""
        with pytest.raises(ValueError) as exc_info:
            calculator.divide(5, 0)
        assert str(exc_info.value) == "Cannot divide by zero."
