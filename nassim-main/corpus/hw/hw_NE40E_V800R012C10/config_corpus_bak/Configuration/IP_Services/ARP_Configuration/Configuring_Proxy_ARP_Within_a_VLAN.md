Configuring Proxy ARP Within a VLAN
===================================

Proxy ARP within a VLAN allows communication between devices in the same VLAN but configured with interface isolation.

#### Usage Scenario

If two users belong to the same VLAN but user isolation is configured in the VLAN, and communication is required between them, you can enable proxy ARP within the VLAN on the interfaces in the VLAN.


#### Pre-configuration Tasks

Before configuring proxy ARP within the VLAN, configure user isolation within a VLAN.


[Configuring an IP Addresses for an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp_cfg_2041.html)

The IP address assigned to an interface needs to be in the same network segment with the IP addresses of the users of all the VLANs associated to this interface. 

[(Optional) Associating the Sub-interface with a VLAN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp_cfg_2042.html)

Before you configure proxy ARP within a VLAN on Ethernet sub-interfaces, GE interfaces, or Eth-Trunk sub-interfaces, associate the sub-interface with a VLAN.

[Enabling Proxy ARP Within a VLAN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp_cfg_2043.html)

To enable communication between isolated devices within the same VLAN, proxy ARP within the VLAN is required.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp_cfg_2044.html)

After configuring proxy ARP within a VLAN, verify the configuration.