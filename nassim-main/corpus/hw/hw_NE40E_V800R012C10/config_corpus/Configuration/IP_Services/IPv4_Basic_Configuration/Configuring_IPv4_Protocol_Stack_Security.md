Configuring IPv4 Protocol Stack Security
========================================

By controlling ICMP packets and IP packets carrying route options, you can effectively defend against attacks by sending these packets on the network.

#### Usage Scenario

The route options in an IP packet can be used to diagnose link faults and temporarily transmit special services. Network attackers may use packets carrying route options to probe the network structure and launch attacks. Therefore, by configuring whether to process IP packets carrying route options, you can effectively defend against attacks by sending these packets.

Network attackers perform scanning by using various types of packets, and devices reply to these packets with ICMP packets. Network attackers then obtain network information from these received ICMP packets and launch attacks on the network. In addition, the devices are busy sending ICMP packets, affecting transmission of normal service packets. By controlling the sending and receiving of ICMP packets, you can effectively defend against attacks by sending these packets.


#### Pre-configuration Tasks

Before configuring IPv4 protocol stack security, configure link layer protocol parameters for the interfaces to ensure that the link layer protocol status of the interfaces is Up.


[Controlling the Processing of IP Packets Carrying Route Options](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv4_cfg_0016.html)

By disabling devices from processing IP packets carrying route options, you can effectively defend networks against attacks by sending these packets.

[Controlling ICMP Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv4_cfg_0034.html)

By controlling the sending and receiving of ICMP packets, you can effectively defend against attacks by sending these packets.

[Setting the Timeout Period for the Reassembly Queue](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv4_cfg_0018.html)

To improve the router performance and prevent against network attacks, configure a proper reassembly timeout period so that reassembly queues that have waited for all fragments to be reassembled for a long period can be aged in time.

[Configuring IP Source Address Check](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv4_cfg_0044.html)

This section describes how to configure IP source address check to prevent routers from network attacks.

[Verifying the Configuration of IPv4 Protocol Stack Security](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ipv4_cfg_0019.html)

After configuring IPv4 protocol stack security, verify the configuration.