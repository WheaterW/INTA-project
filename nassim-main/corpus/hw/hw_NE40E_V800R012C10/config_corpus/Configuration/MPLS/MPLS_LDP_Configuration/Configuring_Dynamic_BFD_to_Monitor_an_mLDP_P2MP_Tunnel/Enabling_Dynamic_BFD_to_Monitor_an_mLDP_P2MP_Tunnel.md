Enabling Dynamic BFD to Monitor an mLDP P2MP Tunnel
===================================================

Dynamic BFD for mLDP P2MP tunnel can detect the primary tree faults of a P2MP tunnel.

#### Context

Perform the following steps on each root and leaf node:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   BFD is enabled globally.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
5. Run [**mpls mldp bfd enable**](cmdqueryname=mpls+mldp+bfd+enable)
   
   
   
   Dynamic BFD is enabled to monitor an mLDP P2MP tunnel.
6. Run [**mpls mldp p2mp bfd-trigger-tunnel all**](cmdqueryname=mpls+mldp+p2mp+bfd-trigger-tunnel+all)
   
   
   
   A policy is configured to dynamically establish a BFD session to monitor an mLDP P2MP tunnel.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.