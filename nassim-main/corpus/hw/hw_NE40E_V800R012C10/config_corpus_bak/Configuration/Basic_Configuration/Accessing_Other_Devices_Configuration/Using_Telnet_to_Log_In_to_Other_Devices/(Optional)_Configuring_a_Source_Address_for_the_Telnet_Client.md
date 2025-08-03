(Optional) Configuring a Source Address for the Telnet Client
=============================================================

You can configure a source address for the Telnet client and use the source address to establish a Telnet connection, ensuring file transfer security.

#### Context

You can assign an IP address to an interface on a device and use this IP address as the source address to establish a Telnet connection.

The source of a Telnet client can be a source interface or a source IP address.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**telnet client-source**](cmdqueryname=telnet+client-source) { { **-a** *source-ip-address* | { **-i** *interface-type* *interface-number* | *interface-name* } } } or [**telnet ipv6 client-source**](cmdqueryname=telnet+ipv6+client-source) **-a** *ipv6-address* [ **-vpn-instance** *ipv6-vpn-instance-name* ]
   
   
   
   A source IP address is configured for the Telnet client.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.