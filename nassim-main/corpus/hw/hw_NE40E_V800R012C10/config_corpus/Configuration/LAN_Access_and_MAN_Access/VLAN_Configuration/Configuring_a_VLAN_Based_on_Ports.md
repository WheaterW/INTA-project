Configuring a VLAN Based on Ports
=================================

Configuring a VLAN based on ports allows PCs in the VLAN to communicate with each other.

#### Applicable Environment

A company has multiple departments located in different buildings. For service security, it is required that employees in one department be able to communicate with each other, whereas employees in different departments be prohibited from communicating with each other. Devices on the network shown in [Figure 1](#EN-US_TASK_0172363083__fig_dc_vrp_vlan_cfg_000401) are configured as follows:

* Add ports connecting devices to PCs of the financial department to VLAN 5 and ports connecting devices to PCs of the marketing department to VLAN 9. This configuration prevents employees in financial and marketing departments from communicating with each other.
* Configure links between CE and PE as trunk links to allow frames from VLAN 5 and VLAN 9 to pass through, allowing employees of the same department but different buildings to communicate with each other.

By configuring port-based VLANs on the PE, CE1, and CE2, employees in the same department can communicate with each other, whereas employees in different departments cannot.

**Figure 1** Configuring a VLAN based on ports  
![](images/fig_dc_vrp_vlan_cfg_000401.png)
#### Pre-configuration Tasks

Before configuring a VLAN based on ports, complete the following task:

* Connect ports and configuring physical parameters of the ports, so that the ports are physically up.


[Creating a VLAN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vlan_cfg_0006.html)

Creating a VLAN isolates PCs that do not need to communicate with each other. This improves network security, reduces broadcast traffic, and prevents broadcast storms.

[Configuring the Type of a Layer 2 Ethernet Port](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vlan_cfg_0007.html)

On a Layer 2 switching device, some ports identify frames with VLAN tags, whereas the others do not. Configure ports types for Layer 2 Ethernet ports as needed.

[Adding a Port to a VLAN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vlan_cfg_0008.html)

Adding a port to a VLAN associates the port with the VLAN.

[Verifying the Configuration of a Layer 2 Interface-based VLAN](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vlan_cfg_0009.html)

After configuring a Layer 2 interface-based VLAN, verify the configuration.