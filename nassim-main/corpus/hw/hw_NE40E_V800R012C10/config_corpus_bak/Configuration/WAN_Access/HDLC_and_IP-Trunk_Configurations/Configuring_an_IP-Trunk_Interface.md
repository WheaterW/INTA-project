Configuring an IP-Trunk Interface
=================================

IP-Trunk interfaces are a type of trunk interface. You
can configure an IP-Trunk interface to implement link backup and traffic
load balancing.

#### Usage Scenario

To improve communication
capabilities of links, you can bundle multiple POS interfaces to form
an IP-Trunk interface. An IP-Trunk interface obtains the sum of bandwidths
of member interfaces. You can add POS interfaces to an IP-Trunk interface
to increase the bandwidth of the interface.

To prevent traffic
congestion, traffic to the same destination can be balanced among
member links of the IP-Trunk interface, not along a single path.

You can configure an IP-Trunk interface to improve link reliability.
If an IP-Trunk member interface goes Down, the IP-Trunk interface
can use other member interfaces in the Up state to transmit data.


#### Pre-configuration Tasks

Before configuring
an IP-Trunk interface, power on the device and verify that it is working
properly.


[Creating an IP-Trunk Interface and Adding Interfaces to the IP-Trunk Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_hdlc_ip-trunk_cfg_0009.html)

You can create an IP-Trunk interface and add interfaces to the IP-Trunk interface.

[Assigning an IP Address to an IP-Trunk Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_hdlc_ip-trunk_cfg_0010.html)

You can assign an IP address to an IP-Trunk interface.

[(Optional) Configuring the Lower Threshold of Up Links](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_hdlc_ip-trunk_cfg_0011.html)

The lower threshold of Up links is the minimum number of member interfaces in the Up state. When the number of member interfaces in the Up state falls below the configured lower threshold, an IP-Trunk interface goes Down. When the number of member interfaces in the Up state reaches the configured lower threshold, the IP-Trunk interface goes Up.

[(Optional) Setting the Lower Limit for an IP-Trunk Interface's Bandwidth](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_hdlc_ip-trunk_cfg_0024.html)

This section describes how to set the lower limit for an IP-Trunk interface's bandwidth. An IP-Trunk interface goes Down when the sum of all Up member interfaces' bandwidth is lower than the lower limit. An IP-Trunk interface goes Up when the sum of all Up member interfaces' bandwidth reaches the lower limit.

[(Optional) Configuring the Load Balancing Mode for an IP-Trunk Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_hdlc_ip-trunk_cfg_0012.html)

You can configure the load balancing mode for an IP-Trunk interface.

[(Optional) Configuring the Weight for a Member Link](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_hdlc_ip-trunk_cfg_0013.html)

An IP-Trunk interface performs load balancing on member links based on link weights. On an IP-Trunk interface, the greater the weight of a member link, the heavier the load over the member link. Therefore, to enable a member link to transmit more traffic, increase the weight for the link.

[(Optional) Configuring the Method of Sending Trap Messages from an IP-Trunk Member Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_hdlc_ip-trunk_cfg_0025.html)

You can configure an IP-Trunk member interface to send trap messages through a private MIB.

[Verifying the IP-Trunk Interface Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_hdlc_ip-trunk_cfg_0014.html)

After configuring the IP-Trunk interface, you can view the status and forwarding table of the IP-Trunk interface and information about member interfaces.