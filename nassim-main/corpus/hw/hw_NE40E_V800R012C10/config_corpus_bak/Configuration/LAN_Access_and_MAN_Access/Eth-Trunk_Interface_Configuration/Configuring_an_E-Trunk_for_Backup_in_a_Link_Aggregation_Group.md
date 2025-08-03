Configuring an E-Trunk for Backup in a Link Aggregation Group
=============================================================

Enhanced Trunk (E-Trunk) implements inter-device link aggregation, ensuring device-level reliability.

#### Usage Scenario

Eth-Trunk implements link reliability between single devices. However, if a device fails, Eth-Trunk ceases to take effect.

To further improve network reliability, device redundancy with one master device and one backup device can be used. If the master device or primary link fails, the backup device can take over user services. In this situation, another device must be dual-homed to the master and backup devices, and inter-device link reliability must be ensured.

In dual-homing networking, Virtual Router Redundancy Protocol (VRRP) can be used to ensure device-level reliability, and Eth-Trunk can be used to ensure link reliability. In some cases, however, traffic cannot be switched to the backup device and secondary link simultaneously if the master device or primary link fails. As a result, traffic is interrupted. To address this issue, use Enhanced Trunk (E-Trunk) to implement both device-level and link reliability.

On the network shown in [Figure 1](#EN-US_TASK_0172362914__fig_dc_vrp_ethtrunk_cfg_003901), you can create an E-Trunk between PE1 and PE2 to implement backup in the E-Trunk link aggregation group, which improves network reliability.

**Figure 1** Networking for Configuring an E-Trunk for Backup in a Link Aggregation Group  
![](images/fig_dc_vrp_ethtrunk_cfg_003901.png)
#### Pre-configuration Tasks

Before Configuring an E-Trunk for Backup in a Link Aggregation Group, complete the following task:

* Add Eth-Trunk interfaces working in manual load balancing mode to an E-Trunk.
  
  + [Configuring an Eth-Trunk Interface to Work in Manual Load Balancing Mode](dc_vrp_ethtrunk_cfg_0006.html) on the PEs.
  + Configure Ethernet operations, administration and maintenance (OAM) on the CE and PEs to improve link reliability.
* Add Eth-Trunk interfaces working in static LACP mode to an E-Trunk.
  
  + [Configuring an Eth-Trunk Interface in Static LACP Mode](dc_vrp_ethtrunk_cfg_0013.html) on the CE and PEs.
  + Before manually create a BFD session and bind it to an E-Trunk, [Enabling BFD Globally](dc_vrp_bfd_cfg_0005.html) and [Establishing a BFD Session](dc_vrp_bfd_cfg_0006.html) on the PEs.
  + Before enable a device to automatically create a BFD session and bind the session to an E-Trunk, [Enabling BFD Globally](dc_vrp_bfd_cfg_0005.html) on the PEs.
* Add a global VE interface to an E-Trunk.
  
  + Create a global VE interface and configure it as an L2VE interface on the PEs.
  + [Enabling BFD Globally](dc_vrp_bfd_cfg_0005.html) and [Establishing a BFD Session](dc_vrp_bfd_cfg_0006.html) on the PEs.


[Creating an E-Trunk](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0043.html)

Eth-Trunk interfaces can be added only to a created E-Trunk. E-Trunk provides device-level reliability.

[Adding an Interface to an E-Trunk](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0044.html)

An E-Trunk forwards packets through its member interfaces, which can be Eth-Trunk interfaces or global VE interfaces.

[(Optional) Configuring E-Trunk Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0045.html)

To ensure reliable E-Trunk communication, configure proper E-Trunk parameters.

[(Optional) Configuring a Working Mode for an E-Trunk Member Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0046.html)

To enable proper traffic transmission, configure a working mode for an E-Trunk member interface. An E-Trunk member interface can work in automatic, forcible master, or forcible backup mode.

[(Optional) Binding an E-Trunk to BFD](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0047.html)

If the master device in an E-Trunk fails, to ensure that the backup device promptly detects the failure and takes over traffic, bind the E-Trunk to a Bidirectional Forwarding Detection (BFD) session for fast failure detection.

[(Optional) Configuring an E-Trunk to Determine the Master/Backup Status of Devices Based on the Number of Available Eth-Trunk Member Links or the Available Eth-Trunk Bandwidth](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0048.html)

When devices added to an E-Trunk greatly differ in their available Eth-Trunk member links, to maximize link bandwidth utilization, you can configure the E-Trunk to determine the master/backup status of the devices based on the number of available Eth-Trunk member links. You can also configure the E-Trunk to determine the master/backup status of the devices based on the available Eth-Trunk bandwidth.

[(Optional) Configuring Whitelist Session-CAR for E-Trunk](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0049.html)

You can configure whitelist session-CAR for E-Trunk to isolate bandwidth resources by session for E-Trunk packets. This configuration prevents bandwidth preemption among E-Trunk sessions in the case of a traffic burst.

[(Optional) Configuring an E-Trunk to Transmit Layer 3 Services](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0050.html)



[Verifying the Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0051.html)

After configuring an E-Trunk, check the configurations, including the E-Trunk priority, system ID, source IP address, peer IP address, revertive switching delay, master/backup status, dynamic BFD session parameters, and E-Trunk description.