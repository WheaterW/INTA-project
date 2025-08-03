(Optional) Associating the Sub-interface with a VLAN
====================================================

Before you configure proxy ARP between VLANs on Ethernet sub-interfaces, GE interfaces, or Eth-Trunk sub-interfaces, associate the sub-interface with a VLAN.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number* [ .*subinterface-number* ]
   
   
   
   The sub-interface view is displayed.
3. Run [**vlan-type dot1q**](cmdqueryname=vlan-type+dot1q) *vlan-id*
   
   
   
   The sub-interface is associated with a VLAN.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.