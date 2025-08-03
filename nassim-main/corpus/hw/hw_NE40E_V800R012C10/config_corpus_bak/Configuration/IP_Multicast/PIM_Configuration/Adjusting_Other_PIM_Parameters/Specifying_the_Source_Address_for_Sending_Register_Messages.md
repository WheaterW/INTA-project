Specifying the Source Address for Sending Register Messages
===========================================================

Specify the source address for sending Register messages on all devices that may become source's Designated routers (DRs). In this manner, registration errors will not occur due to repeated IP addresses on the network or filtered IP addresses.

#### Context

Generally, the source address for sending Register messages is the IP address of the interface connecting the source's DR to the multicast source. An error occurs if the source address for sending Register messages is not unique for the Rendezvous Point (RP) on the network or has been filtered out. To solve the problem, specify a proper interface IP address as the source address for sending Register messages.

Perform the following steps on the PIM-SM-enabled Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**pim**](cmdqueryname=pim) [ **vpn-instance** *vpn-instance-name* ]
   
   
   
   The PIM view is displayed.
3. Run [**register-source**](cmdqueryname=register-source) *interface-type* *interface-number*
   
   
   
   The source address for sending Register messages from the source's DR is specified.
   
   You are advised to specify the IP address of the loopback interface as the source address for sending Register messages from the source's DR.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.