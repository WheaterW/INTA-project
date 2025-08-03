Configuring Extended DCN Functions
==================================

After configuring basic DCN functions, configure extended DCN functions as required.

#### Usage Scenario

In addition to basic data communication network (DCN) functions, an NE supports extended DCN functions.

* If a gateway network element (GNE) belongs to multiple processes and areas, configure DCN with multiple processes and areas so that the GNE can manage all the NEs in different processes and areas.
* When an NE functions as a GNE and manages RTN NEs, configure the GNE to work in compatible mode.
* When a large number of NEs are attached to a GNE that resides on more than one ring network, ring network services may affect each other. To address this problem, configure DCN packet transparent transmission.


#### Pre-configuration Tasks

Before configuring extended DCN functions, globally enable DCN.


[Configuring Multi-Process and Multi-Area DCN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dcn_cfg_0043.html)

If a GNE belongs to multiple processes and areas, multi-process and multi-area DCN can be configured so that the GNE can manage all the NEs in different processes and areas.

[Configuring the DCN Compatible Mode on a GNE](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dcn_cfg_0044.html)

The DCN compatible mode can be configured on a GNE so that it can manage RTNs.

[Configuring an Entry for DCN Packet Transparent Transmission](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dcn_cfg_0052.html)

To protect services of intersecting ring networks, configure an entry (mapping between source and destination interfaces) for DCN packet transparent transmission. After the entry is configured, the source interface transparently transmits DCN packets to the destination interface.

[Disabling Automatic Recovery of Default DCN Interfaces](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dcn_cfg_0057.html)

The DCN plug-and-play function is implemented through automatic creation and recovery of default DCN interfaces. If a default E1 channel of a CPOS or E1 subcard does not require DCN plug-and-play, disable automatic recovery of the corresponding default DCN interface so that the interface can be reserved for other purposes.

[Enabling DCN Communication Through Sub-interface 4094](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dcn_cfg_0060.html)

This section describes how to configure a sub-interface numbered 4094 for each Huawei and non-Huawei NE to implement DCN communication.

[Configuring an Authentication Message for the Private TLV That Supports NMS Automatic NE Management in LLDP Packets](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dcn_cfg_0061.html)

This section describes how to configure an authentication message for the private TLV that supports NMS automatic NE management in LLDP packets.

[Verifying the Configuration of Extended DCN Functions](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_dcn_cfg_0045.html)

After configuring extended DCN functions, verify the configuration.