Configuring the NAT64 Alarm Function
====================================

You can configure the NAT64 alarm function to strengthen the device administrator's capability to monitor NAT64 services in real time.

#### Context

The total number of addresses and the total number of ports available in the system are important resources of NAT64 services. If these resources are exhausted, NAT64 cannot be performed for the traffic of users just going online. Therefore, usage of these resources must be properly monitored. The NAT64 alarm function generates an alarm when the resource usage reaches a certain extent, notifying the customer of the necessity to implement capacity expansion or service adjustment.


#### Procedure

* Set the maximum number of alarm packets that a service board sends every second.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In VS mode, this configuration process is supported only by the admin VS.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**nat alarm rate**](cmdqueryname=nat+alarm+rate) *threshold-value*
     
     
     
     The maximum number of alarm packets that a service board sends every second is set.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set an alarm threshold for user tables.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In VS mode, this configuration process is supported only by the admin VS.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. (Optional) Run [**undo nat alarm user-table**](cmdqueryname=undo+nat+alarm+user-table) { **log** | **trap** } **disable**
     
     
     
     The log and trap functions of the user table are enabled.
  3. Run [**nat alarm user-table threshold**](cmdqueryname=nat+alarm+user-table+threshold) *threshold-value*
     
     
     
     An alarm threshold is set for the user tables.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set an alarm threshold for a No-PAT address pool.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**nat64 instance**](cmdqueryname=nat64+instance) *instance-name* [ **id** *id* ]
     
     
     
     The NAT64 instance view is displayed.
  3. (Optional) Run [**undo nat64 alarm port-number**](cmdqueryname=undo+nat64+alarm+port-number) { **log** | **trap** } **address-group** **disable**
     
     
     
     The log and alarm functions of port usage of a No-PAT NAT64 public IP address pool are enabled.
  4. Run [**nat64 alarm**](cmdqueryname=nat64+alarm) **address-group** **port-number** **threshold** *value*
     
     
     
     The device is enabled to generate an alarm when the number of used ports in a No-PAT NAT64 address pool exceeds a configured threshold.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the log or trap function for CPU forwarding performance on dedicated boards.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In VS mode, this configuration process is supported only by the admin VS.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. (Optional) Run [**vsm alarm cpu-performance**](cmdqueryname=vsm+alarm+cpu-performance) { **log** | **trap** } **disable**
     
     
     
     The log or trap function for CPU forwarding performance on the dedicated board is disabled.
  3. Run [**vsm alarm cpu-performance threshold**](cmdqueryname=vsm+alarm+cpu-performance+threshold) *threshold-value*
     
     
     
     An alarm threshold for CPU forwarding performance on the dedicated board is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.