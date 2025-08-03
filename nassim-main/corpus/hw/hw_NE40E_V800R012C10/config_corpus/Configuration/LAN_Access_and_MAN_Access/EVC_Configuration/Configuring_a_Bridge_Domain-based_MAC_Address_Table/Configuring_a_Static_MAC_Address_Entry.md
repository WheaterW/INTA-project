Configuring a Static MAC Address Entry
======================================

On a network with unchanged users or a device is connected to an important server, to prevent hacker attacks on devices or the server, a static MAC address can be configured and added to a MAC address table.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mac-address**](cmdqueryname=mac-address+bridge-domain) **static** *mac-address* { *interface-type interface-number* | *interface-name* } **bridge-domain** *bd-id* { **untag** | **default** | **vid** *pe-vid* [ **ce-vid** { *ce-vid* | **default** } ] }
   
   
   
   A BD-based static MAC address entry is configured.
   
   
   
   * If the encapsulation type on the involved EVC Layer 2 sub-interface is default, specify **default** in this step.
   * If the encapsulation type on the involved EVC Layer 2 sub-interface is dot1q, specify **vid** *pe-vid* in this step.
   * If the encapsulation type on the involved EVC Layer 2 sub-interface is qinq, specify **vid** *pe-vid* **ce-vid** { *ce-vid* | **default** } in this step.
   * If the encapsulation type on the involved EVC Layer 2 sub-interface is untag, specify **untag** in this step.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.