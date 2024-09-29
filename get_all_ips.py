import socket

def get_ip_addresses(domain):
    """
    Get all IP addresses of the given domain name.

    Args:
        domain (str): The domain name to resolve.

    Returns:
        list: A list of IP addresses or an error message.
    """
    try:
        # Get all IP addresses associated with the domain name
        host_info = socket.gethostbyname_ex(domain)
        return host_info[2]  # The third element contains the list of IP addresses
    except socket.gaierror:
        return [f"Error: Unable to resolve the domain '{domain}'."]

# Example usage
if __name__ == "__main__":
    domain_name = input("Enter the domain name: ")  # e.g., 'example.com'
    ip_addresses = get_ip_addresses(domain_name)
    
    if isinstance(ip_addresses, list):
        print(f"The IP addresses of '{domain_name}' are: {', '.join(ip_addresses)}")
    else:
        print(ip_addresses)
