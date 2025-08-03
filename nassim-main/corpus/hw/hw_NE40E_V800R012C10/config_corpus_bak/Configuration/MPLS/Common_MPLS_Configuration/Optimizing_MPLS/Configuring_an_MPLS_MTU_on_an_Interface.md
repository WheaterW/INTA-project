Configuring an MPLS MTU on an Interface
=======================================

An MPLS MTU can be configured on an interface to determine the maximum number of bytes in an MPLS packet that an interface can forward without fragmenting the packet.

#### Context

The MPLS MTU is a forwarding plane parameter and is irrelevant to LSP establishment. The dependency between the MPLS MTU and the interface MTU is as follows:

* If no MPLS MTU is set and an interface MTU is set on an interface, the interface MTU is used.
* If an MPLS MTU and an interface MTU are set on an interface, the smaller value between the MPLS MTU and interface MTU is used.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of an MPLS-enabled interface is displayed.
3. Run [**mpls mtu**](cmdqueryname=mpls+mtu) *mtu*
   
   
   
   An MPLS MTU is set on the interface.
   
   
   
   The configured MPLS MTU takes effect immediately, and there is no need to restart the interface.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If the MPLS MTU configured using the [**mpls mtu**](cmdqueryname=mpls+mtu) command is used as the MPLS forwarding MTU, run the [**mpls path-mtu independent**](cmdqueryname=mpls+path-mtu+independent) command to allow the MPLS MTU to take effect without being affected the interface MTU. The [**mpls path-mtu independent**](cmdqueryname=mpls+path-mtu+independent) command is used when a Huawei device communicates with a non-Huawei device, which prevents low MPLS forwarding efficiency stemming from different MTU implementations.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.