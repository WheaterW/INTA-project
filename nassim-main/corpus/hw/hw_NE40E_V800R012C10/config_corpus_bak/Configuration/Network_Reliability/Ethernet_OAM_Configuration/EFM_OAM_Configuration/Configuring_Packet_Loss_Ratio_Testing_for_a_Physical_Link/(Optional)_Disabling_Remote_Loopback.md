(Optional) Disabling Remote Loopback
====================================

Remote loopback can be disabled either automatically or manually. Perform the following steps on the device on which an interface in active mode resides:

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**efm loopback**](cmdqueryname=efm+loopback) *stop*
   
   
   
   Remote loopback is disabled on the interface.
   
   After you start remote loopback, you may forget to stop remote loopback, which causes the link to fail to forward service data for a long time. To prevent this issue, remote loopback is automatically disabled after a timeout period. The timeout period of remote loopback is configurable. To disable remote loopback manually, perform this step.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.