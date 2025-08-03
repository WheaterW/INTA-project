(Optional) Configuring MAC Addresses for L2VE and L3VE Interfaces
=================================================================

When the MAC address of an L2VE or L3VE interface conflicts with the MAC address of another type of interface, you can change the MAC address of the L2VE or L3VE interface to allow normal communication.

#### Context

Perform the following steps on each NPE.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
3. Run [**set l2ve-mac**](cmdqueryname=set+l2ve-mac) *mac-address*
   
   
   
   The MAC address of an L2VE interface is configured.
   
   You can modify the MAC address of an L2VE interface on an NPE if this MAC address is the same as that of the UPE interface that connects to the NPE. An L2VE interface has only one MAC address.
4. Run [**set access-ve-mac**](cmdqueryname=set+access-ve-mac) *mac-address*
   
   
   
   The MAC address of an L3VE interface is configured.
   
   When an L2VE interface is in the same BD as a sub-interface of an Eth-Trunk or portswitch interface and this sub-interface needs to communicate with an L3VE interface at Layer 3, you can change the MAC address of the L3VE interface to prevent the packets that are supposed to be sent to the L3VE interface from being discarded on a Layer 2 interface. This is because both the L3VE interface and the portswitch or Eth-Trunk interface use a bridge MAC address as their MAC address. An L3VE interface has only one MAC address.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.