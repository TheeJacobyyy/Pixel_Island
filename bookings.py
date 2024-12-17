import json
from datetime import datetime   

BOOKING_FILE = "bookings.json"

listings = [
    {'id': 1, 'name': 'Tropical Island', 'description': 'Serene tropical retreat.', 'price': 500, 'image': '8BitRetreatOne.jpg'},
    {'id': 2, 'name': 'Winter Island', 'description': 'A winter wonderland island.', 'price': 750, 'image': 'WinterIsland.jpg'},
    {'id': 3, 'name': 'Lava Island', 'description': 'A warm exotic island with a marvelous volcano.', 'price': 1000, 'image': 'LavaIsland.jpg'},
]

def load_bookings():
    try:
        with open(BOOKING_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_bookings(bookings):
    with open(BOOKING_FILE, "w") as file:
        json.dump(bookings, file, indent=4)

def display_listings():
    print("\nAvailable Listings:")
    for listings in listings:
        print(f"ID: {listings['id']}, Name: {listings['name']}, Price: $:{listings['price']}")
    print()

def make_booking():
    display_listings()
    try:
        listing_id = int(input("Enter the ID of the listings you want tp book: "))
        selected_listing = next((l for l in listings if l["id"] == listing_id), None)
        if not selected_listing:
            print("Invalid listing ID. Please try again.")
            return
        
        name = input("Enter your name: ")
        email = input("Please enter your email: ")
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Please enter the end date (YYYY-MM-DD): ")

        try:
            start_date_obj = datetime.strptime(start_date, "%Y-%m-%d")
            end_date_obj = datetime.strptime(end_date, "%Y-%m-%d")
            if start_date_obj >= end_date_obj:
                print("Error: Start date must be before end date.")
                return
        except ValueError:
            print("Error: Invalid date format. Please use YYYY-MM-DD.")
            return
        
        bookings = load_bookings()
        new_booking = {
            "listing_id": listing_id,
            "listing_name": selected_listing["name"],
            "name": name,
            "email": email,
            "start_date": start_date,
            "end_date": end_date
        }
        bookings.append(new_booking)
        save_bookings(bookings)

        print(f"Booking confirmed for '{selected_listing['name']}' from {start_date} to {end_date}.\n")
    except ValueError:
        print("Invalid input. Please try again.")
        
def view_bookings():
    bookings = load_bookings()
    if not bookings:
        print("\nNo bookings available.\n")
        return
    
    print("\nAll Bookings")
    for i, booking in enumerate(bookings, start=1):
        print(f"{i}. Listing: {booking['listing_name']}, Name: {booking['name']}, "
              f"Email: {booking['email']}, Dates: {booking['start_date']} to {booking['end_date']}")
    print()

def main():
    while True:
        print("=== Booking System ===")
        print("1. View Listings")
        print("2. Make a Booking")
        print("3. View All Bookings")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")
        if choice == "1":
            display_listings()
        elif choice == "2":
            make_booking()
        elif choice == "3":
            view_bookings()
        elif choice == "4":
            print("Exiting the booking system.")
            break
        else:
            print("Invalid choice. Please enter 1-4.\n")

if __name__ == "__main__":
    main()