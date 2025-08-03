(Optional) Configuring the Maximum Number of ARP Snooping Entries
=================================================================

You can configure the maximum number of ARP snooping entries on a sub-interface to prevent the entries from consuming excessive system resources. This ensures the normal running of services.

#### Prerequisites

Layer 2 proxy ARP has been enabled using the [**arp l2-proxy enable**](cmdqueryname=arp+l2-proxy+enable) command in the BD view.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number.subnum* **mode l2**
   
   
   
   A Layer 2 sub-interface is created and its view is displayed.
3. Run [**encapsulation**](cmdqueryname=encapsulation) { **dot1q** [ **vid** *vid* ] | **default** | **untag** | **qinq** [ **vid** *pe-vid* **ce-vid** { *low-ce-vid* [ **to** *high-ce-vid* ] } ] }
   
   
   
   A traffic encapsulation type is configured for the Layer 2 sub-interface.
4. Run [**arp l2-proxy learning dynamic-user max-user**](cmdqueryname=arp+l2-proxy+learning+dynamic-user+max-user) *max-user-number*
   
   
   
   The maximum number of ARP snooping entries is configured.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.