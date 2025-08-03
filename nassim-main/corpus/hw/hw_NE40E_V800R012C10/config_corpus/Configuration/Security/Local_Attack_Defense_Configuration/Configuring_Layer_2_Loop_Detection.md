Configuring Layer 2 Loop Detection
==================================

This section describes how to configure Layer 2 loop detection.

#### Usage Scenario

Networks are prone to loops, and loops may occur due to various reasons, such as incorrect link connection and loop prevention protocol failure on an attacked or overloaded ring network. When a Layer 2 loop occurs on an interface, the interface will receive a large number of broadcast and multicast packets, such as Address Resolution Protocol (ARP) packets and Open Shortest Path First (OSPF) packets.

To minimize service loss caused by Layer 2 loops, configure actions in response to an existing or potential Layer 2 loop. This function allows protocols to work normally and prevents major network faults.

The CPU determines whether to enable or disable Layer 2 loop detection based on packet loss caused by the committed access rate (CAR). After Layer 2 loop detection is enabled, the CPU will take the configured responsive action after detecting an existing or a potential loop on an interface.

In VS mode, this feature is supported only by the admin VS.


#### Pre-configuration Tasks

None


[Configuring Actions In Response to Layer 2 Loops](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2loopDetect_cfg_0002.html)

The CPU determines whether to enable or disable Layer 2 loop detection based on packet loss caused by the committed access rate (CAR). After Layer 2 loop detection is enabled, the CPU will take the configured actions in response to Layer 2 loops after the system detects an existing or a potential loop on an interface.

[(Optional) Disabling Layer 2 Loop Detection](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2loopDetect_cfg_0003.html)

If you confirm that Layer 2 loops do not occur on a board, you can disable the Layer 2 loop detection function to improve the fault locating efficiency.

[(Optional) Configuring the Layer 2 Loop Detection Threshold](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2loopDetect_cfg_0005.html)

If the Layer 2 loop detection threshold is not properly set, Layer 2 loop detection may be unexpectedly enabled or display incorrect loop levels, affecting Layer 2 loop detection results. As a result, some services may be affected.

[Verifying the Layer 2 Loop Detection Configuration](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_l2loopDetect_cfg_0004.html)

Check information about Layer 2 loop detection on a specified board and information about packets that cause Layer 2 loops on a specified board.