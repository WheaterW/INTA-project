(Optional) Configuring BFD Packets to Be Transparently Transmitted on an Interface
==================================================================================

On a network, if a customer-side router that functions as a CE has the default BFD function enabled by using the **bfd bind peer-ip default-ip** command, the default BFD packets received by a PE are sent to the CPU instead of being transparently transmitted to the peer CE. In this case, you can adjust the forwarding mode of multicast IPv4 BFD packets on the interface and its sub-interfaces to enable the BFD packets to be transparently transmitted.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The interface view is displayed.
3. Run [**default-ip-bfd transparent-transmission enable**](cmdqueryname=default-ip-bfd+transparent-transmission+enable)
   
   
   
   Transparent transmission is configured for multicast IPv4 BFD packets on the interface and its sub-interfaces.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.