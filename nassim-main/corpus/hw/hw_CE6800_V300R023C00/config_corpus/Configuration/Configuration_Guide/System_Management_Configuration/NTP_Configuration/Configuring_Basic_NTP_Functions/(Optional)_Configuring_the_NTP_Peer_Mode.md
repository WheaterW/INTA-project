(Optional) Configuring the NTP Peer Mode
========================================

(Optional) Configuring the NTP Peer Mode

#### Context

When the peer mode is used, you need to perform the following configurations on the symmetric active peer:


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
4. Perform any of the following steps to specify the symmetric passive peer:
   
   
   ```
   [ntp unicast-peer](cmdqueryname=ntp+unicast-peer) { ipv4Addr [ version number | port port-number | authentication-keyid key-id | source-interface { interface-name | interface-type interface-number } | vpn-instance vpn-instance-name | preferred | maxpoll max-number | minpoll min-number | preempt ] * | ipv6 ipv6Addr [ authentication-keyid key-id | port port-number | source-interface { interface-name | interface-type interface-number } | vpn-instance vpn-instance-name | preferred | maxpoll max-number | minpoll min-number | preempt ] * | domain domain-name [ version number | port port-number | authentication-keyid key-id | source-interface { interface-name | interface-type interface-number } | vpn-instance vpn-instance-name | preferred | maxpoll max-number | minpoll min-number | preempt ] * }
   ```
   
   
   
   The IP address of the symmetric passive peer is a host address and cannot be a broadcast address, a multicast address, or the IP address of the reference clock.
   
   If the **source-interface** parameter is specified, the configured server IP address must be able to communicate with the IP address of the specified source interface. Otherwise, clock synchronization fails.
   
   If the source interface is specified in Step 3 and this step, the configuration in this step takes precedence.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```