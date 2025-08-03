Configuring the Device to Output Traps to a Log Host
====================================================

Configuring the Device to Output Traps to a Log Host

#### Context

After configuring the device to output traps to a log host, you can view traps saved on the log host to monitor device operation.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the device to output traps to a log host.
   
   
   * Configure the device to output traps to an IPv4 log host.
     ```
     [info-center loghost](cmdqueryname=info-center+loghost) ipv4-address [ { local-time | utc } | channel { channel-number | channel-name } | { public-net | vpn-instance vpn-instance-name } | source-ip source-ip-address | facility local-num | level level-num | port server-port | transport { udp | tcp  { [ version rfc6587 ] [ ssl-policy policy-name [ [ security ] | [ verify-dns-name dns-name ] ] * ] } } | brief ] *
     ```
   
   
   * Configure the device to output traps to an IPv6 log host.
     ```
     [info-center loghost ipv6](cmdqueryname=info-center+loghost+ipv6) ipv6-address [ { local-time | utc } | channel { channel-number | channel-name } | { public-net | vpn-instance vpn-instance-name } | source-ip source-ipv6-address | facility local-num | level level-num | port server-port | transport { udp | tcp  { [ version rfc6587 ][ ssl-policy policy-name [ [ security ] | [ verify-dns-name dns-name ] ] * ] } } | brief ] *
     ```
     
     The CE6885-LL supports this configuration only in standard forwarding mode.
   
   
   * Configure the device to output traps to a log host with a specified domain name.
     ```
     [info-center loghost domain](cmdqueryname=info-center+loghost+domain) domain-name [ { local-time | utc } | channel { channel-number | channel-name } | { public-net | vpn-instance vpn-instance-name } | source-ip source-ip-address | facility local-num | level level-num | port server-port | transport { udp | tcp  { [ version rfc6587 ] [ ssl-policy policy-name [ [ security ] | [ verify-dns-name dns-name ] ] * ] } } | brief ] *
     ```
3. Configure a rule for outputting traps to a channel.
   
   
   ```
   [info-center source](cmdqueryname=info-center+source) { module-name | default } channel { channel-number | channel-name } trap { state { off | on } | level severity } *
   ```
4. (Optional) Configure the source interface used by the device to send traps to a log host.
   
   
   ```
   [info-center loghost source](cmdqueryname=info-center+loghost+source) { interface-name | interface-type interface-number }
   ```
   
   By default, the source interface for a device to send traps to a log host is the actual interface that sends the traps.
   
   After the source interface is specified, the log host determines the device that sends messages. In this way, the log host can easily retrieve received messages.
5. (Optional) Configure the source port through which the device sends traps to the log host.
   
   
   ```
   [info-center loghost source-port](cmdqueryname=info-center+loghost+source-port) source-port
   ```
   
   By default, the source port number is 38514.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```