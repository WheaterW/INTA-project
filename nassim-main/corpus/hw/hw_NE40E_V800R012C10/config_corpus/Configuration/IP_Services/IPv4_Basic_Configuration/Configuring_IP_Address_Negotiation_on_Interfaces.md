Configuring IP Address Negotiation on Interfaces
================================================

PPP access users can use PPP address negotiation to apply to a server for IP addresses.

#### Usage Scenario

![](../../../../public_sys-resources/note_3.0-en-us.png) 

This section does not apply to the NE40E-M2K-B.

If devices are connected through PPP links, client interfaces can obtain IP addresses from the server through negotiation. This is applicable when the client accesses the Internet by connecting to the Internet Service Provider (ISP) through PPP links (for example by dial-up). In this case, the ISP device assigns an IP address to the client through negotiation.

As shown in [Figure 1](#EN-US_TASK_0172364891__fig_dc_vrp_ipv4_cfg_000701), after the interfaces that directly connect DeviceA on the server side to DeviceB on the client side are encapsulated with PPP, the client can obtain an IP address from the server through negotiation.

**Figure 1** Configuring IP address negotiation on an interface![](../../../../public_sys-resources/note_3.0-en-us.png) 

interface1 in this example represents GE 0/1/0.


  
![](figure/en-us_image_0000001576462385.png)

When configuring IP address negotiation on interfaces, note the following points:

* IP address negotiation can be configured only on PPP-encapsulated interfaces. If the PPP status is Down, the IP address generated during negotiation is deleted.
* After IP address negotiation is configured for an interface, you do not need to configure any IP address for the interface. If the interface already has an IP address, the original IP address is deleted.
* After an interface obtains an IP address through negotiation, you cannot configure secondary IP addresses for this interface.
* If you configure IP address negotiation for an interface that already has this function enabled, the originally generated IP address is deleted, and the interface obtains a new IP address through negotiation.
* After the IP address generated through negotiation for the interface is deleted, the interface becomes an addressless interface.

#### Pre-configuration Tasks

Before configuring IP address negotiation on interfaces, complete the following tasks:

* Configure IP addresses for server interfaces to ensure that the link layer protocol status of the interfaces is Up.
* Configure physical parameters and the link layer protocol PPP for interfaces on client interfaces.


[Configuring a Server to Assign an IP Address to a Client Through Negotiation](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv4_cfg_0008.html)

After an IP address is specified on a server, the server can assign this IP address to a client.

[Configuring a Client to Obtain an IP Address Through Negotiation](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv4_cfg_0009.html)

After interface IP address negotiation is enabled on a client, the client can obtain an IP address from the server.

[Verifying the Configuration of IP Address Negotiation](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv4_cfg_0010.html)

After configuring IP address negotiation, verify the configuration.