Configuring the CAR
===================

This section describes how to configure the CAR.

#### Usage Scenario

When a large number of users
access the Router, a lot of packets need be sent to the CPU for processing. In such
a case, the Router is prone to be attacked. To protect the Router from being attacked, you need to configure the CAR on the Router.

In VS mode, this feature is supported only
by the admin VS.


#### Pre-configuration Tasks

Before configuring
the CAR, connect interfaces and set the physical parameters of the
interfaces and ensure that their physical layer status is Up.


[Creating an Attack Defense Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0005b.html)

All local attack defense features must be added to an attack defense policy. These features take effect after the attack defense policy is applied to the interface board.

[Configuring a Whitelist](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0019.html)

This section describes how to configure a whitelist. Secure packets that match ACL rules can be added to the whitelist and then provided with higher bandwidth.

[Configuring a Blacklist](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0020.html)

This section describes how to configure a blacklist. Insecure packets that match ACL rules can be added to the blacklist and then provided with lower bandwidth.

[Configuring a User-Defined Flow](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0021.html)

This section describes how to configure a user-defined flow and add the specified traffic to the flow based on ACL rules. In this way, traffic policing can be performed on the packets as required.

[Configuring the Packet Matching Order](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0022.html)

After the packets to be sent to the CPU pass the GTSM check, set the matching sequence of packets: TCPSYN packets, packet fragments, dynamic link protection, whitelist, blacklist, and user-defined flow.

[Configuring the CAR](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0023.html)

This section describes how to configure the CAR. Traffic policing prevents packets to be sent to the CPU from causing higher CPU usage to affect normal services.

[Configuring the Packet Sending Priority](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0024.html)

This section describes how to prioritize packets to be sent to the CPU. Sending higher-priority packets preferentially can protect the CPU when the queues are full of packets to be sent to the CPU.

[Setting Bandwidth Values and Weights for the Protocol Group Whose Packets Are to Be Sent to the CPU](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0048.html)

You can specify the CIR, and weight for a protocol group of packets to be sent to the CPU according to the actual networking requirements. With the configuration, if the queues of packets to be sent to the CPU are full, the packets of the specified protocol group can be processed by the CPU in time.

[Applying the Attack Defense Policy](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0009b.html)

The configured attack defense policy takes effect only after being applied to the interface board.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_sysattack_cfg_0026.html)

After configuring CAR, run the corresponding **display** command to check statistics about packets discarded by CAR.