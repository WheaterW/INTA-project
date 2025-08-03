(Optional) Configuring a Source Address for an FTP Client
=========================================================

You can configure a source address for an FTP client and use the source address to establish an FTP connection, ensuring file transfer security.

#### Context

You can assign an IP address to an interface on an FTP client and use this IP address as the source address to establish an FTP connection.

Perform the following steps on the Router that functions as an FTP client:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ftp client-source**](cmdqueryname=ftp+client-source) { **-a** *ip-address* | **-i** { *interface-type* *interface-number* | *interface-name* } } or [**ftp ipv6 client-source**](cmdqueryname=ftp+ipv6+client-source) **-a** *ipv6-address* [ **-vpn-instance** *ipv6-vpn-instance-name* ]
   
   
   
   A source address is configured for the FTP client.
   
   
   
   After configuring a source address for an FTP client, run the [**display ftp-users**](cmdqueryname=display+ftp-users) command on the FTP server to check that the source address of the FTP client displayed in the command output is the same as the configured one.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.