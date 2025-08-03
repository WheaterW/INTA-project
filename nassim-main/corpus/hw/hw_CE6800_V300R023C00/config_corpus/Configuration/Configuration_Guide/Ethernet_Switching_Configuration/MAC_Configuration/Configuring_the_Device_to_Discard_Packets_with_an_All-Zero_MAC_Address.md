Configuring the Device to Discard Packets with an All-Zero MAC Address
======================================================================

Configuring the Device to Discard Packets with an All-Zero MAC Address

#### Context

Devices and hosts of early versions may send packets with an all-zero source or destination MAC address if their NICs become faulty. To prevent the device from receiving these packets, you can configure it to discard packets with an all-zero MAC address. After this function is configured, the device discards packets with an all-zero source or destination MAC address.

![](public_sys-resources/note_3.0-en-us.png) 

The CE6885-LL (low latency mode) does not support this function.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the device to discard packets with an all-zero MAC address.
   
   
   ```
   [drop illegal-mac enable](cmdqueryname=drop+illegal-mac+enable)
   ```
   
   By default, the device does not discard packets with an all-zero MAC address.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```