############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller,
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name



        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    muskmelon = MelonType('musk', '1998', 'green', 'Seedless', 'Bestseller', 'Muskmelon')
    muskmelon.add_pairing('mint')

    casaba_melon = MelonType('cas', '2003', 'orange', 'Seeded', None, 'Casaba')
    casaba_melon.add_pairing('strawberry')
    casaba_melon.add_pairing('mint')

    crenshaw_melon = MelonType('cren', "1996", 'green', 'Seeded', None, 'Crenshaw')
    crenshaw_melon.add_pairing('proscuitto')

    yellow_wm = MelonType('yw', '2013', 'yellow', "Seeded", 'Bestseller', "Yellow Watermelon")
    yellow_wm.add_pairing('ice cream')


    all_melon_types = []
    all_melon_types.append(muskmelon)
    all_melon_types.append(casaba_melon)
    all_melon_types.append(crenshaw_melon)
    all_melon_types.append(yellow_wm)

    # Fill in the rest

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for indx in range(len(melon_types)):

        melon_name = melon_types[indx].name
        pairings = "\n-".join(melon_types[indx].pairings)
        print "{} pairs with - \n{}".format(melon_name, pairings)
        print

        #print melon_types[indx].name + " pairs with" + " -" + '\n' .join(melon_types[indx].pairings)




def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest

melons = make_melon_types()
print_pairing_info(melons)


