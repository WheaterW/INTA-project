Configuring IP Services
=======================

After a VLAN tag termination sub-interface is configured, you need to configure IP services so that users can access IP services using the VLAN tag termination sub-interface.

#### Context

Sub-interfaces for VLAN tag termination cannot forward broadcast packets. They automatically discard broadcast packets they receive. To allow VLAN tag termination sub-interfaces to forward broadcast packets, run the [**arp broadcast enable**](cmdqueryname=arp+broadcast+enable) command on the sub-interfaces to enable the ARP broadcast function.

When an IP packet is sent on a VLAN tag termination sub-interface without a corresponding ARP entry, the following may occur:

* If the access device supports automatic forwarding of ARP packets, the packets are forwarded even if the ARP broadcast function is disabled on the VLAN tag termination sub-interface.
* If the access device does not support automatic forwarding of ARP packets:
  
  + The system discards the IP packet if the [**arp broadcast enable**](cmdqueryname=arp+broadcast+enable) command is not configured on the VLAN tag termination sub-interface. In this case, the route with the VLAN tag termination sub-interface as the outbound interface is considered a black hole route.
  + If the [**arp broadcast enable**](cmdqueryname=arp+broadcast+enable) command is configured on the VLAN tag termination sub-interface, the system originates a tagged ARP broadcast packet and forwards it through the VLAN tag termination sub-interface.

When you enable or disable the ARP broadcast function on a VLAN tag termination sub-interface, the routing status of the sub-interface goes Down and then Up. This may result in route flapping on the entire network.

* Configure proxy ARP
  
  Configure proxy ARP on the device. For detailed configuration, see the chapter "ARP Configuration" in the *HUAWEI NE40E-M2 series Configuration Guide - IP Services*.
* Configure DHCP
  
  Configure DHCP on the device. For detailed configuration, see the chapter "DHCP Configuration" in the *HUAWEI NE40E-M2 series Configuration Guide - IP Services*.
  
  On a large network, if terminals need to be connected to a server through another device instead of being directly connected to this server through Ethernet interfaces, configure DHCP based on a global address pool on the server, so that the terminals can dynamically obtain IP addresses from the server.
  
  DHCP relay can be configured on the VLAN tag termination sub-interface to insert tag information into Option82. The tag information provides a reference for the DHCP server in IP address allocation.
* Configure VRRP
  
  Configure VRRP on the device. For detailed configuration, see "VRRP Configuration" in the *HUAWEI NE40E-M2 series Configuration Guide - Reliability*.
  
  When a VRRP group is configured on a VLAN tag termination sub-interface, the sub-interface needs to encapsulate inner and outer VLAN tags into VRRP packets. After you enable VRRP on a VLAN tag termination sub-interface, the sub-interface encapsulates and decapsulates the VLAN tags of VRRP packets to ensure that packets can be transmitted in VLANs.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subinterface-number*
   
   
   
   The view of the VLAN tag termination sub-interface is displayed.
3. Configure a VLAN tag termination sub-interface to transmit IP services, as shown in [Table 1](#EN-US_TASK_0172363259__tab_1).
   
   
   
   **Table 1** VLAN tag termination sub-interfaces transmitting IP services
   | Service Type | VLAN Tag Termination Sub-interface | Description |
   | --- | --- | --- |
   | Proxy ARP | Run [**arp-proxy enable**](cmdqueryname=arp-proxy+enable)  Proxy ARP is enabled on the sub-interface. | - |
   | DHCP relay | 1. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* } An IP address is configured for the interface. 2. Run [**ip relay address**](cmdqueryname=ip+relay+address) *ip-address* The IP address of the DHCP server is associated with a DHCP option. 3. Run [**dhcp select relay**](cmdqueryname=dhcp+select+relay) DHCP relay is enabled. | - |
   | VRRP | * Run [**dot1q vrrp**](cmdqueryname=dot1q+vrrp)  VRRP is enabled on the dot1q VLAN tag termination sub-interface. * Run [**qinq vrrp**](cmdqueryname=qinq+vrrp)  VRRP is enabled on the QinQ VLAN tag termination sub-interface. | When you configure VRRP and static ARP on the dot1q VLAN tag termination sub-interface, the QinQ VLAN tag termination sub-interface, or the VLANIF interface, note the following:  * Do not configure the IP address that matches the static ARP entry on the interface as the VRRP virtual address. * Do not configure the virtual address of the VRRP group where the interface resides as the IP address matching the static ARP entry on the interface. Otherwise, incorrect host routes are generated. This affects packet forwarding between devices. |
4. (Optional) Run [**arp broadcast enable**](cmdqueryname=arp+broadcast+enable)
   
   
   
   ARP broadcast is enabled on the VLAN tag termination sub-interface.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.