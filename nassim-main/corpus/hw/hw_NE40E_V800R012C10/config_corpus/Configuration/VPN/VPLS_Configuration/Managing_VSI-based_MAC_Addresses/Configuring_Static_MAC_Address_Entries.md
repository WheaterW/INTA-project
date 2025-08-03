Configuring Static MAC Address Entries
======================================

This section describes how to configure static MAC address entries, including static blackhole MAC address entries. After a static MAC address entry is configured, the packets with a specified destination MAC address are forwarded through the specified interface. This protects the device against attacks with forged MAC addresses. After a blackhole MAC address entry is configured, the packets with a specified destination MAC address are discarded. This process prevents hackers from launching network attacks based on MAC addresses.

#### Context

If a network has fixed users or an important server connects to a device on the network, configure static MAC address entries on the device to prevent hackers from attacking the device or server.

To prevent invalid MAC address entries, such as those of unauthorized users, from occupying a MAC address table and prevent hackers from attacking user devices or networks using MAC addresses, configure the MAC addresses of untrusted users as blackhole MAC addresses to discard packets destined for such MAC addresses.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mac-address**](cmdqueryname=mac-address) **static** *mac-address* *interface-type* *interface-number* **vsi** *vsi-name* [ **pe-vid** *pe-vid* [ **ce-vid** *ce-vid* ] ]
   
   
   
   A VSI-based static MAC address entry is added.
3. Run [**mac-address blackhole**](cmdqueryname=mac-address+blackhole) *mac-address* { **vlan** *vlan-id* | **vsi** *vsi-name* }
   
   
   
   A static blackhole MAC address entry is added.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.