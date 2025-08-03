Verifying the Configuration
===========================

After configuring routed proxy ARP, verify the configuration.

#### Prerequisites

Routed proxy ARP has been configured.


#### Procedure

* Run the [**display arp interface**](cmdqueryname=display+arp+interface) *interface-name* command to check the ARP mapping table on a specified interface.
* Run the [**display arp slot**](cmdqueryname=display+arp+slot) *slot-id* command to check the ARP mapping table on the board in a specified slot.
* Run the [**display arp vpn-instance**](cmdqueryname=display+arp+vpn-instance) *vpn-instance-name* **slot** *slot-id* [ **dynamic** | **static** ] command to check the ARP mapping table of a specified VPN instance.