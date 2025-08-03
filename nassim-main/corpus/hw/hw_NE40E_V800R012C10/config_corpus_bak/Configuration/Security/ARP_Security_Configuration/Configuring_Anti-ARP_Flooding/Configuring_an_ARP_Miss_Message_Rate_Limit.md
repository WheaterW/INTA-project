Configuring an ARP Miss Message Rate Limit
==========================================

Configuring_an_ARP_Miss_Message_Rate_Limit

#### Context

After a rate limit is configured for ARP Miss messages on a device, the device counts the number of received ARP Miss messages. If the number of ARP Miss messages received in a specified period exceeds the limit, the device does not process excess ARP Miss messages.

If a large number of VLANs are configured on an interface, ARP request packets that are triggered by ARP Miss messages need to be copied and sent on all these VLANs, causing the software to be overloaded and not to be able to send ARP request packets to terminals in time. To resolve this problem, you can configure a penalty interval to suppress fake dynamic ARP entry aging. When ARP Miss messages are triggered again after ARP learning fails, the system accumulatively increases the aging time of fake ARP entries by the configured penalty interval to dynamically prolong the life cycle of ARP fake entries, reducing the software workload of sending ARP request packets.


#### Procedure

* Configure rate limiting on ARP Miss messages based on source IP addresses.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**arp-miss speed-limit**](cmdqueryname=arp-miss+speed-limit) **source-ip** **maximum** *maximum* [ **slot** *slot-id* ] command to configure rate limiting on ARP Miss messages based on source IP addresses.
  3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* (Optional) Configure an aging time for fake dynamic ARP entries.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
  3. Run the [**arp-fake expire-time**](cmdqueryname=arp-fake+expire-time) *expire-time* command to configure an aging time for fake dynamic ARP entries.
     
     ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     If the aging time of fake dynamic ARP entries is set to a value smaller than the default value (5s) using the [**arp-fake expire-time**](cmdqueryname=arp-fake+expire-time) command, the CPU usage may be too high.
  4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
* (Optional) Configure a penalty interval for suppressing fake dynamic ARP entry aging.
  1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
  2. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
  3. Run the [**arp-fake penalty-time**](cmdqueryname=arp-fake+penalty-time) *penalty-time* command to configure a penalty interval for suppressing fake dynamic ARP entry aging.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the aging time of fake dynamic ARP entries is set using the [**arp-fake expire-time**](cmdqueryname=arp-fake+expire-time) command, the penalty interval configuration does not take effect.
  4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.