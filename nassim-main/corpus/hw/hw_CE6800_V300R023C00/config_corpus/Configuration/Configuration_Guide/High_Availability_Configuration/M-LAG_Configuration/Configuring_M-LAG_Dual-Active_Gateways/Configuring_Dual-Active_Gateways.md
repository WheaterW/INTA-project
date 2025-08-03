Configuring Dual-Active Gateways
================================

Configuring Dual-Active Gateways

#### Prerequisites

VLANIF interfaces have been configured on M-LAG master and backup devices, and M-LAG member interfaces have been added to the corresponding VLAN. Alternatively, VBDIF interfaces have been configured on M-LAG master and backup devices, a VXLAN VNI has been bound to the corresponding BD, and Layer 2 sub-interfaces of Eth-Trunk interfaces that function as M-LAG member interfaces have been added to the BD.


#### Context

When a server is dual-homed to a Layer 3 or VXLAN network through an M-LAG, both the M-LAG master and backup devices need to function as Layer 3 gateways. You must ensure that VLANIF or VBDIF interfaces corresponding to M-LAG member interfaces have the same IP address and MAC address. You can configure the same IP address for the VLANIF or VBDIF interfaces and run the [**mac-address**](cmdqueryname=mac-address) command to configure the same virtual MAC address for them.

If a server is dual-homed to a VXLAN network through an M-LAG and a downlink of the M-LAG fails, service traffic needs to be transmitted through the peer-link between the M-LAG member devices. Therefore, a static bypass VXLAN tunnel must be configured between the M-LAG member devices in this scenario to divert the service traffic to the peer-link.

For the CE6820H, CE6820H-K, and CE6820S: VXLAN-related configurations are not supported.

For the CE6885-LL (low latency mode): VXLAN and IPv6-related configurations are not supported.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VLANIF or VBDIF interface view.
   
   
   * Enter the VLANIF interface view.
     ```
     [interface](cmdqueryname=interface) vlanif vlan-id
     ```
   * Enter the VBDIF interface view.
     ```
     [interface](cmdqueryname=interface) vbdif bd-id
     ```
3. Configure an IP address for the interface.
   
   
   * Configure an IPv4 address.
     ```
     [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length } [ sub ]
     ```
   * Configure an IPv6 address.
     1. Enable IPv6 on the interface.
        ```
        [ipv6 enable](cmdqueryname=ipv6+enable)
        ```
     2. Configure a global unicast address for the interface.
        ```
        [ipv6 address](cmdqueryname=ipv6+address) { ipv6-address prefix-length | ipv6-address/prefix-length } [ eui-64 ]
        ```
     
     By default, no IP address is configured for an interface.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   VLANIF or VBDIF interfaces corresponding to M-LAG member interfaces of M-LAG master and backup devices must be configured with the same IP address.
4. Configure a virtual MAC address for the VLANIF or VBDIF interface.
   
   
   ```
   [mac-address](cmdqueryname=mac-address) mac-address
   ```
   By default, the MAC address of a VLANIF or VBDIF interface is the same as the system MAC address.![](../public_sys-resources/note_3.0-en-us.png) 
   
   VLANIF or VBDIF interfaces corresponding to M-LAG member interfaces of M-LAG master and backup devices must be configured with the same virtual MAC address. In addition, to simplify device MAC address management and O&M, you are advised to configure a virtual MAC address in the reserved range. The virtual MAC address is in the format of 0000-5E00-01XX or 0000-5E00-02XX.
5. (Optional) Set a delay after which the Layer 3 protocol status of the interface changes to up.
   
   
   ```
   [protocol up-delay-time](cmdqueryname=protocol+up-delay-time) time
   ```
   
   When an M-LAG member device or the peer-link recovers from a fault, a large number of ARP entries need to be synchronized in a batch. After the delay is set for an interface, the protocol status of the interface changes from down to up after ARP entries are synchronized. This prevents protocol packets from being discarded, shortens the packet loss time during link fault recovery, and improves convergence performance.
   
   By default, the delay after which the Layer 3 protocol status changes to up is 1s for a VLANIF interface and 0s for a VBDIF interface. When there are a large number of ARP entries, however, this delay needs to be longer.
   
   ![](../public_sys-resources/note_3.0-en-us.png) 
   
   After an M-LAG member device restarts or a board resets, the physical status of an interface changes to up, but the upper-layer protocol modules do not meet forwarding requirements, resulting in packet loss. To ensure switchback performance, an M-LAG member interface reports the up state after a delay of 240s by default. If a delay after which the Layer 3 protocol status changes to up is configured on the VLANIF or VBDIF interface, ensure that the delay after which an M-LAG member interface reports the up state is longer than the delay configured on the VLANIF or VBDIF interface. Otherwise, the device is triggered to learn ND entries that fail to be synchronized only when ND Miss messages are generated.
   
   To prevent spanning tree protocol flapping caused by device restart and peer-link faults and ensure switchback performance, you are advised to set the delay in reporting the up state to 30s or longer on M-LAG member interfaces.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```