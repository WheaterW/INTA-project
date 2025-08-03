Configuring the SAK Lifetime
============================

Configuring the SAK Lifetime

#### Context

When MACsec is used for secure communication, the SAK is used to encrypt and decrypt data packets. To ensure the security of data packets, if the number of packets encrypted using one SAK exceeds a certain value or one SAK is used for a certain period of time, replace the SAK.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ .*subinterface-number* ]
   
   
   
   The interface view is displayed.
3. Run [**mka timer sak-life**](cmdqueryname=mka+timer+sak-life) *life-time*
   
   
   
   The SAK lifetime is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.