Configuring the NAT Alarm Function
==================================

You can configure the NAT alarm function to strengthen the device administrator's capability to monitor NAT services in real time.

#### Context

NAT sessions and ports available are important resources for NAT services. If these resources are exhausted, NAT cannot be performed for traffic sent by newly logged-in users. Therefore, the usage of these resources must be properly monitored. The NAT alarm function enables a NAT device to generate an alarm when resource usage reaches a specified alarm threshold, which instructs the customer to implement capacity expansion or service adjustment.


#### Procedure

* Set a maximum number of alarm packets that a NAT service board sends every second.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In VS mode, this configuration process is supported only by the admin-VS.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**nat alarm rate**](cmdqueryname=nat+alarm+rate) *threshold-value*
     
     
     
     The maximum number of alarm packets that a NAT service board can send every second is set.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure a device to generate an alarm when the number of NAT sessions on a NAT service board reaches the alarm threshold.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In VS mode, this configuration process is supported only by the admin-VS.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. (Optional) Run [**undo nat alarm session-number**](cmdqueryname=undo+nat+alarm+session-number+log+trap+disable) { **log** | **trap** } **disable**
     
     
     
     The trap or log function for the total number of NAT sessions is enabled.
  3. Run [**nat alarm session-number threshold**](cmdqueryname=nat+alarm+session-number+threshold) *threshold-value*
     
     
     
     An alarm threshold is set for the total number of sessions on a service board.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set an alarm threshold for user tables.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In VS mode, this configuration process is supported only by the admin-VS.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. (Optional) Run [**undo nat alarm user-table**](cmdqueryname=undo+nat+alarm+user-table+log+trap+disable) { **log** | **trap** } **disable**
     
     
     
     The log or trap function is enabled for user tables.
  3. Run [**nat alarm user-table threshold**](cmdqueryname=nat+alarm+user-table+threshold) *threshold-value*
     
     
     
     An alarm threshold is configured for user tables.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set an alarm threshold for the port usage of a NAT PAT address pool.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Only the NE40E-M2K and NE40E-M2K-B support this configuration.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**nat instance**](cmdqueryname=nat+instance+id) *instance-name* [ **id** *id* ]
     
     
     
     The NAT instance view is displayed.
  3. (Optional) Run [**nat alarm port-number**](cmdqueryname=nat+alarm+port-number+log+trap+address-group+disable) { **log** | **trap** } **address-group disable**
     
     
     
     The log or trap function for the port usage of a public address pool is disabled.
  4. Run [**nat alarm address-group port-number threshold**](cmdqueryname=nat+alarm+address-group+port-number+threshold) *threshold*
     
     
     
     An alarm threshold is set for the port usage based on the NAT address pool.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The PAT address pool on a value-added service processing board does not support alarms based on a single IP address.
     
     Port usage of a NAT PAT address pool = Number of ports used by the public network addresses in the PAT address pool/Total number of ports available for the public network addresses in the PAT address pool
* Set an alarm threshold for the user-based port usage.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Only the NE40E-M2K and NE40E-M2K-B support this configuration.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**nat instance**](cmdqueryname=nat+instance+id) *instance-name* [ **id** *id* ]
     
     
     
     The NAT instance view is displayed.
  3. (Optional) Run [**nat alarm port-number**](cmdqueryname=nat+alarm+port-number+log+trap+user+enable) [ **log** | **trap** ] **user enable**
     
     
     
     The log or trap function for the port usage of users is enabled.
  4. Run [**nat alarm user port-number threshold**](cmdqueryname=nat+alarm+user+port-number+threshold) *threshold*
     
     
     
     An alarm threshold is set for the user-based port usage.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The number of user-specific pre-allocated ports is equal to the number of ports configured using the [**port-range**](cmdqueryname=port-range%EF%BC%88NAT%E5%AE%9E%E4%BE%8B%E8%A7%86%E5%9B%BE%EF%BC%89) command run in the NAT instance view. Usage of user-specific ports is equal to the number of user-specific ports in use divided by the number of user-specific pre-allocated ports. The [**nat alarm user port-number threshold**](cmdqueryname=nat+alarm+user+port-number+threshold) command takes effect only after the [**port-range**](cmdqueryname=port-range%EF%BC%88NAT%E5%AE%9E%E4%BE%8B%E8%A7%86%E5%9B%BE%EF%BC%89) command is run in the NAT instance view. If usage of user-specific ports is greater than the alarm threshold *threshold-value* (80% by default), an alarm indicating that usage of user-specific ports exceeds the threshold is generated.
* Set an alarm threshold for No-PAT address pool usage.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**nat instance**](cmdqueryname=nat+instance+id) *instance-name* [ **id** *id* ]
     
     
     
     The NAT instance view is displayed.
  3. (Optional) Run [**nat alarm no-pat address-group**](cmdqueryname=nat+alarm+no-pat+address-group+log+trap+disable) { **log** | **trap** } **disable**
     
     
     
     The log or trap function is disabled for the No-PAT public address pool.
  4. Run [**nat alarm no-pat address-group threshold**](cmdqueryname=nat+alarm+no-pat+address-group+threshold) *threshold-value*
     
     
     
     An alarm threshold is set for No-PAT address pool usage.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the log or trap function for CPU forwarding performance on dedicated boards.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Only the NE40E-M2K and NE40E-M2K-B support this configuration.
  
  
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In VS mode, this configuration process is supported only by the admin-VS.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. (Optional) Run [**vsm alarm cpu-performance**](cmdqueryname=vsm+alarm+cpu-performance+log+trap+disable) { **log** | **trap** } **disable**
     
     
     
     The log or trap function is disabled for CPU forwarding performance on the dedicated board.
  3. Run [**vsm alarm cpu-performance threshold**](cmdqueryname=vsm+alarm+cpu-performance+threshold) *threshold-value*
     
     
     
     An alarm threshold is set for CPU forwarding performance on the dedicated board.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an alarm threshold for the address usage of the global static address pool.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Only the NE40E-M2K and NE40E-M2K-B support this configuration.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**nat ip-pool**](cmdqueryname=nat+ip-pool+vpn-instance+no-pat+slave) *pool-name* [ **vpn-instance** *vpn-instance-name* ] [ **no-pat** ] [ **slave** ]
     
     
     
     A global static address pool is created, and its view is displayed.
  3. (Optional) Run [**nat alarm ip**](cmdqueryname=nat+alarm+ip+log+trap+disable) { **log** | **trap** } **disable**
     
     
     
     The log or trap function for the global static address pool is disabled.
  4. Run [**nat alarm ip threshold**](cmdqueryname=nat+alarm+ip+threshold) *value*
     
     
     
     An alarm threshold for the global static address pool is configured.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the upper and lower alarm thresholds for the global static address pool usage.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Only the NE40E-M2K and NE40E-M2K-B support this configuration.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**nat ip-pool**](cmdqueryname=nat+ip-pool+vpn-instance+no-pat+slave) *pool-name* [ **vpn-instance** *vpn-instance-name* ] [ **no-pat** ] [ **slave** ]
     
     
     
     A global static address pool is created, and its view is displayed.
  3. (Optional) Run [**nat alarm ip**](cmdqueryname=nat+alarm+ip+log+trap+disable) { **log** | **trap** } **disable**
     
     
     
     The log or trap function for the global static address pool is disabled.
  4. Run [**nat-instance ip used-threshold upper-limit**](cmdqueryname=nat-instance+ip+used-threshold+upper-limit+lower-limit) *upper-value* **lower-limit** *lower-value*
     
     
     
     The upper and lower thresholds for the number of address segments in the global static address pool are set.
     
     
     
     Using the default upper limit
     and lower limit of an address segment in a global address pool is
     recommended, and the difference between *upper-value* and *lower-value* must be over 60. For example, **nat-instance ip used-threshold upper-limit 90 lower-limit 20**.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an alarm threshold for the pre-allocation rate of reserved PCP ports in scenarios where a RADIUS authentication user with Huawei proprietary attributes 162 and 163 requests to go online in a NAT instance.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Only the NE40E-M2K and NE40E-M2K-B support this configuration.
  
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Pre-allocation rate of reserved PCP ports in scenarios where a RADIUS authentication user with Huawei proprietary attributes 162 and 163 requests to go online in a NAT instance = Number of PCP ports pre-allocated to this user in the NAT instance/Number of available reserved PCP ports of all public IP addresses in the NAT address pool
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**nat instance**](cmdqueryname=nat+instance+id) *instance-name* [ **id** *id* ]
     
     
     
     The NAT instance view is displayed.
  3. (Optional) Run **undo** [**nat alarm port-number**](cmdqueryname=nat+alarm+port-number) { **log** | **trap** } **pcp-reservation disable**
     
     
     
     The log or trap function is enabled for the pre-allocation rate of the reserved PCP ports in scenarios where a RADIUS authentication user with Huawei proprietary attributes 162 and 163 requests to go online in the NAT instance. The log and tap functions are enabled by default.
  4. Run [**nat alarm pcp-reservation port-number threshold**](cmdqueryname=nat+alarm+pcp-reservation+port-number+threshold) *threshold*
     
     
     
     An alarm threshold is specified for the pre-allocation rate of reserved PCP ports in scenarios where a RADIUS authentication user with Huawei proprietary attributes 162 and 163 requests to go online in the NAT instance.
     
     
     
     In a distributed NAT scenario, when a RADIUS authentication user with Huawei proprietary attributes 162 and 163 requests to go online, PCP ports are pre-allocated to the user from a reserved PCP port range. If the pre-allocation rate of the reserved PCP ports is high, the user may fail to go online. If the alarm function for the threshold of the pre-allocation rate of the reserved PCP ports is enabled and the pre-allocation rate reaches the threshold, an alarm is reported. A proper threshold provides effective monitoring.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the device to generate an alarm when server mapping entry usage exceeds a specified threshold.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In VS mode, this configuration process is supported only by the admin-VS.
  
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. (Optional) Run [**nat alarm server-map**](cmdqueryname=nat+alarm+server-map+log+trap+disable) [ **log** | **trap** ] **disable**
     
     
     
     The log or trap function for server mapping entries is disabled.
     
     By default, the log and trap functions are enabled for server mapping entries. To disable the functions, run the [**nat alarm server-map disable**](cmdqueryname=nat+alarm+server-map+disable) command.
  3. Run [**nat alarm server-map threshold**](cmdqueryname=nat+alarm+server-map+threshold) *threshold-value*
     
     
     
     An alarm threshold for the usage of server mapping entries is set.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Run the [**display nat memory-usage servermap**](cmdqueryname=display+nat+memory-usage+servermap) command to query the number of used server mapping entries and the number of server mapping entries supported by the service board. Server mapping entry usage is as follows:
     
     Server mapping entry usage = Number of used server mapping entries/Number of server mapping entries supported by the service board
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an alarm threshold for users with upstream traffic but without downstream traffic.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**nat alarm vsu-service-fault unidirectional-traffic-user**](cmdqueryname=nat+alarm+vsu-service-fault+unidirectional-traffic-user+log+trap) { **log** | **trap** } **disable**
     
     
     
     An alarm threshold is configured for users with upstream traffic but without downstream traffic.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.