Enabling Defense Against Fragmented Packet Attacks
==================================================

Defense against fragmented packet attacks protects the CPU by restricting the sending rate of fragmented packets and ensuring the correctness of packet reassembly.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed
2. Run [**cpu-defend policy**](cmdqueryname=cpu-defend+policy) *policy-number*
   
   
   
   The attack defense policy view is displayed.
3. Run [**fragment-flood enable**](cmdqueryname=fragment-flood+enable)
   
   
   
   Defense against fragmented packet attacks is enabled.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.