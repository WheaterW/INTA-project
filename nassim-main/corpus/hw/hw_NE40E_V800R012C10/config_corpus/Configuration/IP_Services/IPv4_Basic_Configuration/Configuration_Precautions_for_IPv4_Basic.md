Configuration Precautions for IPv4 Basic
========================================

Configuration Precautions for IPv4 Basic

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| The function to allow a Layer 3 interface to borrow the IPv4 address of a loopback interface:  1. After a Layer 3 interface borrows the IPv4 address of a loopback interface, remote routes can be learned using only IGP or BGP based on IGP.  2. After a Layer 3 interface borrows the IPv4 address of a loopback interface, ARP learning, direct routes, BGP based on direct routes, and lower-layer traffic forwarding are not supported. In this case, the outbound interface of the next hop cannot be determined because the same IP address corresponds to mutiple outbound interfaces. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Static routes imported between VPN and public network instances do not support IP FRR. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |