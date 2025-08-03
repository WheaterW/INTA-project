Enabling NETCONF
================

A NETCONF connection can be established between the client and the server using the well-known port 22 only after NETCONF is enabled on the server.

#### Context

A switch functions as an SSH server to connect to the client through the following two ports:

* Known port 22: Before the SSH server can set up a NETCONF session with the client through this port, the [**snetconf server enable**](cmdqueryname=snetconf+server+enable) command must be run on the SSH server.
* Known port 830: Only the [**protocol inbound ssh port 830**](cmdqueryname=protocol+inbound+ssh+port+830) command needs to be run on the SSH server, but the [**snetconf server enable**](cmdqueryname=snetconf+server+enable) command does not need to be run.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Enable NETCONF.
   
   
   
   Both the [**snetconf server enable**](cmdqueryname=snetconf+server+enable) and [**protocol inbound ssh port 830**](cmdqueryname=protocol+inbound+ssh+port+830) commands can enable the NETCONF function. If both commands are run, the client can use either port 22 or port 830 to set up a NETCONF connection with the server.
   
   * Enable the NETCONF service of the SSH server so that the client can use TCP port 22 to set up a NETCONF connection with the server.
     
     Run [**snetconf**](cmdqueryname=snetconf) [ **ipv4** | **ipv6** ] [**server enable**](cmdqueryname=server+enable)
     
     The NETCONF service of the SSH server is enabled on TCP port 22.
   * Enable the NETCONF service of SSH server on port 830.
     
     1. Run [**netconf**](cmdqueryname=netconf)
        
        The NETCONF user interface view is displayed.
     2. Run [**protocol inbound ssh**](cmdqueryname=protocol+inbound+ssh) [ **ipv4** | **ipv6** ] [**port 830**](cmdqueryname=port+830)
        
        The NETCONF service of SSH server is enabled on port 830.
     3. Run [**quit**](cmdqueryname=quit)
        
        Exit from the NETCONF user interface view.![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   After the NETCONF service of SSH server is disabled on TCP port 22 or 830, all clients connecting to port 22 or 830 through NETCONF are disconnected.
3. (Optional) Set correct NETCONF parameters to ensure secure NETCONF session connections. The default parameters are recommended.
   
   
   1. Run [**netconf**](cmdqueryname=netconf)
      
      The NETCONF user interface view is displayed.
   2. Run [**max-sessions**](cmdqueryname=max-sessions) *count*
      
      The maximum number of NETCONF users that the NETCONF user interface supports is set.
      
      If the maximum number of users that are using NETCONF is reached, subsequent users are prevented from using NETCONF for device operations. This mechanism ensures network management security.
   3. Run [**idle-timeout**](cmdqueryname=idle-timeout) *minutes* [ *seconds* ]
      
      The timeout period of an idle NETCONF connection is set.
      
      If no timeout period is set for an idle NETCONF connection, the idle NETCONF connection cannot be released in time for other authorized users.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.