Configuring the SFTP Client to Use the One-click File Operation Command to Perform File Operations
==================================================================================================

The device functions as an SFTP client and uses the one-click file operation command to upload files from the SFTP client to the SFTP server or download files from the SFTP server to the SFTP client.

#### Prerequisites

The SFTP server has been configured, and the SFTP client and server have reachable routes to each other.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command
   
   
   
   The system view is displayed.
2. Run the [**ssh client first-time enable**](cmdqueryname=ssh+client+first-time+enable) command
   
   
   
   First-time authentication is enabled on the SSH client.
3. Run the [**commit**](cmdqueryname=commit) command
   
   
   
   The configuration is committed.
4. Perform either of the following steps based on a network protocol:
   
   
   * Establish an SFTP connection based on an IPv4 network.
     
     Run the [**sftp client-transfile**](cmdqueryname=sftp+client-transfile) {**get** | **put** }[ **-a***source-address* | **-i** { *interface-type interface-number* | *interface-name* } ] **host-ip***host-ipv4* [ *port* ] [ [ **public-net** | **-vpn-instance***vpn-instance-name* ] | [ **prefer\_kex** { *prefer\_kex* } ] | [ **identity-key***identity-key-type* ] | [ **prefer\_ctos\_cipher***prefer\_ctos\_cipher* ] | [ **prefer\_stoc\_cipher***prefer\_stoc\_cipher* ] | [ **prefer\_ctos\_hmac***prefer\_ctos\_hmac* ] | [ **prefer\_stoc\_hmac***prefer\_stoc\_hmac* ] | [ **-ki***interval* ] | [ **-kc***count* ] ] \* **username***user-name***password***password***sourcefile***destination* [ **destination***source-file* ] command to connect to the SFTP server in IPv4 mode and download files from the SFTP server to the SFTP client or upload files from the SFTP client to the SFTP server.
   * Establish an SFTP connection based on an IPv6 network.
     
     Run the [**sftp client-transfile**](cmdqueryname=sftp+client-transfile){ **put** | **get** }**ipv6**[ **-a***source-ipv6-address* ] **host-ip***host-ipv6* [ **-oi** { *interface-type**interface-number* | *interface-name* } ] [ *port* ] [ [ **public-net** | **-vpn-instance***vpn-instance-name* ] | [ **prefer\_kex** { *prefer\_kex* } ] | [ **identity-key***identity-key-type* ] | [ **prefer\_ctos\_cipher***prefer\_ctos\_cipher* ] | [ **prefer\_stoc\_cipher***prefer\_stoc\_cipher* ] | [ **prefer\_ctos\_hmac***prefer\_ctos\_hmac* ] | [ **prefer\_stoc\_hmac***prefer\_stoc\_hmac* ] | [ **-ki***interval* ] | [ **-kc***count* ] ] \***username***user-name***password***password***sourcefile***source-file* [ **destination***destination* ] command to connect to the SFTP server in IPv6 mode and download files from the SFTP server to the SFTP client or upload files from the SFTP client to the SFTP server.