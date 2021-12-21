# Canister (class):  The main Canister class.
    Args:
        user_agent (str): User Agent to pass to the Canister API.
    
# search_package (function of Canister):  Search for a package.
        Args:
            query (str): Query to search for.
            search_fields (Optional[str]): Fields to search for. (defaults to 'name,author,maintainer,description')
            limit (Optional[str]): Response length limit. (defaults to 100)
        Returns:
            List of packages that Canister found matching the query.
        
# search_repo (function of Canister):  Search for a repo.
        Args:
            query (str): Query to search for.
        Returns:
            List of repos that Canister found matching the query.
        
# Package (class):  
    Canister package object.
    
# Repo (class):  
    Canister repo object.
    
