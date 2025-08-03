Configuration Precautions for L2VPN Accessing L3VPN
===================================================

Configuration Precautions for L2VPN Accessing L3VPN

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| When an L2VPN is configured to access a public network or an L3VPN, you need to create a VE group (Virtual Ethernet group). In this case, a single device needs to implement L2VPN and L3VPN access and termination at the same time. Due to the complex forwarding process, the forwarding performance and delay deteriorate. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When an L2VE interface accesses an L3VE interface and the L2VE interface and Eth-Trunk interface are bound to the same local VSI, you need to manually change the MAC address of the L3VE interface or Eth-Trunk interface if Layer 3 communication is required between the Eth-Trunk interface and L3VE interface. Otherwise, MAC address flapping occurs on the Layer 2 network.  The configuration method is as follows:  Run the mac-address mac-address command in the VE interface view to change the MAC address of the VE interface.  Run the set access-ve-mac <mac-address> command in the slot view to change the MAC address of the L3VE interface.  Run the mac-address <mac-address> command in the Eth-trunk interface view to change the MAC address of the Eth-trunk interface. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| 1. By default, hardware loopback is performed on VE interfaces, and only 33% to 50% of board bandwidth is available. In this case, HQoS scheduling is supported. You can manually change the hardware loopback mode to software loopback.  2. Software loopback is not supported in scenarios with any of the following types of packets:  - BUM packets (VE interfaces support VPLS broadcast.)  - Packets requring HQoS scheduling  - Packets sent to the CPU (VLANIF broadcast packets and reserved multicast packets)  - NetStream sampling packets  - Mirrored packets  - Packets that exceed the MTU and need to be fragmented  Otherwise, services will be affected. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |