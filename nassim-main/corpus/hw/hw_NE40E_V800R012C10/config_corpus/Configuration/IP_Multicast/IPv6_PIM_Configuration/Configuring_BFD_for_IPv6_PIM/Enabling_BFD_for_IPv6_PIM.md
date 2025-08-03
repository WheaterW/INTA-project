Enabling BFD for IPv6 PIM
=========================

BFD detection responds to the fault occurring on the current Designated router (DR) or Assert winner on the shared network segment and instructs the PIM to trigger a new DR or Assert election. This shortens the period during which multicast data transmission is discontinued.

#### Context

Perform the following steps on the Routers that have set up a PIM neighbor relationship:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   PIM BFD applies only to non-broadcast multiple access (NBMA) and broadcast interfaces, not Point-to-point (P2P) interfaces.
3. Run [**pim ipv6 sm**](cmdqueryname=pim+ipv6+sm)
   
   
   
   IPv6 PIM-SM is enabled.
4. Run [**pim ipv6 bfd enable**](cmdqueryname=pim+ipv6+bfd+enable)
   
   
   
   IPv6 BFD for PIM is enabled.