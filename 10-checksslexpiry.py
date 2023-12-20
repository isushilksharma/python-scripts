#Check SSL Certificate Expiry:

import ssl
import datetime
from urllib import request

def check_ssl_certificate_expiry(url):
    context = ssl.create_default_context()
    with request.urlopen(url, context=context) as response:
        cert = response.info()['server_certificate']
        cert_expiry_date = ssl.cert_time_to_seconds(cert['notAfter'])
        current_date = datetime.datetime.utcnow().timestamp()
        days_until_expiry = (cert_expiry_date - current_date) / (24 * 3600)
        return days_until_expiry

# Example usage:
url_to_check = 'https://example.com'
days_until_expiry = check_ssl_certificate_expiry(url_to_check)
print(f"SSL Certificate for {url_to_check} will expire in {days_until_expiry} days.")
