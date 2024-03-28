from artwork import Artwork
from exhibition import Exhibition
from visitor import Visitor
from ticket import Ticket
from event import Event
from payment import Payment

# Test Case: Addition of New Art to the Museum
new_artwork = Artwork("Starry Night", "Vincent van Gogh", 1889, "Iconic painting",  "Permanent Gallery")
print(new_artwork.get_info())

# Test Case: Opening of a New Exhibition
new_exhibition = Exhibition("Main Gallery", "June 2024 - August 2024")
print(new_exhibition.get_details())

# Test Case: Purchase of Tickets by an Individual
visitor_individual = Visitor("John Doe", 30, "789012")
individual_ticket = Ticket(63, "Adult")
visitor_individual.purchase_ticket(individual_ticket)

# Test Case: Purchase of Tickets by a Tour Group
tour_group = Visitor("Tour Group", 20, "345678")
group_ticket = Ticket(500, "Group")
tour_group.purchase_ticket(group_ticket)

# Test Case: Display Payment Receipts
payment_individual = Payment(63, 5)  # Total amount with VAT
payment_individual.process_payment()
print(f"Payment Receipt for Individual: Total Amount - {payment_individual.total_amount} AED (including VAT)")

payment_group = Payment(500, 5)  # Total amount with VAT
payment_group.process_payment()
print(f"Payment Receipt for Tour Group: Total Amount - {payment_group.total_amount} AED (including VAT)")

# Test Case: Opening of a New Event
new_event = Event("Musical Concert", "Outdoor Amphitheater", "July 2024")
print(new_event.get_event_info())