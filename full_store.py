# ba_meta require api 8
import bascenev1 as bs
import _baplus
import babase

# Backup the original purchase checking function
original_get_purchased = _baplus.get_purchased
original_get_tickets = babase.app.classic.accounts.get_ticket_count

# Override the get_purchased function
def get_purchased(item):
    # Allow access to all items
    return True

# Override the get_ticket_count function
def get_ticket_count():
    # Return an artificially inflated ticket count
    return 999999

# ba_meta export plugin
class Unlock(babase.Plugin):
    def on_app_running(self):
        # Enable pro account features
        babase.app.classic.accounts.have_pro = lambda: True
        
        # Override methods to unlock all items and boost ticket count
        _baplus.get_purchased = get_purchased
        babase.app.classic.accounts.get_ticket_count = get_ticket_count
      
