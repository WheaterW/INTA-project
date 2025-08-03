Configuring a Source Address for a TFTP Client
==============================================

You can configure a source address for a TFTP client and use the source address to establish a TFTP connection, ensuring file transfer security.

#### Context

You can assign an IP address to an interface on a TFTP client and use this IP address as the source address to establish a TFTP connection.

Perform the following steps on the Router that functions as a TFTP client:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**tftp client-source**](cmdqueryname=tftp+client-source) { **-a** *ip-address* | **-i** { *interface-type* *interface-number* | *interface-name* } } or [**tftp ipv6 client-source**](cmdqueryname=tftp+ipv6+client-source) **-a** *ipv6-address* [ **-vpn-instance** *ipv6-vpn-instance-name* ]
   
   
   
   A source address is configured for the TFTP client.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The interface type specified by *interface-type* must be loopback.
   
   After configuring a source address for a TFTP client, ensure that the source address of the TFTP client displayed on the server is the same as the configured one.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.