Resetting an Atom GNSS Module
=============================

This section describes how to reset an Atom GNSS module.

#### Context

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

After the Atom GNSS module is reset, the clock source is switched or the clock enters the holdover state. After the module is locked again, the device can trace the module again.

Perform the following operations on the Router where the Atom GNSS module resides:


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
3. Run the [**reset smart-clock**](cmdqueryname=reset+smart-clock) command to reset the Atom GNSS module on the interface.