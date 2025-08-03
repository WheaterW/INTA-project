Configuring Interface Isolation for a Common VLAN
=================================================

This section describes how to configure interface isolation for a common VLAN.

#### Context

Two methods are available to configure interface isolation for a common VLAN:

* Enabling interface isolation in the interface view
* Configuring one or more interfaces as isolated interfaces in the VLAN view

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In a VLAN, isolated interfaces cannot communicate with each other at Layer 2, but can do so with non-isolated interfaces.



#### Procedure

* Enable interface isolation in the interface view.
  
  
  
  Perform the following steps on the device on which the interfaces to be isolated reside:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) { **ethernet** | **gigabitethernet** | **eth-trunk** } *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**portswitch**](cmdqueryname=portswitch)
     
     
     
     The interface is configured as a switched interface.
  4. Run [**port default vlan**](cmdqueryname=port+default+vlan) *vlan-id*
     
     
     
     The interface is added to a VLAN.
  5. Run [**port isolate-state enable vlan**](cmdqueryname=port+isolate-state+enable+vlan) { { *vlan-id1* [ **to** *vlan-id2* ] } &<1-10>}
     
     
     
     Interface isolation is enabled.
* Configure one or more interfaces as isolated interfaces in the VLAN view.
  
  
  
  Perform the following steps on the device on which the interfaces to be isolated reside:
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**vlan**](cmdqueryname=vlan) *vlan-id*
     
     
     
     The VLAN view is displayed.
  3. Run [**port isolate**](cmdqueryname=port+isolate) { { *interface-type* *interface-number* } &<1-10>| **all** }
     
     
     
     The specified interfaces are configured as isolated interfaces.