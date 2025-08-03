Enabling Intra-VLAN Proxy ARP
=============================

This section describes how to configure proxy ARP for isolated interfaces in a VLAN to communicate.

#### Context

Perform the following steps on the device on which the isolated interfaces that require communication reside:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **vlanif** *vlan-id*
   
   
   
   A VLANIF interface is created.
3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } [ **sub** ]
   
   
   
   An IP address is assigned to the VLANIF interface.
   
   
   
   The IP address of the VLANIF interface must be on the same network segment as the IP addresses of interfaces in the VLAN.
   
   The IP addresses of different VLANIF interfaces must be on different network segments so that users in different VLANs can communicate with each other.
4. Run [**arp-proxy**](cmdqueryname=arp-proxy) **inner-sub-vlan-proxy** **enable**
   
   
   
   Intra-VLAN proxy ARP is enabled.