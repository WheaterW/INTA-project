Configuring Remote Loopback
===========================

You can configure remote loopback to locate remote faults and test link quality. Perform the following steps on the device on which an interface in active mode resides:

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The view of the interface in active mode is displayed.
3. Run [**efm loopback**](cmdqueryname=efm+loopback) **start** [ **timeout** *timeout* ]
   
   
   
   The interface is configured to initiate EFM OAM remote loopback.
   
   
   
   Remote loopback can be performed only when the EFM OAM statuses of the local and remote interfaces are Detect and the EFM OAM working mode of the local interface is active. You can run the [**display efm session**](cmdqueryname=display+efm+session) { **all** | **interface** *interface-type* *interface-number* } command to check whether the EFM OAM statuses of the local and remote interfaces are Detect. You can run the [**display efm**](cmdqueryname=display+efm) { **all** | **interface** *interface-type* *interface-number* } command to view the EFM OAM working modes of the local and remote interfaces.
4. (Optional) Run [**efm loopback ignore-request**](cmdqueryname=efm+loopback+ignore-request)
   
   
   
   The interface is configured to ignore loopback requests from the remote interface.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.