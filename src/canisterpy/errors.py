'''Defines all error types for canister.py.'''
# errors.py

class RequestError(Exception):
    '''Error thrown when something goes wrong with a Canister API request.'''
    pass

class InitializationError(Exception):
    '''Error thrown when something goes wrong with the initialization of the Canister class.'''
    pass

class InvalidField(Exception):
    '''Error thrown when an invalid field is passed to SearchFields.'''
    pass