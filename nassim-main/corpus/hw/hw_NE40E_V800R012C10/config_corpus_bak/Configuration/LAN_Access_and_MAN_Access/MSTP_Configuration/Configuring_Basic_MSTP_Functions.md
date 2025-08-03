Configuring Basic MSTP Functions
================================

Multiple Spanning Tree Protocol (MSTP) based on the basic STP/Rapid Spanning Tree Protocol (RSTP) function divides a switching network into multiple regions, each of which has multiple spanning trees that are independent of each other. MSTP isolates user traffic and service traffic, and load-balances VLAN traffic.

#### Applicable Environment

On a complex network, loops are inevitable. With the requirement for network redundancy backup, network designers tend to deploy multiple physical links between two devices, one of which is the master and the others are the backup. Loops are likely or bound to occur in such a situation. Loops will cause broadcast storms, thereby exhausting network resources and paralyzing the network. Loops also cause flapping of MAC address tables and thus damages MAC address entries.

MSTP can be deployed on a network to eliminate loops. If a loop is detected, MSTP blocks one or more ports to eliminate the loop. In addition, Multiple Spanning Tree Instances (MSTIs) can be configured to load-balance VLAN traffic.

As shown in [Figure 1](#EN-US_TASK_0172363607__fig_dc_vrp_mstp_cfg_0004_01), DeviceA, DeviceB, DeviceC, and DeviceD all support MSTP. It is required to create MSTI 1 and MSTI 2, configure a root bridge for each MSTI, and set the ports to be blocked to load-balance traffic of VLANs 1 to 10 and VLANs 11 to 20 among different paths.

**Figure 1** Networking diagram of configuring basic MSTP functions  
![](figure/en-us_image_0000002086841158.png)
![](../../../../public_sys-resources/note_3.0-en-us.png) 

If the current device supports MSTP, configuring MSTP is recommended.



#### Pre-configuration Tasks

Before configuring basic MSTP functions, complete the following task:

* Connecting interfaces and setting physical parameters for the interfaces to ensure that the physical status of the interfaces is Up


#### Configuration Procedures

**Figure 2** Flowchart for configuring basic MSTP functions  
![](figure/en-us_image_0190492331.png)


[Configuring the MSTP Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mstp_cfg_0006.html)

Before configuring basic Multiple Spanning Tree Protocol (MSTP) functions, you need to configure the working mode of a device to MSTP. MSTP is compatible with STP and Rapid Spanning Tree Protocol (RSTP).

[Configuring an MST Region](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mstp_cfg_0007.html)

Multiple Spanning Tree Protocol (MSTP) divides a switching network into multiple MST regions. After an MST region name, VLAN-to-Multiple Spanning Tree Instance (MSTI) mapping, and MSTP revision level are configured, MST region configuration is complete.

[(Optional) Configuring a Priority for a Device in an MSTI](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mstp_cfg_0008.html)

The lower the numerical value is, the higher priority a device has and the more likely the device will be selected as a root bridge. You can configure the cost of the path from a device to the root bridge to preferentially select a root port.

[(Optional) Configuring a Path Cost of a Port in an MSTI](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mstp_cfg_0009.html)

The Multiple Spanning Tree Protocol (MSTP) path cost determines root port selection in a Multiple Spanning Tree Instance (MSTI). The port with the lowest path cost to the root bridge is selected as a root port.

[(Optional) Configuring a Port Priority in an MSTI](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mstp_cfg_0010.html)

The lower the numerical value, the more likely the port on a device becomes a designated port; the higher the numerical value, the more likely the port is to be blocked.

[Enabling MSTP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mstp_cfg_0011.html)

After basic Multiple Spanning Tree Protocol (MSTP) functions are configured on a device, enabling the MSTP function is required so that MSTP can work properly.

[Verifying the Basic MSTP Function Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mstp_cfg_0012.html)

After basic Multiple Spanning Tree Protocol (MSTP) functions are configured, verify the configuration.