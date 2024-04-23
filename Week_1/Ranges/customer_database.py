def process_customer(customer):
    """
    Process a single customer record.

    Args:
        customer (dict): Dictionary containing customer information.

    Returns:
        None
    """
    # Example processing logic
    print(f"Processing customer {customer['name']} with ID {customer['id']}")
    # Add your processing logic here, such as updating a database, sending emails, etc.

# Example usage:
customer_database = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
]

for customer in customer_database:
    process_customer(customer)
