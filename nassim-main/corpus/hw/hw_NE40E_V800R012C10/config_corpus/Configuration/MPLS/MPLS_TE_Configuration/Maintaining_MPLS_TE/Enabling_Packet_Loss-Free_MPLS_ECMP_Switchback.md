Enabling Packet Loss-Free MPLS ECMP Switchback
==============================================

Enable packet loss-free MPLS ECMP switchback to prevent packet loss during switchback. ECMP stands for equal-cost multi-path.

#### Context

After configuring an MPLS TE tunnel in an L3VPN over BGP over TE or IP over BGP over TE scenario, you can run the [**mpls load-balance wtr**](cmdqueryname=mpls+load-balance+wtr) command in the system view to enable packet loss-free MPLS ECMP switchback and set the switchback WTR time. This function helps prevent packet loss during switchback.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls load-balance wtr**](cmdqueryname=mpls+load-balance+wtr) *wtr-value*
   
   
   
   The WTR time is set for packet loss-free MPLS ECMP switchback.