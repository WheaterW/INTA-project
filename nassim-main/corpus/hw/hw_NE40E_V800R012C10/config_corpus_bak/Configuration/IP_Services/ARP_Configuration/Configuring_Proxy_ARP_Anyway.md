Configuring Proxy ARP Anyway
============================

This section describes how to deploy proxy ARP anyway when the gateways to which VMs are connected have the same IP address.

#### Usage Scenario

In scenarios where servers are partitioned into VMs, to allow flexible deployment and migration of VMs on multiple servers or switches, the common solution is to configure Layer 2 interconnection between multiple switches. However, this approach may lead to larger Layer 2 domains on the network and the risk of broadcast storms. To resolve this problem, the common method is to configure a VM gateway on an access switch and enable proxy ARP anyway on the gateway so that the gateway sends its own MAC address to a source VM and communication between VMs is implemented through route forwarding.


#### Pre-configuration Tasks

Before configuring proxy ARP anyway, complete the following tasks:

* Connect interfaces and set their physical parameters to ensure that the physical status of the interfaces is Up.
* Configure link layer protocol parameters for the interfaces to ensure that the link layer protocol status of the interfaces is Up.


[Configuring an IP Address for an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp_cfg_3091.html)

This section describes how to configure an IP address for a device so that the device can communicate with other devices on the network.

[Enabling Proxy ARP Anyway](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp_cfg_3092.html)

This section describes how to enable proxy ARP anyway on a gateway to interconnect different subnets of an IP network when the gateways connected to VMs have the same IP address.

[Checking the Configurations](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp_cfg_3093.html)

This section describes how to check the configurations of proxy ARP anyway.