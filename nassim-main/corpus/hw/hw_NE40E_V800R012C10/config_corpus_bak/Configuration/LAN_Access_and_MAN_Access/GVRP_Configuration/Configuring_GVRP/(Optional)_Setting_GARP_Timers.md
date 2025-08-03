(Optional) Setting GARP Timers
==============================

(Optional)_Setting_GARP_Timers

#### Context

When a GARP device starts, its LeaveAll timer starts. When the LeaveAll timer expires, the device sends a LeaveAll message to request other GARP devices to re-register all of its attributes. It then restarts its LeaveAll timer for a new round of polling.

Devices on a network may have different settings for the LeaveAll timer, but only the LeaveAll timer with the smallest value takes effect. When the LeaveAll timer with the smallest value expires, that device whose LeaveAll timer value is the smallest sends a LeaveAll message to all other devices and restarts its own LeaveAll timer. After receiving the LeaveAll message, the other devices restart all of their GARP timers, including the LeaveAll timer. They then propagate the LeaveAll messages to all other connected devices except for the device from whom they initially received the LeaveAll message.

When setting GARP timers for an interface, note the following:

* The [**undo garp timer**](cmdqueryname=undo+garp+timer) command restores the default values of GARP timers. If the default value of a timer is out of the valid range, the [**undo garp timer**](cmdqueryname=undo+garp+timer) command does not take effect.
* The value range of each timer changes with the values of the other timers. If a timer value that you wish to set falls outside of the allowed range, you can change the value of another timer that relates to the value range of this timer.
* To restore the default values of all GARP timers, restore in sequence the Hold timer, Join timer, Leave timer, and LeaveAll timer to default values.

When many dynamic VLANs need to be registered or the network radius is large, using the default values of GARP timers may cause VLAN flapping and high CPU usage. To prevent such problems, increase timer values. The following values are recommended depending on the number of VLANs.

**Table 1** Relationship between GARP timer values and number of dynamic VLANs to be registered
| Timer | Number of Dynamic VLANs to Be Registered (N) | | | |
| --- | --- | --- | --- | --- |
| N <= 500 | 500 < N <= 1000 | 1000 < N <= 1500 | N > 1500 |
| GARP Hold timer | 100 centiseconds (1s) | 200 centiseconds (2s) | 800 centiseconds (8s) | 1000 centiseconds (10s) |
| GARP Join timer | 600 centiseconds (6s) | 1200 centiseconds (12s) | 4000 centiseconds (40s) | 6000 centiseconds (1 min) |
| GARP Leave timer | 3000 centiseconds (30s) | 6000 centiseconds (1 min) | 20000 centiseconds (3 min and 20s) | 30000 centiseconds (5 min) |
| GARP LeaveAll timer | 12000 centiseconds (2 min) | 24000 centiseconds (4 min) | 30000 centiseconds (5 min) | 32765 centiseconds (5 min and 27.65s) |




#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**garp timer leaveall**](cmdqueryname=garp+timer+leaveall) *timer-value*
   
   
   
   The value of a LeaveAll timer is set.
   
   
   
   The Leave timer value of each interface is restricted by the global LeaveAll timer value. When setting a value for the global LeaveAll timer, ensure that all the interfaces configured with a GARP Leave timer are working properly.
3. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
4. Run [**garp timer**](cmdqueryname=garp+timer) { **hold** | **join** | **leave** } *timer-value*
   
   
   
   The value of the Hold timer, Join timer, or Leave timer is set for the interface.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.