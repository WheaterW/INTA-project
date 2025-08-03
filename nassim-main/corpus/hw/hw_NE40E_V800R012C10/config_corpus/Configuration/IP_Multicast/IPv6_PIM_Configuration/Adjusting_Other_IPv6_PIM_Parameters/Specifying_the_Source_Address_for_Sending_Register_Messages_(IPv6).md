Specifying the Source Address for Sending Register Messages (IPv6)
==================================================================

Specify the source address for sending Register messages on all devices that may become source's Designated routers (DRs). In this manner, registration errors will not occur due to repeated IP addresses on the network or filtered IPv6 addresses.

#### Context

Generally, the source IPv6 address for sending Register messages is the IPv6 address of the interface connecting the source's DR to the multicast source. An error occurs if the source IPv6 address for sending Register messages is not unique for the RP on the network or has been filtered out. To solve the problem, specify a proper IPv6 global unicast address as the source address for sending Register messages (IPv6).

Perform the following steps on the IPv6 PIM-SM-enabled Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pim-ipv6**](cmdqueryname=pim-ipv6)
   
   
   
   The IPv6 PIM view is displayed.
3. Run [**register-source**](cmdqueryname=register-source) *ipv6-address*
   
   
   
   The source IPv6 address for sending Register messages from the source's DR is specified.
   
   
   
   You are advised to specify the IPv6 address of the loopback interface as the source IPv6 address for sending Register messages from the source's DR.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.