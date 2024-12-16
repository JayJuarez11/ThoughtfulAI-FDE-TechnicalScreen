class Solution:

    def sort(self, width, height, length, mass):
        """
        :param width: centimeters (float)
        :param height: centimeters (float)
        :param length: centimeters (float)
        :param mass: kilograms (float)
        :return: name of the stack (string)
        """
        # Determining if package is bulky and/or heavy
        volume = width * height * length
        is_bulky = volume >= 1000000 or max(width, height, length) >= 150
        is_heavy = mass >= 20

        # Dispatch package to the correct stack
        if is_bulky and is_heavy:
            return "REJECTED"
        if is_bulky or is_heavy:
            return "SPECIAL"
        return "STANDARD"
