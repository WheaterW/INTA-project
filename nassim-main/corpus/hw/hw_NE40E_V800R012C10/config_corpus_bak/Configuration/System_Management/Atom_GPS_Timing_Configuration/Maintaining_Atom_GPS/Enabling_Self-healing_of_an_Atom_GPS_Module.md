Enabling Self-healing of an Atom GPS Module
===========================================

This section describes how to enable self-healing of an Atom GPS module in response to an IIC watchdog abnormality.

#### Context

After self-healing is enabled on an Atom GPS module, the Atom GPS module is automatically reset, and the SyncE and 1588v2 functions are disabled from the involved interface. After the WTR timer is expired, the SyncE and 1588v2 functions are re-enabled, and services are restored. If self-healing is not enabled, the involved device remains abnormal and waits for user processing.

Perform the following operations on the Router where the Atom GPS module houses:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**smart-clock recovery enable**](cmdqueryname=smart-clock+recovery+enable)
   
   
   
   Self-healing is enabled on the Atom GPS module.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.