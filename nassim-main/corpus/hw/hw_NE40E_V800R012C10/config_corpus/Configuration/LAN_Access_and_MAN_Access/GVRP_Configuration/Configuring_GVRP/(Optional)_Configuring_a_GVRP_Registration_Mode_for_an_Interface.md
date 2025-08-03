(Optional) Configuring a GVRP Registration Mode for an Interface
================================================================

(Optional) Configuring a GVRP Registration Mode for an Interface

#### Context

The following three GVRP registration modes are available on GVRP interfaces:

* Normal mode: allows a GVRP interface to register, deregister, and propagate dynamic and static VLANs.
* Fixed mode: forbids a GVRP interface to register, deregister, or propagate dynamic VLANs, but allows it to register, deregister, and propagate static VLANs. If a trunk interface is set to work in fixed mode, even if packets of all VLANs are allowed to pass, only packets in manually created VLANs actually pass through the trunk interface.
* Forbidden mode: forbids a GVRP interface to register or deregister all VLANs. If a trunk interface is set to work in forbidden mode, all VLANs are not allowed to pass.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

When the GARP timer uses the default value, the device supports a maximum of 100 dynamic VLANs. When the GARP timer uses the recommended value, the device supports a maximum of 4094 dynamic VLANs.

The GVRP function runs only on CIST instances on MSTP, and the interfaces congested by MSTP on CIST instances cannot send or receive GVRP messages.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**gvrp registration**](cmdqueryname=gvrp+registration) { **fixed** | **forbidden** | **normal** }
   
   
   
   A GVRP registration mode is configured for the interface.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Before configuring a GVRP registration mode for an interface, you must enable GVRP on the interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.