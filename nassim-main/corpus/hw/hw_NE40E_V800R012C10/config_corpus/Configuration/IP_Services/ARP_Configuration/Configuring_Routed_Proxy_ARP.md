Configuring Routed Proxy ARP
============================

Routed proxy ARP allows devices that have IP addresses on the same network segment but different physical networks to communicate with each other.

#### Usage Scenario

A large company network is usually divided into multiple subnets to facilitate management. The routing information of a host in a subnet can be modified so that IP datagrams sent from this host to another subnet are first sent to the gateway and then to another subnet. However, this solution makes it hard to manage and maintain devices. Deploying proxy ARP on the gateway effectively resolves management and maintenance problems caused by network division.


#### Pre-configuration Tasks

Before configuring routed proxy ARP, complete the following tasks:

* Configure physical parameters for interfaces to ensure that the physical status of the interfaces is Up.
* Configure link layer protocol parameters for interfaces to ensure that the link layer protocol status of the interfaces is Up.


[Configuring an IP Addresses for an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp_cfg_2037.html)

The IP address assigned to a routed proxy ARP-enabled interface must be on the same network segment with the IP address of the host on the LAN to which this interface connects. 

[Enabling Routed Proxy ARP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp_cfg_2038.html)

To allow subnets on the same IP network to communicate, enable routed proxy ARP.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp_cfg_2039.html)

After configuring routed proxy ARP, verify the configuration.