Configuring BMP
===============

The BGP Monitoring Protocol (BMP) monitors BGP4+ running status of devices in real time, such as the establishment and termination status of BGP4+ peer relationships and route update status.

#### Usage Scenario

Without BMP, you have to run a query command on a BGP4+ device if you want to learn the BGP4+ running status of the device, which is inconvenient. To improve the network monitoring efficiency, you can configure BMP so that the BGP4+ running status of a client can be monitored by servers.


#### Pre-configuration Tasks

Before configuring BMP, [configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bmp**](cmdqueryname=bmp)
   
   
   
   BMP is started, and the BMP view is displayed.
3. (Optional) Run [**statistics-timer**](cmdqueryname=statistics-timer) *time*
   
   
   
   An interval is set. It determines the frequency at which the BMP device sends BGP4+ running statistics to a monitoring server.
   
   Configure the interval based on BGP4+ stability requirements. In the case of high BGP4+ stability requirements, configure a short interval. However, if the device frequently sends BGP4+ running statistics, a large number of bandwidth resources will be consumed.
4. Run [**bmp-session**](cmdqueryname=bmp-session+vpn-instance+alias) [ **vpn-instance** *vrf-name* ] *ipv6-address* [ **alias** *alias-name* ]
   
   
   
   An IPv6 session address is specified for the TCP connection to be established between the BMP device and the monitoring server.
   
   **alias** *alias-name* specifies an alias for a BMP session. If the device needs to establish multiple TCP connections with the same monitoring server through different port numbers, specify one IPv6 address and different session aliases (through the **alias** *alias-name* parameter) for differentiation.
5. Set the type of route whose statistics are to be sent by the BMP device to the monitoring server.
   
   
   * Configure the BMP device to send statistics about RIB-in routes (of a specified type) of BGP4+ peers in a specified address family to the monitoring server.
     1. Run one of the following commands to enter the BMP-Monitor view:
        + [**monitor public**](cmdqueryname=monitor+public): displays the BMP-Monitor view and allows the BGP4+ running status of all BGP4+ peers in the public network address family to be monitored.
        + [**monitor all-vpn-instance**](cmdqueryname=monitor+all-vpn-instance): displays the BMP-Monitor view and allows the BGP4+ running status of BGP4+ peers in all VPN instance address families to be monitored.
        + [**monitor peer**](cmdqueryname=monitor+peer): displays the BMP-Monitor view and allows the BGP4+ running status of a specified BGP4+ peer in the public address family to be monitored.
        + [**monitor vpn-instance**](cmdqueryname=monitor+vpn-instance): displays the BMP-Monitor view and allows the BGP4+ running status of all BGP4+ peers in a specified VPN instance address family to be monitored.
        + [**monitor vpn-instance peer**](cmdqueryname=monitor+vpn-instance+peer): displays the BMP-Monitor view and allows the BGP4+ running status of a specified BGP4+ peer in a specified VPN instance address family to be monitored.
     2. Run the [**route-mode**](cmdqueryname=route-mode+ipv6-family+unicast+ipv6-family+vpnv6+adj-rib-in) { **ipv6-family** **unicast** | **ipv6-family** **vpnv6** } **adj-rib-in** { **pre-policy** | **post-policy** } command to configure the BMP device to send statistics about RIB-in routes of BGP4+ peers in a specified address family to the monitoring server.
        
        To configure the device to send statistics about all received routes to the monitoring server, specify **pre-policy** in the command. To configure the device to send statistics about only the routes that match the import policy (those delivered to the routing table) to the monitoring server, specify **post-policy** in the command.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        If **pre-policy** is specified in the command, run the [**keep-all-routes**](cmdqueryname=keep-all-routes) command in the BGP view to save the routes carried in the BGP4+ Update messages that are received from all BGP4+ peers or peer groups after BGP4+ connections are established. Alternatively, run the [**peer keep-all-routes**](cmdqueryname=peer+keep-all-routes) command to save the routes carried in the BGP4+ Update messages that are received from a specified BGP4+ peer or peer group after the BGP4+ connection is established.
   * Configure the BMP device to send statistics about RIB-out routes (of a specified type) of BGP4+ peers in a specified address family to the monitoring server.
     1. Run one of the following commands to enter the BMP-Monitor view:
        + [**monitor public**](cmdqueryname=monitor+public): displays the BMP-Monitor view and allows the BGP4+ running status of all BGP4+ peers in the public network address family to be monitored.
        + [**monitor all-vpn-instance**](cmdqueryname=monitor+all-vpn-instance): displays the BMP-Monitor view and allows the BGP4+ running status of BGP4+ peers in all VPN instance address families to be monitored.
        + [**monitor peer**](cmdqueryname=monitor+peer): displays the BMP-Monitor view and allows the BGP4+ running status of a specified BGP4+ peer in the public address family to be monitored.
        + [**monitor vpn-instance**](cmdqueryname=monitor+vpn-instance): displays the BMP-Monitor view and allows the BGP4+ running status of all BGP4+ peers in a specified VPN instance address family to be monitored.
        + [**monitor vpn-instance peer**](cmdqueryname=monitor+vpn-instance+peer): displays the BMP-Monitor view and allows the BGP4+ running status of a specified BGP4+ peer in a specified VPN instance address family to be monitored.
     2. Run the [**route-mode**](cmdqueryname=route-mode+ipv6-family+unicast+ipv6-family+vpnv6+adj-rib-out) { **ipv6-family** **unicast** | **ipv6-family** **vpnv6** } **adj-rib-out** { **pre-policy** | **post-policy** } command to configure the device to send statistics about RIB-out routes of BGP4+ peers in a specified address family to the monitoring server.
        
        If you want the monitoring server to monitor all the routes to be advertised, regardless of whether they match the export policy, specify **pre-policy** in the command. If you want the monitoring server to monitor only the routes that match the export policy, specify **post-policy** in the command.
   * Configure the BMP device to send statistics about Local-RIB routes of BGP4+ peers in a specified address family to the monitoring server.
     1. Run one of the following commands to enter the BMP-Monitor view:
        + [**monitor public**](cmdqueryname=monitor+public): displays the BMP-Monitor view and allows the BGP4+ running status of all BGP4+ peers in the public network address family to be monitored.
        + [**monitor vpn-instance**](cmdqueryname=monitor+vpn-instance): displays the BMP-Monitor view and allows the BGP4+ running status of all BGP4+ peers in a specified VPN instance address family to be monitored.
     2. Run the [**route-mode**](cmdqueryname=route-mode+ipv6-family+unicast+ipv6-family+vpnv6+local-rib) { **ipv6-family** **unicast** | **ipv6-family** **vpnv6** } **local-rib** [ **add-path** | **all** ] [ **path-marking** ] command to configure the BMP device to send statistics about Local-RIB routes of BGP4+ peers in a specified address family to the monitoring server.
6. Run [**quit**](cmdqueryname=quit)
   
   
   
   The BMP session view is displayed.
7. Run [**tcp**](cmdqueryname=tcp+connect+port+password+md5+keychain) **connect** **port** *port-number* [ **password md5** *cipher-password* | **keychain** *keychain-name* ]
   
   
   
   Parameters for the TCP connection to be established between the device and the monitoring server are configured.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function first.
   
   The MD5 algorithm is not recommended if high security is required.
8. (Optional) Run [**connect-interface**](cmdqueryname=connect-interface) { *interface-type* *interface-number* | *ipv6-source-address* | *interface-type* *interface-number* *ipv6-source-address* }
   
   
   
   The source interface for sending BMP messages is specified.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a configuration of a BMP session is changed and the new configuration needs to take effect immediately, run the [**reset bmp session**](cmdqueryname=reset+bmp+session) command to reset the BMP session.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display bmp session**](cmdqueryname=display+bmp+session+vpn-instance+alias+verbose) [ **vpn-instance** *vrf-name* ] [ *ipv6-address* [ **alias** *alias-name* ] **verbose** ] command to check BMP session configurations.
* Run the [**display bgp bmp-monitor**](cmdqueryname=display+bgp+bmp-monitor+all+vpnv6+ipv6+vpnv6+vpn-instance) { **all** | **vpnv6** *ipv4-address* | **ipv6** { *ipv4-address* | *ipv6-address* } | **vpnv6** **vpn-instance** *vpn-instance-name* { *ipv4-address* | *ipv6-address* } } command to check information about all BGP4+ peers or a specified BGP4+ peer monitored through BMP in a specified address family.