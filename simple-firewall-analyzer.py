firewall_logs = []
banned_ips = []
def analyze_packet(log_list, ban_list, ip_address, port):
    if port == 22 or port == 8080:
        dle = f"BLOCKED: IP {ip_address} targeted critical port {port}"
        log_list.append(dle)
        ban_list.append(ip_address)
        return "DANGER"
    else :
       dle = f"INFO: IP {ip_address} checked port {port}"
       log_list.append(dle)
       return "OK"
status1 = analyze_packet(firewall_logs, banned_ips, "192.168.1.10", 80)
print(f"{status1}")
status2 = analyze_packet(firewall_logs, banned_ips, "10.0.0.5", 22)
print(f"{status2}")
status3 = analyze_packet(firewall_logs, banned_ips, "172.16.0.4", 8080)
print(f"{status3}")
print("Your firewall logs")
for lol1 in firewall_logs:
    print("-", lol1)
print("-"*30)
print("Your banned ips")
for lol2 in banned_ips:
    print("-", lol2)

       
    