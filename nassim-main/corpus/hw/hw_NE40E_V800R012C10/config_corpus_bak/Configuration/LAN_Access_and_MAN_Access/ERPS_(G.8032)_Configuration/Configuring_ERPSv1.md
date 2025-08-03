Configuring ERPSv1
==================

ERPS eliminates loops on an Ethernet ring network when no faulty links exist and promptly restores communication if a link fault occurs. ERPSv1 supports only single rings.

#### Usage Scenario

Generally, redundant links are used to access an upper-layer network to provide link backup and enhance network reliability. The use of redundant links, however, may produce loops, causing broadcast storms and rendering the MAC address table unstable. As a result, the communication quality deteriorates, and communication services may even be interrupted. To resolve these problems, ERPS can be used for loop avoidance purposes. ERPS blocks redundant links under normal conditions and unblocks them to promptly restore communication if a link fault occurs. ERPSv1 and ERPSv2 are currently available. As ERPSv2 is fully compatible with ERPSv1, configuring ERPSv2 is recommended if all devices on an ERPS ring support both ERPSv1 and ERPSv2. If any devices on an ERPS ring support only ERPSv1, configure ERPSv1 on all devices on the ring.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

ERPS and other ring network protocols, such as Spanning Tree Protocol (STP) and Smart Link, cannot run on the same port.



#### Pre-configuration Tasks

Before configuring ERPSv1, complete the following tasks:

* Establish a ring network.
* Connect interfaces and set their physical parameters to ensure that the physical status of the interfaces is Up.


[Configuring an ERPS Ring](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_erps_cfg_0005.html)

A ring is the basic ERPS unit. After an ERPS ring is configured, ERPS runs to block redundant links and eliminate loops on Layer 2 networks.

[(Optional) Configuring Association Between ERPS and Ethernet CFM](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_erps_cfg_0007.html)

Association between Ethernet CFM and ERPS on an ERPS ring port helps promptly detect failures, converge topologies, and shorten the traffic interruption time. Currently, ERPS can be associated only with outward-facing MEPs.

[(Optional) Configuring the TC Notification Function on an ERPS-enabled Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_erps_cfg_0023.html)

When an ERPS-enabled interface has sub-interfaces bound to a BD or VPLS, to allow the interface to immediately instruct these sub-interfaces to update their ARP and MAC address entries after the interface receives topology change (TC) packets, configure the TC change notification function on the interface.

[(Optional) Configuring ERPS Self-Healing](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_erps_cfg_0029.html)



[Verifying the ERPSv1 Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_erps_cfg_0008.html)

After configuring ERPSv1, verify the configuration of ports added to an ERPS ring, port roles, control VLAN ID, ERP instances, WTR timer, and guard timer.