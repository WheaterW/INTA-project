Configuring the MACsec Encryption Offset
========================================

Configuring_the_MACsec_Encryption_Offset

#### Context

The MACsec encryption offset indicates that encryption starts after the specified offset bytes from the MACsec TAG field. Some applications (such as load balancing) that need to identify the IPv4/IPv6 header require that the packet header not be encrypted. In this case, the encryption offset must be configured.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ .*subinterface-number* ]
   
   
   
   The interface view is displayed.
3. Run [**macsec confidentiality-offset**](cmdqueryname=macsec+confidentiality-offset) *offset-value*
   
   
   
   The MACsec encryption offset is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.