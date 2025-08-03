Configuring Basic OSPFv3 Functions
==================================

To construct an OSPFv3 network, configure basic OSPFv3 functions first.

#### Usage Scenario

OSPFv3 functions take effect only after an OSPFv3 process, the router ID, the interface, and the area ID are specified.

OSPFv3 functions can be configured in the interface view, regardless of whether OSPFv3 is enabled. If OSPFv3 is disabled from the interface, OSPFv3 functions configured on this interface are still valid.


#### Pre-configuration Tasks

Before configuring basic OSPFv3 functions, complete the following tasks:

* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* Enable IPv6.


[Enabling OSPFv3](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2004.html)

Creating an OSPFv3 process is a prerequisite for configuring OSPFv3 features. When creating an OSPFv3 process, you need to manually specify a router ID for it.

[Creating an OSPFv3 Area](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2006.html)

After an AS is divided into different areas and OSPFv3 interfaces and areas to which these interfaces belong are specified, OSPFv3 can discover and calculate routes in the AS.

[Enabling OSPFv3 on an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2005.html)

For an interface with multiple instances, you need to specify which instance on the interface is enabled in the OSPFv3 process when enabling OSPFv3 on the interface.

[(Optional) Configuring the Router to Comply with Route Selection Rules Defined in a Standard Protocol](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2101.html)

You can configure the Router to comply with the route selection rule defined in RFC 1583 or RFC 5340.

[(Optional) Configuring an Alarm Threshold for the Number of LSAs Learned by OSPFv3](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_3002.html)

You can configure an alarm threshold for the number of LSAs learned by OSPFv3 so that an alarm is reported when this threshold is reached or exceeded.

[(Optional) Configuring the Maximum Number of Packet Retransmission Attempts](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2098.html)

When no response to DD packets, Update packets, or Request packets is received, the retransmission mechanism is used and the maximum number of packet retransmission attempts is set to prevent dead loops caused by repeated transmissions.

[(Optional) Disabling an Interface from Receiving and Sending OSPFv3 Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2085.html)

Disabling an interface from receiving and sending OSPFv3 packets prevents other network devices from obtaining OSPFv3 routing information and prevents the local device from receiving routing updates advertised by other network devices.

[Verifying the Basic OSPFv3 Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ospfv3_cfg_2007.html)

After configuring basic OSPFv3 functions, verify information about neighbors, interfaces, and the OSPFv3 routing table.