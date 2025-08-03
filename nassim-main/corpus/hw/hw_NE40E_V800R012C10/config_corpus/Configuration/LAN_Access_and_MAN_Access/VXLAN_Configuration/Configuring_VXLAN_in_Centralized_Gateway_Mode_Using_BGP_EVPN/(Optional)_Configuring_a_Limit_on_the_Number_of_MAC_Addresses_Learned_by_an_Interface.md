(Optional) Configuring a Limit on the Number of MAC Addresses Learned by an Interface
=====================================================================================

MAC address learning limiting helps improve VXLAN network security.

#### Context

Configure the maximum number of MAC addresses that a device can learn to limit the number of access users and defend against attacks on MAC address tables. If the device has learned the maximum, no more addresses can be learned. However, you can also configure the device to discard packets after learning the maximum allowed number of MAC addresses, improving network security.

Disable MAC address learning for a BD if a Layer 3 VXLAN gateway does not need to learn MAC addresses of packets in the BD, reducing the number of MAC address entries. You can also disable MAC address learning on Layer 2 gateways after the VXLAN network topology becomes stable and MAC address learning is complete.

MAC address learning can be limited only on Layer 2 VXLAN gateways and can be disabled on both Layer 2 and Layer 3 VXLAN gateways.


#### Procedure

* Limit MAC address learning.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
     
     The BD view is displayed.
  3. Run [**mac-limit**](cmdqueryname=mac-limit) { **action** { **discard** | **forward** } | **maximum** *max* [ **rate** *interval* ] } \*
     
     A MAC address learning limit rule is configured.
  4. (Optional) Run [**mac-limit**](cmdqueryname=mac-limit) **up-threshold** *up-threshold* **down-threshold** *down-threshold*
     
     The threshold percentages for MAC address limit alarm generation and clearing are configured.
  5. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Disable MAC address learning.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**bridge-domain**](cmdqueryname=bridge-domain) *bd-id*
     
     The BD view is displayed.
  3. Run [**mac-address learning disable**](cmdqueryname=mac-address+learning+disable)
     
     MAC address learning is disabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.