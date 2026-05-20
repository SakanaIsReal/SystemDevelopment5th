"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException


class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self):
        """Test adding positive number with zero."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self):
        """Test adding zero with positive number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self):
        """Test adding floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_add_upper_limit_a(self):
        """Test adding upper limit raises InvalidInputException."""
        # Arrange
        calc = Calculator()
        a = 10000000000000
        b = 10

        # Act & Assert
        with pytest.raises(
            InvalidInputException,
            match=r"Input value 10000000000000 is outside the valid range\[-1000000, 1000000\]",
        ):
            calc.add(a, b)

    def test_add_lower_limit_a(self):
        """Test adding lower limit raises InvalidInputException."""
        # Arrange
        calc = Calculator()
        a = -10000000000000
        b = 10

        # Act & Assert
        with pytest.raises(
            InvalidInputException,
            match=r"Input value -10000000000000 is outside the valid range\[-1000000, 1000000\]",
        ):
            calc.add(a, b)

    def test_add_upper_limit_b(self):
        """Test adding upper limit raises InvalidInputException."""
        # Arrange
        calc = Calculator()
        a = 10
        b = 10000000000000

        # Act & Assert
        with pytest.raises(
            InvalidInputException,
            match=r"Input value 10000000000000 is outside the valid range\[-1000000, 1000000\]",
        ):
            calc.add(a, b)

    def test_add_lower_limit_b(self):
        """Test adding lower limit raises InvalidInputException."""
        # Arrange
        calc = Calculator()
        a = 10
        b = -10000000000000

        # Act & Assert
        with pytest.raises(
            InvalidInputException,
            match=r"Input value -10000000000000 is outside the valid range\[-1000000, 1000000\]",
        ):
            calc.add(a, b)

    def test_add_exact_min_value_raises(self):
        """Test that exactly MIN_VALUE (-1000000) raises InvalidInputException."""
        # Arrange
        calc = Calculator()
        a = -1000000
        b = 0

        # Act & Assert
        with pytest.raises(
            InvalidInputException,
            match=r"Input value -1000000 is outside the valid range\[-1000000, 1000000\]",
        ):
            calc.add(a, b)

    def test_add_exact_max_value_raises(self):
        """Test that exactly MAX_VALUE (1000000) raises InvalidInputException."""
        # Arrange
        calc = Calculator()
        a = 1000000
        b = 0

        # Act & Assert
        with pytest.raises(
            InvalidInputException,
            match=r"Input value 1000000 is outside the valid range\[-1000000, 1000000\]",
        ):
            calc.add(a, b)


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self):
        """Test subtracting two positive numbers."""
        # Arrange
        calc = Calculator()
        a = 3
        b = 2
        expected = 1

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_subtract_negative_numbers(self):
        """Test subtracting two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -2

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_subtract_positive_and_negative(self):
        """Test subtracting a negative from a positive number."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 8

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_subtract_negative_and_positive(self):
        """Test subtracting a positive from a negative number."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -8

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_subtract_positive_with_zero(self):
        """Test subtracting zero from a positive number."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_subtract_zero_with_positive(self):
        """Test subtracting a positive number from zero."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = -5

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_subtract_floats(self):
        """Test subtracting floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 5.5
        b = 2.2
        expected = 3.3

        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_subtract_upper_limit_a(self):
        """Test subtracting upper limit raises InvalidInputException."""
        # Arrange
        calc = Calculator()
        a = 10000000000000
        b = 10

        # Act & Assert
        with pytest.raises(
            InvalidInputException,
            match=r"Input value 10000000000000 is outside the valid range\[-1000000, 1000000\]",
        ):
            calc.subtract(a, b)

    def test_subtract_lower_limit_a(self):
        """Test subtracting lower limit raises InvalidInputException."""
        # Arrange
        calc = Calculator()
        a = -10000000000000
        b = 10

        # Act & Assert
        with pytest.raises(
            InvalidInputException,
            match=r"Input value -10000000000000 is outside the valid range\[-1000000, 1000000\]",
        ):
            calc.subtract(a, b)

    def test_subtract_upper_limit_b(self):
        """Test subtracting upper limit in b raises InvalidInputException."""
        # Arrange
        calc = Calculator()
        a = 10
        b = 10000000000000

        # Act & Assert
        with pytest.raises(
            InvalidInputException,
            match=r"Input value 10000000000000 is outside the valid range\[-1000000, 1000000\]",
        ):
            calc.subtract(a, b)

    def test_subtract_lower_limit_b(self):
        """Test subtracting lower limit in b raises InvalidInputException."""
        # Arrange
        calc = Calculator()
        a = 10
        b = -10000000000000

        # Act & Assert
        with pytest.raises(
            InvalidInputException,
            match=r"Input value -10000000000000 is outside the valid range\[-1000000, 1000000\]",
        ):
            calc.subtract(a, b)


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self):
        """Test multiplying two positive numbers."""
        # Arrange
        calc = Calculator()
        a = 6
        b = 7
        expected = 42

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_multiply_negative_numbers(self):
        """Test multiplying two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -6
        b = -7
        expected = 42

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_multiply_positive_and_negative(self):
        """Test multiplying a positive and a negative number."""
        # Arrange
        calc = Calculator()
        a = 6
        b = -7
        expected = -42

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_multiply_with_zero(self):
        """Test multiplying a number by zero."""
        # Arrange
        calc = Calculator()
        a = 6
        b = 0
        expected = 0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_multiply_floats(self):
        """Test multiplying floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 4.0
        expected = 10.0

        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_multiply_upper_limit_a(self):
        """Test multiplying upper limit raises InvalidInputException."""
        # Arrange
        calc = Calculator()
        a = 10000000000000
        b = 10

        # Act & Assert
        with pytest.raises(
            InvalidInputException,
            match=r"Input value 10000000000000 is outside the valid range\[-1000000, 1000000\]",
        ):
            calc.multiply(a, b)

    def test_multiply_lower_limit_a(self):
        """Test multiplying lower limit raises InvalidInputException."""
        # Arrange
        calc = Calculator()
        a = -10000000000000
        b = 10

        # Act & Assert
        with pytest.raises(
            InvalidInputException,
            match=r"Input value -10000000000000 is outside the valid range\[-1000000, 1000000\]",
        ):
            calc.multiply(a, b)

    def test_multiply_upper_limit_b(self):
        """Test multiplying upper limit in b raises InvalidInputException."""
        # Arrange
        calc = Calculator()
        a = 10
        b = 10000000000000

        # Act & Assert
        with pytest.raises(
            InvalidInputException,
            match=r"Input value 10000000000000 is outside the valid range\[-1000000, 1000000\]",
        ):
            calc.multiply(a, b)

    def test_multiply_lower_limit_b(self):
        """Test multiplying lower limit in b raises InvalidInputException."""
        # Arrange
        calc = Calculator()
        a = 10
        b = -10000000000000

        # Act & Assert
        with pytest.raises(
            InvalidInputException,
            match=r"Input value -10000000000000 is outside the valid range\[-1000000, 1000000\]",
        ):
            calc.multiply(a, b)


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self):
        """Test dividing two positive numbers."""
        # Arrange
        calc = Calculator()
        a = 4
        b = 2
        expected = 2

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_divide_negative_numbers(self):
        """Test dividing two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -4
        b = -2
        expected = 2

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_divide_positive_and_negative(self):
        """Test dividing a positive by a negative number."""
        # Arrange
        calc = Calculator()
        a = 4
        b = -2
        expected = -2

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_divide_zero_by_number(self):
        """Test dividing zero by a number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_divide_floats(self):
        """Test dividing floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 7.5
        b = 2.5
        expected = 3.0

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)

    def test_divide_by_zero(self):
        """Test dividing by zero raises ValueError."""
        # Arrange
        calc = Calculator()
        a = 4
        b = 0

        # Act & Assert
        with pytest.raises(ValueError, match=r"^Cannot divide by zero$"):
            calc.divide(a, b)

    def test_divide_upper_limit_a(self):
        """Test dividing upper limit raises InvalidInputException."""
        # Arrange
        calc = Calculator()
        a = 10000000000000
        b = 10

        # Act & Assert
        with pytest.raises(
            InvalidInputException,
            match=r"Input value 10000000000000 is outside the valid range\[-1000000, 1000000\]",
        ):
            calc.divide(a, b)

    def test_divide_lower_limit_a(self):
        """Test dividing lower limit raises InvalidInputException."""
        # Arrange
        calc = Calculator()
        a = -10000000000000
        b = 10

        # Act & Assert
        with pytest.raises(
            InvalidInputException,
            match=r"Input value -10000000000000 is outside the valid range\[-1000000, 1000000\]",
        ):
            calc.divide(a, b)

    def test_divide_upper_limit_b(self):
        """Test dividing upper limit in b raises InvalidInputException."""
        # Arrange
        calc = Calculator()
        a = 10
        b = 10000000000000

        # Act & Assert
        with pytest.raises(
            InvalidInputException,
            match=r"Input value 10000000000000 is outside the valid range\[-1000000, 1000000\]",
        ):
            calc.divide(a, b)

    def test_divide_lower_limit_b(self):
        """Test dividing lower limit in b raises InvalidInputException."""
        # Arrange
        calc = Calculator()
        a = 10
        b = -10000000000000

        # Act & Assert
        with pytest.raises(
            InvalidInputException,
            match=r"Input value -10000000000000 is outside the valid range\[-1000000, 1000000\]",
        ):
            calc.divide(a, b)

    def test_divide_by_one(self):
        """Test dividing by one returns the numerator unchanged."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 1
        expected = 5

        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == pytest.approx(expected)
