Configuration Precautions for Load Balancing
============================================

Configuration Precautions for Load Balancing

#### Feature Requirements

**Table 1** Feature requirements
| Feature Requirements | Series | Models |
| --- | --- | --- |
| Support for ECMP load balancing consistency:  1. Only pure IP forwarding is supported, including IPv4 unicast and IPv6 unicast. Only GE main interfaces and sub-interfaces and Eth-Trunk main interfaces and sub-interfaces are supported.  2. The number of interfaces for load balancing can only be reduced. If an interface fails and is added to an ECMP group again, the consistent hash algorithm does not take effect, and traffic needs to be hashed again.  3. This feature is mutually exclusive with [undo]load-balance unequal-cost enable in the system view, [undo]load-balance unequal-cost enable in the interface view, and [undo]load-balance dynamic-adjust enable in the slot view.  ECMP load balancing consistency is mutually exclusive with other load balancing modes. If a load balancing link member is deleted and then added, ECMP load balancing consistency does not take effect. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| 1. When multiple load balancing hash modes are configured on a device, the SIP-based or DIP-based hash mode takes precedence over other load balancing hash modes. There is no mutual exclusion restriction on commands.  2. When traffic from the same board is load balanced, the hash algorithm is performed based on the source IP address and the outbound interfaces of the traffic are the same.  Properly plan the load balancing mode based on service requirements. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| When the hash algorithm is set to random, symmetric load balancing does not take effect. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Symmetric load balancing does not support CE dual-homing scenarios. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Symmetric load balancing does not support E-Trunk scenarios. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Symmetric load balancing does not support trunk localization scenarios. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Symmetric load balancing does not support multi-level load balancing scenarios. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Symmetric load balancing does not support multicast scenarios. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Symmetric load balancing cannot work with MAC address- or label-based load balancing.  Plan services properly. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Symmetric load balancing supports data traffic packets instead of protocol packets between two devices. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| For symmetric load balancing:  1. When a Huawei device is connected to a non-Huawei device, upstream and downstream traffic may not be hashed to the same link due to different load balancing algorithms.  2. When the device is connected to a Huawei device that does not support symmetric load balancing, it cannot be ensured that upstream and downstream traffic is hashed to the same link. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Fragmented and non-fragmented packets of the same flow are transmitted through different paths. The first fragment and subsequent fragments are transmitted through the same path. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| Symmetric load balancing does not support port extension. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |
| In scenarios where common IP routes and tunnels work in hybrid load balancing mode (including SRv6 tunnels, LDP tunnels, and SR-MPLS BE tunnels decoupled), load balancing is performed based on the peer granularity. | NE40E-M2 | NE40E-M2E/NE40E-M2F/NE40E-M2H/NE40E-M2K/NE40E-M2K-B |