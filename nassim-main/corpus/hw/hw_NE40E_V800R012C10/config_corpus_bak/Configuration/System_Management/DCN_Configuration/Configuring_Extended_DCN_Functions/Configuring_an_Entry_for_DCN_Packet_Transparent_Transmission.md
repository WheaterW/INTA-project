Configuring an Entry for DCN Packet Transparent Transmission
============================================================

To protect services of intersecting ring networks, configure an entry (mapping between source and destination interfaces) for DCN packet transparent transmission. After the entry is configured, the source interface transparently transmits DCN packets to the destination interface.

#### Context

When a large number of NEs are deployed on a DCN network, the network needs to be divided. After the network division, if a large number of NEs are attached to a GNE that resides on more than one ring network, ring network services may affect each other. To address this problem, configure DCN packet transparent transmission.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**dcn**](cmdqueryname=dcn)
   
   
   
   The DCN view is displayed.
3. Run [**transparent-transmission interface**](cmdqueryname=transparent-transmission+interface) { *interface-type1* *interface-number1* | *interface-name1* } to { *interface-type2* *interface-number2* | *interface-name2* }
   
   
   
   An entry is configured for DCN packet transparent transmission.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.