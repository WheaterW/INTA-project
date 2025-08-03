Configuring FTP Server Parameters
=================================

Configuring proper parameters for the FTP server ensures device security and maximizes resource usage efficiency.

#### Context

FTP server parameters can be configured as follows:

* Specifying the source address or source interface of the FTP server restricts the destination address accessed by clients, ensuring security.
* You can configure the maximum number of FTP connections to the server. If the maximum number of FTP connections is less than or equal to the existing FTP connections, the system retains the existing FTP connections but rejects new connection requests.
* You can configure the timeout period of an idle FTP connection. If no messages are exchanged between the client and the FTP server within the specified timeout period, the connection between them is terminated and FTP connection resources are reclaimed.

Perform the following steps on the device to be used as an FTP server:


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. To configure the source address or source interface of the FTP server, perform one of the following operations as required:
   
   
   * Run the [**ftp server-source**](cmdqueryname=ftp+server-source) { **-a** *ip-address* | **i** { *interface-type* *interface-number* | *interface-name* } } command to configure a source IP address for the FTP server.
     
     After the source IP address is configured, the address specified in the [**ftp**](cmdqueryname=ftp) command for login to the FTP server must be the configured source IP address. Otherwise, the login fails.
   * Run the [**ftp server-source**](cmdqueryname=ftp+server-source)**all-interface** command to allow any interface having an IPv4 address configured to be used as the source interface of an FTP server.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     After this command is run, the FTP server will receive login connection requests from all interfaces, which increases system security risks. Therefore, running this command is not recommended.
   * Run the [**ftp ipv6 server-source**](cmdqueryname=ftp+ipv6+server-source) **-a** *ipv6-address* [ **-vpn-instance** *vpn-instance-name* ] command to configure a source IPv6 address for the FTP server.
   * Run the [**ftp ipv6 server-source**](cmdqueryname=ftp+ipv6+server-source)**all-interface** command to allow any interface having an IPv6 address configured to be used as the source interface of an FTP server.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     After this command is run, the FTP server will receive login connection requests from all interfaces with an IPv6 address configured, which increases system security risks. Therefore, running this command is not recommended.
   * Run the [**ftp server-source**](cmdqueryname=ftp+server-source) **physic-isolate** **-i** { *interface-type* *interface-number* | *interface-name* } **-a** *ip-address* command to specify a source IPv4 interface for the FTP server and set the interface isolation attribute for the FTP server.
   * Run the [**ftp ipv6 server-source**](cmdqueryname=ftp+ipv6+server-source) **physic-isolate** **-i** { *interface-type* *interface-number* | *interface-name* } **-a** *ipv6-address* command to specify a source IPv6 interface for the FTP server and set the interface isolation attribute for the FTP server.![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     After the interface isolation attribute is set successfully, packets can be sent to the server only through the specified physical interface, and those sent through other interfaces are discarded.
3. (Optional) Run [**ftp server max-sessions**](cmdqueryname=ftp+server+max-sessions) *max-sessions-num*
   
   
   
   The maximum number of FTP connections to the server is set.
4. (Optional) Run [**ftp**](cmdqueryname=ftp) [ **ipv6** ] **timeout** *minutes*
   
   
   
   A timeout period of an idle FTP connection is configured.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.