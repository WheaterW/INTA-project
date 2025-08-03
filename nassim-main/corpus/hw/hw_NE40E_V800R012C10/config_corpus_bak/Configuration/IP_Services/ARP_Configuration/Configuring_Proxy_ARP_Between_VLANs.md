Configuring Proxy ARP Between VLANs
===================================

Proxy ARP between VLANs allows communication between devices in different VLANs.

#### Usage Scenario

If two hosts belong to different VLANs and communication is required between them, proxy ARP between VLANs must be enabled on interfaces associated with the VLANs.


#### Pre-configuration Tasks

Before configuring proxy ARP between VLANs, complete the following task:

* Configure VLAN aggregation.


[Configuring an IP Addresses for an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp_cfg_2046.html)

The IP address assigned to an interface needs to be in the same network segment with the IP addresses of the users of all the VLANs associated to this interface. 

[(Optional) Associating the Sub-interface with a VLAN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp_cfg_2047.html)

Before you configure proxy ARP between VLANs on Ethernet sub-interfaces, GE interfaces, or Eth-Trunk sub-interfaces, associate the sub-interface with a VLAN.

[Enabling Proxy ARP Between VLANs](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp_cfg_2048.html)

To enable communication between devices in different VLANs, proxy ARP between VLANs is required.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_arp_cfg_2049.html)

After configuring proxy ARP between VLANs, verify the configuration.