Verifying the Configuration
===========================

This section describes how to verify the configuration of anti-ARP spoofing.

#### Prerequisites

All anti-ARP spoofing functions have been configured.


#### Procedure

* Run the [**display arp packet statistics**](cmdqueryname=display+arp+packet+statistics) command to check statistics about ARP packets sent and received by the device.
* Run the **display arp-check** { **check-destination-ip** | **check-valid** } **statistics** **slot** *slot-id* command to check statistics about invalid ARP packets discarded by a specified interface board.