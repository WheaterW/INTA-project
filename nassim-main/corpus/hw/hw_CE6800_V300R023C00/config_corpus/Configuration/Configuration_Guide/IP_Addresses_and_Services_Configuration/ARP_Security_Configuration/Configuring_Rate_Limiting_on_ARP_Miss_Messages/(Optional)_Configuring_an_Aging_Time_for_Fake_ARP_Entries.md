(Optional) Configuring an Aging Time for Fake ARP Entries
=========================================================

(Optional) Configuring an Aging Time for Fake ARP Entries

#### Context

If a device fails to find the destination MAC address (corresponding to the destination IP address) of a packet to be forwarded, the device sends an ARP Miss message to the upper-layer software. After receiving the ARP Miss message, the upper-layer software generates a dynamic fake ARP entry and sends it to the device. The upper-layer software then sends an ARP request message to request the MAC address of the destination host. After receiving an ARP reply message, the upper-layer software learns the address information in the message and sends the real ARP entry to the device, which then replaces the fake entry. The device can then forward IP datagrams.

This mechanism can be exploited by unauthorized users sending a large number of ARP messages with forged IP addresses to a device. When trying to forward these messages, the device cannot find the required destination MAC addresses, and so sends a large number of ARP Miss messages to the upper-layer software. This consumes excessive CPU resources and prevents the device from processing normal services.

To alleviate the impact of ARP Miss message processing on the system, you can configure an aging time for fake dynamic ARP entries. Until the aging time elapses, the device does not send ARP Miss messages to the upper-layer software, reducing the frequency of sending ARP Miss messages. After the aging time elapses, the device clears fake dynamic ARP entries. If the device cannot find a matching ARP entry, it sends another ARP Miss message to the upper-layer software.


#### Procedure

* Configure an aging time for fake ARP entries in the interface view.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the interface view.
     
     
     ```
     [interface](cmdqueryname=interface) { interface-name | interface-type interface-number }
     ```
  3. Switch the interface working mode to Layer 3.
     
     
     ```
     [undo portswitch](cmdqueryname=undo+portswitch)
     ```
     
     Determine whether to perform this step based on the current interface working mode.
  4. Set the aging time of fake ARP entries to a fixed value to suppress the frequency of sending ARP Miss messages.
     
     
     ```
     [arp fake timeout](cmdqueryname=arp+fake+timeout) expire-time
     ```
     
     By default, the aging time of fake ARP entries is 5s.
     
     
     
     ![](public_sys-resources/notice_3.0-en-us.png) 
     
     If the aging time of fake ARP entries is set to a value smaller than the default value (5s) using the [**arp fake timeout**](cmdqueryname=arp+fake+timeout) command, the CPU usage may be too high.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```