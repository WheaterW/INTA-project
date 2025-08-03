Importing Labeled Routes to a Public Network's Unicast Routing Table
====================================================================

To allow mutual access between public network users and
users with labeled routes, configure labeled routes to be imported
into the public network's unicast routing table.

#### Procedure

* Import labeled routes to a public network's unicast
  routing table.
  
  Perform the following steps on each ASBR:
  
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**import-rib public labeled-unicast**](cmdqueryname=import-rib+public+labeled-unicast)
     
     
     
     Labeled routes are imported to the public network's unicast
     routing table.