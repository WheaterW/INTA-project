Configuring BMP
===============

BGP Monitoring Protocol (BMP) allows the BGP running status and route processing records and on network devices to be monitored in real time.

#### Usage Scenario

BMP is mainly used in networking scenarios where monitoring servers exist and need to monitor the BGP running status and route processing records and on network devices in real time. The running status includes the establishment and disconnection of peer relationships and update of routing information. BGP route processing records indicate the process of processing BGP routes on a device, for example, processing of the routes that match an import or export policy. Without BMP, only manual query can be used to obtain the BGP running status and processing records. The emergence of BMP eliminates this restriction and significantly improves network monitoring efficiency.


#### Pre-configuration Tasks

Before configuring BMP, complete the following tasks:

* [Configure basic BGP functions.](dc_vrp_bgp_cfg_3004.html)

#### Procedure

* Configure BMP to report the BGP running status to a monitoring server.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bmp**](cmdqueryname=bmp)
     
     
     
     BMP is enabled, and the BMP view is displayed.
  3. (Optional) Run [**statistics-timer**](cmdqueryname=statistics-timer) *time*
     
     
     
     The interval at which BMP sends BGP running statistics to a monitoring server is configured.
     
     Configure the interval based on BGP stability requirements. In the case of high BGP stability requirements, configure a short interval. However, if the device frequently sends BGP running statistics, a large number of bandwidth resources will be consumed.
  4. Run [**bmp-session**](cmdqueryname=bmp-session+vpn-instance+alias) [ **vpn-instance** *vrf-name* ] *ipv4-address* [ **alias** *alias-name* ]
     
     
     
     An IPv4 session address is set for the TCP connection between the BMP device and the monitoring server.
     
     
     
     **alias** *alias-name* specifies an alias for a BMP session. If the device needs to establish TCP connections with monitoring servers that have the same destination IP address but different destination port numbers, specify different values for the **alias** *alias-name* parameter to differentiate the connections.
  5. Configure the BMP device to send statistics about routes of specific types to the monitoring server.
     
     
     + Configure the BMP device to send statistics about RIB-in routes (all received routes or only accepted routes) of BGP peers in a specified address family to the monitoring server.
       1. Run one of the following commands to enter the BMP-Monitor view:
          - [**monitor public**](cmdqueryname=monitor+public): displays the BMP-Monitor view and allows the BGP running status of all BGP peers in the public network address family to be monitored.
          - [**monitor all-vpn-instance**](cmdqueryname=monitor+all-vpn-instance): displays the BMP-Monitor view and allows the BGP running status of BGP peers in all VPN instance address families to be monitored.
          - [**monitor peer**](cmdqueryname=monitor+peer): displays the BMP-Monitor view and allows the BGP running status of a specified BGP peer in the public address family to be monitored.
          - [**monitor vpn-instance**](cmdqueryname=monitor+vpn-instance): displays the BMP-Monitor view and allows the BGP running status of all BGP peers in a specified VPN instance address family to be monitored.
          - [**monitor vpn-instance peer**](cmdqueryname=monitor+vpn-instance+peer): displays the BMP-Monitor view and allows the BGP running status of a specified BGP peer in a specified VPN instance address family to be monitored.
       2. Run [**route-mode**](cmdqueryname=route-mode+ipv4-family+unicast+ipv4-family+vpnv4+adj-rib-in) { **ipv4-family** **unicast** | **ipv4-family** **labeled-unicast** | **ipv4-family** **vpnv4** } **adj-rib-in** { **pre-policy** | **post-policy** }
          
          The BMP device is configured to send statistics about RIB-in routes of BGP peers in a specified address family and the BGP running status of these peers to the monitoring server.
          
          To configure the device to send statistics about all received routes to the monitoring server, specify **pre-policy** in the command. To configure the device to send statistics about only the routes that match the import policy (those delivered to the routing table) to the monitoring server, specify **post-policy** in the command.
          
          ![](../../../../public_sys-resources/note_3.0-en-us.png) 
          
          If **pre-policy** is specified in the command, run the [**keep-all-routes**](cmdqueryname=keep-all-routes) command in the BGP view to save the routes carried in the BGP Update messages that are received from all BGP peers or peer groups after BGP connections are established, or run the [**peer keep-all-routes**](cmdqueryname=peer+keep-all-routes) command to save the routes carried in the BGP Update messages that are received from a specified BGP peer or peer group after the BGP connection is established.
     + Configure the BMP device to send statistics about RIB-out routes of BGP peers in a specified address family to the monitoring server.
       1. Run one of the following commands to enter the BMP-Monitor view:
          - [**monitor public**](cmdqueryname=monitor+public): displays the BMP-Monitor view and allows the BGP running status of all BGP peers in the public network address family to be monitored.
          - [**monitor all-vpn-instance**](cmdqueryname=monitor+all-vpn-instance): displays the BMP-Monitor view and allows the BGP running status of BGP peers in all VPN instance address families to be monitored.
          - [**monitor peer**](cmdqueryname=monitor+peer): displays the BMP-Monitor view and allows the BGP running status of a specified BGP peer in the public address family to be monitored.
          - [**monitor vpn-instance**](cmdqueryname=monitor+vpn-instance): displays the BMP-Monitor view and allows the BGP running status of all BGP peers in a specified VPN instance address family to be monitored.
          - [**monitor vpn-instance peer**](cmdqueryname=monitor+vpn-instance+peer): displays the BMP-Monitor view and allows the BGP running status of a specified BGP peer in a specified VPN instance address family to be monitored.
       2. Run the [**route-mode**](cmdqueryname=route-mode+ipv4-family+unicast+ipv4-family+vpnv4+adj-rib-out) { **ipv4-family** **unicast** | **ipv4-family** **labeled-unicast** | **ipv4-family** **vpnv4** } **adj-rib-out** { **pre-policy** | **post-policy** } command to configure the BMP device to send statistics about RIB-out routes of BGP peers in a specified address family and the BGP running status of these peers to the monitoring server.
       
       If you want the monitoring server to monitor all the routes to be advertised, regardless of whether they match the export policy, specify **pre-policy** in the command. If you want the monitoring server to monitor only the routes that match the export policy, specify **post-policy** in the command.
     + Configure the BMP device to send statistics about Local-RIB routes of BGP peers in a specified address family to the monitoring server.
       1. Run one of the following commands to enter the BMP-Monitor view:
          - [**monitor public**](cmdqueryname=monitor+public): displays the BMP-Monitor view and allows the BGP running status of all BGP peers in the public network address family to be monitored.
          - [**monitor vpn-instance**](cmdqueryname=monitor+vpn-instance): displays the BMP-Monitor view and allows the BGP running status of all BGP peers in a specified VPN instance address family to be monitored.
       2. Run the [**route-mode**](cmdqueryname=route-mode+ipv4-family+unicast+ipv4-family+vpnv4+local-rib) { **ipv4-family** **unicast** | **ipv4-family** **labeled-unicast** | **ipv4-family** **vpnv4** } **local-rib** [ **add-path** | **all** ] [ **path-marking** ] command to configure the BMP device to send statistics about Local-RIB routes of BGP peers in a specified address family and the BGP running status of these peers to the monitoring server.
  6. Run [**quit**](cmdqueryname=quit)
     
     
     
     Return to the BMP session view.
  7. Run [**tcp**](cmdqueryname=tcp+connect+port+password+md5+keychain) **connect** **port** *port-number* [ **password md5** *cipher-password* | **keychain** *keychain-name* ]
     
     
     
     Parameters for the TCP connection to be established between the device and the monitoring server are configured.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function first.
     
     The MD5 algorithm is not recommended if high security is required.
  8. (Optional) Run [**ssl-policy name**](cmdqueryname=ssl-policy+name) *policy-name*
     
     
     
     An SSL policy is configured for BMP.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     Ensure that the specified SSL policy has been created using the [**ssl policy**](cmdqueryname=ssl+policy) *policy-name* command in the system view.
  9. (Optional) Run [**connect-interface**](cmdqueryname=connect-interface) { *interface-type* *interface-number* | *ipv4-source-address* | *interface-type* *interface-number* *ipv4-source-address* }
     
     
     
     The source interface for sending BMP messages is specified.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If a configuration of a BMP session is changed and the new configuration needs to take effect immediately, run the [**reset bmp session**](cmdqueryname=reset+bmp+session) command to reset the BMP session.
* Configure BMP to report the processing records of IPv4 public network unicast routes to the monitoring server.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bmp**](cmdqueryname=bmp)
     
     
     
     BMP is enabled, and the BMP view is displayed.
  3. Run [**bmp-session**](cmdqueryname=bmp-session+vpn-instance+alias) [ **vpn-instance** *vrf-name* ] *ipv4-address* [ **alias** *alias-name* ]
     
     
     
     An IPv4 BMP session address is specified for the TCP connection to be established between the device and monitoring server.
     
     
     
     **alias** *alias-name* specifies an alias for a session. If the device needs to establish TCP connections with monitoring servers that have the same destination IP address but different destination port numbers, specify different values for the **alias** *alias-name* parameter to differentiate the connections.
  4. Run [**ipv4 unicast**](cmdqueryname=ipv4+unicast)
     
     
     
     The BMP session IPv4 unicast view is created and displayed.
  5. Run the [**trace-prefix all**](cmdqueryname=trace-prefix+all) command to monitor the processing records of all IPv4 public network unicast routes, or run the [**trace-prefix**](cmdqueryname=trace-prefix) *ipv4-address* *mask-length* command to monitor the processing records of a specified IPv4 public network unicast route.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure BMP to report the trace data of VPNv4 routes and the IPv4 VPN unicast routes (transformed from the VPNv4 routes) to the monitoring server.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bmp**](cmdqueryname=bmp)
     
     
     
     BMP is enabled, and the BMP view is displayed.
  3. Run [**bmp-session**](cmdqueryname=bmp-session) [ **vpn-instance** *vrf-name* ] *ipv4-address* [ **alias** *alias-name* ]
     
     
     
     An IPv4 BMP session address is specified for the TCP connection to be established between the device and monitoring server.
     
     
     
     **alias** *alias-name* specifies an alias for a session. If the device needs to establish TCP connections with monitoring servers that have the same destination IP address but different destination port numbers, specify different values for the **alias** *alias-name* parameter to differentiate the connections.
  4. Run [**ipv4 vpn**](cmdqueryname=ipv4+vpn)
     
     
     
     The BMP session IPv4 VPN view is created and displayed.
  5. Run the [**trace-prefix route-distinguisher**](cmdqueryname=trace-prefix+route-distinguisher+all) *vrfRD* **all** command to configure the function of monitoring the processing records of all VPNv4 routes and IPv4 VPN unicast routes based on a specified RD. Alternatively, run the [**trace-prefix route-distinguisher**](cmdqueryname=trace-prefix+route-distinguisher) *vrfRD* *ipv4-address* *mask-length* command to configure the function of monitoring the processing records of the VPNv4 route and IPv4 VPN unicast route based on a specified RD and route prefix.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display bmp session**](cmdqueryname=display+bmp+session+vpn-instance+alias+verbose) [ **vpn-instance** *vrf-name* ] [ *ipv4-address* [ **alias** *alias-name* ] **verbose** ] command to check BMP session configurations.
* Run the [**display bgp bmp-monitor**](cmdqueryname=display+bgp+bmp-monitor+all+ipv4+vpnv4+vpn-instance+vpnv4) { **all** | { **ipv4** | **vpnv4** **vpn-instance** *vpn-instance-name* | **vpnv4** } *ipv4-address* } command to check information about BGP peers monitored through BMP in all address families or in a specified address family.