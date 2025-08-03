(Optional) Configuring Time Attributes for SMPTE-2059-2 Packets
===============================================================

This section describes how to configure time attributes for SMPTE-2059-2 packets. SMPTE-2059-2 nodes exchange Announce, Sync, and Delay or Pdelay packets to send time information and maintain SMPTE-2059-2 connections. You can set the interval at which an SMPTE-2059-2 interface sends Announce, Sync, and Delay or Pdelay packets and the maximum number of Announce packet timeouts. Using the default time attribute values is recommended.

#### Context

During SMPTE-2059-2 clock synchronization, an Announce packet is sent to determine the master-slave hierarchy, where the upstream node that advertises the synchronization time is the master device and the downstream node that receives the synchronization time is called the slave device. The master device sends Sync packets to the slave device to transmit performance parameters of time signals. In addition, the delay measurement mechanism can be implemented to ensure the accuracy of time signals.

If the packet sending interval is too small, devices frequently exchange SMPTE-2059-2 packets, consuming too many bandwidth resources. If the packet sending interval is too large, the precision of time synchronization cannot be guaranteed. Given that the time precision is guaranteed, set the packet sending interval to a large value.

Perform the following operations on an SMPTE-2059-2 device:


#### Procedure

* Configure time attributes for Announce packets.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**ptp announce-interval**](cmdqueryname=ptp+announce-interval) *announce-interval*
     
     
     
     The interval at which the interface sends Announce packets is set. The following formula applies:
     
     Interval = 2n x 1/1024s, where *n* equals to *announce-interval*.
     
     Remote timeout period of receiving Announce packets = Remotely configured *receipt-timeout* x Local interval at which Announce packets are sent
  4. Run [**ptp announce receipt-timeout**](cmdqueryname=ptp+announce+receipt-timeout) *receipt-timeout*
     
     
     
     The maximum number of timeouts for receiving Announce packets is set.
     
     Local timeout period of receiving Announce packets = Locally configured *receipt-timeout* x Remote interval at which Announce packets are sent
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure time attributes for Sync packets.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**ptp sync-interval**](cmdqueryname=ptp+sync-interval) *sync-interval*
     
     
     
     The interval at which the interface sends Sync packets is set. The following formula applies:
     
     Interval = 2n x 1/1024s, where *n* equals to *sync-interval*.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure time attributes for Delay or Pdelay packets.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface view is displayed.
  3. Run [**ptp min-delayreq-interval**](cmdqueryname=ptp+min-delayreq-interval) *min-delayreq-interval*
     
     
     
     The interval at which the interface sends Delay\_Req packets is set. The following formula applies:
     
     Interval = 2n x 1/1024s, where *n* equals to *min-delayreq-interval*.
  4. Run [**ptp min-pdelayreq-interval**](cmdqueryname=ptp+min-pdelayreq-interval) *min-pdelayreq-interval*
     
     
     
     The interval at which the interface sends Pdelay\_Req packets is set. The following formula applies:
     
     Interval = 2n x 1/1024s, where *n* equals to *min-pdelayreq-interval*.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.