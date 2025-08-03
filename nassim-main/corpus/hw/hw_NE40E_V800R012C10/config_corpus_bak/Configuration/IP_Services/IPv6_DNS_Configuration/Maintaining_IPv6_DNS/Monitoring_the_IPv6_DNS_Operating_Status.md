Monitoring the IPv6 DNS Operating Status
========================================

This section describes how to monitor the IPv6 DNS operating status.

#### Context

In routine maintenance, run the following commands in any view to check the IPv6 DNS operating status.


#### Procedure

* Run the [**display ipv6 host**](cmdqueryname=display+ipv6+host+vpn-instance) [ **vpn-instance** *vpn-name* ] command to check static DNS entries.
* Run the [**display dns server**](cmdqueryname=display+dns+server+vpn-instance) [ **vpn-instance** *vpn-name* ] command to check DNS server configurations.
* Run the [**display dns domain**](cmdqueryname=display+dns+domain+vpn-instance) [ **vpn-instance** *vpn-name* ] command to check domain name suffixes.
* Run the [**display dns ipv6 dynamic-host**](cmdqueryname=display+dns+ipv6+dynamic-host+vpn-instance) [ **vpn-instance** *vpn-name* ] command to check dynamic IPv6 DNS entries in the domain name cache.