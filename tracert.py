import socket
import subprocess
import re
import os
from typing import List
from urllib.parse import urlparse
from urlmixin import UrlMixin
from routemixin import RouteMixin


class Tracert(UrlMixin,RouteMixin):

    def __init__(self,url):
        self.url = url
        self._data = None

    def __repr__(self):
        return f"Tracert({self.url})"

    def traceroute(self, outfile: str=''):
        self._data = str(self._traceroute())
        if outfile:
            with open(outfile,'w') as file:
                for c in self._data:
                    file.write(c)
        return self._data if not outfile else None

    def parse_ms(self) -> List[int]:
        """returns a list of 3-packet measurements for all of traceroute"""
        if not self._data:
            raise ValueError("Traceroute must be performed first. try Tracert.traceroute")

        milliseconds = re.findall(r"(\d+[^ms])",
                                  ''.join(re.findall(r"(\d+\sms)+",self._data))
                                  )
        return [int(ms) for ms in milliseconds if ms]

    def avg_round_trip(self) -> float:
        """returns average roundtrip for all of traceroute"""
        last = self.parse_ms()[-3:]
        return sum(last)/len(last)

    @classmethod
    def whois(cls, url: str, outfile=None):
        """looks up url on whois and returns message from server"""

        
        domain = UrlMixin.get_domain(url)
        ext = UrlMixin.get_ext(url)
        whois_url = 'whois.internic.net'

        if UrlMixin.is_country(ext):
            ext = ext.split('.')[-1]
            whois_url = 'whois.iana.org'

        msg = RouteMixin.query_server(whois_url,domain,port=43)
        str_msg = msg.decode()
        remove_idx = str_msg.index("URL of the ICANN Whois Inaccuracy")
        str_msg = str_msg[:remove_idx].strip()
        

        if outfile:
            if os.path.exists(outfile):
                with open(outfile,'a') as file:
                    file.write('\n\n')
                    file.write(str_msg)
            else:
                with open(outfile,'w') as file:
                    file.write(str_msg)
        else:
            return str_msg


    
        

        

        

        
        
        

    

    
    
        
                 
                 
