Verifying the Configuration
===========================

After configuring the rate limit for Address Resolution Protocol (ARP) packets to be sent to the CPU, you can verify the configuration.

#### Procedure

* Run the [**display arp-safeguard statistics**](cmdqueryname=display+arp-safeguard+statistics) **slot** *slot-id* command to check ARP bidirectional isolation statistics about a specified interface board.
* Run the [**display arp rate-limit interface**](cmdqueryname=display+arp+rate-limit+interface) *interface-type* *interface-number* command to check the ARP packet rate limit configured for a specified interface.
* Run the [**display arp attack**](cmdqueryname=display+arp+attack) **interface** { **interface-type** *interface-num* | *interface-name* } [ **vlan-id** *vlan-number* | **pe-vid** *pe-vid* **ce-vid** *ce-vid* ] [ **history** ] command to check information about ARP attacks on a specified interface.
* Run the [**display arp attack**](cmdqueryname=display+arp+attack) **slot** { *slot-id* | **all** } [ **history** ] command to check information about ARP attacks on a specified interface board.