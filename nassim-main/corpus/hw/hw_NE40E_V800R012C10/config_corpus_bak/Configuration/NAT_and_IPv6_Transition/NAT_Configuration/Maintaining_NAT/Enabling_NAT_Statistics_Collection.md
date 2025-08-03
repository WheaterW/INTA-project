Enabling NAT Statistics Collection
==================================

Before checking the usage of IP addresses in an address pool and the number of packets and bytes matching ACL rules in the traffic diversion policy on the outbound interface, enable the NAT statistics collection function. Perform the following steps on the NE40E:

#### Procedure

* Enable collection of NAT forwarding payload statistics in the system view.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Only the NE40E-M2K and NE40E-M2K-B support this configuration.
  
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In VS mode, this configuration process is supported only by the admin-VS.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**nat statistics payload**](cmdqueryname=nat+statistics+payload+slot+enable) **slot** *slot-id* **enable**
     
     Collection of NAT forwarding payload statistics is enabled. After this function is enabled, the average and maximum values of the outbound and inbound forwarding payloads on the service board can be obtained.
     
     After this function is enabled, the system samples packets every 10 minutes and records the data collected within the last 72 hours. To check the NAT forwarding payload statistics, run the [**display nat statistics payload**](cmdqueryname=display+nat+statistics+payload) command.
  3. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Enable collection of NAT forwarding payload statistics in the NAT instance view.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Only the NE40E-M2K and NE40E-M2K-B support this configuration.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**nat instance**](cmdqueryname=nat+instance+id) *instance-name* [ **id** *id* ]
     
     The NAT instance view is displayed.
  3. Run [**nat statistics payload enable**](cmdqueryname=nat+statistics+payload+enable)
     
     Collection of NAT forwarding payload statistics is enabled.
     
     After this function is enabled, the system samples packets every 10 minutes and records the data collected within the last 72 hours. To check the NAT forwarding payload statistics, run the [**display nat statistics payload**](cmdqueryname=display+nat+statistics+payload) command.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Enable the NAT statistics collection function.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**nat instance**](cmdqueryname=nat+instance+id) *instance-name* [ **id** *id* ]
     
     The NAT instance view is displayed.
  3. Run [**nat statistics**](cmdqueryname=nat+statistics+address-pool-usage+enable) { **port-usage** | **session-usage** | **address-pool-usage** } **enable**
     
     The NAT statistics collection function is enabled.
     
     After running this command, wait for 10 minutes before running the [**display nat statistics**](cmdqueryname=display+nat+statistics) command to check statistics.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The **port-usage** and **session-usage** parameters are supported only on the NE40E-M2K and NE40E-M2K-B.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.