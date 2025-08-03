Configuring a Device to Send ARP Messages at a Constant Speed
=============================================================

Configuring a Device to Send ARP Messages at a Constant Speed

#### Context

By default, a device sends ARP messages at inconstant rates. If the number of ARP messages received by the peer device within milliseconds exceeds its processing capability, ARP messages may be lost and services may be affected. To resolve the problem, enable the device to send ARP messages at a constant rate and adjust the constant rate as required so that normal services of the peer device are not affected.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable the device to send ARP messages at a constant rate.
   
   
   ```
   [arp constant-send enable](cmdqueryname=arp+constant-send+enable)
   ```
3. Configure a constant rate at which ARP messages are sent.
   
   
   ```
   [arp constant-send maximum](cmdqueryname=arp+constant-send+maximum) maximum-value
   ```
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display arp packet statistics**](cmdqueryname=display+arp+packet+statistics) [ **interface** { *interface-name* | *interface-type* *interface-number* } ] command to check ARP message statistics.