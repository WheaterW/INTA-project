Understanding Layer 2 Proxy ARP
===============================

Understanding Layer 2 Proxy ARP

#### Application Scenarios

**VLAN-based Layer 2 proxy ARP**

ARP request messages are broadcast messages. After receiving an ARP request message, a switching device broadcasts the message in its broadcast domain (BD). If a switching device receives a large number of ARP request messages within a period of time and broadcasts the messages, a large amount of network resources are consumed, causing network congestion. As a result, network performance deteriorates and user services are affected. Layer 2 proxy ARP can relieve the pressure on processing ARP messages by isolating ARP BDs. With this function enabled, a device preferentially uses learned ARP snooping entries to respond to received ARP request messages. After receiving an ARP request message, the device with Layer 2 proxy ARP enabled checks whether the user information in the request message matches an ARP snooping binding entry. If a matching entry exists, the device sends an ARP reply message. If no matching entry exists, the device broadcasts the ARP request message.

**BD-based Layer 2 proxy ARP**

In [Figure 1](#EN-US_CONCEPT_0000001176743489__fig_dc_vrp_arp_feature_000101), BD-based Layer 2 proxy ARP is enabled on a Layer 2 device. After receiving an ARP message on an interface connected to a host, the device listens to the message for ARP source information and records information such as the source IP address, source MAC address, inbound interface in local ARP snooping entries for Layer 2 proxy ARP. In addition, you can enable EVPN to collect host information based on BDs on Layer 2 devices. After the configuration is complete, the Layer 2 devices use EVPN routes (that is, MAC/IP routes) to synchronize learned user ARP information from one another and add the information to their local ARP snooping entries. The information contains the source IP and MAC addresses.

After receiving another ARP request message, a Layer 2 device searches its local ARP snooping entries (including the locally listened ones and those synchronized from other Layer 2 devices) for an entry that matches the message's destination IP address.

* If the matching entry exists, the device directly sends an ARP reply message based on the entry.
* If no matching entry exits, the device broadcasts the ARP request message.

**Figure 1** Network diagram of BD-based Layer 2 proxy ARP  
![](figure/en-us_image_0000001130783850.png)