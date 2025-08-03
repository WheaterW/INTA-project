Ending a Connection to the FTP Server
=====================================

To save system resources and ensure successful logins of authorized users to the FTP server, end connections to the FTP server.

#### Context

After the number of users logging in to an FTP server reaches the upper limit, no more authorized users can log in. To allow authorized users to log in to the FTP server, end idle connections to the FTP server.


#### Procedure

1. Perform either of the following steps on the client, based on the type of the server's IP address:
   
   
   * Run the [**ftp**](cmdqueryname=ftp) [ [ **-a** *source-ip-address* | **-i** { *interface-type interface-number* | *interface-name* } ] *host-ip* [ *port-number* ] [ **vpn-instance** *vpn-instance-name* ] | **public-net** ] command to configure the device to use an IPv4 address to establish a connection to the FTP server and enter the FTP client view.
   * Run the [**ftp**](cmdqueryname=ftp) **ipv6** [ **-a** *source-ip6* ] *host-ipv6-address* [ [ **vpn-instance** *ipv6-vpn-instance-name* ] | **public-net** ] [ **-oi** { *interface-type interface-number* | *interface-name* } ] [ *port-number* ] command to configure the device to use an IPv6 address to establish a connection to the FTP server and enter the FTP client view.
2. Perform either of the following operations as needed to end an FTP connection.
   
   
   * Run the [**bye/quit**](cmdqueryname=bye%2Fquit) command to end the connection to the FTP server and return to the user view.
   * Run the [**close/disconnect**](cmdqueryname=close%2Fdisconnect) command to end both the connection to the FTP server and the FTP session and remain in the FTP client view.