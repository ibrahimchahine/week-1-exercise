def f_c(f):
    c = float(f - 32) * 5 / 9
    return c


def c_f(c):
    f = float(c * 9 / 5) + 32
    return f


def mile_to_kilometer(mile):
    return float(mile * 1.60934)


def kilometer_to_mile(kilometer):
    return float(kilometer / 1.60934)


def kg_to_stone(kilo):
    return float(kilo / 0.157)


def kg_to_pounds(kilo):
    return float(kilo / 2.20462)


def stone_to_kg(stone):
    return float(stone * 6.35029)


def stone_to_pounds(stone):
    return float(stone * 14)


def pounds_to_kg(pounds):
    return float(pounds * 2.20462)


def pounds_to_stone(pounds):
    return float(pounds / 14)


def convert(source_type, dest_type, source_val):
    """
    This method converts a value from a source type to a dest type.
    source_type:
    dest_type:
    source_val:
    """
    match source_type:
        case "F":
            return f_c(source_val)
        case "C":
            return c_f(source_val)
        case "MPH":
            return mile_to_kilometer(source_val)
        case "KPH":
            return kilometer_to_mile(source_val)
        case "kg":
            if dest_type == "stone":
                return kg_to_stone(source_val)
            elif dest_type == "lbs":
                return kg_to_pounds(source_val)
        case "stone":
            if dest_type == "kg":
                return stone_to_kg(source_val)
            elif dest_type == "lbs":
                return stone_to_pounds(source_val)
        case "lbs":
            if dest_type == "kg":
                return pounds_to_kg(source_val)
            elif dest_type == "stone":
                return pounds_to_stone(source_val)
    return 0


def get_data():
    print(
        "Options: \n1. Temperature fahrenheit <-> celsius. Example: Write F>C for converting F to C\n"
    )
    print("2. Speed MPH <-> KPH. Example: Write MPH>KPH for converting MPH to KPH\n")
    print(
        "3. Weight kg <-> stone <-> lbs. Example: Write kg>stone for converting kg to stone for example. \n"
    )

    conversion_type = input("Enter the type of conversion Type1>Type2: ")

    check_type = True if ">" in conversion_type else False
    if check_type:
        # https://stackoverflow.com/questions/27260811/python-find-position-of-element-in-array
        index = conversion_type.index(">")
        source_type = conversion_type[:index]
        dest_type = conversion_type[index + 1 :]
        source_val = float(input("Enter the source value: "))
    return source_type, dest_type, source_val


source_type, dest_type, source_val = get_data()
res = convert(source_type, dest_type, source_val)
print(res)
