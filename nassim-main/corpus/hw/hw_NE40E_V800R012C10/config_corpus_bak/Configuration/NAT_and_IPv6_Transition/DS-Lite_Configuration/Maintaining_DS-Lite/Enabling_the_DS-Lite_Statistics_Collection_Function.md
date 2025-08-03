Enabling the DS-Lite Statistics Collection Function
===================================================

The DS-Lite statistics collection functions help improve DS-Lite performance on a DS-Lite device.

#### Context

Perform the following steps on the NE40E:


#### Procedure

* Enable the NE40E to collect statistics about forwarded DS-Lite packets.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In VS mode, this configuration process is supported only by the admin VS.
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**nat statistics payload**](cmdqueryname=nat+statistics+payload) **slot** *slot-id* **enable**
     
     The device is enabled to collect statistics about forwarded DS-Lite packets. After this function is enabled, the average and maximum numbers of sent and received packets on service boards can be counted.
     
     After this function is enabled, the NE40E samples data every 10 minutes and records data collected within the last 72 hours. Run the [**display nat statistics payload**](cmdqueryname=display+nat+statistics+payload) command to view statistics about forwarded DS-Lite packets.
  3. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.
* Enable the DS-Lite statistics collection function.
  
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     The system view is displayed.
  2. Run [**ds-lite instance**](cmdqueryname=ds-lite+instance) *instance-name* [ **id** *id* ]
     
     The DS-Lite instance view is displayed.
  3. Run [**ds-lite statistics { port-usage | session-usage | address-pool-usage } enable**](cmdqueryname=ds-lite+statistics+%7B+port-usage+%7C+session-usage+%7C+address-pool-usage+%7D+enable)
     
     The DS-Lite statistics function is enabled.
  4. Run [**commit**](cmdqueryname=commit)
     
     The configuration is committed.