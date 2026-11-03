# Module 3: Numeric in Python

---

## 1. Understanding Numbers and Basic Arithmetic

Python has three distinct built-in numeric types:
1. **Integers (`int`)**: Arbitrary precision. Unlike C/Java where integers overflow at 32-bit ($2^{31}-1$) or 64-bit ($2^{63}-1$), Python integers can grow as large as your computer's RAM permits:
   ```python
   googol = 10 ** 100
   print(googol) # Fully supported without overflow!
   ```
2. **Floating-Point Numbers (`float`)**: Implemented using double-precision (64-bit) IEEE 754 representation.
   - 53 bits of precision (~15-17 significant decimal digits).
   - Range approximately $1.79 \times 10^{308}$.
3. **Complex Numbers (`complex`)**: Written in the form `real + imag*j`:
   ```python
   z = 3 + 4j
   print(z.real, z.imag, abs(z)) # 3.0, 4.0, 5.0
   ```

---

## 2. Floats, Modulo Operations, and Order of Operations

### Standard Arithmetic Operators

| Operator | Name | Description | Example | Result |
| :---: | :--- | :--- | :---: | :---: |
| `+` | Addition | Sum of operands | `15 + 4` | `19` |
| `-` | Subtraction | Difference | `15 - 4` | `11` |
| `*` | Multiplication | Product | `15 * 4` | `60` |
| `/` | True Division | Always returns a float | `15 / 4` | `3.75` |
| `//` | Floor Division | Division rounded down to nearest integer | `15 // 4` | `3` |
| `%` | Modulo | Remainder after division | `15 % 4` | `3` |
| `**` | Exponentiation | Power operation | `2 ** 8` | `256` |

### Operator Precedence (PEMDAS / BODMAS)
Python evaluates expressions strictly by precedence:
1. **P**arentheses: `(...)`
2. **E**xponentiation: `**` (Evaluated right-to-left: `2 ** 3 ** 2` is $2^9 = 512$)
3. **M**ultiplication, **D**ivision, **F**loor Division, **M**odulo: `*`, `/`, `//`, `%`
4. **A**ddition, **S**ubtraction: `+`, `-`

### Floating-Point Representation Quirks
In binary floating-point, numbers like $0.1$ cannot be represented with infinite exactness:
```python
0.1 + 0.2 == 0.3 # Evaluates to FALSE!
0.1 + 0.2        # 0.30000000000000004
```
**Solutions**:
1. For scientific/general tolerance checking: Use `math.isclose(a, b)`:
   ```python
   import math
   math.isclose(0.1 + 0.2, 0.3) # True
   ```
2. For financial and accounting systems: Use Python's built-in `decimal.Decimal`:
   ```python
   from decimal import Decimal
   Decimal("0.1") + Decimal("0.2") == Decimal("0.3") # True
   ```

---

## 3. Introduction to Python's `math` Module

The standard library `math` module supplies C-standard mathematical functions:

```python
import math

math.sqrt(64)        # 8.0 (Square root)
math.pow(2, 5)       # 32.0 (Float power)
math.ceil(4.15)      # 5 (Round UP)
math.floor(4.85)     # 4 (Round DOWN)
math.trunc(-3.7)     # -3 (Truncate decimal part)
math.factorial(5)    # 120 (5!)
math.gcd(48, 18)     # 6 (Greatest common divisor)
math.pi              # 3.141592653589793
math.e               # 2.718281828459045
math.log(100, 10)    # 2.0 (Logarithm base 10)
```

---

## 4. Hands-On Project: Financial Loan EMI & Compound Interest

In financial applications:
- **Compound Interest Formula**:
  $$A = P \left(1 + \frac{r}{n}\right)^{nt}$$
  Where:
  - $P$ = Principal investment
  - $r$ = Annual nominal interest rate (decimal)
  - $n$ = Compounding periods per year
  - $t$ = Number of years
- **Equated Monthly Installment (EMI) Formula**:
  $$\text{EMI} = \frac{P \cdot r \cdot (1 + r)^n}{(1 + r)^n - 1}$$
  Where $r$ is monthly interest rate ($\text{annual rate} / 12 / 100$) and $n$ is total months.

