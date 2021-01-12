"""Print out all the melons in our inventory."""


from melons import melon_dict

def print_melon(dictionary):
    """Print each melon with corresponding attribute information."""

    for melon, melon_info in dictionary.items():
        melon = melon.upper()
        print(f'{melon}') 

        for key, value in melon_info.items():
            print(f'\t {key}: {value}')

print_melon(melon_dict)