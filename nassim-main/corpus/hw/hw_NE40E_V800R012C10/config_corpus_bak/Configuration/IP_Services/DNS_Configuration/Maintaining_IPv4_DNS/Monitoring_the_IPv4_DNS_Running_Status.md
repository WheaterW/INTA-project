Monitoring the IPv4 DNS Running Status
======================================

This section describes how to monitor the DNS running status.

#### Context

In routine maintenance, you can run the following commands in all views to check the running status of DNS.


#### Procedure

* Run the [**display ip host**](cmdqueryname=display+ip+host+vpn-instance) [ **vpn-instance** *vpn-name* ] command to check information about the static domain name resolution table.
* Run the [**display dns server(IPv4)**](cmdqueryname=display+dns+server%28IPv4%29+vpn-instance) [ **vpn-instance** *vpn-name* ] command to check DNS server configurations.
* Run the [**display dns domain(IPv4)**](cmdqueryname=display+dns+domain%28IPv4%29+vpn-instance) [ **vpn-instance** *vpn-name* ] command to check domain name suffixes.
* Run the [**display dns dynamic-host**](cmdqueryname=display+dns+dynamic-host+vpn-instance) [ **vpn-instance** *vpn-name* ] command to check information about dynamic DNS entries in the cache.