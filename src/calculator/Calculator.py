from .numberConverter import NumberConverter

class Calculator:
    converter = NumberConverter()
    # Opérations de base
    def add(self, a, b):
        return self.converter.to_number(a) + self.converter.to_number(b)

    def sub(self, a, b):
        return self.converter.to_number(a) - self.converter.to_number(b)

    def mul(self, a, b):
        return self.converter.to_number(a) * self.converter.to_number(b)

    def div(self, a, b):
        b_val = self.converter.to_number(b)
        if b_val == 0:
            raise ValueError("Cannot divide by zero")
        return self.converter.to_number(a) / b_val

    # Factorisation en nombres premiers
    def factorize(self, n):
        n_val = int(self.converter.to_number(n))
        if n_val < 2:
            return [n_val]
        factors = []
        i = 2
        while i * i <= n_val:
            while n_val % i == 0:
                factors.append(i)
                n_val //= i
            i += 1
        if n_val > 1:
            factors.append(n_val)
        return factors
