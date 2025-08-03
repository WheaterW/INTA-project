(Optional) Disabling a VBDIF Interface from Sending ARP Miss Messages
=====================================================================

(Optional) Disabling a VBDIF Interface from Sending ARP Miss Messages

#### Context

When a device needs to communicate with another device on the same network segment, it queries ARP entries for packet forwarding. If the device fails to find ARP entries from the forwarding plane, it sends an ARP Miss message, which triggers the device to send an ARP broadcast packet for ARP learning. In some scenarios, if you want to limit the number of broadcast packets on a VXLAN, you can disable a VBDIF interface from sending ARP Miss messages.

![](public_sys-resources/note_3.0-en-us.png) 

This function is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6885, CE6885-T, CE6885-LL in standard forwarding mode, and CE6863E-48S8CQ.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VBDIF interface view.
   
   
   ```
   [interface vbdif](cmdqueryname=interface+vbdif) bd-id
   ```
3. Disable the VBDIF interface from sending ARP Miss messages.
   
   
   ```
   [arp miss disable](cmdqueryname=arp+miss+disable)
   ```
   
   By default, a VBDIF interface can send ARP Miss messages.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```