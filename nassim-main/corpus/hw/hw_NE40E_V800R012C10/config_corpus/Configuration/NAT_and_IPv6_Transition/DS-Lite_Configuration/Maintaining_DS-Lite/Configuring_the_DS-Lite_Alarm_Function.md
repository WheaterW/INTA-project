Configuring the DS-Lite Alarm Function
======================================

You can configure the DS-Lite alarm function to strengthen the device administrator's capability to monitor DS-Lite services in real time.

#### Context

DS-Lite sessions and ports available are important resources for DS-Lite services. If these resources are exhausted, DS-Lite cannot be performed for traffic sent by newly logged-in users. Therefore, the usage of these resources must be properly monitored. The DS-Lite alarm function generates an alarm when the resource usage reaches a certain extent, notifying the customer of the necessity to implement capacity expansion or service adjustment.


#### Procedure

* Configure the maximum number of alarm packets that a service board is allowed to send every second.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**nat alarm rate**](cmdqueryname=nat+alarm+rate) *threshold-value*
     
     
     
     The maximum number of alarm packets that the service board sends every second is set.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a device to generate an alarm when the number of sessions on a service board reaches a specified alarm threshold.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. (Optional) Run [**undo nat alarm session-number**](cmdqueryname=undo+nat+alarm+session-number) { **log** | **trap** } **disable**
     
     
     
     The trap and log functions for the number of NAT sessions are disabled.
  3. Run [**nat alarm session-number threshold**](cmdqueryname=nat+alarm+session-number+threshold) *threshold-value*
     
     
     
     An alarm threshold for the total number of sessions on a service board is configured.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Enable a device to generate an alarm when the number of used ports in a DS-Lite PAT address pool exceeds a configured threshold.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* [ **id** *id* ]
     
     
     
     The DS-Lite instance view is displayed.
  3. (Optional) Run [**ds-lite alarm port-number**](cmdqueryname=ds-lite+alarm+port-number) { **log** | **trap** } **address-group disable**
     
     
     
     The log and alarm functions for the port usage of a public IP address pool are disabled.
  4. Run [**ds-lite alarm address-group port-number threshold**](cmdqueryname=ds-lite+alarm+address-group+port-number+threshold) *threshold-value*
     
     
     
     An alarm threshold is set for the port usage rate of a DS-Lite address pool.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The PAT address pool does not support alarms based on a single IP address.
     
     Port usage of a DS-Lite PAT address pool = Number of ports used by the public network addresses in the PAT address pool/Total number of ports available for the public network addresses in the PAT address pool
* Enable the device to generate an alarm when the number of ports used by a DS-Lite user exceeds a configured threshold.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* [ **id** *id* ]
     
     
     
     The DS-Lite instance view is displayed.
  3. (Optional) Run [**ds-lite alarm port-number**](cmdqueryname=ds-lite+alarm+port-number) [ **log** | **trap** ] **user enable**
     
     
     
     The log or trap function for user port usage is enabled.
  4. Run [**ds-lite alarm user port-number threshold**](cmdqueryname=ds-lite+alarm+user+port-number+threshold) *alarm-threshold-value*
     
     
     
     An alarm threshold for user-based port usage is set.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The number of user-specific pre-allocated ports is equal to the number of ports configured using the [**port-range**](cmdqueryname=port-range) command in the DS-Lite instance view. Usage of user-specific ports is equal to the number of user-specific ports in use divided by the number of user-specific pre-allocated ports. The [**ds-lite alarm user port-number threshold**](cmdqueryname=ds-lite+alarm+user+port-number+threshold) command takes effect only after the [**port-range**](cmdqueryname=port-range) command is run in the DS-Lite instance view. If the usage of user-specific ports is greater than the corresponding alarm threshold value (80% by default), an alarm indicating that the usage of user-specific ports exceeds the threshold is generated.
* Configure an alarm threshold for the pre-allocation rate of reserved PCP ports in scenarios where a RADIUS authentication user with Huawei proprietary attributes 162 and 163 requests to go online in a DS-Lite instance. 
  
  
  
  Pre-allocation rate of reserved PCP ports in scenarios where a RADIUS authentication user with Huawei proprietary attributes 162 and 163 requests to go online in a DS-Lite instance = Number of PCP ports pre-allocated to this user in the DS-Lite instance/Number of available reserved PCP ports of all public IP addresses in the DS-Lite address pool
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* [ **id** *id* ]
     
     
     
     The DS-Lite instance view is displayed.
  3. (Optional) Run **undo** [**ds-lite alarm port-number**](cmdqueryname=ds-lite+alarm+port-number) { **log** | **trap** } **pcp-reservation disable**
     
     
     
     The log or trap function is enabled for the pre-allocation usage rate of the reserved PCP ports in scenarios where a RADIUS authentication user with Huawei proprietary attributes 162 and 163 requests to go online in the DS-Lite instance. The log and trap functions are enabled by default.
  4. Run [**ds-lite alarm pcp-reservation port-number threshold**](cmdqueryname=ds-lite+alarm+pcp-reservation+port-number+threshold) *threshold-value*
     
     
     
     An alarm threshold is specified for the pre-allocation usage rate of reserved PCP ports in scenarios where a RADIUS authentication user with Huawei proprietary attributes 162 and 163 requests to go online in the DS-Lite instance.
     
     
     
     In a distributed DS-Lite scenario, when a RADIUS authentication user with Huawei proprietary attributes 162 and 163 requests to go online, PCP ports are pre-allocated to the user from a reserved PCP port range. If the usage rate of the reserved PCP ports is high, the PCP user may fail to go online. If the alarm function for the usage rate of the reserved PCP ports is enabled and the usage rate reaches the threshold, an alarm is reported. A proper threshold provides effective monitoring.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the device to generate an alarm when server mapping entry usage exceeds a specified threshold.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. (Optional) Run [**nat alarm server-map**](cmdqueryname=nat+alarm+server-map) [ **log** | **trap** ] **disable**
     
     
     
     The log and trap functions for server mapping entries are disabled.
     
     
     
     The log and trap functions are enabled by default. To disable the functions, run the [**nat alarm server-map disable**](cmdqueryname=nat+alarm+server-map+disable) command.
  3. Run [**nat alarm server-map threshold**](cmdqueryname=nat+alarm+server-map+threshold) *threshold-value*
     
     
     
     The alarm threshold for the usage of server mapping entries is set.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Run the [**display nat memory-usage servermap**](cmdqueryname=display+nat+memory-usage+servermap) command to query the number of used server mapping entries and the number of supported server mapping entries. Server mapping entry usage rate = Number of used server mapping entries/Number of server mapping entries supported by the service board