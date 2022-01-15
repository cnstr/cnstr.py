# Canister (class):  The main Canister class.
    Args:
        user_agent (str): User Agent to pass to the Canister API.
        session (Optional[ClientSession]): Optional session to use for requests.
    
# __canister_request (`asynchronous` function of Canister):  Make a request to the Canister API.
    Args:
        path (str): The Canister route to make a request to.
    Returns:
        dict[str, str]: The request's return value.
    
# __piracy_repos (`asynchronous` function of Canister):  Get all piracy repositories.
    Returns:
        list[str]: List of piracy repos.
    
# close (`synchronous` function of Canister):  Close the client.

    No client methods should be running.

    This is idempotent and irreversible.

    No other methods should be called after this one.
# is_closed (`synchronous` function of Canister):  Check if the client is closed.
# is_repo_safe (`asynchronous` function of Canister):  Find out if a repo is safe.
    Args:
        query (str): Repo URI.
    Returns:
        bool: Whether or not the repo is safe.
    
# search_package (`asynchronous` function of Canister):  Search for a package.
    Args:
        query (str): Query to search for.
        search_fields (Optional[PackageSearchFields]): Fields to search for.
        limit (Optional[str]): Response length limit. (defaults to 100)
    Returns:
        List[Package]: List of packages that Canister found matching the query.
    
# search_repo (`asynchronous` function of Canister):  Search for a repo.
    Args:
        query (str): Query to search for.
        search_fields (Optional[PackageSearchFields]): Fields to search for.
    Returns:
        List[Repo]: List of repos that Canister found matching the query.
    
# Package (class):  
    Canister package object.
    
# Repo (class):  
    Canister repo object.
    
# PackageSearchFields (class):  
    Fields to search for packages with.
    
# all_true (`synchronous` function of PackageSearchFields):  Sets all fields to true.
# set (`synchronous` function of PackageSearchFields):  Set a field value.
    Args:
        key (str): Key to set.
        value (bool): Value to set key to.
    Returns:
        SearchFields: Updated class object.
    
# RepositorySearchFields (class):  
    Fields to search for repositories with.
    
# all_true (`synchronous` function of RepositorySearchFields):  Sets all fields to true.
# set (`synchronous` function of RepositorySearchFields):  Set a field value.
    Args:
        key (str): Key to set.
        value (bool): Value to set key to.
    Returns:
        SearchFields: Updated class object.
    
