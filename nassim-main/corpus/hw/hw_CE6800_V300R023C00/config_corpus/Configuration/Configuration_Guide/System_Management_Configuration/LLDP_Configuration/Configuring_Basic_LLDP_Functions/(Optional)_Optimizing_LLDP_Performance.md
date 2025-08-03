(Optional) Optimizing LLDP Performance
======================================

(Optional) Optimizing LLDP Performance

#### Context

This section describes how to adjust LLDP parameters based on the load of a network to reduce the consumption of system resources and optimize the LLDP performance.

LLDP parameters include: interval for sending LLDP frames, delay in sending LLDP frames, hold time multiplier of device information on neighbors, delay in initializing LLDP on interfaces, and number of LLDP frames quickly sent by the device to a neighbor. Values of these parameters should be appropriate. You can adjust these parameters based on the load of a network. [Table 1](#EN-US_TASK_0000001130782862__tab_dc_vrp_lldp_cfg_000701) describes the usage scenarios of LLDP parameters.

**Table 1** LLDP parameters
| Parameter Name | Description | Value Description |
| --- | --- | --- |
| **message-transmission interval** | Sets the interval for sending LLDP frames to adjust the frequency of network topology discovery. | * The longer the interval, the lower the frequency of LLDP frames being exchanged. This saves system resources. However, if the interval for sending LLDP frames is too long, the device cannot notify neighbors of its status in a timely manner, reducing network topology discovery efficiency. * The shorter the interval, the higher the frequency of the local status information being sent to neighbors. This ensures prompt network topology discovery. However, if the interval is too short, LLDP frames are exchanged too frequently, increasing the system load and wasting resources. |
| **message-transmission delay** | Sets the delay in sending LLDP frames to avoid network flapping of neighbors caused by LLDP frames being frequently sent to neighbors. | When the status of a device changes frequently:  * The longer the delay, the lower the frequency of the local status information being sent to neighbors. This saves system resources. However, if the delay for sending LLDP frames is too long, the device cannot notify neighbors of its status in a timely manner, reducing network topology discovery efficiency. * The shorter the delay, the higher the frequency of the local status information being sent to neighbors. This ensures prompt network topology discovery. However, if the interval is too short, LLDP frames are exchanged too frequently, increasing the system load and wasting resources. |
| **message-transmission hold-multiplier** | Sets the hold time multiplier of device information on neighbors to calculate the valid time of LLDP frames being sent to neighbors. The time of device information held in neighbors can be adjusted by setting this parameter. | * The higher the time multiplier, the lower the frequency of network topology changes of neighbors. However, if the time of device information held in neighbors is too long, the device cannot notify neighbors of its status in a timely manner, reducing network topology discovery efficiency. * The lower the time multiplier, the higher the frequency of network topology changes of neighbors. This ensures prompt network topology discovery. However, if the time multiplier is too low, neighbors refresh local status information frequently, increasing the system load and wasting resources. |
| **restart-delay** | Sets the delay in initializing LLDP on interfaces to avoid network flapping caused by frequent LLDP status changes on interfaces. | * The longer the delay, the lower the frequency of network topology changes on a device. However, if the delay for initializing LLDP on interfaces is too long, the device cannot trace changes of neighbor status. As a result, the device cannot detect network topology of neighbors in a timely manner. * The shorter the delay, the higher the frequency of network topology changes on a device. This ensures prompt network topology discovery. However, if the delay is too short, the device refreshes status information about neighbors frequently, increasing the system load and wasting resources. |
| **fast-count** | Sets the number of LLDP frames quickly sent by the device to a neighbor to help the neighbor quickly obtain information about the local device, and help the NMS quickly detect network topology. | A device sends LLDP frames to neighbors every second if LLDP frames are being sent in quick succession and are not restricted by the delay time. After sending a specified number of LLDP frames in quick succession, the device periodically sends LLDP frames to neighbors based on the set interval. |




#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure LLDP parameters to optimize LLDP performance. Perform the following operations as required:
   
   
   * Configure the global interval for a device to send LLDP frames.
     ```
     [lldp transmit interval](cmdqueryname=lldp+transmit+interval) interval
     ```
     
     By default, the interval for sending LLDP frames is 30 seconds. Generally, you are advised to use the default interval for sending LLDP frames.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     
     By default, the LLDP-enabled interfaces use the global interval to send LLDP frames. To change the interval at which an interface sends LLDP frames, run the [**lldp transmit fast-mode interval**](cmdqueryname=lldp+transmit+fast-mode+interval) *packet-interval* command in the interface view.
   * Configure the delay for sending LLDP frames.
     ```
     [lldp transmit delay](cmdqueryname=lldp+transmit+delay) delay
     ```
     
     The delay for sending LLDP frames is configured. The default delay for sending LLDP frames is 2s.
     
     The parameters *interval* and *delay* for sending LLDP frames affect each other. Take the value of *delay* into consideration when adjusting the value of *interval*.
     + Increasing the value of *interval* is not restricted by the value of *delay*. *interval* can be any number from 5 to 32768.
     + Decreasing the value of *interval* is not restricted by the value of *delay*. The target value of *interval* must be greater than or equal to four times the value of *delay*. Otherwise, the value of *delay* must be adjusted to be less than or equal to a quarter of the target value of *interval*.
   * Configure time multiplier of device information held in neighbors.
     ```
     [lldp transmit multiplier](cmdqueryname=lldp+transmit+multiplier) hold-multiplier
     ```
     
     By default, the hold time multiplier of local status information on neighbors is 4. Generally, it is recommended that you keep the default hold time multiplier value of local status information on neighbors.
     
     ![](public_sys-resources/note_3.0-en-us.png) 
     + You can increase the value of *hold-multiplier* to prolong the time that device information is held in neighbors.
     + The value of *hold-multiplier* ranges from 2 to 10. The configuration does not take effect if the value of *hold-multiplier* x *interval* is greater than 65535.
   * Configure the delay for initializing LLDP on interfaces.
     ```
     [lldp restart](cmdqueryname=lldp+restart) delay
     ```
     
     By default, the delay for initializing LLDP on an interface is 2 seconds. Generally, you are advised to set the delay for initializing LLDP on an interface to the default value.
   * Configure the number of LLDP frames being sent in quick succession to neighbors.
     ```
     [lldp fast-count](cmdqueryname=lldp+fast-count) count
     ```
     
     By default, the number of LLDP frames being sent in quick succession to neighbors is 4.
     
     To help neighbors quickly obtain information about a local device, the local device sends a number of LLDP frames to neighbors when the local device detects a new neighbor (that is, when the device receives an LLDP frame from a transmitting device for which it has no information), or when LLDP is enabled for the device that previously had LLDP disabled, or the interface connected to a neighbor goes up.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```