Configuring VPN Services
========================

After you configure the VLAN tag termination sub-interface, you need to configure VPN services so as to enable users to communicate with each other over an L2VPN or an L3VPN.

#### Context

Sub-interfaces for VLAN tag termination cannot forward broadcast packets. They automatically discard broadcast packets they receive. To allow VLAN tag termination sub-interfaces to forward broadcast packets, run the [**arp broadcast enable**](cmdqueryname=arp+broadcast+enable) command on the sub-interfaces to enable the ARP broadcast function.

When an IP packet is sent on a VLAN tag termination sub-interface without a corresponding ARP entry, the following may occur:

* If the access device supports automatic forwarding of ARP packets, the packets are forwarded even if the ARP broadcast function is disabled on the VLAN tag termination sub-interface.
* If the access device does not support automatic forwarding of ARP packets:
  
  + The system discards the IP packet if the [**arp broadcast enable**](cmdqueryname=arp+broadcast+enable) command is not configured on the VLAN tag termination sub-interface. In this case, the route with the VLAN tag termination sub-interface as the outbound interface is considered a black hole route.
  + If the [**arp broadcast enable**](cmdqueryname=arp+broadcast+enable) command is configured on the VLAN tag termination sub-interface, the system originates a tagged ARP broadcast packet and forwards it through the VLAN tag termination sub-interface.

When you enable or disable the ARP broadcast function on a VLAN tag termination sub-interface, the routing status of the sub-interface goes Down and then Up. This may result in route flapping on the entire network.

* Configure L2VPN.
  
  For configuration details, see "VPWS Configuration" and "VPLS Configuration" in *HUAWEI NE40E-M2 series Configuration Guide - VPN*.
* Configure L3VPN.
  
  For configuration details, see "BGP MPLS IP VPN Configuration" in *HUAWEI NE40E-M2 series Configuration Guide - VPN*.

Perform the following steps on the device that supports VPN services:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subinterface-number*
   
   
   
   The view of the VLAN tag termination sub-interface is displayed.
3. Configure a VLAN tag termination sub-interface to transmit VPN services, as shown in [Table 1](#EN-US_TASK_0172363269__tab_1).
   
   
   
   **Table 1** VLAN tag termination sub-interfaces transmitting VPN services
   | Service Type | VLAN Tag Termination Sub-interface | Description |
   | --- | --- | --- |
   | VPWS | Run the [**mpls l2vc**](cmdqueryname=mpls+l2vc)  [ **instance-name** *instance-name* ] { *ip-address* | **pw-template** *template-name* } \* *vc-id* [ **tunnel-policy** *policy-name* [ { **endpoint** *endpoint-address* | [ **endpoint** *endpoint4-address* ] } **color** *color-value* ] | [ **control-word** | **no-control-word** ] | [ **raw** | **tagged** | **ip-layer2** | **ip-interworking**] | **access-port** | **ignore-standby-state** ] \* command to create a VPWS connection. | * **ip-interworking** must be configured when Huawei devices interwork with each other over heterogeneous media. * **ip-layer2** must be configured when Huawei devices interwork with non-Huawei devices over heterogeneous media. |
   | VPLS | Run the [**l2 binding**](cmdqueryname=l2+binding) **vsi** *vsi-name* command to bind the VLAN tag termination sub-interface to a VSI. | - |
   | L3VPN | Run the [**ip binding vpn-instance**](cmdqueryname=ip+binding+vpn-instance) *vpn-instance-name* command to bind the VLAN tag termination sub-interface to a VPN instance. | - |
4. (Optional) Run [**arp broadcast enable**](cmdqueryname=arp+broadcast+enable)
   
   
   
   The ARP broadcast function is enabled on the VLAN tag termination sub-interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   This step takes effect only on QinQ VLAN tag termination sub-interfaces that provide L3VPN access.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.