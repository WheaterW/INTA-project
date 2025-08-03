Enabling the Detection of Traffic with New mLDP MBB Incoming Labels
===================================================================

After the detection of traffic with new mLDP MBB incoming labels is enabled, an MBB switchover can be performed as soon as possible after a fault occurs, reducing traffic loss.

#### Context

On a network with mLDP MBB enabled, if a network path fails, transient packet loss occurs because of the delayed switching timer for MBB LSPs on a downstream node. To prevent packet loss, enable the local device to monitor traffic with new mLDP MBB incoming labels.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**mpls ldp**](cmdqueryname=mpls+ldp)
   
   
   
   The MPLS-LDP view is displayed.
3. Run [**mldp p2mp**](cmdqueryname=mldp+p2mp)
   
   
   
   mLDP P2MP is enabled globally.
4. Run [**mldp make-before-break**](cmdqueryname=mldp+make-before-break)
   
   
   
   The mLDP make-before-break (MBB) capability is enabled.
5. Run [**mldp make-before-break p2mp traffic-detect**](cmdqueryname=mldp+make-before-break+p2mp+traffic-detect)
   
   
   
   The detection of traffic with new mLDP MBB incoming labels is enabled.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.