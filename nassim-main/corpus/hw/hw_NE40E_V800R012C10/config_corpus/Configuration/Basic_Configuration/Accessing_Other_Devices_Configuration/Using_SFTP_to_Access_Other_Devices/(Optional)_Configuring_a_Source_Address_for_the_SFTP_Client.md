(Optional) Configuring a Source Address for the SFTP Client
===========================================================

You can configure a source address for an SFTP client and use the source address to establish an SFTP connection, ensuring file transfer security.

#### Context

You can assign an IP address to an interface on the SFTP client and use this IP address as the source address to establish an SFTP connection.

The source address for an SFTP client can be either a source interface or a source IP address.

Perform the following steps on the device functioning as an SFTP client:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure an SFTP source IP address or source interface as required.
   
   
   * In IPv4 scenarios, run the [**sftp client-source -a**](cmdqueryname=sftp+client-source+-a) *source-ip-address* { **public-net** | **-vpn-instance** *vpn-instance-name* } } or [**sftp client-source -i**](cmdqueryname=sftp+client-source+-i) { *interface-type* *interface-number* | *interface-name* } command.
   * In IPv6 scenarios, run the [**sftp ipv6 client-source**](cmdqueryname=sftp+ipv6+client-source) **-a** *source-ipv6-address* [ **-vpn-instance** *ipv6-vpn-instance-name* ] command.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.