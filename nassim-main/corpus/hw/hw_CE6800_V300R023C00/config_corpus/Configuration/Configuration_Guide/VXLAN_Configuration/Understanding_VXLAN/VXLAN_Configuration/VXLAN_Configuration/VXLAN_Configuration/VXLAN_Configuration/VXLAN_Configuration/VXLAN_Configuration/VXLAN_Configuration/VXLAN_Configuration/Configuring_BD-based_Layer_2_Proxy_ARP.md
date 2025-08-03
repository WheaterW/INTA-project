Configuring BD-based Layer 2 Proxy ARP
======================================

Configuring BD-based Layer 2 Proxy ARP

#### Prerequisites

Before configuring BD-based Layer 2 proxy ARP, you have completed one of the following tasks:

* [Establishing VXLAN Tunnels in Static Mode (Centralized VXLAN Gateway)](dc_vrp_vxlan_cfg_1039.html)
* [Establishing VXLAN Tunnels in BGP EVPN Mode (Centralized VXLAN Gateway)](dc_vrp_vxlan_cfg_1072.html)


#### Context

After a Layer 2 VXLAN gateway receives an ARP request packet, it broadcasts the packet within the BD. If the Layer 2 gateway receives and broadcasts a large number of ARP request packets in a period, too many ARP request packets are forwarded on the VXLAN. This consumes excessive network resources and causes network congestion, resulting in network performance deterioration and affecting user services. To address this problem, Layer 2 proxy ARP can be configured on Layer 2 gateways. Layer 2 proxy ARP follows these basic principles: A Layer 2 gateway listens to a received ARP packet and generates an ARP snooping binding entry to record the source user information, including the source IP and MAC addresses, and inbound interface of the packet. After receiving an ARP request packet, the Layer 2 gateway preferentially responds to the request based on the information in the ARP snooping binding entry.

Perform the following steps on a Layer 2 VXLAN gateway.

![](../public_sys-resources/note_3.0-en-us.png) 

* Layer 2 proxy ARP can be configured by IPv4 overlay networks only.
* No VBDIF interface can be created for a BD enabled with Layer 2 proxy ARP.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the BD view.
   
   
   ```
   [bridge-domain](cmdqueryname=bridge-domain) bd-id
   ```
3. Enable Layer 2 proxy ARP.
   
   
   ```
   [arp l2-proxy enable](cmdqueryname=arp+l2-proxy+enable)
   ```
   
   By default, Layer 2 proxy ARP is not enabled.
4. (Optional) Enable BGP EVPN to collect host information on a per BD basis.
   
   
   ```
   [arp collect host enable](cmdqueryname=arp+collect+host+enable)
   ```
   
   By default, BGP EVPN is not enabled to collect host information on a per BD basis.
   
   If a VXLAN tunnel is established in BGP EVPN mode, it is advised to perform this step on Layer 2 VXLAN gateways. This will allow them to synchronize the locally listened user ARP information with each other through BGP EVPN routes, and complement information in their own ARP snooping binding entries, maximizing the effect of the Layer 2 proxy ARP function.
5. (Optional) Configure an aging time for ARP snooping entries.
   
   
   ```
   [arp l2-proxy timeout](cmdqueryname=arp+l2-proxy+timeout) expire-time
   ```
   
   The default aging time of ARP snooping entries is 900s.
   
   Each ARP snooping binding entry has a life cycle, called aging time. An ARP snooping binding entry will be deleted if it is not updated before its aging time expires. If the device stores a large number of ARP snooping binding entries, the CPU resources are wasted and ARP snooping binding entries for new users cannot be generated. To resolve this problem, perform this step to set an aging time, which allows ARP snooping binding entries to be updated regularly.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```