Configuring Basic STP/RSTP Functions
====================================

STP/Rapid Spanning Tree Protocol (RSTP) is used to block redundant links on the Layer 2 network and trim a network into a loop-free tree topology.

#### Applicable Environment

On a complex network, loops are inevitable. With the requirement for network redundancy backup, network designers tend to deploy multiple physical links between two devices, one of which is the master and the others are the backup. Loops are likely or bound to occur in such a situation. Loops will cause broadcast storms, thereby exhausting network resources and paralyzing the network. Loops also cause flapping of MAC address tables and thus damages MAC address entries. STP/RSTP can be deployed on a network to eliminate loops. If a loop is detected, STP/RSTP blocks one port to eliminate the loop.

On the network shown in [Figure 1](#EN-US_TASK_0172363536__fig_dc_vrp_stp_cfg_0004_01), DeviceA, DeviceB, DeviceC, and DeviceD form a ring network. STP or RSTP is deployed on the ring network to eliminate loops, enhancing reliability of the network.**Figure 1** Diagram of a ring network
  
![](images/fig_dc_vrp_stp_cfg_0004_01.png)  



![](../../../../public_sys-resources/note_3.0-en-us.png) 

If the current device supports STP and RSTP, RSTP is recommended.



#### Pre-configuration Tasks

Before configuring basic STP/RSTP functions, complete the following task:

* Connecting interfaces and setting physical parameters for the interfaces to ensure that the physical status of the interfaces is Up


[Configuring the STP/RSTP Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_stp_cfg_0006.html)

Before configuring basic STP/Rapid Spanning Tree Protocol (RSTP) functions, you need to configure the working mode of a device to STP/RSTP. RSTP is compatible with STP.

[(Optional) Configuring Device Priorities](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_stp_cfg_0007.html)

Select a device (functioning as a root bridge) from devices for each spanning tree. You can configure the priorities of the devices to preferentially select a root bridge. The lower the numerical value is, the higher priority a device has and the more likely the device will be selected as a root bridge.

[(Optional) Configuring the Path Cost for a Port](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_stp_cfg_0008.html)

The STP/Rapid Spanning Tree Protocol (RSTP) path cost determines root port selection. The port from which to the root port costs the least is selected as the root port.

[(Optional) Configuring Port Priorities](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_stp_cfg_0009.html)

Select a designated port for each connection based on the root path cost, bridge ID (BID), and port ID of each port. The lower the port priority value, the more likely the port on a device becomes a designated port; the higher the port priority value, the more likely the port is to be blocked.

[Enabling STP/RSTP](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_stp_cfg_0010.html)

After STP/Rapid Spanning Tree Protocol (RSTP) is enabled, spanning trees are calculated.

[Verifying the Basic STP/RSTP Function Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_stp_cfg_0011.html)

After basic STP/Rapid Spanning Tree Protocol (RSTP) functions are configured, you can view the information such as the port role and port status to check whether the spanning tree calculation is correctly performed.