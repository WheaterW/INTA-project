Configuring an Eth-Trunk Interface to Work in Manual Load Balancing Mode
========================================================================

You can configure Eth-Trunk interfaces working in manual load balancing mode on two connected devices if one or both of them do not support LACP. Then, you can add physical interfaces to the Eth-Trunk interfaces to increase bandwidth and improve reliability.

#### Usage Scenario

As the volume of services deployed on networks increases, the bandwidth provided by a single P2P physical link working in full-duplex mode cannot meet the requirements of service traffic.

To increase bandwidth without obtaining more hardware resources or requiring more IP addresses, configure Eth-Trunk interfaces using the link aggregation technique. When one or both of the devices at the two ends of an Eth-Trunk link do not support LACP, you can configure the Eth-Trunk interfaces to work in manual load balancing mode. In addition, you can add multiple member interfaces to increase the bandwidth between the two devices and improve reliability.

On the network shown in [Figure 1](#EN-US_TASK_0172362855__fig_dc_vrp_ethtrunk_cfg_003201), an Eth-Trunk interface is configured to work in manual load balancing mode on each of the two directly connected devices to implement load balancing.**Figure 1** Eth-Trunk interfaces in manual load balancing mode  
![](images/fig_dc_vrp_ethtrunk_cfg_003201.png)

![](../../../../public_sys-resources/note_3.0-en-us.png) 

An Eth-Trunk interface working in manual load balancing mode can contain member interfaces at different rates, in different duplex modes, and on different boards.

#### Pre-configuration Tasks

Before configuring an Eth-Trunk interface to work in manual load balancing mode, complete the following tasks:

* Connect interfaces and set their physical parameters to ensure that the physical status of the interfaces is up.
* Activate the hardware RTU for the involved physical interfaces.



[Creating an Eth-Trunk Interface and Configuring It to Work in Manual Load Balancing Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0007.html)

You can add physical interfaces to an Eth-Trunk interface working in manual load balancing mode. All the member interfaces are in the forwarding state and load-balance traffic.

[Adding Physical Interfaces to the Eth-Trunk Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0008.html)

After creating an Eth-Trunk interface and configuring it to work in manual load balancing mode, add physical interfaces to the Eth-Trunk interface to increase interface bandwidth and improve reliability.

[Configuring Eth-Trunk Interface Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0009.html)

Eth-Trunk interfaces in manual load balancing mode working in Layer 2 and Layer 3 modes need to be configured with different parameters.

[Configuring Parameters for Eth-Trunk Member Interfaces](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0010.html)

To ensure reliable communication between Eth-Trunk interfaces, configure proper parameters for Eth-Trunk member interfaces.

[(Optional) Configuring an Eth-Trunk Sub-interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0011.html)

To transmit both Layer 2 and Layer 3 services over the same physical link, create a sub-interface on a Layer 2 Eth-Trunk interface.

[Verifying the Configuration of the Eth-Trunk Interface in Manual Load Balancing Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0012.html)

After an Eth-Trunk interface in manual load balancing mode is successfully configured, verify the configuration, including the Eth-Trunk ID, working mode, and status of member interfaces.