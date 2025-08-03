(Optional) Changing a Login User Role
=====================================

You can use different user roles to log in to an FTP server.

#### Context

After you log in to an FTP server from a device functioning as an FTP client, you can use another user name to log in to the server. Changing a login user role does not affect the current FTP connection. That is, FTP control and data connections and the connection status do not change.

If you entered an incorrect user name or password, the current FTP connection is ended. To log in to the server again, you must enter a correct user name and name.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

After logging in to the HUAWEI NE40E-M2 series, you can log in to the FTP server by using another user name without logging out of the FTP client view. The established FTP connection is identical with that established by running the [**ftp**](cmdqueryname=ftp) command.



#### Procedure

1. Perform either of the following steps on the client, based on the type of the server's IP address:
   
   
   * Run the [**ftp**](cmdqueryname=ftp) [ [ **-a** *source-ip-address* | **-i** { *interface-type interface-number* | *interface-name* } ] *host-ip* [ *port-number* ] [ **vpn-instance** *vpn-instance-name* ] | **public-net** ] command to configure the device to use an IPv4 address to establish a connection to the FTP server and enter the FTP client view.
   * Run the [**ftp**](cmdqueryname=ftp) **ipv6** [ **-a** *source-ip6* ] *host-ipv6-address* [ [ **vpn-instance** *ipv6-vpn-instance-name* ] | **public-net** ] [ **-oi** { *interface-type interface-number* | *interface-name* } ] [ *port-number* ] command to configure the device to use an IPv6 address to establish a connection to the FTP server and enter the FTP client view.
2. Run [**user**](cmdqueryname=user) *user-name*
   
   
   
   The login user role is changed.
   
   
   
   After the login user role is changed, the connection between the original user role and the FTP server is ended.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   Only FTP users at Level 3 or higher can run the [**user**](cmdqueryname=user) *user-name* command to change the user role and log in to the FTP server.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.