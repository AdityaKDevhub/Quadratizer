def ProofReading(eq):
      if (len(eq) != 5):
            print("\nPlease try again in the format of ±ax^2 ± bx ± c (inclusive of spaces)")
      else:
            if ("-" not in eq[0]):
                  pol.insert(0, "+")
            else:
                  term_a = eq[0]
                  term_a = term_a.replace("-", "")
                  eq.insert(0, "-")
                  eq.insert(1, term_a)
                  eq.pop(2)

            if (f"{var}^2" in eq[3]):
                  print("\nPlease enter in the format of ±ax^2 ± bx ± c.")

            Coefficient(eq)

def Coefficient(eq):
      x_sq_term = eq[1]
      x_term = eq[3]
      if (var in x_sq_term):
            if (var in x_term):
                  a = x_sq_term.replace(f"{var}^2", "")
                  if (a.isdigit()):
                        if (eq[0] == "-"):
                              a = -int(a)
                        else:
                              a = int(a)
                  elif a == "":
                        a = -1 if eq[0] == "-" else 1
                  else:
                         a = -int(a) if eq[0] == "-" else int(a)
            
                  b = x_term.replace(f"{var}", "")
                  if b.isdigit():
                        b = -int(b) if eq[2] == "-" else int(b)
                  elif b == "":
                        b = 1
                  else:
                        b = -int(b) if eq[2] == "-" else b
      
                  if (var in x_term):
                        c = eq[5]
                        if c.isdigit():
                              c = -int(c) if eq[4] == "-" else int(c)
                        Formula(a, b, c)
            else:
                   print(f"\n{polynomial} is not quadratic in one variable. Please try again.")
      else:
             print(f"\nVariable '{var}' not found in {polynomial}. Please try again.")

def Formula(a, b, c):
      D = (b**2) - (4 * a * c)
      if (D < 0):
            print("\nThis polynomial does not have real roots.")
      else:
            r1 = (-(b) + (D**(1/2))) / (2 * a)
            r2 = (-(b) - (D**(1/2))) / (2 * a)

            r1 = int(r1) if r1.is_integer() else r1
            r2 = int(r2) if r2.is_integer() else r2
            Factorise(r1, r2)

def Factorise(var1, var2):
      r1 = var1
      r2 = var2
      if (r1 > 0):
            if (r2 > 0):
                  Factorised = f"({var} - {r1})({var} - {r2})"
            elif (r2 < 0):
                  r2 = abs(r2)
                  Factorised = f"({var} - {r1})({var} + {r2})"
      elif (r1 < 0):
            r1 = abs(r1)
            if (r2 > 0):
                  Factorised = f"({var} + {r1})({var} - {r2})"
            elif (r2 < 0):
                  r2 = abs(r2)
                  Factorised = f"({var} + {r1})({var} + {r2})"
      elif (r1 == 0):
            if (r2 > 0):
                  Factorised = f"({r1})({var} - {r2})"
            elif (r2 < 0):
                  r2 = abs(r2)
                  Factorised = f"({r1})({var} + {r2})"
            elif (r2 == 0):
                  Factorised = f"({r1})({r2})"
      print(f"\n{polynomial} = {Factorised}")
      print(f"Zeroes are {var1} and {var2}")

print("Quadratizer v1.0\nBuilt by ADITYA VN KADIYALA")
polynomial = input("\nEnter quadratic polynomial\n(Give in format ±ax^2 ± bx ± c (inclusive of spaces): ")
var = input("Enter variable: ")

pol = polynomial.split(" ")
ProofReading(pol)
