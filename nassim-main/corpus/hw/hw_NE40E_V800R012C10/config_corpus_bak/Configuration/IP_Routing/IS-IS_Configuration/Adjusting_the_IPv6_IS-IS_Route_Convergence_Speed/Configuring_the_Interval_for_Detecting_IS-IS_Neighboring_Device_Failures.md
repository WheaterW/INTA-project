Configuring the Interval for Detecting IS-IS Neighboring Device Failures
========================================================================

To minimize the effects caused by neighboring device failures on an IS-IS network, accelerate the speed of detecting IS-IS neighboring device failures.

#### Context

Connection status between an IS-IS device and its neighboring devices can be monitored by exchanging Hello packets at intervals. An IS-IS neighboring device is considered Down if the IS-IS device does not receive any Hello packets from the neighboring device within a specified period (holdtime). A failure in an IS-IS neighboring device will trigger LSP flooding and SPF calculation, after which IS-IS routes re-converge.

To adjust the fault detection speed, use the following methods to accelerate the speed of detecting IS-IS neighboring device failures:

* Configure the interval at which Hello packets are sent.
* Configure the number of Hello packets that are sent before the local device considers the neighbor Down.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Holdtime of neighboring devices = Interval at which Hello packets are sent x Number of Hello packets that are sent before the local device considers the neighbor Down. The maximum value of the holdtime is 65535s.
* [Configuring Dynamic IPv6 BFD for IS-IS.](dc_vrp_isis_cfg_2003.html)
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  Configuring IPv6 BFD for IS-IS is recommended because this method provides a faster fault detection speed than the other two methods.


#### Procedure

* Set an interval at which Hello packets are sent.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**isis timer hello**](cmdqueryname=isis+timer+hello) *hello-interval* [ **level-1** | **level-2** ] [ **conservative** ]
     
     
     
     The interval at which Hello packets are sent is set.
     
     
     
     If the **conservative** parameter is specified in the command, the conservative mode is enabled for the holdtime of the IS-IS neighbor relationship.
     + If the parameter is specified and the holdtime of the IS-IS neighbor relationship is less than 20s, the IS-IS neighbor relationship is disconnected when the hold time elapses.
     + If the parameter is not specified and the holdtime of the IS-IS neighbor relationship is less than 20s, the IS-IS neighbor relationship is disconnected when the period of the hold time and a delay elapses.
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     A broadcast link can transmit both Level-1 and Level-2 Hello packets. You can set different intervals for these two types of Hello packets. By default, both Level-1 and Level-2 Hello packets are sent.
     
     A P2P link can transmit only one type of Hello packets. Therefore, neither **level-1** or **level-2** needs to be specified if a P2P link is used.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set the holding multiplier for neighboring devices.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**isis timer holding-multiplier**](cmdqueryname=isis+timer+holding-multiplier) *number* [ **level-1** | **level-2** ]
     
     
     
     The number of Hello packets that are sent before the local device considers the neighbor Down is configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     A broadcast link can transmit both Level-1 and Level-2 Hello packets. You can set different intervals for these two types of Hello packets. By default, both Level-1 and Level-2 Hello packets are sent.
     
     A P2P link can transmit only one type of Hello packets. Therefore, neither **level-1** or **level-2** needs to be specified if a P2P link is used.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.