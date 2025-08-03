Binding a VT to an Interface
============================

Bind a VT to an interface so that data on the interface can be transmitted based on parameters defined in the VT.

#### Context

After configuring a VT, bind it to an interface. The type of the interface to which a VT is bound varies depending on the user access type.

* The VT configured for PPPoE services must be bound to an interface.
* The VT configured for PPPoEoVLAN services must be bound to a sub-interface.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [. *subinterface-number* ]
   
   
   
   The interface or sub-interface view is displayed.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Specify an interface for PPPoE access users or a sub-interface for PPPoEoVLAN access users.
3. Run [**pppoe-server bind**](cmdqueryname=pppoe-server+bind) **virtual-template** *virtual-template-number*
   
   
   
   A VT is bound to the interface or sub-interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.