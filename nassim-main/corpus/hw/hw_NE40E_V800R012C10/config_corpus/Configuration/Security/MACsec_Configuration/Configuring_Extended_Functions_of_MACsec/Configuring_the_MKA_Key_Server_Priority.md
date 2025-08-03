Configuring the MKA Key Server Priority
=======================================

Configuring the MKA Key Server Priority

#### Context

When MACsec is used to encrypt and decrypt data packets, the local device interface and the peer device interface must use the same security key to establish MKA sessions. The key server is responsible for generating and distributing the key. Therefore, you need to configure the priority of the key server on the interfaces of both ends. A smaller value indicates a higher priority. The interface with a higher priority is elected as the key server. If the key servers of the two interfaces have the same priority, the interface with a smaller Secure Channel Identifier (SCI) value is elected as the key server. The SCI is formed based on the MAC address and Port ID.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number* [ .*subinterface-number* ]
   
   
   
   The interface view is displayed.
3. Run [**mka keyserver priority**](cmdqueryname=mka+keyserver+priority) *priority*
   
   
   
   The MKA key server priority is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.