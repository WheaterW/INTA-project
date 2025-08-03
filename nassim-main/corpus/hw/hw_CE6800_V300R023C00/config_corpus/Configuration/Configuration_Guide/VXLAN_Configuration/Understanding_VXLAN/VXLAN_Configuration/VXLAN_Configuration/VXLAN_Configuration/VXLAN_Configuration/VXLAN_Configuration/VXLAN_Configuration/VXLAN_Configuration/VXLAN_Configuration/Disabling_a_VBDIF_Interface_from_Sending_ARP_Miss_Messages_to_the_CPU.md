Disabling a VBDIF Interface from Sending ARP Miss Messages to the CPU
=====================================================================

Disabling a VBDIF Interface from Sending ARP Miss Messages to the CPU

#### Prerequisites

Before disabling a VBDIF interface from sending ARP Miss messages to a CPU, you have completed one of the following tasks:

* [Establishing VXLAN Tunnels in Static Mode (Centralized VXLAN Gateway)](dc_vrp_vxlan_cfg_1039.html)
* [Establishing VXLAN Tunnels in BGP EVPN Mode (Centralized VXLAN Gateway)](dc_vrp_vxlan_cfg_1072.html)
* [Establishing VXLAN Tunnels in BGP EVPN Mode (Distributed VXLAN Gateway)](dc_vrp_vxlan_cfg_1066.html)


#### Context

When a local device wants to communicate with another device in the same network segment, it queries ARP entries to direct packet forwarding. If the device fails to find the corresponding ARP entry from the forwarding plane, it sends an ARP Miss message to the CPU. The ARP Miss message will trigger the device to send an ARP broadcast packet to start ARP learning. To limit the number of broadcast packets on a VXLAN network, disable a VBDIF interface from sending ARP Miss messages to the CPU.

After this configuration takes effect, the device cannot learn ARP entries from this VBDIF interface, so ARP entries need to be manually configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This function is supported on IPv4 overlay networks only.



#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the VBDIF interface view.
   
   
   ```
   [interface vbdif](cmdqueryname=interface+vbdif) bd-id
   ```
3. Disable the VBDIF interface from sending ARP Miss messages to the CPU.
   
   
   ```
   [arp miss disable](cmdqueryname=arp+miss+disable)
   ```
   
   By default, a VBDIF interface can send ARP Miss messages to the CPU.
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Verifying the Configuration

Run the [**display interface vbdif**](cmdqueryname=display+interface+vbdif) [ *bd-id* | **main** ] command to check VBDIF interface information.