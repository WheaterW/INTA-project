Configuring Hash Factors for Load Balancing
===========================================

Configuring Hash Factors for Load Balancing

#### Context

This section describes how to adjust hash factors for load balancing.


#### Procedure

* System-view IP forwarding scenario
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run **load-balance hash-key ip** { **destination-ip** | **source-ip** } **slot** { **all** | *slot-id* }
     
     
     
     Hash factors are configured for load balancing in IP forwarding scenarios.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Slot-view IP forwarding scenario
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**slot**](cmdqueryname=slot) *slot-id*
     
     
     
     The slot view is displayed.
  3. Run [**load-balance hash-fields ip**](cmdqueryname=load-balance+hash-fields+ip) { **l2** | **l3** | **l4** }
     
     
     
     Hash factors are configured for load balancing on the interface board in IP forwarding scenarios.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     In IPv6 unicast scenarios, the default hash factors for TCP/UDP packets are "5-tuple + flow label" (the tuples are source IPv6 address, destination IPv6 address, source port number, destination port number, and protocol number), and those for other packets are "3-tuple + flow label" (the tuples are source IPv6 address, destination IPv6 address, and protocol number). If the flow label field in the IPv6 header is used as a hash factor for load balancing and the flow label of a given flow (with the same 5-tuple or 3-tuple) changes, out-of-order packets are generated during load balancing. To prevent this problem, run the [**load-balance hash-fields flow-label disable**](cmdqueryname=load-balance+hash-fields+flow-label+disable) command to disable flow-label-based load balancing in IPv6 unicast scenarios.
     
     IFIT occupies the 4 most significant bits of the flow label. For a given flow, the 4 most significant bits change periodically. When the flow label is used as a hash factor for load balancing, the same flow is hashed to different paths. To prevent this problem, run the **load-balance hash-fields flow-label bit-16 enable** command to enable the system to use the 16 least significant bits of the flow label and ignore the 4 most significant bits during load balancing.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* VPLS and MAC forwarding scenario
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**slot**](cmdqueryname=slot) *slot-id*
     
     
     
     The slot view is displayed.
  3. Run [**load-balance hash-fields mac**](cmdqueryname=load-balance+hash-fields+mac) { **l2** | **l3** | **l4** | **label-ip** }
     
     
     
     Hash factors are configured for per-flow load balancing on the interface board in a VPLS and MAC forwarding scenario.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* MPLS forwarding scenario
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**slot**](cmdqueryname=slot) *slot-id*
     
     
     
     The slot view is displayed.
  3. Run [**load-balance hash-fields mpls**](cmdqueryname=load-balance+hash-fields+mpls) { **payload-header** | **label** | **ip** | **ip-tos** | **mac** }
     
     
     
     Hash factors are configured for per-flow load balancing for MPLS packets on the interface board.
  4. Run [**load-balance hash-fields mpls**](cmdqueryname=load-balance+hash-fields+mpls) { **label** | **ip** | **ip-tos** | **mac** }
     
     
     
     Hash factors are configured for per-flow load balancing for MPLS packets on the interface board.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  The **ip-tos** parameter takes effect only for IPv4 packets encapsulated with MPLS packets and uses the ToS field for hash calculation. This parameter does not take effect for IPv6 packets encapsulated with MPLS packets, meaning that the configuration effect is the same as that of the **load-balance hash-fields mpls ip** command.
* VLL forwarding scenario
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**slot**](cmdqueryname=slot) *slot-id*
     
     
     
     The slot view is displayed.
  3. Run [**load-balance hash-fields vll**](cmdqueryname=load-balance+hash-fields+vll) { **l2** | **l3** | **l4** | **label-ip** | **label** }
     
     
     
     Hash factors are configured for traffic load balancing on the interface board in a VLL forwarding scenario.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* System-view L2TPv2 forwarding scenario
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run **load-balance hash-key ip** { **destination-ip** | **source-ip** } **slot** { **all** | *slot-id* }
     
     
     
     Hash factors are configured for load balancing in L2TPv2 forwarding scenarios.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Slot-view L2TPv2 forwarding scenario
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**slot**](cmdqueryname=slot) *slot-id*
     
     
     
     The slot view is displayed.
  3. Run [**load-balance hash-fields ip**](cmdqueryname=load-balance+hash-fields+ip) { **l2** | **l3** | **l4** }
     
     
     
     Hash factors are configured for load balancing on the interface board in L2TPv2 forwarding scenarios.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     In slot-view L2TPv2 forwarding scenarios, the **l4** parameter is used by default. This means that the default hash factors <source IP address, destination IP address, tunnel ID, session ID> are used for hash calculation. The same default hash factors are used for hash calculation if the **l3** parameter is specified. If the **l2** parameter is specified, the hash factors <source MAC address, destination MAC address> is used for hash calculation.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* L2/L3VPN over L2VPN scenario
  
  
  
  [Figure 1](#EN-US_TASK_0000001175223970__fig_load-balance_feature_07801) shows an L2/L3VPN over L2VPN scenario. By default, L2-P1 balances traffic among outbound Eth-Trunk member interfaces based on MAC addresses of packets. Because packets transmitted over the same VPLS tunnel carry the same MAC address, traffic from the same site but different L3VPNs cannot be load-balanced among different Eth-Trunk member interfaces. To resolve this problem, you can run the **load-balance hash-fields ip l3** command on the inbound interface of L2-PE1 to enable IP address-based load balancing in an L3VPN over VPLS scenario. This allows L2-PE1 to load-balance traffic from the same site but different L3VPNs among links between L2-PE1 and L2-P1.
  
  
  
  **Figure 1** L2/L3VPN over L2VPN networking  
  ![](figure/en-us_image_0000001237821101.png)
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
     
     
     
     The view of the interface where load balancing needs to be configured is displayed.
  3. Run [**load-balance hash-fields ip l3**](cmdqueryname=load-balance+hash-fields+ip+l3)
     
     
     
     IP address-based load balancing is configured in L3VPN over L2VPN, L2VPN over L2VPN, or IP over IP scenarios where the router functions as the PE of the backbone network or as the P.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* VXLAN scenario
  
  **Figure 2** VXLAN tunnel networking  
  ![](../vrp/figure/en-us_image_0172352793.png)
  
  In the preceding distributed gateway scenario, packets passing through the VXLAN tunnel endpoint Leaf1 are VXLAN encapsulated and then forwarded. When the VXLAN tunnel can be recursed to multiple equal-cost links, the configurations in different scenarios are as follows:
  
  
  
  + VXLAN Layer 2 forwarding scenario: Host3 communicates with Host2, and Leaf1 functions as a Layer 2 gateway.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**load-balance hash-fields l2vxlan-vni enable**](cmdqueryname=load-balance+hash-fields+l2vxlan-vni+enable)
       
       Load balancing for VXLAN Layer 2 forwarding is enabled.
    3. (Optional) Run [**load-balance hash-fields l2vxlan-deep-hash enable**](cmdqueryname=load-balance+hash-fields+l2vxlan-deep-hash+enable)
       
       Deep load balancing is enabled for a Layer 2 VXLAN.
    4. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
  + VXLAN Layer 3 forwarding scenario: Host1 communicates with Host2, and Leaf1 functions as a Layer 3 gateway.
    1. Run [**system-view**](cmdqueryname=system-view)
       
       The system view is displayed.
    2. Run [**load-balance hash-fields l3vxlan-vni enable**](cmdqueryname=load-balance+hash-fields+l3vxlan-vni+enable)
       
       Load balancing for VXLAN Layer 3 forwarding is enabled.
    3. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.
* Disable a device from using tunnel information as a hash factor during hash calculation for non-fragmented IPv4 and IPv6 tunnel packets.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**slot**](cmdqueryname=slot) *slot-id*
     
     
     
     The slot view is displayed.
  3. Run [**load-balance hash-fields tunnel-info disable**](cmdqueryname=load-balance+hash-fields+tunnel-info+disable)
     
     
     
     The device is disabled from using tunnel information as a hash factor during hash calculation for non-fragmented IPv4 and IPv6 tunnel packets.
     
     
     
     In IPv4 and IPv6 tunnel load balancing scenarios, a device uses tunnel information as a hash factor during hash calculation for non-fragmented packets but hashes fragmented packets based only on IP addresses (3-tuple information) by default. If both fragmented and non-fragmented packets exist, different load balancing modes cause packets to be out of order. To solve this problem, run the command to disable a device from using tunnel information as a hash factor during hash calculation for non-fragmented IP tunnel packets. If the device can obtain 5-tuple information, it hashes packets based on this information. Otherwise, it hashes packets based on 3-tuple information.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Disable a device from using tunnel information as a hash factor during hash calculation for GTP tunnel packets.
  
  
  
  In an ESQM scenario, GTP packets are balanced based on tunnel IDs by default. GTP heartbeat packets and data packets are balanced on different paths based on tunnel IDs, which causes inaccurate statistics. To resolve this issue, disable the device from using tunnel information as a hash factor during hash calculation for GTP packets. By default, the device performs hash calculation for GTP packets based on the 5-tuple information. In this way, GTP heartbeat packets and data packets are hashed to the same path based on the 5-tuple information, improving statistics accuracy.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**slot**](cmdqueryname=slot) *slot-id*
     
     
     
     The slot view is displayed.
  3. Run [**load-balance hash-fields tunnel-info gtp disable**](cmdqueryname=load-balance+hash-fields+tunnel-info+gtp+disable)
     
     
     
     The device is disabled from using tunnel information as a hash factor during hash calculation for GTP tunnel packets.
  4. Run [**load-balance hash-fields tunnel-info**](cmdqueryname=load-balance+hash-fields+tunnel-info) *tunnel-type* **disable**
     
     
     
     The device is disabled from using tunnel information as a hash factor during hash calculation for GTP tunnel packets.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Load balancing based on the inner IP header of GTP packets
  
  
  
  On a P node in an L3VPN, a GTP packet carries double MPLS labels and the inner IP header. Load balancing is typically performed based on the outer IP header's source and destination IP addresses and the tunnel endpoint identifier (TEID). However, because the source and destination IP addresses of the inner IP header change frequently but those of the outer IP header do not, load balancing is uneven. To address this problem, run the command to enable load balancing for GTP packets carrying the inner IP header based on the inner IP header's source and destination IP addresses and the TEID. If the inner IP header is completely present in the packet window, this header and the TEID are obtained for hash calculation. If the inner IP header is not completely present in the packet window and deep hash is not configured, the outer IP header and TEID are obtained according to the original process for hash calculation. If the inner IP header is not completely present in the packet window and deep hash is configured, the packet window is moved to obtain the inner IP header and TEID for hash calculation.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**slot**](cmdqueryname=slot) *slot-id*
     
     
     
     The slot view is displayed.
  3. Run [**load-balance hash-fields gtp-inner-ip enable**](cmdqueryname=load-balance+hash-fields+gtp-inner-ip+enable)
     
     
     
     Load balancing based on GTP inner IP packets is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Load balancing based on inner SRv6 packets
  
  
  
  In a public network IP over SRv6 BE, public network IP over SRv6 TE Policy, private network IP over SRv6 BE, or private network IP over SRv6 TE Policy load balancing scenario, a P node does not consider inner IP information when performing hash calculation for SRv6 packets by default. After the [**load-balance hash-fields tunnel-inner-ip enable**](cmdqueryname=load-balance+hash-fields+tunnel-inner-ip+enable) command is run, the inner SRv6 packet information can be mapped to the FlowLabel values of outer IPv6 packets, and the P node performs load balancing based on the new FlowLabel hash factors.
  
  In an IPv4 over SRv6 BE or IPv4 over SRv6 TE Policy load balancing scenario, load balancing is performed based on inner packets only when inner IPv4 packets carry GTP, 6over4, GRE, L2TP and 4over4 information. In IPv6 over SRv6 BE or IPv6 over SRv6 TE Policy load balancing scenarios, load balancing is performed based on inner packets only when inner IPv6 packets carry GTP information.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**slot**](cmdqueryname=slot) *slot-id*
     
     
     
     The slot view is displayed.
  3. Run [**load-balance hash-fields tunnel-inner-ip enable**](cmdqueryname=load-balance+hash-fields+tunnel-inner-ip+enable)
     
     
     
     Load balancing based on inner SRv6 packets is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Load balancing for PPPoE packets
  
  
  
  To load-balance PPPoE packets based on 2-tuple or 5-tuple information in the inner IP and TCP/UDP headers of the packets, enable a device to identify the IP headers of the PPPoE packets during load balancing.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**slot**](cmdqueryname=slot) *slot-id*
     
     
     
     The slot view is displayed.
  3. Run [**load-balance identify pppoe**](cmdqueryname=load-balance+identify+pppoe)
     
     
     
     The device is enabled to identify the IP headers of PPPoE packets during load balancing.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.