(Optional) Setting Interface Parameters
=======================================

This section describes how to set parameters for an interface based on the actual service requirements. The parameters include the description and maximum transmission unit (MTU).

#### Context

[Table 1](#EN-US_TASK_0172362566__tab_dc_vrp_ifm_cfg_002701) describes the configurable parameters of an interface.

**Table 1** Configurable parameters of an interface
| Parameter | Description |
| --- | --- |
| Interface description | When you maintain a large number of interfaces, an interface description helps identify an interface easily. |
| Interface MTU | After the MTU is configured for an interface, the device fragments a packet transmitted on the interface if the size of the packet exceeds the MTU.  NOTE:  Loopback and NULL interfaces do not support the MTU. |
| Interface bandwidth that can be obtained by the NMS through the MIB | You can calculate the bandwidth usage by setting the interface bandwidth that can be obtained by the NMS through the MIB. |
| Whether the device sends a trap message to the NMS when the interface status changes | You can enable the device to send a trap message to the NMS when the interface status changes. After this function is enabled, the NMS monitors the interface status in real time.  However, if an interface alternates between up and down, the device will frequently send trap messages to the NMS, which increases the processing load on the NMS. In this situation, you can disable the device from sending trap messages to the NMS to avoid adverse impact on the NMS. |
| Interval at which traffic statistics are collected | After setting the interval at which traffic statistics are collected for an interface, you can view the traffic volumes and rates of the interface in different time ranges. |
| Whether the control-flap function is enabled | Control-flap controls the frequency of interface status alternations between up and down, which minimizes the impact on device and network stability.  NOTE:  Loopback and NULL interfaces do not support the control-flap function. |



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
   
   
   
   In this command, *interface-type* specifies the type of the interface, and *interface-number* specifies the number of the interface.
3. Perform one or more operations in [Table 2](#EN-US_TASK_0172362566__tab_dc_vrp_ifm_cfg_002702) to set the desired interface parameters.
   
   
   
   **Table 2** Setting interface parameters
   | Operation | Description |
   | --- | --- |
   | Configure a description for an interface. | Run the [**description**](cmdqueryname=description) *regular-expression* command to configure a description for an interface. |
   | Set an MTU for an interface. | Run the [**mtu**](cmdqueryname=mtu) *mtu* or [**ipv6 mtu**](cmdqueryname=ipv6+mtu) *mtu* command to set an MTU for an interface.  Run the [**mtu**](cmdqueryname=mtu) *mtu* **spread** or [**ipv6 mtu**](cmdqueryname=ipv6+mtu) *mtu* **spread** command to set an MTU for an interface and apply the MTU to all the sub-interfaces on the interface.  NOTE:  * After changing the MTU on a POS interface using the [**mtu**](cmdqueryname=mtu) or [**mtu spread**](cmdqueryname=mtu+spread) command, run the [**shutdown**](cmdqueryname=shutdown) and [**undo shutdown**](cmdqueryname=undo+shutdown) commands in the interface view for the change to take effect. Alternatively, you can run the [**restart**](cmdqueryname=restart) command in the interface view to restart the interface for the change to take effect. * If IPv4 attributes are configured on an interface, run the [**mtu**](cmdqueryname=mtu) or [**mtu spread**](cmdqueryname=mtu+spread) command to set an MTU for the IPv4 packets to be sent by the interface. * If IPv6 attributes are configured on an interface, run the [**ipv6 mtu**](cmdqueryname=ipv6+mtu) or [**ipv6 mtu spread**](cmdqueryname=ipv6+mtu+spread) command to set an MTU for the IPv6 packets to be sent by the interface. |
   | Set configuration bandwidth for an interface. | Run the [**bandwidth**](cmdqueryname=bandwidth) command to set configuration bandwidth for an interface.  NOTE:  To view the command configurations, you can check the ifSpeed and ifHighSpeed objects in the IF-MIB on the NMS.  By default, services typically use only the physical bandwidth for protocol route selection calculation. You can run the **bandwidth-config effect service enable** command to use the configuration bandwidth for protocol route selection calculation. |
   | Configure whether the device sends a trap message to the NMS when the interface status changes. | Run the [**enable snmp trap updown**](cmdqueryname=enable+snmp+trap+updown) command to enable the device to send a trap message to the NMS when the interface status changes.  NOTE:  If an interface alternates between up and down, the device will frequently send trap messages to the NMS, which increases the processing load on the NMS. In this situation, you can run the [**undo enable snmp trap updown**](cmdqueryname=undo+enable+snmp+trap+updown) command to disable the device from sending trap messages to the NMS to avoid adverse impact on the NMS. |
   | Set the interval at which traffic statistics are collected. | Run the [**set flow-stat interval**](cmdqueryname=set+flow-stat+interval) *interval* command to set the interval at which traffic statistics are collected.  NOTE:  * To set a global interval at which traffic statistics are collected, run the [**set flow-stat interval**](cmdqueryname=set+flow-stat+interval) *interval* command in the system view, and you do not need to run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command. You can configure a global traffic statistic collection interval, which takes effect on all interfaces, including the interfaces on which no traffic statistic collection interval has been set. * The new interval takes effect after the original interval expires. If the interface is logical, traffic statistics about the interface are updated when the new interval takes effect for the second time. If the interface is physical, traffic statistics about the interface are updated immediately after the new interval takes effect. |
   | Enable the control-flap function. | Run the [**control-flap**](cmdqueryname=control-flap) [ *suppress* *reuse* *ceiling* *decay-ok* *decay-ng* ] command to enable the control-flap function on an interface.  The value of *suppress* is 1000 times the interface suppression threshold. It ranges from 1 to 20000. The default value is 2000. The value of *suppress* must be greater than the value of *reuse* and less than the value of *ceiling*.  The value of *reuse* is 1000 times the interface reuse threshold. It ranges from 1 to 20000. The default value is 750. The value of *reuse* must be less than the value of *suppress*.  The value of *ceiling* is 1000 times the maximum interface suppression penalty value. It ranges from 1001 to 20000. The default value is 6000. The value of *ceiling* must be greater than the value of *suppress*.  *decay-ok* specifies the half life for the penalty value when an interface is up. It ranges from 1 to 900, in seconds. The default value is 54.  *decay-ng* specifies the half life for the penalty value when an interface is down. It ranges from 1 to 900, in seconds. The default value is 54. |
   | Configure whether to adjust the modulation mode of an interface. | Run the [**signal-coding**](cmdqueryname=signal-coding) { **dqpsk** | **qpsk** } command to configure a modulation mode for an interface. |
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.