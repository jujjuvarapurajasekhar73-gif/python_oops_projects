# =====================================================================
# 1. ABSTRACT BASE RESERVATION INTERFACE (WITH SEAT ALLOCATION LOCKS)
# =====================================================================
from abc import ABC, abstractmethod

class flightbooking(ABC):
    def __init__(self, passenger_name: str, base_fare: float) -> None:
        """
        Initializes the abstract base flight booking with passenger details
        and hidden private attributes for seat security.
        """
        self.passenger_name = passenger_name
        self.base_fare = base_fare
        
        # Strict private attributes to secure sensitive seating allocation data
        self.__seat_number: str = "Not Assigned"
        self.__seat_type: str = "Standard"

    def book_seat(self, seat_number: str, seat_type: str) -> None:
        """
        Validates the seat choice, assigns the seat number, 
        and dynamically updates the fare structure for premium window seats.
        """
        self.__seat_number = seat_number
        
        # Business Rule: Window seats incur an exclusive premium luxury surcharge
        if seat_type == "Window":
            self.__seat_type = "Window"
            self.base_fare += 500.0
        elif seat_type == "Aisle":
            self.__seat_type = "Aisle"
        else:
            self.__seat_type = "Standard"

    @abstractmethod
    def calculate_total_fare(self) -> float:
        """
        Abstract contract forcing subclasses to implement localized fare calculations.
        """
        pass

    def __str__(self) -> str:
        """
        Magic Method: Generates a professional digital boarding pass ticket layout dynamically.
        """
        return f"""
        ====================================================
                    SKYLINE AIRWAYS BOARDING PASS           
        ====================================================
        PASSENGER    : {self.passenger_name}
        ASSIGNED SEAT: {self.__seat_number} ({self.__seat_type})
        BASE FARE    : ${self.base_fare}
        FINAL COST   : ${self.calculate_total_fare()}
        STATUS       : CONFIRMED & PROTECTED
        ====================================================
        """


# =====================================================================
# 2. SUBCLASS IMPLEMENTATION: DOMESTIC FLIGHT RULES (5% GST TAX)
# =====================================================================

class domesticbooking(flightbooking):
    def __init__(self, passenger_name: str, base_fare: float) -> None:
        """
        Initializes a domestic flight booking using the base template.
        """
        super().__init__(passenger_name, base_fare)

    def calculate_total_fare(self) -> float:
        """
        Calculates total fare by adding a fixed 5% GST tax to the base fare.
        """
        gst_tax = self.base_fare * 0.05
        return self.base_fare + gst_tax


# =====================================================================
# 3. SUBCLASS IMPLEMENTATION: INTERNATIONAL FLIGHT W/ PASSPORT LOCKS
# =====================================================================

class internationalbooking(flightbooking):
    def __init__(self, passenger_name: str, base_fare: float, passport_number: str) -> None:
        """
        Initializes an international flight booking with a private passport attribute.
        """
        super().__init__(passenger_name, base_fare)
        # Encapsulating highly sensitive passport data using strict private names
        self.__passport_number = passport_number

    def calculate_total_fare(self) -> float:
        """
        Calculates total fare by verifying passport data integrity and adding flat travel tax.
        """
        if self.__passport_number == "":
            raise ValueError("International flights require a valid passport number.")
            
        international_travel_tax = 2000.0
        return self.base_fare + international_travel_tax


# =====================================================================
# 4. POLYMORPHIC RUNTIME FLIGHT ENGINE ROUTER
# =====================================================================

def run_flight_booking_system(booking_object: flightbooking) -> None:
    """
    Demonstrates Abstraction, Magic Methods, and Polymorphism by executing 
    and printing any flight type boarding pass dynamically.
    """
    # Because of the __str__ magic method, printing the object displays our boarding ticket directly!
    print(booking_object)


# =====================================================================
# 5. AUTOMATED INTEGRATION TESTING SUITE (WITH LIVE SEAT ALLOCATIONS)
# =====================================================================

def run_automated_tests() -> None:
    """
    Executes automated test cases to verify domestic, international, 
    private attributes, and dynamic seat booking rules.
    """
    print("--- 1. Processing Domestic Booking with Premium Window Seat ---")
    # Raja buys a $5000 base ticket, but chooses a premium Window Seat (adds $500) + 5% GST
    domestic_ticket = domesticbooking("Raja", 5000.0)
    domestic_ticket.book_seat("12A", "Window")
    run_flight_booking_system(domestic_ticket)

    print("\n--- 2. Processing International Booking with Standard Aisle Seat ---")
    # Surya buys a $15000 base ticket, chooses an Aisle Seat (no extra cost) + $2000 International tax
    international_ticket = internationalbooking("Surya", 15000.0, "IND998877")
    international_ticket.book_seat("04C", "Aisle")
    run_flight_booking_system(international_ticket)

    print("\n--- 3. Processing International Passport Validation Edge Case ---")
    try:
        # Venkat attempts to book without providing a passport number (triggers guard clause)
        invalid_international = internationalbooking("Venkat", 12000.0, "")
        invalid_international.book_seat("22D", "Standard")
        run_flight_booking_system(invalid_international)
    except ValueError as error:
        print(f"Captured Expected Booking Error: {error}")


# =====================================================================
# 6. SYSTEM RUNTIME ENTRY POINT
# =====================================================================

if __name__ == "__main__":
    run_automated_tests()
