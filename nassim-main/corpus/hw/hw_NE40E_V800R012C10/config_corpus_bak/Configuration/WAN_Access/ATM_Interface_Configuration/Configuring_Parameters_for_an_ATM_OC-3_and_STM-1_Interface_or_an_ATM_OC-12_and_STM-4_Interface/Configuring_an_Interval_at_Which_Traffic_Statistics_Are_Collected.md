Configuring an Interval at Which Traffic Statistics Are Collected
=================================================================

This section describes how to configure an interval at which traffic statistics are collected on an ATM interface or on an ATM sub-interface. Note that the interval must be a multiple of 10.

#### Context

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The NE40E supports traffic statistics collection on the ATM interface and sub-interface. Before configuring the interval at which traffic statistics are collected, configure the PVC for the interface and the sub-interface so that the configured statistics interval can be applied to the PVC.

Perform the following steps on the Router:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Perform either of the following configurations as required:
   
   
   * Run [**interface atm**](cmdqueryname=interface+atm) *interface-number*
     
     The ATM interface view is displayed.
   * Run [**interface atm**](cmdqueryname=interface+atm) *interface-number.subinterface-number*
     
     The ATM sub-interface view is displayed.
3. Run [**set flow-stat interval**](cmdqueryname=set+flow-stat+interval) *interval*
   
   
   
   An interval at which traffic statistics are collected is configured.
   
   The *interval* value must be a multiple of 10.