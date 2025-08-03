Configuring LDP Multi-Instance
==============================

You need to configure LDP multi-instance when deploying BGP/MPLS IP VPN.

#### Usage Scenario

LDP multi-instance is mainly used in MPLS L3VPN scenarios of carrier networks. To configure LDP multi-instance on a BGP/MPLS IP VPN network, bind LDP to a created VPN instance. Disabled


#### Pre-configuration Tasks

Before configuring LDP multi-instance, complete the following tasks:

* Enable MPLS.
* Enable MPLS LDP.
* Configure an IP VPN instance.


[Enabling LDP Multi-Instance](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0107.html)

This section describes how to configure LDP multi-instance. Before you configure LDP multi-instance, enable LDP for the specified VPN instance on each node.

[(Optional) Enabling the Function to Trigger Trap Messages Only for Public Network LDP Sessions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_2047.html)

In an LDP multi-instance scenario, a device can be enabled to trigger trap messages only for public network LDP sessions, which prevents a failure to distinguish trap messages for both the private and public network sessions with the same ID.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ldp-p2p_cfg_0108.html)

After the LDP multi-instance is configured, verify information about LDP of the specified VPN instance.