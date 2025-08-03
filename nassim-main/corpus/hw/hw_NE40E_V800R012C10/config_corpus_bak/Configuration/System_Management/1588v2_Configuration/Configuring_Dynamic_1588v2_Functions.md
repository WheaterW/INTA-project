Configuring Dynamic 1588v2 Functions
====================================

On a 1588v2 network, the best master clock algorithm (BMCA) is typically used to dynamically determine a master clock. 1588v2 functions need to be configured according to the device type.

#### Usage Scenario

A 1588v2 network has to import BITS time signals before implementing time synchronization. The BMCA algorithm can be used to select the grandmaster and determine the master and slave clocks. A dynamic 1588v2 network allows devices to elect a time source with the highest priority.

On the network shown in [Figure 1](#EN-US_TASK_0000001825841177__fig1646519193816), time synchronization is required between gNodeBs, and core nodes are connected to BITSs. Starting from the core nodes, all nodes on the transport network start hop-by-hop time synchronization using 1588v2, achieving time synchronization on the entire network. The entire synchronization process is implemented through PTP packet exchange. All nodes are organized based on the master/slave relationship (determined using the BMCA).

**Figure 1** Typical 1588v2 scenario  
![](figure/en-us_image_0000002078258746.png)

To prevent 1588v2 tracing loops, you need to plan hierarchical isolation for the ring network before deployment. On devices that are interconnected at different layers in the network topology, including metro core devices BC1 and BC2 that are directly connected to BITSs, edge nodes BC3 and BC4 between the metro core layer and backbone aggregation layer, edge nodes BC7, BC8, BC9, and BC10 between the common aggregation layer and access layer, BC15 and BC18 that connect to base stations at the access layer, perform the following configurations:

* Disable upper-layer devices from tracing lower-layer devices, and set the default status of downstream interfaces (upper-layer devices' interfaces connecting to lower-layer devices) to Master.
* In the interconnection scenario, if the upper-layer devices' interfaces do not have the default Master state, you are advised to set the default status of the upstream interfaces (lower-layer devices' interfaces connecting to upper-layer devices) to Slave to avoid reverse tracing.
* Do not configure the default status for horizontal interfaces. Otherwise, clock sources may fail to be traced in clock source switching scenarios.

#### Pre-configuration Tasks

* Set physical parameters of interfaces and ensure that the interfaces are physically up.
* Run the [**license active**](cmdqueryname=license+active) *file-name* command to activate the clock synchronization license file on the active main control board. If the clock synchronization license file is not loaded, the [**ptp enable**](cmdqueryname=ptp+enable) configuration is not allowed.


[Importing Time Signals from an External BITS Time Source](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_1588v2_cfg_5005.html)

On a 1588v2 network, time signals are typically imported from an external BITS time source. You can configure multiple Routers to import time signals from an external BITS time source. A master clock can be selected dynamically using the BMCA.

[Configuring Time Source Attributes for BMCA Selection](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_1588v2_cfg_5006.html)

This section describes how to configure time source attributes used for BMCA selection. The devices configured with time source attributes can participate in BMCA selection. A local clock on a 1588v2 device can also participate in BMCA selection. The BMCA helps 1588v2 devices select a grandmaster clock. The grandmaster clock provides time signals for other devices over a 1588v2 network. 1588v2 devices obtain time synchronization information from the grandmaster.

[Globally Enabling 1588v2](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_1588v2_cfg_5007_a.html)

1588v2 takes effect after you configure 1588v2 in both the system and interface views. After 1588v2 is enabled in the system view, you also need to set other basic information, including the domain number, to establish a 1588v2 network.

[Enabling 1588v2 on a Specific Interface](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_1588v2_cfg_5008_a.html)

1588v2 takes effect after you configure 1588v2 in both the system and interface views. After enabling 1588v2 in the system view, enable it in the interface view.

[(Optional) Configuring Time Attributes for 1588v2 Packets](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_1588v2_cfg_5009.html)

This section describes how to configure time attributes for 1588v2 packets. 1588v2 devices exchange Announce, Sync, and Delay or Pdelay packets to send time information and maintain 1588v2 connections. You can set the interval at which a 1588v2 interface sends Announce, Sync, and Delay or Pdelay packets and the maximum number of Announce packet timeouts. Using the default time attribute values is recommended.

[(Optional) Configuring a 1588v2 Packet Encapsulation Mode](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_1588v2_cfg_5010.html)

1588v2 packets can be encapsulated into Layer 2 or Layer 3 packets. You can configure an encapsulation mode for 1588v2 packets based on the actual network conditions, as well as the source and destination addresses and transmission priority for the 1588v2 packets.

[Verifying the Configuration of Dynamic 1588v2 Functions](../../../../software/nev8r10_vrpv8r16/user/ne/dc_ne_1588v2_cfg_5012.html)

After configuring dynamic 1588v2 functions, verify the configuration.