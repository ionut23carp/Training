import re


ping_output = """PING google.com (172.217.18.78): 56 data bytes
64 bytes from 172.217.18.78: icmp_seq=0 ttl=55 time=51.868 ms
64 bytes from 172.217.18.78: icmp_seq=1 ttl=55 time=28.568 ms
64 bytes from 172.217.18.78: icmp_seq=2 ttl=55 time=27.779 ms
64 bytes from 172.217.18.78: icmp_seq=3 ttl=55 time=29.447 ms
^C
--- google.com ping statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 27.779/34.416/51.868/10.093 ms
"""


matches = re.finditer(r'\d+(\.\d{1,2}%)?(?= packet)', ping_output)
print([match.group() for match in matches])

matches = re.findall(r'(?<=ttl=)\d+', ping_output)
ttl_values = [int(m) for m in matches]
print('Min TTL:', min(ttl_values))
print('Max TTL:', max(ttl_values))


hidden_ips = re.sub(r'(\d{1,3}\.){3}\d{1,3}', '[x.x.x.x]', ping_output)
print(hidden_ips)
