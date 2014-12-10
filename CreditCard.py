class CreditCard:
    """ Implementation of a credit card class. """
    
    def __init__(self, customer, bank, account, limit):
        """ create a new credit card instance. the initial balance is zero.
        
        """
        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0
        
    def get_customer(self):
        """ Return the name of the customer. """
        return self._customer
        
    def get_bank(self):
        """ Return bank's name """
        return self._bank
        
    def get_account(self):
        """ Return the card ID number"""
        return self._account
    
    def get_limit(self):
        """ Return current credit limit. """
        return self._limit
    
    def get_balance(self):
        """ Return current balance. """
        return self._balance
    
    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
            Return True if charge was processed; False if charge was denied.
        """
        '''try:
            type(price) == int or type(price) == float
        except ValueError:       
            print 'Not a number!'
        
        if type(price) != int or type(price) != float:
            raise ValueError("Not a number!")
        '''
        if price < 0:
            return False
        elif price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True
    
    def make_payment(self, payment):
        """Process customer payment that reduces balance."""
        self._balance -= payment
        
          
        