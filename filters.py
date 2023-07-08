""" Jinja2 filters for the html version """
import fractions
import re


def ingredient_display(value):
    """Remove annotations on ingredients"""
    return re.sub(r"[{}]", "", value)


def get_computable_quantity(quantity):
    """1/2 to 0.5, for example"""
    try:
        return float(quantity)
    except ValueError:
        pass
    try:
        fraction = fractions.Fraction(quantity)
    except ValueError:
        return 0
    return fraction.numerator / fraction.denominator


def ingredient_data(value):
    """Extract ingredient data"""
    # find teh first set of numbers
    result = re.findall(r"([^\d]*)([\d\/.]+)([^\d]*)", value)
    if not result:
        yield [{"text": ingredient_display(value)}]

    for group in result:
        yield [
            {"type": "text", "text": ingredient_display(group[0])},
            {
                "type": "quantity",
                "text": group[1],
                "value": get_computable_quantity(group[1]),
            },
            {"type": "text", "text": ingredient_display(group[2])},
        ]
