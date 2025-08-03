(Optional) Enabling 6PE Routes Sharing the Explicit Null Label
==============================================================

By enabling IPv6 provider edge (6PE) routes sharing the explicit null label, you can save label resources on 6PE devices.

#### Context

By default, the 6PE device applies for a label for each 6PE route. When a large number of 6PE routes need to be sent, a large number of labels are required. This greatly wastes label resources and causes IPv6 routes unable to be advertised due to the shortage of label resources.

After 6PE routes sharing the explicit null label is enabled, all 6PE routes to be sent to the same 6PE peer share the explicit null label 2.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bgp**](cmdqueryname=bgp) *as-number*
   
   
   
   The BGP view is displayed.
3. Run [**ipv6-family unicast**](cmdqueryname=ipv6-family+unicast)
   
   
   
   The BGP-IPv6 unicast address family view is displayed.
4. Run [**apply-label explicit-null**](cmdqueryname=apply-label+explicit-null)
   
   
   
   All 6PE routes to be sent to the same 6PE peer share the explicit null label.
   
   If you run this command after a 6PE peer relationship is established, temporary packet loss occurs.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.