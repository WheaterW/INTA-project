Configuring Loop Detection on the VPLS Access Side
==================================================

To ensure that broadcast storms do not occur on a VPLS network, you can configure loop detection on the AC interfaces of PEs.

#### Usage Scenario

If a CE accesses a VPLS network over redundant ACs, or if redundant PWs exist on a VPLS network, a loop may form and potentially cause broadcast storms. To prevent this from occurring, configure Ethernet loop detection on the network. Then, when a loop occurs, the affected AC or PW will be blocked to prevent broadcast storms.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

A router with loop detection enabled periodically sends specially constructed loop detection packets. These packets will be looped back to the router if a loop exists on a network, enabling the router to determine that a loop has occurred. By sending loopback detection packets obtained using Sniffer to the router, a malicious attacker can trick it into believing that a loop has occurred. It is therefore recommended that you disable this function on devices that are operating normally. If it is used to detect link connectivity during the site deployment stage, disable it after this stage is complete.



#### Pre-configuration Tasks

Before configuring Ethernet loop detection on a VPLS network, complete the following task:

Deploy VPLS on the network so that CEs can communicate.


[Enabling Loop Detection Globally](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_loop-detect_cfg_5006.html)

Before loop detection is enabled on an interface, loop detection must be enabled in the system view.

[Configuring Loop Detection](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_loop-detect_cfg_5007.html)

Loop detection and blocking priorities can be configured in the interface view.

[(Optional) Configuring a VLAN Range for Loop Detection Packets Sent by a VLAN Tag Termination Sub-interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_loop-detect_cfg_5008.html)

Specifying the VLAN range for the loop detection packets sent by dot1q or QinQ VLAN tag termination sub-interfaces helps prevent PEs from sending detection packets with the VLAN IDs of all ranges, thereby avoiding unnecessary CPU consumption.

[Checking the Configurations](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_loop-detect_cfg_5009.html)

After configuring successfully, you can check information about the loop detect status and loop detect blocking of each interface.