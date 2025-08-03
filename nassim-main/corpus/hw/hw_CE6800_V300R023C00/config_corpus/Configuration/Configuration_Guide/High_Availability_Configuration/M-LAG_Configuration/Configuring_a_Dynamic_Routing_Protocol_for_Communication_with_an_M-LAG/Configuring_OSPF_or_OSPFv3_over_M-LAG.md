Configuring OSPF or OSPFv3 over M-LAG
=====================================

Configuring OSPF or OSPFv3 over M-LAG

#### Prerequisites

Before configuring OSPF or OSPFv3 over M-LAG, you have completed the following tasks:

* Establish an M-LAG and an OSPF or OSPFv3 network.
* Add M-LAG member interfaces to the corresponding VLAN.
* Enable OSPF or OSPFv3 on the user-side device.

#### Context

![](../public_sys-resources/note_3.0-en-us.png) 

OSPF or OSPFv3 over M-LAG can be configured only for an M-LAG in dual-active mode. The active/standby mode and OSPF or OSPFv3 over M-LAG are mutually exclusive.

For the CE6820H, CE6820H-K, and CE6820S: VXLAN-related configurations are not supported.

For the CE6885-LL (low latency mode): VXLAN and IPv6-related configurations are not supported.

On the network shown in [Figure 1](#EN-US_TASK_0000001563769141__fig1098641724019), DeviceC (a user-side device) is dual-homed to an M-LAG and has a small number of static routes configured so that it can communicate with the M-LAG through Layer 3 routes. However, the network using static routes is difficult to configure and maintain and is lack of flexible and fast deployment capabilities, thereby cannot meet the requirements of rapidly growing services. To address this problem, M-LAG master and backup devices need to establish neighbor relationships of dynamic routing protocols with the user-side device. Therefore, M-LAG member interfaces need to support dynamic routing protocols.

**Figure 1** Configuring OSPF or OSPFv3 over M-LAG  
![](figure/en-us_image_0000001564009129.png)

In the scenario where a device is dual-homed to an OSPF or OSPFv3 network through an M-LAG, you must configure IP addresses for VLANIF or VBDIF interfaces corresponding to M-LAG member interfaces on M-LAG master and backup devices. When configuring OSPF or OSPFv3, configure different M-LAG IPv4/IPv6 link-local addresses for the VLANIF or VBDIF interfaces so that M-LAG master and backup devices can establish OSPF or OSPFv3 neighbor relationships with the user-side device DeviceC.

![](../public_sys-resources/note_3.0-en-us.png) 

* Topology isolation is required between the network side and the M-LAG side. You can perform one of the following configurations to implement topology isolation:
  + Deploy different dynamic routing protocols on the network side and the M-LAG side.
  + Deploy OSPF/OSPFv3 on the network side and the M-LAG side, but configure different OSPF/OSPFv3 processes on the two sides.
  + Deploy OSPF/OSPFv3 on the network side and the M-LAG side and configure the same OSPF/OSPFv3 process on the two sides, but configure different OSPF/OSPFv3 areas on the two sides.

* You are advised to configure BFD for M-LAG between M-LAG devices and the user-side device DeviceC to quickly detect link faults.
* If a VPN instance is specified when OSPF/OSPFv3 is configured, you are advised to run the **[**vpn-instance-capability simple**](cmdqueryname=vpn-instance-capability+simple)** command in the OSPF/OSPFv3 view to enable the device to directly calculate routes without conducting routing loop detection.


#### Procedure

* Configure OSPF over M-LAG.
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
  5. Configure the secondary IP address of the M-LAG member device as the source IP address.
     
     
     ```
     [ospf source sub-address](cmdqueryname=ospf+source+sub-address) ipv4-address
     ```
  6. Configure the source IP address as the M-LAG IPv4 address.
     
     
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
  7. Configure routed proxy ARP.
     
     
     + Configure routed proxy ARP on the VLANIF interface.
       ```
       [arp proxy enable](cmdqueryname=arp+proxy+enable)
       ```
     + Configure routed proxy ARP on the VBDIF interface.
       ```
       [arp-proxy local enable](cmdqueryname=arp-proxy+local+enable)
       ```![](../public_sys-resources/note_3.0-en-us.png) 
     
     When a user-side device sends an ARP request packet to the M-LAG master device, the packet is forwarded to the M-LAG backup device because of the hash operation on the Eth-Trunk interface. The M-LAG backup device detects that the destination IP address in the packet is not its IP address, and does not perform ARP packet synchronization. As a result, the user-side device cannot receive a reply packet. Therefore, routed proxy ARP needs to be configured.
  8. Exit the interface view.
     
     
     ```
     [quit](cmdqueryname=quit)
     ```
  9. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
  10. Create an OSPF process and enter the OSPF view.
      
      
      ```
      [ospf](cmdqueryname=ospf) process-id [ router-id route-id | vpn-instance vpname ] *
      ```
  11. Enter the OSPF area view.
      
      
      ```
      [area](cmdqueryname=area) area-id
      ```
  12. Configure a network segment for the area.
      
      
      ```
      [network](cmdqueryname=network) address wildcard-mask [ description text ]
      ```
  13. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
* Configure OSPFv3 over M-LAG.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create an OSPFv3 process and enter the OSPFv3 view.
     
     
     ```
     [ospfv3](cmdqueryname=ospfv3) process-id [ vpn-instance vpn-instance-name ]
     ```
  3. Configure a router ID.
     
     
     ```
     [router-id](cmdqueryname=router-id) router-id
     ```
  4. Enter the OSPFv3 area view.
     
     
     ```
     [area](cmdqueryname=area) area-id
     ```
  5. Return to the system view.
     
     
     ```
     [return](cmdqueryname=return)
     ```
  6. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
  7. Enter the VLANIF or VBDIF interface view.
     
     
     + Enter the VLANIF interface view.
       ```
       [interface](cmdqueryname=interface) vlanif vlan-id
       ```
     + Enter the VBDIF interface view.
       ```
       [interface](cmdqueryname=interface) vbdif bd-id 
       ```
  8. Enable IPv6 on the interface.
     
     
     ```
     [ipv6 enable](cmdqueryname=ipv6+enable)
     ```
  9. Configure the device to generate ND entries on the interface upon receipt of valid NA messages if no ND entry exists on the interface.
     
     
     ```
     [ipv6 nd na glean](cmdqueryname=ipv6+nd+na+glean)
     ```
     
     By default, the device does not generate ND entries on an interface upon receipt of valid NA messages if no ND entry exists on the interface.
     
     ![](../public_sys-resources/note_3.0-en-us.png) 
     
     To synchronize ND entries in an M-LAG, configure the [**ipv6 nd na glean**](cmdqueryname=ipv6+nd+na+glean) command. This configuration enables the M-LAG backup device to generate ND entries upon receipt of valid NA messages if no ND entry exists. After learning the entries, the M-LAG backup device synchronizes the entries to the M-LAG master device.
  10. Configure an IPv6 address.
      
      
      ```
      [ipv6 address](cmdqueryname=ipv6+address) { ipv6-address prefix-length | ipv6-address/prefix-length }
      ```
  11. Configure a virtual MAC address for the VLANIF or VBDIF interface.
      
      
      ```
      [mac-address](cmdqueryname=mac-address) mac-address
      ```
  12. Enable OSPFv3 on the interface.
      
      
      ```
      [ospfv3](cmdqueryname=ospfv3) process-id area area-id [ instance instance-id ]
      ```
  13. Configure the IPv6 address as the M-LAG link-local address.
      
      
      ```
      [m-lag ipv6 address](cmdqueryname=m-lag+ipv6+address) ipv6-address link-local
      ```
      ![](../public_sys-resources/note_3.0-en-us.png) 
      + Each interface can be configured with only one M-LAG link-local address. (Each interface can be configured with only one link-local address.)
      + The M-LAG link-local address cannot be the same as any link-local address on the peer M-LAG member device.
      + Before configuring an M-LAG link-local address for an interface, you must enable IPv6 on the interface.
      + If you unbind a VNI from a BD and a dedicated M-LAG IPv6 link-local address has been configured on the corresponding VBDIF interface using the [**m-lag ipv6 address link-local**](cmdqueryname=m-lag+ipv6+address+link-local) command, the dedicated M-LAG IPv6 link-local address on the VBDIF interface is also deleted.
      + The [**m-lag ipv6 address link-local**](cmdqueryname=m-lag+ipv6+address+link-local) command can be configured on a VBDIF interface only after a VNI is bound to the corresponding BD.
      + If an M-LAG IPv6 link-local address configured for an interface using the [**m-lag ipv6 address link-local**](cmdqueryname=m-lag+ipv6+address+link-local) command is the same as a primary or secondary IPv6 address on the interface, the M-LAG IPv6 link-local address cannot be delivered.
      + If the [**ipv6 address link-local**](cmdqueryname=ipv6+address+link-local) command is configured on an interface, the [**m-lag ipv6 address link-local**](cmdqueryname=m-lag+ipv6+address+link-local) command cannot be configured on the interface.
      + When an IPv6 address is configured using the [**m-lag ipv6 address link-local**](cmdqueryname=m-lag+ipv6+address+link-local) command, the prefix of the specified IPv6 address must match FE80::/10. When an IPv6 address is configured using the [**m-lag ipv6 address**](cmdqueryname=m-lag+ipv6+address) command, the prefix of the specified IPv6 address cannot be FE80::/10.
      + On a device, all VLANIF or VBDIF interfaces bound to the same VPN instance cannot be configured with the same M-LAG link-local address. If Layer 3 interfaces on M-LAG master and backup devices are bound to the same VPN instance, the link-local address of the Layer 3 interface on the local M-LAG device cannot be the same as the M-LAG link-local address configured on the peer M-LAG device.
      + The M-LAG link-local address on an interface of a device cannot be the same as the VRRP6 link-local address on the interface.
  14. Configure routed proxy ND.
      
      
      ```
      [ipv6 nd proxy route enable](cmdqueryname=ipv6+nd+proxy+route+enable) [[](cmdqueryname=%5B)[prune](cmdqueryname=prune)[]](cmdqueryname=%5D)
      ```
      ![](../public_sys-resources/note_3.0-en-us.png) 
      
      When a user-side device sends an ND request packet to the M-LAG master device, the packet is forwarded to the M-LAG backup device because of the hash operation on the Eth-Trunk interface. The M-LAG backup device detects that the destination IP address in the packet is not its IP address, and does not perform ND packet synchronization. As a result, the user-side device cannot receive a reply packet. Therefore, routed proxy ND needs to be configured.
      
      If the interface that receives NS packets from the user side is the same as the next-hop interface of the route on the M-LAG device when the **[**ipv6 nd proxy route enable**](cmdqueryname=ipv6+nd+proxy+route+enable) **prune**** command is configured, the M-LAG device does not perform routed proxy or reply with NA packets.
  15. Commit the configuration.
      
      
      ```
      [commit](cmdqueryname=commit)
      ```
  
  ![](../public_sys-resources/note_3.0-en-us.png) 
  
  If two member devices in an M-LAG need to establish a routing neighbor relationship, you are advised to manually configure router IDs on the two M-LAG devices. If the devices automatically obtain router IDs, the neighbor relationship may fail to be established due to a router ID conflict.