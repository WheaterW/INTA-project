Configuring an Interval for Detecting IS-IS Neighbor Faults
===========================================================

Configuring an Interval for Detecting IS-IS Neighbor Faults

#### Prerequisites

Before configuring an interval for detecting IS-IS neighbor faults, you have completed the following task:

* [Configure basic IPv6 IS-IS functions](vrp_isis_ipv6_cfg_0011.html).

#### Context

IS-IS uses IIHs to discover neighbors and establish neighbor relationships. After a neighbor relationship is established, the two ends exchange IIHs periodically to monitor the neighbor relationship and detect neighbor faults. An IS-IS neighbor is considered down if the local device has not received any IIHs from the neighbor when the holdtime expires. Then LSP flooding and SPF calculation are triggered, followed by IS-IS route re-convergence. To adjust the neighbor fault detection speed, you can configure the interval at which IIHs are sent, as well as a Hello multiplier (the number of IIHs sent before the neighbor is declared down).

![](public_sys-resources/note_3.0-en-us.png) 

If the interval at which IIHs are sent is too short, a large number of system resources are consumed, leading to a heavy CPU load. If the Hello multiplier is too large, the local device needs to wait a long time before detecting the fault of its neighbor, which slows down IS-IS route convergence. If the Hello multiplier is too small, the IS-IS neighbor relationships will frequently alternate between up and down in the case of an IIH loss or error due to a network delay or transmission error. As a result, route flapping occurs on the IS-IS network. To ensure IS-IS route convergence is not slowed down if some devices detect link failures slower than others do, you are advised to set the same interval at which IIHs are sent and the same Hello multiplier on all the devices on the IS-IS network.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the interface view.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
4. Configure the interval at which IIHs are sent.
   
   
   ```
   [isis timer](cmdqueryname=isis+timer) hello hello-interval [ level-1 | level-2 ] [ conservative ]
   ```
   
   
   
   By default, the interval at which IIHs are sent is 10 seconds.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Parameters **level-1** and **level-2** are mandatory on broadcast network interfaces because Level-1 and Level-2 IIHs are sent on the broadcast network and each level requires one interval. Interfaces over P2P links send P2P IIHs, rather than Level-1 or Level-2 IIHs; therefore, such interfaces do not require the **level-1** or **level-2** configuration.
   
   The interval at which IIHs are sent should not be less than the time required for a device to perform a master/slave main control board switchover. Otherwise, an intermittent protocol interruption may occur during a switchover. The default timer value is recommended.
5. Configure an IS-IS neighbor holdtime.
   
   
   ```
   [isis timer holding-multiplier](cmdqueryname=isis+timer+holding-multiplier) number [ level-1 | level-2 ]
   ```
   
   The holdtime is the interval at which IIHs are sent multiplied by the Hello multiplier. The default Hello multiplier is 3. That is, if the local device has not received any IIHs from its neighbor when the holdtime (three times the interval at which IIHs are sent) expires, the local device considers the neighbor down.
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   Parameters **level-1** and **level-2** are mandatory on interfaces over broadcast links because both Level-1 and Level-2 IIHs are sent on the broadcast links and each level needs one interval. Interfaces over P2P links send P2P IIHs, rather than Level-1 or Level-2 IIHs. Therefore, neither **level-1** nor **level-2** is required.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```