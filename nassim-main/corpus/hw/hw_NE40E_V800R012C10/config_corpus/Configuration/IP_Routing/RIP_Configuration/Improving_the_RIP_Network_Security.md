Improving the RIP Network Security
==================================

On a network requiring high security, you can configure RIP authentication and Generalized TTL Security Mechanism (GTSM) to improve network security.

#### Usage Scenario

With the increase in attacks on TCP/IP networks and the defects in the TCP/IP protocol suite, network attacks have increasing impacts on the network security. Attacks on network devices may even cause a network crash or lead to network unavailability. Therefore, it is necessary to protect the network from attacks. RIP uses the following methods to ensure network security:

* RIP authentication: RIP checks the authentication mode and password in each packet to protect the local device against potential attacks.
* Check on the source IP address of each packet: RIP interfaces accept packets only from the same network to protect the local device from potential attacks from other networks.
* RIP GTSM: GTSM protects the local router by checking whether the time to live (TTL) value in the IP packet header is in a pre-defined range.


#### Pre-configuration Tasks

Before improving RIP network security, complete the following tasks:

* Configure network layer addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configuring Basic RIP Functions](dc_vrp_rip_cfg_0003.html)

#### Configuration Procedure

Perform one or more of the following configuration tasks (excluding verifying the configuration) as required.


[Configuring an Authentication Mode for RIP-2 Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0040.html)

RIP-2 supports authentication for protocol packets. You are advised to configure authentication to ensure system security.

[Configuring the Check on the Source Addresses in RIP Packets on the Broadcast Network](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0041.html)

By default, a RIP interface checks the source address in each received packet and accepts only those from the same network.

[Configuring GTSM for RIP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0059.html)

Generalized TTL Security Mechanism (GTSM) defends against attacks by checking the TTL value. 

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_rip_cfg_0042.html)

After the security function of RIP is successfully configured, you can view information about RIP interfaces and the current running status of RIP.