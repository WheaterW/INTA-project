Configuring Interface Isolation for an Outside VLAN in VLAN Stacking or VLAN Mapping Scenarios
==============================================================================================

This section describes how to configure interface isolation for an outside VLAN in VLAN stacking or VLAN mapping scenarios.

#### Context

Perform the following steps on a device to configure interface isolation for an outside VLAN in VLAN stacking or VLAN mapping scenarios:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) { **ethernet** | **gigabitethernet** | **eth-trunk** } *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**portswitch**](cmdqueryname=portswitch)
   
   
   
   The interface is configured as a switched interface.
4. Run [**outside-vlan port isolate**](cmdqueryname=outside-vlan+port+isolate)
   
   
   
   Interface isolation is enabled for the outside VLAN in VLAN stacking or VLAN mapping scenarios.