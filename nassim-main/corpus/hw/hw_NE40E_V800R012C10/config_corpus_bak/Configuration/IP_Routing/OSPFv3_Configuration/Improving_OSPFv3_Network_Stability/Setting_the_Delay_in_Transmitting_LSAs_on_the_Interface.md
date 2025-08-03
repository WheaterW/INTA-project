Setting the Delay in Transmitting LSAs on the Interface
=======================================================

It takes time to transmit OSPFv3 packets on a link. Therefore, a certain delay is added to the aging time of an LSA before the LSA is sent. This configuration is especially necessary on low-speed links.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The OSPFv3 interface view is displayed.
3. Run [**ospfv3 trans-delay**](cmdqueryname=ospfv3+trans-delay) *interval* [ **instance** *instance-id* ]
   
   
   
   The delay in transmitting LSAs is set on the interface.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.