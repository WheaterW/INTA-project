Configuring URPF on an Interface
================================

You can configure URPF on an interface to check packets in order to prevent source address spoofing attacks.

#### Usage Scenario

To prevent source address spoofing attacks, you can configure URPF to check the source address and inbound interface of packets. If the source address passes the check, the packets are allowed to pass; otherwise, the source address is considered forged and the packets are discarded.


#### Pre-configuration Tasks

Before configuring URPF, complete the following task:

Configure link layer protocol parameters and IP addresses for interfaces and ensure that the link layer protocol of each interface is up.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run the following commands based on the network type:
   1. On an IPv4 network, run the [**ip urpf**](cmdqueryname=ip+urpf) { **loose** | **strict** } [ **allow-default**] [ **statistics** **enable** ] command to enable URPF on the interface.
   2. On an IPv6 network, run the [**ipv6 urpf**](cmdqueryname=ipv6+urpf) { **loose** | **strict** } [ **allow-default** ] [ **statistics** **enable** ] command to enable IPv6 URPF on the interface.
   
   
   
   If **loose** is configured, URPF performs checks in loose mode. Specifically, the device searches the forwarding information base (FIB) table for the outbound interface according to the source IP address of a received packet. If the outbound interface is found, the packet is forwarded; otherwise, the packet is discarded.
   
   If **strict** is configured, URPF performs checks in strict mode. Specifically, the device searches the FIB table for the slot ID, interface number, and VLAN ID (if the packet is a VLAN packet) according to the source IP address of a received packet. It then compares them with the slot ID and interface number of the packet's inbound interface as well as the VLAN ID (if the packet is a VLAN packet) carried in the packet. If they are the same, the device considers the packet to have passed the URPF check and forwards it. Otherwise, the packet is discarded.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.