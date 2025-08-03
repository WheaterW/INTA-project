Configuring the Global MAC Hopping-based Loop Detection Alarm Function
======================================================================

To allow network administrators to promptly detect that a loop has occurred in a forwarding domain, configure the global MAC hopping-based loop detection alarm function. If a loop occurs, an alarm will be generated.

#### Context

Generally, redundant
links are used on an Ethernet switching network to provide link backup
and enhance network reliability. The use of redundant links, however,
may produce loops and cause broadcast storms and MAC address hopping.
As a result, the communication quality deteriorates, and communication
may even be interrupted. To resolve the loop problem, the global MAC
hopping-based loop detection alarm function must be configured.

In VS mode, this configuration task is supported only by the admin VS.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

If a forwarding domain has had the MAC flapping-based loop detection alarm function configured, this configuration takes precedence over that configured in the system view. For example, if the MAC flapping-based loop detection alarm function has been configured in the BD view, this function takes effect, irrespective of whether this function is configured in the system view.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**loop-detect eth-loop**](cmdqueryname=loop-detect+eth-loop) **loop-times** *loop-times* **detect-cycle** *detect-cycle-time* **cycles** *cycles*
   
   
   
   MAC hopping-based loop detection alarm parameters are configured globally.
3. (Optional) Run [**loop-detect eth-loop alarm disable**](cmdqueryname=loop-detect+eth-loop+alarm+disable)
   
   
   
   The global MAC hopping-based loop detection alarm function is disabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.