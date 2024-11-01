class HammingCode:
    def __init__(self, code):
        self.code = code
        self.parity_loc = [1, 2, 4, 8]

    def find_parity(self):
        bit_list = []
        parity_bits = {}

        for bit in self.code:
            bit_list.append(int(bit))

        for p in self.parity_loc:
            parity_sum = sum(bit_list[i - 1] for i in range(1, len(bit_list) + 1) if i & p)
            parity_bits[p] = parity_sum % 2

        return parity_bits

    def check_code(self):
        parity_bits = self.find_parity()
        error_position = 0

        for p in self.parity_loc:
            if parity_bits[p] != int(self.code[p - 1]):
                error_position += p

        return error_position
