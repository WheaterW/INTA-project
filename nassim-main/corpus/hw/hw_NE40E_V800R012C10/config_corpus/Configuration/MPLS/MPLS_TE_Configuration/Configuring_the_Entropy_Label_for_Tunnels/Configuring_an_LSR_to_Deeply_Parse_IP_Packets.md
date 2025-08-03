Configuring an LSR to Deeply Parse IP Packets
=============================================

This section describes how to enable an LSR to deeply parse IP packets.

#### Context

After the entropy label function is enabled on the LSR, the LSR uses IP header information to generate an entropy label and adds the label to the packets. The entropy label is used as a key value by a transit node to load-balance traffic. If the length of a data frame carried in a packet exceeds the parsing capability, the LSR fails to parse the IP header or generate an entropy label. Perform the following operations on the LSR:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**load-balance identify entropy-label**](cmdqueryname=load-balance+identify+entropy-label)
   
   
   
   The LSR is enabled to deeply parse IP packets.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.