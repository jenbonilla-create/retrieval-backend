class PricingEngine:
    def __init__(self):
        self.packages = {
            'backpack_bliss': 79,
            'box_bonanza': 119,
            'mega_box_madness': 159,
            'the_whole_shebang': 199
        }

    def calculate_price(self, package_name, item_count, two_way=False, no_contact=False):
        if package_name not in self.packages:
            raise ValueError('Invalid package name!')
        base_price = self.packages[package_name]

        # Modifier computations
        if item_count < 1:
            raise ValueError('At least one item is required!')
        if item_count in [1, 2]:
            modifier = 0
        elif item_count in [3, 4]:
            modifier = 0
        elif item_count in [5, 6, 7]:
            modifier = 0
        else:
            modifier = 0

        total_price = base_price

        # Apply modifiers
        if two_way:
            total_price += total_price * 0.50  # 50% for two-way retrieval
        if no_contact:
            total_price += total_price * 0.60  # 60% for no-contact service

        return total_price

# Example usage:
if __name__ == '__main__':
    engine = PricingEngine()
    
    # Test cases
    print("Backpack Bliss for 2 items:", engine.calculate_price('backpack_bliss', 2))  # Should return 79
    print("Box Bonanza for 3 items:", engine.calculate_price('box_bonanza', 3))  # Should return 119
    print("Mega Box Madness for 5 items and two-way:", engine.calculate_price('mega_box_madness', 5, two_way=True))  # Should return 238.5
    print("The Whole Shebang for 10 items and no-contact:", engine.calculate_price('the_whole_shebang', 10, no_contact=True))  # Should return 318.4
    print("Box Bonanza for 4 items with two-way and no-contact:", engine.calculate_price('box_bonanza', 4, two_way=True, no_contact=True))  # Should return 318.4
