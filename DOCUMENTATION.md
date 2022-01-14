# Canister (class):  The main Canister class.
    Args:
        user_agent (str): User Agent to pass to the Canister API.
        session (Optional[ClientSession]): Optional session to use for requests.
    
# close (`synchronous` function of Canister):  Close and deallocate the current client.
# is_repo_piracy (`asynchronous` function of Canister):  Find out if a repo is piracy.
    Args:
        query (str): Repo URI.
    Returns:
        bool: Whether or not the repo is piracy.
    
# search_package (`asynchronous` function of Canister):  Search for a package.
    Args:
        query (str): Query to search for.
        search_fields (Optional[SearchFields]): Fields to search for. (defaults to 'name,author,maintainer,description')
        limit (Optional[str]): Response length limit. (defaults to 100)
    Returns:
        List[Package]: List of packages that Canister found matching the query.
    
# search_repo (`asynchronous` function of Canister):  Search for a repo.
    Args:
        query (str): Query to search for.
    Returns:
        List[Repo]: List of repos that Canister found matching the query.
    
# InvalidField (class):  Error thrown when an invalid field is passed to SearchFields.
# args (`synchronous` getset_descriptor of InvalidField):  None
# with_traceback (`synchronous` method_descriptor of InvalidField):  Exception.with_traceback(tb) --
    set self.__traceback__ to tb and return self.
# Package (class):  
    Canister package object.
    
# Repo (class):  
    Canister repo object.
    
# SearchFields (class):  
    Fields to search for packages with.
    
# set (`synchronous` function of SearchFields):  
    Set a field value.
    Args:
        key (str): Key to set.
        value (bool): Value to set key to.
    Returns:
        SearchFields: Updated class object.
    
