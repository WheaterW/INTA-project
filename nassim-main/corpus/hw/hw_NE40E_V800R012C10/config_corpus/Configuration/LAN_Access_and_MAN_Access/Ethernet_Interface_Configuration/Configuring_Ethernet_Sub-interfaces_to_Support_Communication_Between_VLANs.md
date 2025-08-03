Configuring Ethernet Sub-interfaces to Support Communication Between VLANs
==========================================================================

To implement communication between hosts in a VLAN and hosts in another VLAN, create sub-interfaces on the Ethernet interface of a Layer 3 device that connects to a Layer 2 device and encapsulate 802.1q on the sub-interfaces.

#### Usage Scenario

When a Layer 2 switch belongs to different VLANs, create sub-interfaces on the Ethernet interface of a Layer 3 device that connects to the Layer 2 switch and add each sub-interface to a VLAN to ensure communication between hosts from different VLANs. In addition, configure 802.1q encapsulation and an IP address on each sub-interface.

As shown in [Figure 1](#EN-US_TASK_0172362784__fig_dc_vrp_ethernet_cfg_000701), the PE uses an Ethernet interface to connect to CE, and CE is connected to hosts in VLAN 10 and VLAN 20.

**Figure 1** Network diagram of Ethernet sub-interfaces supporting communication between VLANs  
![](images/fig_dc_vrp_ethernet_cfg_000701.png)

To allow hosts in VLAN 10 to communicate with hosts in VLAN 20, perform the following steps on the PE:

* Create Ethernet sub-interfaces.
* Configure 802.1q encapsulation on the sub-interfaces and associate the sub-interfaces with VLANs.
* Assign IP addresses to the sub-interfaces.

#### Pre-configuration Tasks

Power on the device and ensure that its self-check is normal.



[Creating a Sub-interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethernet_cfg_0008.html)

To ensure communication between VLANs, create Ethernet sub-interfaces on a Layer 3 device.

[Configuring IP Addresses](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethernet_cfg_0009.html)

To implement communication between VLANs, establish IP routes.

[Configuring 802.1Q Encapsulation](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethernet_cfg_0010.html)

When a Layer 3 device and a Layer 2 device are directly connected through Ethernet interfaces and the interface that directly connects the Layer 2 device to the Layer 3 device is added to a VLAN, configure an encapsulation mode for the Ethernet sub-interface on the Layer 3 device to ensure that the two devices normally communicate with each other. 

[Verifying the Ethernet Sub-interface Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_ethernet_cfg_0011.html)

After Ethernet sub-interfaces are configured to support communication between VLANs, you can view information about the sub-interface, including the MTU, IP address, and VLAN encapsulation.