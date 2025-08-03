(Optional) Configuring the Maximum Number of ARP Snooping Entries
=================================================================

(Optional) Configuring the Maximum Number of ARP Snooping Entries

#### Prerequisites

Before configuring the maximum number of ARP snooping entries, you have completed the following tasks:

* Enable Layer 2 proxy ARP in the BD view.
* Configure different traffic encapsulation types for Layer 2 sub-interfaces to transmit various types of data packets.

#### Context

You can configure the maximum number of ARP snooping entries to prevent the entries from consuming excessive system resources. This ensures the normal running of services.


#### Procedure

* Configure the maximum number of ARP snooping entries that a Layer 2 sub-interface can learn.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Create a Layer 2 sub-interface and enter its view.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number.subinterface-number mode l2
     ```
  3. Add the Layer 2 sub-interface to a BD.
     
     
     ```
     [bridge-domain](cmdqueryname=bridge-domain) bd-id
     ```
  4. Configure the maximum number of ARP snooping entries that the Layer 2 sub-interface can learn.
     
     
     ```
     [arp l2-proxy learning dynamic-user max-user](cmdqueryname=arp+l2-proxy+learning+dynamic-user+max-user) max-user-number
     ```
     
     The default maximum number of ARP snooping entries that a Layer 2 sub-interface can learn is set to 0, indicating that the maximum number of ARP snooping entries is not limited.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```