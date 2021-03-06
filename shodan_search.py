import shodan


def shodan_query(shodan_api_key, ip):

    try:
        api = shodan.Shodan(shodan_api_key)

        # Lookup the host
        host = api.host(ip)

        # Print general info
        print("""[+] Shodan Result: 
        IP: %s
        Organization: %s
        Operating System: %s
        """) % (host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a'))

        # Print all banners
        for item in host['data']:
            print """   
            Port: %s    
            Banner: %s
            """ % (item['port'], item['data'])

        return host

    except shodan.exception.APIError:
        host = "No information"

        return host