(Optional) Optimizing LLDP Performance
======================================

This section describes how to adjust LLDP parameters based on the load of a network to reduce the consumption of system resources and optimize the LLDP performance.

#### Background Information

LLDP parameters include: interval for sending LLDP packets, delay for sending LLDP packets, time multiplier of device information held in neighbors, delay for initializing LLDP on interfaces, and number of LLDP packets being sent in quick succession to neighbors. Values of these parameters should be appropriate. You can adjust these parameters based on the load of a network. [Table 1](#EN-US_TASK_0172360372__tab_dc_vrp_lldp_cfg_000701) describes the usage scenarios of LLDP parameters.

**Table 1** LLDP parameters
| Parameter Name | Parameter Description | Value Description |
| --- | --- | --- |
| **message-transmission interval** | Sets the interval for sending LLDP packets to adjust the frequency of network topology discovery. | * The longer the interval, the lower the frequency of LLDP packets being exchanged. This saves system resources. However, if the interval for sending LLDP packets is too long, the device cannot notify neighbors of its status in a timely manner, reducing network topology discovery efficiency. * The shorter the interval, the higher the frequency of the local status information being sent to neighbors. This ensures prompt network topology discovery. However, if the interval is too short, LLDP packets are exchanged too frequently, increasing the system load and wasting resources. |
| **message-transmission delay** | Sets the delay for sending LLDP packets to avoid network flapping of neighbors caused by LLDP packets being frequently sent to neighbors. | When the status of a device changes frequently:  * The longer the delay, the lower the frequency of the local status information being sent to neighbors. This saves system resources. However, if the delay for sending LLDP packets is too long, the device cannot notify neighbors of its status in a timely manner, reducing network topology discovery efficiency. * The shorter the delay, the higher the frequency of the local status information being sent to neighbors. This ensures prompt network topology discovery. However, if the interval is too short, LLDP packets are exchanged too frequently, increasing the system load and wasting resources. |
| **message-transmission hold-multiplier** | Sets the time multiplier of device information held in neighbors to calculate the valid time of LLDP packets being sent to neighbors. The time of device information held in neighbors can be adjusted by setting this parameter. | * The higher the time multiplier, the lower the frequency of network topology changes of neighbors. However, if the time of device information held in neighbors is too long, the device cannot notify neighbors of its status in a timely manner, reducing network topology discovery efficiency. * The lower the time multiplier, the higher the frequency of network topology changes of neighbors. This ensures prompt network topology discovery. However, if the time multiplier is too low, neighbors refresh local status information frequently, increasing the system load and wasting resources. |
| **restart-delay** | Sets the delay for initializing LLDP on interfaces to avoid network flapping caused by frequent LLDP status changes on interfaces. | * The longer the delay, the lower the frequency of network topology changes on a device. However, if the delay for initializing LLDP on interfaces is too long, the device cannot trace changes of neighbor status. As a result, the device cannot detect network topology of neighbors in a timely manner. * The shorter the delay, the higher the frequency of network topology changes on a device. This ensures prompt network topology discovery. However, if the delay is too short, the device refreshes status information about neighbors frequently, increasing the system load and wasting resources. |
| **fast-count** | Sets the number of LLDP packets being sent in quick succession to neighbors to help neighbors quickly obtain information about the local device, and help the NMS quickly detect network topology. | A device sends LLDP packets to neighbors every second if LLDP packets are being sent in quick succession and are not restricted by the delay time. After sending a specified number of LLDP packets in quick succession, the device periodically sends LLDP packets to neighbors based on the set interval. |




#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**lldp message-transmission interval**](cmdqueryname=lldp+message-transmission+interval) *interval*
   
   
   
   The global interval for a device to send LLDP packets is configured.
   
   It is recommended that you use the default interval for sending LLDP packets.
3. Run [**lldp message-transmission delay**](cmdqueryname=lldp+message-transmission+delay) *delay*
   
   
   
   The delay for sending LLDP packets is configured.
   
   It is recommended that you use the default delay for sending LLDP packets unless otherwise noted.
   
   
   
   The parameters *interval* and *delay* for sending LLDP packets affect each other. Take the value of *delay* into consideration when adjusting the value of *interval*.
   * Increasing the value of *interval* is not restricted by the value of *delay*. *interval* can be any number from 5 to 32768.
   * Decreasing the value of *interval* is not restricted by the value of *delay*. The target value of *interval* must be greater than or equal to four times the value of *delay*. Otherwise, the value of *delay* must be adjusted to be less than or equal to a quarter of the target value of *interval*.
4. Run [**lldp message-transmission hold-multiplier**](cmdqueryname=lldp+message-transmission+hold-multiplier) *hold-multiplier*
   
   
   
   Time multiplier of device information held in neighbors is configured.
   
   
   
   It is recommended that you use the default time multiplier of device information held in neighbors unless otherwise noted.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * You can increase the value of *hold-multiplier* to prolong the time that device information is held in neighbors.
   * The value of *hold-multiplier* ranges from 2 to 10. The configuration does not take effect if the value of *hold-multiplier* x *interval* is greater than 65535.
5. Run [**lldp restart-delay**](cmdqueryname=lldp+restart-delay) *delay*
   
   
   
   The delay for initializing LLDP on interfaces is configured.
   
   It is recommended that you use the default delay for initializing LLDP unless otherwise noted.
6. Run [**lldp fast-count**](cmdqueryname=lldp+fast-count) *count*
   
   
   
   The number of LLDP packets being sent in quick succession to neighbors is configured.
   
   
   
   To help neighbors quickly obtain information about a local device, the local device sends a number of LLDP packets to neighbors when the local device detects a new neighbor (that is, when the device receives an LLDP packet from a transmitting device for which it has no information), or when LLDP is enabled for the device that previously had LLDP disabled, or the interface connected to a neighbor goes Up.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.