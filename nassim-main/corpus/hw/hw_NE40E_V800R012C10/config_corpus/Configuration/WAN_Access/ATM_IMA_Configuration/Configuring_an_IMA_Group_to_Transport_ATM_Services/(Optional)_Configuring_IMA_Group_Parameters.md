(Optional) Configuring IMA Group Parameters
===========================================

Configure IMA group parameters as required.

#### Context

The following table lists the IMA group parameters and their usage scenarios in inverse multiplexing and de-multiplexing of ATM cells.

**Table 1** IMA Group Parameters
| Parameter | Description | Usage Scenario |
| --- | --- | --- |
| differential-delay | Maximum link differential delay for an IMA group | Link differential delay (LDD) is the difference between delays at which packets are sent along member links in an IMA group. The difference between delays at which packets are sent by member links in an IMA group must be less than or equal to the value configured using the **differential-delay** command.  To improve bandwidth usage of IMA channels and prevent empty packets from consuming bandwidth, decrease the maximum LDD if traffic is heavy on the network. |
| frame-length | Number of ATM cells in an IMA frame | The transmit and receive ends of an IMA group work as follows:  * Transmit end: receives an ATM cell stream from the ATM layer, distributes the ATM cells in the stream on a cell by cell basis among the member links in the IMA group, and sends them to the receive end periodically. * Receive end: reassembles received cells to recover the original ATM cell stream and transmits the stream to the ATM layer.  You can run the [**frame-length**](cmdqueryname=frame-length) command to set the number of ATM cells in an IMA frame. To ensure transmission efficiency on links, use the default configuration. |
| min-active-links | Minimum number of active links that are required for an IMA group to work properly | An IMA group is a logical link that consists of one or more physical links. It provides more bandwidth than a single link. The minimum number of active links must be set in an IMA group before the IMA group can work properly. If a link fails, the number of active links in an IMA group in the Operational state may be less than the configured minimum value. As a result, the IMA group status changes and even becomes Down.  The minimum number of active links that are required for an IMA group to work properly depends on the bandwidth allocated to the IMA group. An IMA group can work properly only when the number of active links in an IMA group is greater than or equal to **min-active-links**. The configured minimum number of active links must be less than or equal to the number of links in the IMA group. |
| bandwidth-overload | Logical bandwidth for an IMA group interface | The physical bandwidth on an interface is limited, which restricts the bandwidth that can be allocated to PVCs. After logical bandwidth is configured for an IMA group interface, the bandwidth that can be allocated to the interface to be added to the IMA group interface is increased. Bandwidth for PVCs must meet the following requirements:  * Bandwidth for each PVC cannot be greater than the physical interface's bandwidth. * Total bandwidth for all PVCs must be lower than the sum of the physical bandwidth and logical bandwidth. |
| clock | Clock mode | If two devices are directly connected using global IMA-group interfaces, run the [**clock**](cmdqueryname=clock) command to configure a clock mode for each global IMA-group interface so that the two devices can communicate. A global IMA-group interface can work in either of the following clock modes:  * CTC mode: All member links of an IMA group share the same clock source, which is either an external clock or the clock of a member link. * ITC mode: Member links of an IMA group use different clock sources. |



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface ima-group**](cmdqueryname=interface+ima-group) *interface-number*[.*subinterface* ]
   
   
   
   The IMA group interface (sub-interface) view is displayed.
3. Run any of the following commands:
   
   
   * To set the maximum LDD for an IMA group, run the [**differential-delay**](cmdqueryname=differential-delay) *diffDelay* command.
   * To set the number of ATM cells in an IMA frame, run the [**frame-length**](cmdqueryname=frame-length) *frameLen* command.
   * To set the minimum number of active links that are required for an IMA group to work properly, run the [**min-active-links**](cmdqueryname=min-active-links) *minLinks* command.
   * To configure logical bandwidth for an IMA group interface, run the [**service bandwidth-overload**](cmdqueryname=service+bandwidth-overload) *overload-value* command.
   * To configure a clock mode for the global IMA-group interface, run the [**clock**](cmdqueryname=clock) { **ctc** | **itc** } command.