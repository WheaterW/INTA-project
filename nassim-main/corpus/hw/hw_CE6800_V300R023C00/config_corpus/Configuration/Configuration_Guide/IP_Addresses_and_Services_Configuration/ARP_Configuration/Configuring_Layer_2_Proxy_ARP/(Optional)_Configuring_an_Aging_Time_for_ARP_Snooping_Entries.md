(Optional) Configuring an Aging Time for ARP Snooping Entries
=============================================================

(Optional) Configuring an Aging Time for ARP Snooping Entries

#### Prerequisites

Before configuring an aging time for ARP snooping entries, enable Layer 2 proxy ARP in the BD view.


#### Context

You can configure an aging time for ARP snooping entries to prevent entry resources from being still consumed after users go offline. This ensures that new access users' ARP snooping entries can be generated normally.


#### Procedure

* Configure an aging time for ARP snooping entries in a BD.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the BD view.
     
     
     ```
     [bridge-domain](cmdqueryname=bridge-domain) bd-id
     ```
  3. Configure an aging time for ARP snooping entries.
     
     
     ```
     [arp l2-proxy timeout](cmdqueryname=arp+l2-proxy+timeout) expire-time
     ```
     
     The default aging time of ARP snooping entries is 900s in a BD.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```