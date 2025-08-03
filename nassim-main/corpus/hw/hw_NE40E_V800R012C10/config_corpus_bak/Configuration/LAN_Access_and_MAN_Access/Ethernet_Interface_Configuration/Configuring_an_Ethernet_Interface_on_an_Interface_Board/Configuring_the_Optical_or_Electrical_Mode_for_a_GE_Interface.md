Configuring the Optical or Electrical Mode for a GE Interface
=============================================================

In most cases, the system recognizes the interface module and therefore automatically sets the optical or electrical mode of an interface. If the system fails to recognize the interface module, configure the optical or electrical mode for an interface.

#### Context

Perform the following steps on each Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **gigabitethernet** *interface-number*
   
   
   
   The specified Ethernet interface view is displayed.
3. Run [**port-type**](cmdqueryname=port-type) { **copper** | **fiber-100** | **fiber-1000** }
   
   
   
   The interface type is configured.
   
   
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   This command can be used only on auto-sensing optical or electrical GE interfaces.
   
   If the Router recognizes the type of a Small Form-Factor Pluggable (SFP) module, the system sets the optical or electrical mode of the interface accordingly without additional configurations.
   
   If the Router does not recognize the type of an SFP module that works properly, you need to configure the working mode for the interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.