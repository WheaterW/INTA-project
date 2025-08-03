(Optional) Configuring Time Attributes for 1588v2 Packets
=========================================================

This section describes how to configure time attributes for 1588v2 packets. 1588v2 devices exchange Announce, Sync, and Delay or Pdelay packets to send time information and maintain 1588v2 connections. You can set the interval at which a 1588v2 interface sends Announce, Sync, and Delay or Pdelay packets and the maximum number of Announce packet timeouts. Using the default time attribute values is recommended.

#### Context

Two devices exchange Announce packets to determine the master/slave relationship. The master device sends Sync packets to notify the slave device of time signal parameters and uses a delay measurement mechanism to achieve time signals accuracy.

If devices exchange 1588v2 packets frequently and consume a lot of bandwidth resources, increase the interval value. If the time synchronization accuracy is low, reduce the interval value.

* **Announce packets**
  
  To set the maximum number of Announce packets that a 1588v2 interface fails to receive consecutively, run the ptp announce receipt-timeout command. If the 1588v2 interface on a device fails to receive a specified number of Announce packets, the interface status becomes Master, and the device stops attempting to synchronize the time with other 1588v2 devices. The device uses the BMC algorithm to select a clock source and synchronize the time with the clock source. Increase receipt-timeout to reduce the clock source switching frequency; reduce receipt-timeout to switch clock sources. Using the default value is recommended.
* **Sync packets**
  
  The master interface periodically sends multicast Sync packets.
  
  The time when the Sync packets can be stamped into the Sync packets if the one-step timestamping mode is used or into Follow\_Up packets if the two-step timestamping mode is used. To specify a timestamping mode, run the [**ptp clock-step**](cmdqueryname=ptp+clock-step) { **one-step** | **two-step** } command.
* **Delay or Pdelay packets**
  
  A Router uses a delay measurement mechanism to send request packets and receive response packets from its remote Router. The Router uses timestamps carried in the packets to correct time signals.

Perform the following steps on each 1588v2 device:


#### Procedure

* Configure time attributes for Announce packets.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
  3. Run the [**ptp announce-interval**](cmdqueryname=ptp+announce-interval) *announce-interval* command to set the interval at which the interface sends Announce packets. The following formula applies: Interval = 2n x 1/1024s, where *n* equals to *announce-interval*.
     
     
     
     Timeout interval for receiving Announce packets on the peer interface = Number of timeouts for receiving Announce packets on the peer interface (*receipt-timeout*) x Interval for sending Announce packets on the local interface (*announce-interval*)
  4. Run the [**ptp announce receipt-timeout**](cmdqueryname=ptp+announce+receipt-timeout) *receipt-timeout* command to set the maximum number of Announce packets that the interface fails to receive.
     
     
     
     Timeout interval for receiving Announce packets on the local interface = Number of timeouts for receiving Announce packets on the local interface (*receipt-timeout*) x Interval for sending Announce packets on the peer interface (*announce-interval*)
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure time attributes for Sync packets.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
  3. Run the [**ptp sync-interval**](cmdqueryname=ptp+sync-interval) *sync-interval* command to set the interval at which the interface sends Sync packets. The following formula applies: Interval = 2n x 1/1024s, where *n* equals to *sync-interval*.
  4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* Configure time attributes for Delay or Pdelay packets.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
  3. Run the [**ptp min-delayreq-interval**](cmdqueryname=ptp+min-delayreq-interval) *min-delayreq-interval* command to set the interval at which the interface sends Delay\_Req packets. The following formula applies: Interval = 2n x 1/1024s, where *n* equals to *min-delayreq-interval*.
  4. Run the [**ptp min-pdelayreq-interval**](cmdqueryname=ptp+min-pdelayreq-interval) *min-pdelayreq-interval* command to set the interval at which the interface sends Pdelay\_Req packets. The following formula applies: Interval = 2n x 1/1024s, where *n* equals to *min-pdelayreq-interval*.
  5. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.