# int -> value/value
def extNum1_calc(num: int) -> str:
    if num >= 100000000:
        return "ERROR"
    
    num_str = str(num).zfill(8)
    
    life = int(num_str[4:])
    total = int(num_str[:4])
    
    return f"{life}/{total}"

# value/value -> int
def extNum1_restore(ratio: str) -> int:
    try:
        life_str, total_str = ratio.split("/")
    except ValueError:
        raise ValueError(f"ERROR: must be 'int/int', but got: {ratio!r}")

    life = int(life_str)
    total = int(total_str)

    if life >= 10000 or total >= 10000:
        return "ERROR"

    total_z = str(total).zfill(4)
    life_z = str(life).zfill(4)
    combined = total_z + life_z

    return int(combined)

# usage
print(extNum1_calc(9990999))
print(extNum1_restore("9/999"))