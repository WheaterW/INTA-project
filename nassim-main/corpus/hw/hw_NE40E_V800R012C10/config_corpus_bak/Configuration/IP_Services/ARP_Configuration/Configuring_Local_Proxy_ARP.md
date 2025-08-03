Configuring Local Proxy ARP
===========================

To enable users who are isolated in the same bridge domain (BD) to communicate with each other, configure local proxy ARP.

#### Usage Scenario

In an EVC model, a BD is a broadcast domain, and member interfaces in a BD broadcast the packets they receive. To minimize broadcast traffic, split horizon can be configured on member interfaces that do not need to communicate with each other. After split horizon is enabled on member interfaces in a BD, users who are served by these interfaces are isolated. However, as services become more diverse and keep increasing, users have growing needs for intra-BD communication. To meet the service requirements, local proxy ARP can be configured on a VBDIF interface for member interfaces in a BD. (A VBDIF interface is a virtual interface.)


#### Pre-configuration Tasks

Before configuring local proxy ARP, complete the following tasks:

* Isolate users who are in the same BD.
* Create a VBDIF interface.


[Assigning an IP address to a VBDIF Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp_cfg_2070.html)

The IP address assigned for a VBDIF interface that performs local proxy ARP for a bridge domain (BD) must be in the same network segment as the IP addresses of the member interfaces in the BD.

[Enabling Local Proxy ARP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp_cfg_2071.html)

To allow isolated devices in a BD to communicate, enable the local proxy ARP function.