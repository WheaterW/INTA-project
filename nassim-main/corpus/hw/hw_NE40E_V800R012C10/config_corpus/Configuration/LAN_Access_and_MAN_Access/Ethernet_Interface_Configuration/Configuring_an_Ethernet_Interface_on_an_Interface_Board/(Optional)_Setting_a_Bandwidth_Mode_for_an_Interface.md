(Optional) Setting a Bandwidth Mode for an Interface
====================================================

Whether the bandwidth can be set to 1 Gbit/s/10 Gbit/s/25 Gbit/s depends on a device's hardware conditions.

#### Context

In some special scenarios where interconnected interfaces require the same bandwidth mode, you can run the [**port-mode**](cmdqueryname=port-mode) command to set the interface bandwidth.

Perform the following steps on target Routers:

If the VS mode is used, this configuration task is supported only by the admin VS.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) **interface-type** *interface-number*
   
   
   
   The specified GE interface view is displayed.
3. Set the interface's bandwidth mode.
   
   
   
   Run [**port-mode**](cmdqueryname=port-mode)
   
   A bandwidth mode is set for the GE interface.
   
   
   
   For the NE40E-M2F, this configuration is supported only by ports 4 and 5 on the CX68L4XEKGFB subcard.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.