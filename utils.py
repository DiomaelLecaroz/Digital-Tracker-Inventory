import os

# CSV File Paths
USER_CSV = "users.csv"
INVENTORY_CSV = "inventory.csv"
TRANSACTION_CSV = "transactions.csv"

def init_files():
    """Initialize required CSV files if they do not exist."""
    for f in [USER_CSV, INVENTORY_CSV, TRANSACTION_CSV]:
        if not os.path.exists(f):
            open(f, 'w').close()
