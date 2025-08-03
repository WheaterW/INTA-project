Configuring the BMP Device to Report Local-RIB Routes in the BGP-IPv6-Flow Address Family
=========================================================================================

BGP Monitoring Protocol (BMP) allows the BGP status of devices on the network to be monitored in real time.

#### Usage Scenario

BMP is mainly used on a network where a monitoring server exists and the BGP status of devices on the network needs to be monitored. The status includes the establishment and disconnection of peer relationships and update of routing information. BMP greatly improves the efficiency of network monitoring, because without it, BGP status of devices can be obtained only through manual query.


#### Pre-configuration Tasks

Before configuring BMP, [configure basic BGP4+ functions](dc_vrp_bgp6_cfg_0003.html).


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**bmp**](cmdqueryname=bmp)
   
   
   
   BMP is enabled, and the BMP view is displayed.
3. (Optional) Run [**statistics-timer**](cmdqueryname=statistics-timer) *time*
   
   
   
   An interval at which the BMP device sends BGP4+ running statistics to a monitoring server is configured.
   
   
   
   You can configure the interval at which the BMP device sends BGP4+ running statistics to a monitoring server based on BGP4+ stability requirements. Generally, if high network quality is required, you need to set a small interval for reporting the statistics. However, if the statistics are frequently reported, some network bandwidth resources are occupied.
4. Run [**bmp-session**](cmdqueryname=bmp-session+alias) [ **vpn-instance** *vrf-name* ] *ipv6-address* [ **alias** *alias-name* ]
   
   
   
   An IPv6 session address is specified for the TCP connection to be established between the BMP device and the monitoring server.
   
   
   
   **alias** *alias-name* specifies a session alias. If the device needs to establish TCP connections with monitoring servers that have the same destination IPv6 address but different destination port numbers, specify different values for the **alias** *alias-name* parameter to differentiate the connections.
5. Run one of the following commands to enter the BMP-Monitor view:
   
   
   * [**monitor public**](cmdqueryname=monitor+public): displays the BMP-Monitor view and allows the status of all BGP4+ peers in public address families to be monitored.
   * [**monitor vpn-instance**](cmdqueryname=monitor+vpn-instance): displays the BMP-Monitor view and allows the status of all BGP4+ peers in address families of a specified VPN instance to be monitored.
6. Run [**route-mode**](cmdqueryname=route-mode+ipv6-family+flow+local-rib+report+route-identifier) **ipv6-family** **flow** **local-rib** [ **report route-identifier** ]
   
   
   
   The BMP device is configured to send statistics about Local-RIB routes of BGP4+ peers in the BGP-IPv6-Flow address family to the monitoring server.
7. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the BMP session view.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify the configuration.

* Run the [**display bmp session**](cmdqueryname=display+bmp+session+vpn-instance+alias+verbose) [ **vpn-instance** *vrf-name* ] [ *ipv6-address* [ **alias** *alias-name* ] **verbose** ] command to check BMP session configurations.
* Run the [**display bgp bmp-monitor**](cmdqueryname=display+bgp+bmp-monitor+all) **all** command to check information about all the BGP4+ peers monitored by BMP.