"""Classes for melon orders."""


class AbstractMelonOrder(object):
    """Abstract Melon class to Initialize melon"""

    def __init__(self, species, qty, shipped):
        self.species = species
        self.qty = qty
        self.shipped = shipped

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        if (self.species.lower() == "christmas melon"):
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        if (self.qty > 10 and self.order_type == "international"):
            flat_fee = 3.00
            total = total + flat_fee

        return total

    def mark_shipped(self):
        """Record the fact that an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, country_code, species, qty, shipped):
        """Initialize melon order attributes."""
        self.country_code = country_code

        super(InternationalMelonOrder, self).__init__(species, qty, shipped)

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
