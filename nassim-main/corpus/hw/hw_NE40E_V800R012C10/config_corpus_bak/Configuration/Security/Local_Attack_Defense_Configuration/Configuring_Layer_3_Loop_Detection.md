Configuring Layer 3 Loop Detection
==================================

Layer 3 loop detection reports traps when detecting a routing loop so that you can take rapid measures to ensure proper service running.

#### Usage Scenario

The Layer 3 loop detection function detects whether a loop exists on a network. If a routing loop is detected, the device generates reports a trap.

Perform the following operations when no routing loop trap information is required.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

To ensure network reliability, exercise caution when running the [**l3-loop-detect**](cmdqueryname=l3-loop-detect+disable) **disable** command.

In VS mode, this feature is supported only by the admin VS.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**l3-loop-detect**](cmdqueryname=l3-loop-detect+disable) **disable**
   
   
   
   Layer 3 loop detection is disabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.