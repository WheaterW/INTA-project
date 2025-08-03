DHCPv4 Client Reusing an IPv4 Address
=====================================

A non-newly connected DHCPv4 client can reuse an IPv4 address that has been allocated to it. As shown in [Figure 1](#EN-US_CONCEPT_0000001563886113__fig014112710512), the DHCPv4 client exchanges DHCPv4 messages with the DHCPv4 server to re-obtain network parameters such as the previously used IPv4 address. This process is performed through two steps.

![](public_sys-resources/note_3.0-en-us.png) 

Not all clients can reuse IPv4 addresses that have been allocated to them. The following figure uses a PC as the DHCPv4 client to describe how the client reuses an IPv4 address.


**Figure 1** Message exchange for IPv4 address reuse between a DHCPv4 client and server  
![](figure/en-us_image_0000001563886149.png)
#### Step 1: Request Stage

The DHCPv4 client broadcasts a DHCPREQUEST message carrying the IPv4 address that the client has used. The requested IPv4 address is added in Option 50.


#### Step 2: Acknowledgement Stage

After receiving the DHCPREQUEST message, the DHCPv4 server checks whether there is a lease record based on the MAC address in the message. If there is a lease record matching the MAC address, the DHCPv4 server replies with a DHCPACK message to notify the DHCPv4 client that the requested IPv4 address can be used. Otherwise, the DHCPv4 server performs no operation and waits for a new DHCPDISCOVER message from the client.