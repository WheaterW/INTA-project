(Optional) Enabling IP Multicast VPN
====================================

Specifying a board for centralized multicast VPN service processing is a prerequisite for implementing centralized multicast VPN.

#### Context

Perform the following steps on a PE:

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If distributed multicast VPN service processing is configured, the following steps are not required.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**multicast-vpn slot**](cmdqueryname=multicast-vpn+slot) *slot-id*
   
   
   
   A board is specified for centralized multicast VPN service processing.
   
   
   
   A device supports two multicast VPN service processing modes: distributed and centralized.
   * Distributed mode: interface boards support the complete multicast VPN function and therefore can independently implement multicast VPN packet forwarding.
   * Centralized mode: For the interface boards that do not support the multicast VPN function, they send multicast VPN packets to a specific board for processing. The device does not have interface boards that do not support the distributed mode.
   
   In centralized mode, you must run the **multicast-vpn** **slot** command to specify a board for multicast VPN services. In the case of trunk interfaces, a board supports centralized multicast VPN but does not support distributed multicast VPN.