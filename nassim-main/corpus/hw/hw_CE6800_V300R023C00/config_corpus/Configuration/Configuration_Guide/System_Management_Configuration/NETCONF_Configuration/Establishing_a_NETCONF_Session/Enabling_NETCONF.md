Enabling NETCONF
================

Enabling NETCONF

#### Context

A NETCONF connection can be established between the client and server using the well-known port 22 only after NETCONF is enabled on the server.

A device functioning as an SSH server can establish a NETCONF connection with a client through the following two ports:

* Well-known port 22: Before the SSH server can set up a NETCONF session with the client through this port, the [**snetconf server enable**](cmdqueryname=snetconf+server+enable) command must be run on the SSH server.
* Well-known port 830: Only the [**protocol inbound ssh port 830**](cmdqueryname=protocol+inbound+ssh+port+830) command needs to be run on the SSH server (running the [**snetconf server enable**](cmdqueryname=snetconf+server+enable) command is not required).


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable NETCONF.
   
   
   
   Both the [**snetconf server enable**](cmdqueryname=snetconf+server+enable) and [**protocol inbound ssh port 830**](cmdqueryname=protocol+inbound+ssh+port+830) commands can enable NETCONF. If both commands are run, the client can use either port 22 or port 830 to set up a NETCONF connection with the server.
   
   * Enable the NETCONF service of the SSH server so that the client can use TCP port 22 to set up a NETCONF connection with the server.
     
     ```
     [snetconf](cmdqueryname=snetconf) [ ipv4 | ipv6 ] [server enable](cmdqueryname=server+enable)
     ```
   * Enable the NETCONF service of the SSH server so that the client can use TCP port 830 to set up a NETCONF connection with the server.
     
     ```
     [netconf](cmdqueryname=netconf)
     [protocol inbound ssh](cmdqueryname=protocol+inbound+ssh) [ ipv4 | ipv6 ] [port 830](cmdqueryname=port+830)
     [quit](cmdqueryname=quit)
     [commit](cmdqueryname=commit)
     ```![](public_sys-resources/notice_3.0-en-us.png) 
   
   After the NETCONF service of the SSH server is disabled on TCP port 22 or 830, all clients connecting to port 22 or 830 through NETCONF are disconnected.
3. (Optional) Set NETCONF parameters as required. Using default values is recommended.
   
   
   
   **Table 1** NETCONF parameters
   | Operation | Command | Description |
   | --- | --- | --- |
   | Configure the maximum number of NETCONF users that the NETCONF user interface supports. | [**netconf**](cmdqueryname=netconf)  [**max-sessions**](cmdqueryname=max-sessions) *count* | If the maximum number of users that are using NETCONF is reached, subsequent users are prevented from using NETCONF for device operations. This mechanism ensures network management security.  By default, a maximum of 15 NETCONF users are permitted to access the SSH server. |
   | Configure the timeout period for disconnecting from the NETCONF user interface. | [**netconf**](cmdqueryname=netconf)  [**idle-timeout**](cmdqueryname=idle-timeout) *minutes* [ *seconds* ] | If no timeout period is set for an idle NETCONF connection, other authorized users may not obtain idle NETCONF connections. That is, authorized users cannot use NETCONF to manage the device.  The default timeout period is 10 minutes. |
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```