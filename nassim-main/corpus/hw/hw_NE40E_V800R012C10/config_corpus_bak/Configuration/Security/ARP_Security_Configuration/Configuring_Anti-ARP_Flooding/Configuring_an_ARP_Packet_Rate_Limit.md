Configuring an ARP Packet Rate Limit
====================================

If a device receives excessive Address Resolution Protocol (ARP) packets in a short period, the device becomes busy learning entries and replying to the ARP packets, which can interrupt the processing of other services. To resolve this problem, configure an ARP packet rate limit on the device.

#### Context

The device has no sufficient CPU resource to process other services when processing a large number of ARP packets. To protect CPU resources of the device, limit the rate of ARP packets.

After a rate limit is configured for ARP packets, if the number of ARP packets received in one second exceeds the limit, the device discards the excess ARP packets.


#### Procedure

* Configure ARP packet rate limit based on user addresses.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**arp speed-limit**](cmdqueryname=arp+speed-limit) { **destination-ip** | **source-ip** } **maximum** *maximum* [ **slot** *slot-id* ]
     
     
     
     ARP packet rate limit based on user addresses is configured.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.