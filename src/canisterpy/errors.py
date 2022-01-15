'''Defines all error types for canister.py.'''
# errors.py

class ClosedError(Exception):
    '''Error thrown when a client is trying to be used after it is closed..'''
    pass

class InitializationError(Exception):
    '''Error thrown when something goes wrong with the initialization of the Canister class.'''
    pass

class InvalidFieldError(Exception):
    '''Error thrown when an invalid field is passed to SearchFields.'''
    pass

class RequestError(Exception):
    '''Error thrown when something goes wrong with a Canister API request.'''
    pass