Configuring an Eth-Trunk Interface in Static LACP Mode
======================================================

If two LACP-capable devices are directly connected through an Eth-Trunk link, you can configure the Eth-Trunk interfaces on the two devices to work in static LACP mode. Eth-Trunk interfaces working in static LACP mode implement both load balancing and link backup.

#### Usage Scenario

As network services expand, the bandwidth provided by a single P2P physical link working in full-duplex mode cannot meet the requirement of service traffic.

To increase bandwidth without obtaining more hardware resources or requiring more IP addresses, configure Eth-Trunk interfaces using the link aggregation technique. Configuring an Eth-Trunk interface to work in static LACP mode increases interface bandwidth and provides reliability. When an Eth-Trunk member link fails, traffic is automatically switched to other available links, preventing traffic interruption. In addition, Eth-Trunk interfaces working in static LACP mode can implement load balancing. The configuration is simple.

As shown in [Figure 1](#EN-US_TASK_0172362865__fig_dc_vrp_ethtrunk_cfg_002501), the Eth-Trunk interfaces on the two directly connected devices can be configured to work in static LACP mode to implement load balancing. The static LACP mode is also called the M:N mode. M links function as active links and N links function as standby links to implement link backup.**Figure 1** Eth-Trunk interfaces in static LACP mode  
![](images/fig_dc_vrp_ethtrunk_cfg_002501.png)

![](../../../../public_sys-resources/note_3.0-en-us.png) 

Interfaces operating at different rates, in different duplex modes, and on different boards can be added to the same Eth-Trunk interface working in static LACP mode. Member interfaces working at different rate, however, cannot be in the forwarding state at the same time, and member interfaces working in half-duplex mode cannot forward traffic. Confirm the boards where member interfaces reside, interface rate, and duplex mode.

To enable interfaces operating at different rates to forward traffic after they are added to an Eth-Trunk interface, run the [**lacp mixed-rate link enable**](cmdqueryname=lacp+mixed-rate+link+enable) command.

#### Pre-configuration Tasks

Before configuring an Eth-Trunk interface to work in static LACP mode, complete the following tasks:

* Connect interfaces and set their physical parameters to ensure that the physical status of the interfaces is up.
* Activate the hardware RTU for the involved physical interfaces.



[Creating an Eth-Trunk Interface in Static LACP Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0014.html)

An Eth-Trunk interface must be created before you add physical interfaces to the Eth-Trunk interface.

[Adding Physical Interfaces to the Eth-Trunk Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0015.html)

After an Eth-Trunk interface is created and configured to work in static LACP mode, add physical interfaces to the Eth-Trunk interface to increase interface bandwidth, carry out load balancing, and improve reliability.

[Configuring Eth-Trunk Interface Parameters](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0016.html)

Layer 2 and Layer 3 Eth-Trunk interfaces need to be configured with different parameters as required.

[Configuring Parameters for Eth-Trunk Member Interfaces](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0017.html)

To ensure reliable communication between Eth-Trunk interfaces, configure proper parameters for Eth-Trunk member interfaces.

[(Optional) Configuring an Eth-Trunk Sub-interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0018.html)

To transmit both Layer 2 and Layer 3 services over the same physical link, create a sub-interface on a Layer 2 Eth-Trunk interface.

[(Optional) Enabling State Flapping Suppression on an Eth-Trunk Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0019.html)

You can enable state flapping suppression on an Eth-Trunk interface to prevent the Eth-Trunk interface from alternating between up and down due to member interface state flapping or received incorrect packets.

[Verifying the Configuration of the Eth-Trunk Interface in Static LACP Mode](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethtrunk_cfg_0020.html)

After an Eth-Trunk interface is configured in static LACP mode, verify the configuration, including the interface ID, working mode, member interface status, LACP system priority, LACP interface priority, and LACP preemption delay.