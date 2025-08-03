Configuring Layer 2 Protocol Tunneling (By Replacing Multicast Destination MAC Address)
=======================================================================================

Some Layer 2 protocols running between user networks, such as Multiple Spanning Tree Protocol (MSTP) and Link Aggregation Control Protocol (LACP), must traverse a backbone network to perform Layer 2 protocol calculation. Therefore, Layer 2 protocol tunneling must be configured.

#### Usage Scenario

To allow Layer 2 PDUs from user networks to be transparently transmitted over a backbone network, configure Layer 2 protocol tunneling. Layer 2 PDUs from the user networks then travel through different Layer 2 tunnels to reach the destinations to perform Layer 2 protocol calculation.

#### Pre-configuration Tasks

Before configuring Layer 2 protocol tunneling, complete the following tasks:

* Connect the interfaces properly.
* Configure the interface type based on whether tagged packets are received.


[Configuring an Edge Device to Replace the Multicast Destination MAC Address](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2bptnl_cfg_0005.html)

To prevent a backbone network edge device from sending the received Layer 2 protocol data units (PDUs) to its CPU for processing and ensure that the Layer 2 PDUs are tunneled across the backbone network, configure the edge device to replace the multicast destination MAC address in Layer 2 PDUs with a specified multicast MAC address.

[Enabling Layer 2 Protocol Tunneling on an Interface](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2bptnl_cfg_0026.html)

If you want backbone network devices to transparently transmit Layer 2 PDUs from user networks, enable Layer 2 protocol tunneling on the device interfaces.

[Configuring Transparent Transmission of PDUs on a VLL/EVPL/VPLS/EVPN Network](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_ne_vpws_cfg_5021.html)

This section describes how to transparently transmit untagged Layer 2 protocol data units (PDUs), such as LACP, LLDP, BPDU, CDP, and UDLD packets, on a VLL/EVPL/VPLS/EVPN network to implement Layer 2 negotiation with remote users.

[Verifying the Configuration of Interface-based Layer 2 Protocol Tunneling](../../../../software/nev8r10_vrpv8r16/user/vrp/dc_vrp_l2bptnl_cfg_0007.html)

After configuring interface-based Layer 2 protocol tunneling, check Layer 2 protocol tunneling information, such as the tunneled Layer 2 protocol names, protocol types, multicast destination MAC addresses, and specified multicast MAC addresses (group MAC addresses).