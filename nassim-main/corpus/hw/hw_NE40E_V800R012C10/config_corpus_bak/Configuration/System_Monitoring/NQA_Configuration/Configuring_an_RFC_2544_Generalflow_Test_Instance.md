Configuring an RFC 2544 Generalflow Test Instance
=================================================

This section describes how to configure a generalflow test instance to monitor the performance of interconnected network devices.

#### Context

An NQA generalflow test is a standard traffic testing method for evaluating network performance and is in compliance with RFC 2544. This test can be used in various networking scenarios that have different packet formats. It is a standard method for evaluating network performance implemented based on UDP.

Before a network service cutover, an NQA generalflow test helps customers evaluate whether network performance meets pre-designed performance requirements. An NQA generalflow test has the following advantages:

* Enables a device to send simulated service packets to itself before services are deployed on the device.
  
  Existing methods, unlike generalflow tests, can only be used when services have been deployed on networks. If no services are deployed, testers must be used to send and receive test packets.
* Uses standard methods and procedures that comply with RFC 2544, facilitating network performance comparison between different vendors.

A generalflow test measures the following performance indicators:

* Throughput: maximum rate at which packets are sent without loss.
* Packet loss rate: percentage of discarded packets among all sent packets.
* Delay: difference between the time when a device sends a packet and the time when the packet is looped back to the device. The delay includes the period during which a forwarding device processes the packet.

A generalflow test can be used in the following scenarios:

* Layer 2: native Ethernet, EVPN, and L2VPN scenarios
  
  On the network shown in [Figure 1](#EN-US_TASK_0172373103__fig_dc_vrp_nqa_cfg_004601), an initiator and a reflector perform a generalflow test to measure the performance of end-to-end services between two user-to-network interfaces (UNIs).
  
  **Figure 1** Generalflow test in a Layer 2 scenario  
  ![](figure/en-us_image_0000001497131973.png)
* Layer 3: native IP and L3VPN scenarios
  
  Layer 3 networking is similar to Layer 2 networking.
* L2VPN accessing L3VPN: VLL accessing L3VPN scenario
  
  **Figure 2** Generalflow test in an L2VPN accessing L3VPN scenario  
  ![](figure/en-us_image_0000001497372061.png)  
  
  In the L2VPN accessing L3VPN networking shown in [Figure 2](#EN-US_TASK_0172373103__fig_dc_vrp_nqa_cfg_004603), the initiator and reflector can reside in different locations to represent different scenarios.
  + If the initiator and reflector reside in locations 1 and 5 (or 5 and 1), respectively, or the initiator and reflector reside in locations 4 and 6 (or 6 and 4), respectively, it is a native Ethernet scenario.
  + If the initiator and reflector reside in locations 2 and 3 (or 3 and 2), respectively, it is a native IP scenario.
  + If the initiator resides in location 3 and the reflector in location 1, or the initiator resides in location 2 and the reflector in location 4, it is similar to an IP gateway scenario, and the simulated IP address must be configured on the L2VPN device.
  + If the initiator and reflector reside in locations 1 and 2 (or 2 and 1), respectively, or the initiator and reflector reside in locations 3 and 4 (or 4 and 3), respectively, it is an IP gateway scenario.
  + If the initiator resides in location 1 and the reflector in location 4, the initiator resides in location 1 and the reflector in location 3, or the initiator resides in location 4 and the reflector in location 2, it is an L2VPN accessing L3VPN scenario. In this scenario, the destination IP and MAC addresses and the source IP address must be specified on the initiator, and the destination IP address for receiving test flows must be specified on the reflector. If the initiator resides on the L2VPN, the simulated IP address must be specified as the source IP address.
* IP gateway scenario:
  
  On the network shown in [Figure 3](#EN-US_TASK_0172373103__fig_dc_vrp_nqa_cfg_004602), user CE side's Layer 3 services are transmitted to the IP gateway through a Layer 2 network.
  
  **Figure 3** Generalflow test in Layer 2 access to Layer 3 networking  
  ![](figure/en-us_image_0000001447292016.png)

#### Pre-configuration Tasks

Before configuring an NQA generalflow test, complete the following tasks:

* Layer 2:
  + In a native Ethernet scenario, configure reachable Layer 2 links between the initiator and reflector.
  + In an L2VPN scenario, configure reachable links between CEs on both ends of an L2VPN connection.
  + In an EVPN scenario, configure reachable links between CEs on both ends of an EVPN connection.
* Layer 3:
  + In a native IP scenario, configure reachable IP links between the initiator and reflector.
  + In an L3VPN scenario, configure reachable links between CEs on both ends of an L3VPN connection.
* L2VPN accessing L3VPN scenario: configure reachable links between the L2VPN and L3VPN.
* IP gateway scenario: configure reachable Layer 2 links between an IP gateway and the reflector.


[Configuring a Reflector](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0047.html)

This section describes how to configure a reflector, which loops traffic to an initiator. You can set reflector parameters based on each scenario.

[Configuring an Initiator](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0048.html)

This section describes how to configure an initiator that sends simulated service traffic. You can set initiator parameters based on usage scenarios and test indicator types.

[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_nqa_cfg_0049.html)

After configuring the generalflow test, you can view the generalflow test results.