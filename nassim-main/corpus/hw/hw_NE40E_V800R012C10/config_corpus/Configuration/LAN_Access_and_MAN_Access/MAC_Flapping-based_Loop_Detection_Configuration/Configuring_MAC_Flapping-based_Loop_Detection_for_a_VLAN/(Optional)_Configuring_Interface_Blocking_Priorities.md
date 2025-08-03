(Optional) Configuring Interface Blocking Priorities
====================================================

You can configure blocking priorities for interfaces so that a specific interface is preferentially blocked when a loop is detected.

#### Context

* MAC flapping-based loop detection has the following blocking policies:
  + Blocking interfaces based on their blocking priorities
    
    The blocking priority of an interface can be configured. When detecting a loop, a device blocks the interface with a lower blocking priority.
  + Blocking interfaces based on their trusted or untrusted states (accurate blocking)
    
    If a dynamic MAC address entry remains the same in the MAC address table within a specified period and is not deleted, the outbound interface in the MAC address entry is trusted. When detecting a loop, a device blocks an interface that is not trusted.
  
  Configure a blocking priority for a PE's interface.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number*
   
   
   
   The Ethernet interface view is displayed. The interface must be a VLAN's interface that has MAC flapping-based loop detection configured.
3. Run [**loop-detect eth-loop priority**](cmdqueryname=loop-detect+eth-loop+priority) *priority*
   
   
   
   A blocking priority is configured for the VLAN's interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.