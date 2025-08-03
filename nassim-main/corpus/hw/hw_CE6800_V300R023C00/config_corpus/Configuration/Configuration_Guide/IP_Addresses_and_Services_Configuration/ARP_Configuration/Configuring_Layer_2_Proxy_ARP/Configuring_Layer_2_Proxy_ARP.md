Configuring Layer 2 Proxy ARP
=============================

Configuring Layer 2 Proxy ARP

#### Prerequisites

Before configuring Layer 2 proxy ARP, configure link layer protocol parameters for interfaces to ensure that the link layer protocol status of the interfaces is up.


#### Context

Layer 2 proxy ARP can effectively isolate ARP BDs and reduce the impact of ARP broadcast messages on the network.

![](public_sys-resources/note_3.0-en-us.png) 

When Layer 2 proxy ARP is enabled on a device, ARP snooping is automatically enabled. The device then creates ARP snooping entries by snooping ARP messages. The entries record senders' information.

When most users obtain IP addresses through DHCP, attackers may frequently send bogus ARP messages to attack ARP snooping entries, causing Layer 2 proxy ARP failures. To prevent the preceding issue, run the [**arp l2-proxy learning dynamic-user disable**](cmdqueryname=arp+l2-proxy+learning+dynamic-user+disable) command in the VLAN or Layer 2 sub-interface view to disable ARP snooping entry learning.



#### Procedure

* Configure VLAN-based Layer 2 proxy ARP.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the VLAN view.
     
     
     ```
     [vlan](cmdqueryname=vlan) vlan-id
     ```
  3. Enable Layer 2 proxy ARP.
     
     
     ```
     [arp l2-proxy enable](cmdqueryname=arp+l2-proxy+enable)
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure BD-based Layer 2 proxy ARP.
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
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```