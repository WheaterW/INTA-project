Configuring a MAC Address for a Sub-interface
=============================================

Configure a MAC address for a sub-interface and bind the MAC address to a PVC to allow services to travel through a specific PVC.

#### Usage Scenario

If services are transmitted from a home gateway to a DSLAM over permanent virtual channels (PVCs), different services are mapped to different PVCs according to the unicast or multicast MAC address entries on the home gateway. If the home gateway does not learn MAC entries, it learns the outbound interface PVC based on the MAC address of network-to-user traffic. Because the sub-interfaces of the same interface have the same MAC address by default, the home gateway learns the incorrect mapping between the MAC address and PVCs. As a result, services cannot be sent to the correct PVC. To solve this problem, run the [**mac-address**](cmdqueryname=mac-address) command to configure a unique MAC address for the sub-interface. The home gateway then correctly learns the binding between MAC addresses and PVCs through different source MAC addresses, ensuring the normal transmission of services while improving network reliability.


#### Pre-configuration Tasks

Before configuring a MAC address for an Ethernet sub-interface, ensure that the VLAN to be associated with the sub-interface has been created.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* *.subinterface-number*
   
   
   
   The Ethernet sub-interface view is displayed.
3. Run [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) *vlan-id*
   
   
   
   The Ethernet sub-interface is associated with VLANs, and the VLAN encapsulation mode is configured for the Ethernet sub-interface.
4. Run [**mac-address**](cmdqueryname=mac-address) *mac-address*
   
   
   
   A MAC address is configured for the Ethernet sub-interface.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, check whether the configuration takes effect.

* Run the [**display interface**](cmdqueryname=display+interface) or [**display this interface**](cmdqueryname=display+this+interface) command to check the configured MAC address.