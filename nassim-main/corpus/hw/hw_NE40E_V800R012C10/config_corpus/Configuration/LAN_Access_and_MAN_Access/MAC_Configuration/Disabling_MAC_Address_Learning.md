Disabling MAC Address Learning
==============================

On a network where networking is fixed, after MAC address learning is disabled on an interface of a device, other servers or terminals cannot communicate with this device through this interface, improving the device security.

#### Usage Scenario

On the network shown in [Figure 1](#EN-US_TASK_0172362729__fig_dc_vrp_mac_cfg_002501), a CE connects to the server through a fixed interface. To improve device security, the network administrator can configure the interface to allow only packets with certain MAC addresses to pass through. Specifically, the network administrator can configure the server's static MAC address on this interface, disable MAC address learning on this interface, and specify the action as discard. In this way, other servers or terminals cannot communicate with the device named CE through this interface, improving network security and stability.**Figure 1** Networking diagram for disabling MAC address learning
  
![](images/fig_dc_vrp_mac_cfg_002501.png)  


#### Pre-configuration Tasks

Before disabling MAC address learning, complete the following task: Connect interfaces and set their physical parameters to ensure that the physical status of the interfaces is up.



[Disabling MAC Address Learning in a VLAN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mac_cfg_0027.html)

Disabling MAC address learning in a VLAN helps defend against MAC address attacks and improves security for users in this VLAN.

[Verifying the Configuration of Disabling MAC Address Learning](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_mac_cfg_0028.html)

After disabling MAC address learning on an interface and in a VLAN, verify the configuration.