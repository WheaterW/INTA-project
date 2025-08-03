Configuring Telnet Server Parameters
====================================

Properly setting parameters for a Telnet server improves network security. Telnet server parameters include a listening port number and source interface.

#### Context

* Listening port number
  
  Attackers may access the default listening port, consuming bandwidth, deteriorating server performance, and causing authorized users unable to log in to the server. After the listening port number of the Telnet server is changed, attackers do not know the new listening port number, which prevents attackers from accessing the listening port.
* Source interface
  
  A Telnet server receives connection requests from all interfaces after a restart with non-base configuration, leading to low system security. To enhance system security, specify a source interface for the Telnet server so that only authorized users can log in to the Telnet server.
  
  If no source interface is specified after the server starts with base configuration, users cannot log in to the server through Telnet.
  
  After a source interface is specified, the system allows Telnet users to log in to the Telnet server only through this source interface. Setting this parameter does not affect the Telnet users who have logged in to the server.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Configure Telnet server parameters.
   
   
   * (Optional) Run [**telnet server port**](cmdqueryname=telnet+server+port) *port-number*
     
     A listening port number is set for the Telnet server.
     
     If a new listening port number is set, the Telnet server terminates all established Telnet connections and uses the new port number to listen for new Telnet connection requests.
   * Configure the source interface or source address for the Telnet server.
     
     + Run [**telnet server-source**](cmdqueryname=telnet+server-source) **-i** { *interface-type* *interface-number* | *interface-name* }The source interface is specified for the Telnet server.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       If you specify a logical interface as the source interface of the Telnet server, this interface must have been created. Otherwise, the command cannot be executed successfully.
     + Run [**telnet server-source**](cmdqueryname=telnet+server-source) **all-interface**
       
       Any interface on the Telnet server can be used as its source interface.
       
       After the command is run, users can log in to the Telnet server through any physical interface configured with an IPv4 address or any created logical interface configured with an IPv4 address.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       If the [**telnet server-source**](cmdqueryname=telnet+server-source) **all-interface** command is run, users can log in to the Telnet server through any interface with a valid IPv4 address, which increases system security risks. Therefore, running the command is not recommended.
     + Run [**telnet ipv6 server-source**](cmdqueryname=telnet+ipv6+server-source) **-a** *ipv6-address* [ **-vpn-instance** *vpn-instance-name* ]
       
       A source IPv6 address is specified for the Telnet server.
       
       If a source IPv6 address is specified, the Telnet server allows users to log in using this source IPv6 address only and denies access of the users who attempt to log in using other IPv6 addresses.
     + Run [**telnet ipv6 server-source**](cmdqueryname=telnet+ipv6+server-source) **all-interface**
       
       The IPv6 address of any interface on the Telnet server can be used as the source IPv6 address of the Telnet server.
       
       After the command is run, users can log in to the Telnet server through any physical interface configured with an IPv6 address or any created logical interface configured with an IPv6 address.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       If the [**telnet ipv6 server-source**](cmdqueryname=telnet+ipv6+server-source) **all-interface** command is run, users can log in to the Telnet server through any valid interface IPv6 address, which increases system security risks. Therefore, running the command is not recommended.
     + Run [**telnet server-source**](cmdqueryname=telnet+server-source) **physic-isolate** **-i** { *interface-type* *interface-number* | *interface-name* } **-a** *ip-address*
       
       A source IPv4 interface is specified for the Telnet server, and the interface isolation attribute is set for the Telnet server.
     + Run [**telnet ipv6 server-source**](cmdqueryname=telnet+ipv6+server-source) **physic-isolate** **-i** { *interface-type* *interface-number* | *interface-name* } **-a** *ipv6-address*A source IPv6 interface is specified for the Telnet server, and the interface isolation attribute is set for the Telnet server.![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       After the interface isolation attribute is set successfully, packets can be sent to the server only through the specified physical interface, and those sent through other interfaces are discarded.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.