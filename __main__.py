from flight import Flight
from planes import AirbusA380, Boeing737Max
from helpers import card_printer


def main():
    airbus = AirbusA380()
    boeing = Boeing737Max()
    f = Flight('LO127', boeing)
    f.allocate_passenger(passenger="Edward E", seat="12C")
    f.allocate_passenger(passenger="Alfons E", seat="12B")
    f.allocate_passenger(passenger="Jacek A", seat="12A")
    f.relocate_passenger("12A", "18G")
    f.print_tickets(card_printer)


if __name__ == '__main__':
    main()
