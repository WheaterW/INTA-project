Disabling SRPOLICY CPU Overload Control
=======================================

On live networks, you are advised not to disable SRPOLICY CPU overload control unless otherwise required.

#### Context

If the CPU is overloaded, each module needs to take necessary measures to control the CPU usage. After receiving a CPU overload notification from the system, the SRPolicy module adjusts the processing speeds of internal operations, such as decreasing the IOB speed and delaying reconciliation, based on the CPU overload status, thereby enhancing resilience.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**segment-routing policy cpu-overload control disable**](cmdqueryname=segment-routing+policy+cpu-overload+control+disable) command to disable SRPOLICY CPU overload control.
   
   
   
   To reduce the impact of CPU overload on services, you are advised not to disable SRPOLICY CPU overload control.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.