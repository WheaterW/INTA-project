(Optional) Configuring Time Attributes for G.8275.1 Packets
===========================================================

T-BCs exchange Announce, Sync, and Delay or Pdelay packets to send time information and maintain G.8275.1 connections. You can set the interval at which a G.8275.1 interface sends Announce, Sync, and Delay or Pdelay packets and the maximum number of Announce packet timeouts. Using the default time attribute values is recommended.

#### Context

Perform the following operations on the T-BC:


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
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**ptp min-delayreq-interval**](cmdqueryname=ptp+min-delayreq-interval) *min-delayreq-interval*
     
     
     
     The interval at which the interface sends Delay\_Req packets is set. The following formula applies: Interval = 2n x 1/1024s, where n equals to *min-delayreq-interval*.
     
     The default *min-delayreq-interval* value is 6, which means that an interface sends a Delay\_Req every 64/1024s.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.