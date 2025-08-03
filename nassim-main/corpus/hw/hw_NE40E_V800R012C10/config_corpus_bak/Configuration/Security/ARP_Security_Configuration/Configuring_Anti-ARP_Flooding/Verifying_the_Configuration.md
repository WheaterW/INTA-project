Verifying the Configuration
===========================

This section describes how to verify the configuration of anti-ARP flooding.

#### Prerequisites

All anti-ARP flooding functions have been configured.


#### Procedure

* Run the [**display arp learning strict**](cmdqueryname=display+arp+learning+strict) command to check the configuration of strict ARP learning.
* Run the [**display arp-limit**](cmdqueryname=display+arp-limit) [ **interface** { *interface-name* | *interface-type interface-number* } ] command to check the configuration of ARP entry limiting.
* Run the [**display arp speed-limit**](cmdqueryname=display+arp+speed-limit) { **destination-ip** | **source-ip** } [ **slot** *slot-id* ] command to check the configuration of ARP packet rate limiting.
* Run the [**display arp-miss speed-limit**](cmdqueryname=display+arp-miss+speed-limit) **source-ip** [ **slot** *slot-id* ] command to check the configuration of rate limiting on ARP Miss messages.
* Run the [**display arp-safeguard statistics**](cmdqueryname=display+arp-safeguard+statistics) **slot** *slot-id* command to check ARP bidirectional isolation statistics about a specified interface board.
* Run the [**display arp rate-limit interface**](cmdqueryname=display+arp+rate-limit+interface) *interface-type* *interface-number* command to check the ARP packet rate limit configured for a specified interface.
* Run the [**display arp attack**](cmdqueryname=display+arp+attack) **interface** *interface-type* *interface-number* command to check information about ARP attacks on a specified interface.
* Run the [**display arp attack**](cmdqueryname=display+arp+attack) **slot** { *slot-id* | **all** } [ **history** ] command to check information about ARP attacks on a specified interface board.
* Run the [**display arp anti-attack record**](cmdqueryname=display+arp+anti-attack+record) command to check detailed information about ARP packets discarded because the rate of ARP packets exceeds the limit.
* Run the [**display arp miss anti-attack record**](cmdqueryname=display+arp+miss+anti-attack+record) command to check detailed information about ARP Miss messages discarded because the rate of ARP Miss messages exceeds the limit.