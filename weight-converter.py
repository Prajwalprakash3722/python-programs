is_weight = input("Enter your weight: ")
is_type = input("(K)gs  (L)bs  (O)unce: ")
if is_type == 'l' and 'L':
    weight = float(is_weight) * 0.45
    weightOO: float = float(weight) *35.274
    print(f" {weight}  kgs")
    print(f" {weightOO}  Ounces (approx)")
elif is_type == 'k' and 'K':
    weight = float(is_weight) / 0.45
    print(f"{weight} lbs")
elif is_type == 'o' and 'O':
    weight = float(is_weight) / 35.274
    weightlbs = float(weight) * 0.45
    print(f"{weight} Kgs")
    print(f"{weightlbs} lbs")

else:
    print("enter only in (L)bs or (K)gs or (O)unces")
