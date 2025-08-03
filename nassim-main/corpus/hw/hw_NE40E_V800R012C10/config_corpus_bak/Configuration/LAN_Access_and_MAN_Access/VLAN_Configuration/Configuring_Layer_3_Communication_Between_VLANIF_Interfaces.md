Configuring Layer 3 Communication Between VLANIF Interfaces
===========================================================

VLANIF interfaces are Layer 3 logical interfaces. After creating VLANIF interfaces on Layer 2 devices, you can configure Layer 3 features on these interfaces.

#### Usage Scenario

A Layer 2 device cannot communicate with a Layer 3 device because no IP address can be configured on the Layer 2 device. To allow a Layer 2 device to communicate with a Layer 3 device, create a VLANIF interface on the Layer 2 device and assign an IP address to the VLANIF interface. The Layer 2 device then can communicate with the Layer 3 device.

Layer 3 switching combines both routing and switching techniques to implement routing on a switch, improving the overall performance of the network. After sending the first data flow based on a routing table, a Layer 3 switch generates a mapping table, in which the mapping between the MAC address and the IP address about this data flow is recorded. If the switch needs to send the same data flow again, it directly sends the data flow at Layer 2 but not Layer 3 based on the mapping table. In this manner, delays on the network caused by route selection are eliminated, and data forwarding efficiency is improved.

To allow the first data flow to be correctly forwarded based on the routing table, the routing table must contain correct routing entries. Therefore, configuring a Layer 3 interface and a routing protocol on the Layer 3 switch is required. VLANIF interfaces are therefore introduced.

#### Pre-configuration Tasks

Before creating a VLANIF interface, complete the following task:

* Creating a VLAN


[Creating a VLANIF Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vlan_cfg_0012.html)

Before configuring Layer 3 features on a Layer 2 device, create a VLANIF interface on the device first.

[Assigning an IP Address to a VLANIF Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vlan_cfg_0013.html)

As a VLANIF interface is a Layer 3 logical interface, it can communicate with other interfaces at the network layer only after being assigned an IP address.

[(Optional) Setting a Delay After Which a VLANIF Interface Goes Down](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vlan_cfg_0014.html)

Setting a delay after which a VLANIF interface goes down prevents network flapping caused by changes of VLANIF interface status. This function is also called VLAN damping.

[(Optional) Configuring Bandwidth for a VLANIF Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vlan_cfg_0015.html)

After configuring bandwidth for VLANIF interfaces, you can use the NMS to query the bandwidth. This facilitates traffic monitoring.

[Verifying the VLANIF Interface Configuration](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_vlan_cfg_0016.html)

After the configuration is complete, verify the VLANIF interface configuration, such as whether an IP address is correctly assigned to the VLANIF interface and status of the VLANIF interface.