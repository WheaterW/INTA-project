(Optional) Adjusting Dynamic BFD Parameters
===========================================

You can adjust BFD parameters, including the minimum interval at which BFD packets are sent, the minimum interval at which BFD packets are received, and the BFD detection multiplier.

#### Context

Perform the following steps on each root and leaf node:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bfd**](cmdqueryname=bfd)
   
   
   
   The BFD view is displayed.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Exit the BFD view.
4. Run [**mpls**](cmdqueryname=mpls)
   
   
   
   The MPLS view is displayed.
5. (Optional) Run [**mpls mldp p2mp bfd-tunnel**](cmdqueryname=mpls+mldp+p2mp+bfd-tunnel+min-tx-interval+detect-multiplier) { **min-tx-interval** *tx-interval* | **detect-multiplier** *multiplier* } \*
   
   
   
   The minimum interval at which BFD packets are sent and the BFD detection multiplier are set.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.