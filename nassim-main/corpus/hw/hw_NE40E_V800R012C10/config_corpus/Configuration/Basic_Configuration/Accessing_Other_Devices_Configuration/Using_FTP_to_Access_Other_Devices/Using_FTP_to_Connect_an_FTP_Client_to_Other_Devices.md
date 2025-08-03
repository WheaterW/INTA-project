Using FTP to Connect an FTP Client to Other Devices
===================================================

FTP commands can be used to log in to other devices from an FTP client.

#### Context

Commands can be run in the user or FTP client view to establish connections to remote FTP servers.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

* If the [**ftp**](cmdqueryname=ftp) command without any parameters is used in the user view to establish a control connection to an FTP server, the FTP client view is displayed but the connection is not established.
* When you run the [**ftp**](cmdqueryname=ftp) command in the user view or the [**open**](cmdqueryname=open) in the FTP client view to establish a control connection to a remote FTP server using the default listening port number of the FTP server, you do not need to specify a listening port number in the command. Otherwise, you must specify a listening port number in the command.
* Before logging in to the FTP server, you can run the [**set net-manager vpn-instance**](cmdqueryname=set+net-manager+vpn-instance) command to configure a default VPN instance. After a default VPN instance is configured, it will be used for FTP operations.

Perform either of the following operations on the FTP client based on the type of the server's IP address:


#### Procedure

* If the server has an IPv4 address, use commands described in [Table 1](#EN-US_TASK_0172360099__tab_dc_vrp_basic_cfg_009601) to connect the client to other devices.
  
  
  
  **Table 1** Using FTP commands to connect the FTP client to other devices
  | View | Operation |
  | --- | --- |
  | User view | Run the [**ftp**](cmdqueryname=ftp) [ **-a** *source-ip-address* | { **-i** *interface-type interface-number* | *interface-name* } ] *host-ip* [ *port-number* ] [ **public-net |** **vpn-instance** *vpn-instance-name* ] command to establish a connection to the FTP server. |
  | FTP client view | Run the [**open**](cmdqueryname=open) [ **-a** *source-ip* | { **-i** *interface-type interface-number* | *interface-name* } ] *host-ip-address* [ *port-number* ] [ **public-net |** **vpn-instance** *vpn-instance-name* ] command to establish a connection to the FTP server. |
* If the server has an IPv6 address, use commands described in [Table 2](#EN-US_TASK_0172360099__tab_dc_vrp_basic_cfg_009602) to connect the client to other devices.
  
  
  
  **Table 2** Using FTP commands to connect the FTP client to other devices
  | View | Operation |
  | --- | --- |
  | User view | Run the [**ftp**](cmdqueryname=ftp) **ipv6** [ **-a** *source-ip6* ] *host-ipv6-address* [ [ **vpn-instance** *ipv6-vpn-instance-name* ] | **public-net** ] [ **-oi** { *interface-type interface-number* | *interface-name* } ] [ *port-number* ] command to establish a connection to the FTP server. |
  | FTP client view | Run the [**open**](cmdqueryname=open) **ipv6** [ **-a** *source-ip6* ] *host-ipv6-address* [ **-oi** { **-i** *interface-type interface-number* | *interface-name* } ] [ *port-number* ] [ **vpn-instance** *vpn-instance* | **public-net** ] command to establish a connection to the FTP server. |