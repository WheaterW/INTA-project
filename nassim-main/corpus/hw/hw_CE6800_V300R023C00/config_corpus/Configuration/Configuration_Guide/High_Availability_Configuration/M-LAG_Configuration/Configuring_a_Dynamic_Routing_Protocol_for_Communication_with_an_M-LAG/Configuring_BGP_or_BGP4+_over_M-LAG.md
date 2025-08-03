Configuring BGP or BGP4+ over M-LAG
===================================

Configuring BGP or BGP4+ over M-LAG

#### Prerequisites

Before configuring BGP or BGP4+ over M-LAG, you have completed the following tasks:

* Establish an M-LAG and a BGP or BGP4+ network.
* Add M-LAG member interfaces to the corresponding VLAN.
* Enable BGP or BGP4+ on the user-side device.

#### Context

![](../public_sys-resources/note_3.0-en-us.png) 

BGP or BGP4+ over M-LAG can be configured only for an M-LAG in dual-active mode. The active/standby mode and BGP or BGP4+ over M-LAG are mutually exclusive.

For the CE6820H, CE6820H-K, and CE6820S: VXLAN-related configurations are not supported.

For the CE6885-LL (low latency mode): VXLAN and IPv6-related configurations are not supported.

On the network shown in [Figure 1](#EN-US_TASK_0000001512689674__fig1098641724019), DeviceC (a user-side device) is dual-homed to an M-LAG and has a small number of static routes configured so that it can communicate with the M-LAG through Layer 3 routes. However, the network using static routes is difficult to configure and maintain and is lack of flexible and fast deployment capabilities, thereby cannot meet the requirements of rapidly growing services. To address this problem, M-LAG master and backup devices need to establish neighbor relationships of dynamic routing protocols with the user-side device. Therefore, M-LAG member interfaces need to support dynamic routing protocols.

**Figure 1** Configuring BGP over M-LAG  
![](figure/en-us_image_0000001563769357.png)

In the scenario where a device is dual-homed to a BGP or BGP4+ network through an M-LAG, you must configure IP addresses for VLANIF or VBDIF interfaces corresponding to M-LAG member interfaces on M-LAG master and backup devices. When configuring BGP or BGP4+, configure different M-LAG IPv4/IPv6 global/IPv6 link-local addresses for the VLANIF or VBDIF interfaces so that M-LAG master and backup devices can establish BGP or BGP4+ peer relationships with the user-side device DeviceC.


#### Procedure

* Configure BGP over M-LAG.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the VLANIF or VBDIF interface view.
     
     
     + Enter the VLANIF interface view.
       ```
       [interface](cmdqueryname=interface) vlanif vlan-id
       ```
     + Enter the VBDIF interface view.
       ```
       [interface](cmdqueryname=interface) vbdif bd-id 
       ```
  3. Configure an IP address.
     
     
     ```
     [ip address](cmdqueryname=ip+address) ip-address { mask | mask-length }
     ```
  4. Configure a virtual MAC address for the VLANIF or VBDIF interface.
     
     
     ```
     [mac-address](cmdqueryname=mac-address) mac-address
     ```
  5. Configure an M-LAG IP address.
     
     
     ```
     [m-lag ip address](cmdqueryname=m-lag+ip+address) ip-address { mask | mask-length }
     ```
     ![](../public_sys-resources/note_3.0-en-us.png) 
     + An M-LAG IPv4 address is a secondary IP address. Each VLANIF or VBDIF interface can be configured with only one M-LAG secondary IPv4 address. (Each interface can be configured with a maximum of 255 secondary IP addresses.)
     + An M-LAG secondary IPv4 address must be unique on the entire network, and cannot be the same as any secondary address on the local device or other devices on the network.
     + A multicast, broadcast, or loopback address cannot be configured as an M-LAG IPv4 address.
     + If an M-LAG secondary IPv4 address has been configured on an interface and a new M-LAG secondary IPv4 address is configured on the interface, the new address overwrites the original one.
     + An M-LAG IPv4 address can be configured on a VLANIF or VBDIF interface only after a primary address is configured on the interface, and the M-LAG IPv4 address must be on the same network segment as the primary address.
     + If you unbind a VNI from a BD and a dedicated M-LAG IPv4 address has been configured on the corresponding VBDIF interface using the **[**m-lag ip address**](cmdqueryname=m-lag+ip+address)** command, the dedicated M-LAG IPv4 address on the VBDIF interface is also deleted.
     + The **[**m-lag ip address**](cmdqueryname=m-lag+ip+address)** command can be configured on a VBDIF interface only after a VNI is bound to the corresponding BD.
     + If the [**ip address ignore primary-sub enable**](cmdqueryname=ip+address+ignore+primary-sub+enable) command is configured on the device, the **[**m-lag ip address**](cmdqueryname=m-lag+ip+address)** command cannot be configured.
     + If an M-LAG IPv4 address configured for an interface using the **[**m-lag ip address**](cmdqueryname=m-lag+ip+address)** command is the same as a primary or secondary IP address on the interface, the M-LAG IPv4 address cannot be delivered.
  6. Configure routed proxy ARP.
     
     
     + Configure routed proxy ARP on the VLANIF interface.
       ```
       [arp proxy enable](cmdqueryname=arp+proxy+enable)
       ```
     + Configure routed proxy ARP on the VBDIF interface.
       ```
       [arp-proxy local enable](cmdqueryname=arp-proxy+local+enable)
       ```![](../public_sys-resources/note_3.0-en-us.png) 
     
     When a user-side device sends an ARP request packet to the M-LAG master device, the packet is forwarded to the M-LAG backup device because of the hash operation on the Eth-Trunk interface. The M-LAG backup device detects that the destination IP address in the packet is not its IP address, and does not perform ARP packet synchronization. As a result, the user-side device cannot receive a reply packet. Therefore, routed proxy ARP needs to be configured.
  7. Exit the interface view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  8. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
  9. Enable BGP, specify the local AS number, and enter the BGP view.
     
     
     ```
     [bgp](cmdqueryname=bgp) as-number
     ```
  10. Configure a router ID for BGP.
      
      
      ```
      [router-id](cmdqueryname=router-id) ipv4-address
      ```
  11. Create a BGP peer.
      
      
      ```
      [peer](cmdqueryname=peer) ipv4-address as-number as-number
      ```
  12. Specify the source interface and source IP address used to set up a TCP connection between BGP peers.
      
      
      ```
      [peer](cmdqueryname=peer) ipv4-address [connect-interface](cmdqueryname=connect-interface) { interface-type interface-number [ ipv4-source-address ] | ipv4-source-address }
      ```
  13. Enter the BGP-IPv4 unicast address family view.
      
      
      ```
      [ipv4-family unicast](cmdqueryname=ipv4-family+unicast)
      ```
  14. Enable MP-BGP for the BGP peer so that it becomes an MP-BGP peer.
      
      
      ```
      [peer](cmdqueryname=peer) ipv4-address enable
      ```
  15. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
* Configure BGP4+ over M-LAG.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the VLANIF or VBDIF interface view.
     
     
     + Enter the VLANIF interface view.
       ```
       [interface](cmdqueryname=interface) vlanif vlan-id
       ```
     + Enter the VBDIF interface view.
       ```
       [interface](cmdqueryname=interface) vbdif bd-id 
       ```
  3. Enable IPv6 on the interface.
     
     
     ```
     [ipv6 enable](cmdqueryname=ipv6+enable)
     ```
  4. Configure the device to generate ND entries on the interface upon receipt of valid NA messages if no ND entry exists on the interface.
     
     
     ```
     [ipv6 nd na glean](cmdqueryname=ipv6+nd+na+glean)
     ```
     
     By default, the device does not generate ND entries on an interface upon receipt of valid NA messages if no ND entry exists on the interface.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     To synchronize ND entries in an M-LAG, configure the [**ipv6 nd na glean**](cmdqueryname=ipv6+nd+na+glean) command. This configuration enables the M-LAG backup device to generate ND entries upon receipt of valid NA messages if no ND entry exists. After learning the entries, the M-LAG backup device synchronizes the entries to the M-LAG master device.
  5. Configure an IPv6 address.
     
     
     ```
     [ipv6 address](cmdqueryname=ipv6+address) { ipv6-address prefix-length | ipv6-address/prefix-length }
     ```
  6. Configure a virtual MAC address for the VLANIF or VBDIF interface.
     
     
     ```
     [mac-address](cmdqueryname=mac-address) mac-address
     ```
  7. Configure an M-LAG IPv6 address.
     
     
     ```
     [m-lag ipv6 address](cmdqueryname=m-lag+ipv6+address) ipv6-address [ link-local ]
     ```
     
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     + An M-LAG IPv6 address can only be a global unicast address. An interface can be configured with only one M-LAG IPv6 address and a maximum of 16 global unicast addresses.
     + An M-LAG IPv6 address must be unique on the entire network, and cannot be the same as any IPv6 address on the local device or other devices on the network.
     + A multicast, anycast, or loopback address cannot be configured as an M-LAG IPv6 address.
     + If an M-LAG IPv6 address has been configured on an interface and a new M-LAG IPv6 address is configured on the interface, the new address overwrites the original one.
     + A link-local address cannot be configured as an M-LAG IPv6 address.
     + Before configuring an M-LAG IPv6 address for an interface, you must enable IPv6 on the interface.
     + If you unbind a VNI from a BD and a dedicated M-LAG IPv6 address has been configured on the corresponding VBDIF interface using the [**m-lag ipv6 address**](cmdqueryname=m-lag+ipv6+address) command, the dedicated M-LAG IPv6 address on the VBDIF interface is also deleted.
     + The [**m-lag ipv6 address**](cmdqueryname=m-lag+ipv6+address) command can be configured on a VBDIF interface only after a VNI is bound to the corresponding BD.
     + If an M-LAG IPv6 address configured for an interface using the [**m-lag ipv6 address**](cmdqueryname=m-lag+ipv6+address) command is the same as a primary or secondary IPv6 address on the device, the M-LAG IPv6 address cannot be delivered.
     + When an IPv6 address is configured using the [**m-lag ipv6 address**](cmdqueryname=m-lag+ipv6+address) command, the prefix of the specified IPv6 address cannot be FE80::/10. When an IPv6 address is configured using the [**m-lag ipv6 address link-local**](cmdqueryname=m-lag+ipv6+address+link-local) command, the prefix of the specified IPv6 address must match FE80::/10.
     ![](../public_sys-resources/note_3.0-en-us.png) 
     + The M-LAG link-local address on an interface references the link-local address of the interface. Each interface can be configured with only one M-LAG link-local address.
     + The M-LAG link-local address cannot be the same as any link-local address on the local or peer M-LAG member device.
     + Before configuring an M-LAG link-local address for an interface, you must enable IPv6 on the interface.
     + If you unbind a VNI from a BD and a dedicated M-LAG IPv6 link-local address has been configured on the corresponding VBDIF interface using the [**m-lag ipv6 address link-local**](cmdqueryname=m-lag+ipv6+address+link-local) command, the dedicated M-LAG IPv6 link-local address on the VBDIF interface is also deleted.
     + The [**m-lag ipv6 address link-local**](cmdqueryname=m-lag+ipv6+address+link-local) command can be configured on a VBDIF interface only after a VNI is bound to the corresponding BD.
     + If an M-LAG IPv6 link-local address configured for an interface using the [**m-lag ipv6 address link-local**](cmdqueryname=m-lag+ipv6+address+link-local) command is the same as a primary or secondary IPv6 address on the interface, the M-LAG IPv6 link-local address cannot be delivered.
     + If the [**ipv6 address link-local**](cmdqueryname=ipv6+address+link-local) command is configured on an interface, the [**m-lag ipv6 address link-local**](cmdqueryname=m-lag+ipv6+address+link-local) command cannot be configured on the interface.
     + On a device, all VLANIF or VBDIF interfaces bound to the same VPN instance cannot be configured with the same M-LAG link-local address. If Layer 3 interfaces on M-LAG master and backup devices are bound to the same VPN instance, the link-local address of the Layer 3 interface on the local M-LAG device cannot be the same as the M-LAG link-local address configured on the peer M-LAG device.
     + The M-LAG link-local address on an interface of a device cannot be the same as the VRRP6 link-local address on the interface.
  8. Configure routed proxy ND.
     
     
     ```
     [ipv6 nd proxy route enable](cmdqueryname=ipv6+nd+proxy+route+enable) [[](cmdqueryname=%5B)[prune](cmdqueryname=prune)[]](cmdqueryname=%5D)
     ```
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     When a user-side device sends an ND request packet to the M-LAG master device, the packet is forwarded to the M-LAG backup device because of the hash operation on the Eth-Trunk interface. The M-LAG backup device detects that the destination IP address in the packet is not its IP address, and does not perform ND packet synchronization. As a result, the user-side device cannot receive a reply packet. Therefore, routed proxy ND needs to be configured.
     
     If the interface that receives NS packets from the user side is the same as the next-hop interface of the route on the M-LAG device when the **[**ipv6 nd proxy route enable**](cmdqueryname=ipv6+nd+proxy+route+enable) **prune**** command is configured, the M-LAG device does not perform routed proxy or reply with NA packets.
  9. Exit the interface view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  10. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
  11. Enable BGP, specify the local AS number, and enter the BGP view.
      
      
      ```
      [bgp](cmdqueryname=bgp) as-number
      ```
  12. Configure a router ID for BGP.
      
      
      ```
      [router-id](cmdqueryname=router-id) ipv4-address
      ```
  13. Create a BGP peer.
      
      
      ```
      [peer](cmdqueryname=peer) ipv6-address [as-number](cmdqueryname=as-number) as-number
      ```
  14. Specify the source interface and source IP address used to set up a TCP connection between BGP peers.
      
      
      ```
      [peer](cmdqueryname=peer) ipv6-address [connect-interface](cmdqueryname=connect-interface) { interface-type interface-number [ ipv6-source-address ] | ipv6-source-address }
      ```
  15. Enter the BGP-IPv6 unicast address family view.
      
      
      ```
      [ipv6-family unicast](cmdqueryname=ipv6-family+unicast)
      ```
  16. Enable MP-BGP for the BGP peer so that it becomes an MP-BGP peer.
      
      
      ```
      [peer](cmdqueryname=peer) peerIpv6Addr [enable](cmdqueryname=enable)
      ```
  17. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```