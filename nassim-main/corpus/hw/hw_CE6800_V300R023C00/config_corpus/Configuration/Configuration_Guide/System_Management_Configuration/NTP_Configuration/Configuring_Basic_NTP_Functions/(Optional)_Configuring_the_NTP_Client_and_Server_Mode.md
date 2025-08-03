(Optional) Configuring the NTP Client/Server Mode
=================================================

(Optional) Configuring the NTP Client/Server Mode

#### Context

When the client/server mode is used, you need to perform the following configurations on the client:


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Configure the maximum polling interval in unsynchronized mode and the step value by which a polling interval is decreased.
   
   
   ```
   [ntp unsync max-poll-interval](cmdqueryname=ntp+unsync+max-poll-interval) poll-interval-value dec-step step-value
   ```
3. (Optional) Specify the source interface for sending NTP packets.
   
   
   ```
   [ntp](cmdqueryname=ntp) [ ipv6 ] source-interface { interface-name | interface_type interface_num } [ vpn-instance vpnName ]
   ```
   
   By default, no interface is specified for sending NTP packets.
   
   The IP address of the source interface specified in this step must be able to communicate with the IP address of the server specified in the following step. Otherwise, clock synchronization fails.
4. Specify the service mode of the NTP server.
   
   
   ```
   [ntp unicast-server](cmdqueryname=ntp+unicast-server) { ipv4Addr [ version number | authentication-keyid key-id | port port-number | source-interface { interface-name | interface-type interface-number } | vpn-instance vpn-instance-name | preferred | maxpoll max-number | minpoll min-number | burst | iburst | preempt ] * | ipv6 ipv6-address [ authentication-keyid key-id | port port-number | source-interface { interface-name | interface-type interface-number } | vpn-instance vpn-instance-name | preferred | maxpoll max-number | minpoll min-number | burst | iburst | preempt ] * | domain-name [ version number | authentication-keyid key-id | port port-number | source-interface { interface-name | interface-type interface-number } | vpn-instance vpn-instance-name | preferred | maxpoll max-number | minpoll min-number | burst | iburst | preempt ] * }
   ```
   
   
   
   The IP address of the NTP server is a host address and cannot be a broadcast address, a multicast address, or the IP address of the reference clock.
   
   If the **source-interface** parameter is specified, the IP address of the specified source interface must be able to communicate with the configured server IP address. Otherwise, clock synchronization fails.
   
   If the source interface is specified in Step 3 and this step, the configuration in this step takes precedence.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```