Configuring the Device to Output Logs to a Log Host
===================================================

Configuring the Device to Output Logs to a Log Host

#### Context

After configuring the device to output logs to a log host, you can view logs saved on the log host to monitor device operation.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the device to output logs to a log host.
   
   
   * Configure the device to output logs to an IPv4 log host.
     ```
     [info-center loghost](cmdqueryname=info-center+loghost) ipv4-address [ { local-time | utc } | channel { channel-number | channel-name } | { public-net | vpn-instance vpn-instance-name } | source-ip source-ip-address | facility local-num | level level-num | port server-port | transport { udp | tcp  { [ version rfc6587 ] [ ssl-policy policy-name [ [ security ] | [ verify-dns-name dns-name ] ] * ] } } | brief ] *
     ```
   
   
   * Configure the device to output logs to an IPv6 log host.
     ```
     [info-center loghost ipv6](cmdqueryname=info-center+loghost+ipv6) ipv6-address [ { local-time | utc } | channel { channel-number | channel-name } | { public-net | vpn-instance vpn-instance-name } | source-ip source-ipv6-address | facility local-num | level level-num | port server-port | transport { udp | tcp  { [ version rfc6587 ][ ssl-policy policy-name [ [ security ] | [ verify-dns-name dns-name ] ] * ] } } | brief ] *
     ```
     
     The CE6885-LL supports this configuration only in standard forwarding mode.
   
   
   * Configure the device to output logs to a log host with a specified domain name.
     ```
     [info-center loghost domain](cmdqueryname=info-center+loghost+domain) domain-name [ { local-time | utc } | channel { channel-number | channel-name } | { public-net | vpn-instance vpn-instance-name } | source-ip source-ip-address | facility local-num | level level-num | port server-port | transport { udp | tcp  { [ version rfc6587 ] [ ssl-policy policy-name [ [ security ] | [ verify-dns-name dns-name ] ] * ] } } | brief ] *
     ```
3. Configure a rule for outputting logs to a channel.
   
   
   ```
   [info-center source](cmdqueryname=info-center+source) { module-name | default } channel { channel-number | channel-name } log { state { off | on } | level severity } *
   ```
4. (Optional) Configure the source interface used by the device to send logs to a log host.
   
   
   ```
   [info-center loghost source](cmdqueryname=info-center+loghost+source) { interface-name | interface-type interface-number }
   ```
   
   By default, the source interface for a device to send logs to a log host is the actual interface that sends the logs.
   
   After the source interface is specified, the log host determines the device that sends messages. In this way, the log host can easily retrieve received messages.
5. (Optional) Configure the source port through which the device sends logs to the log host.
   
   
   ```
   [info-center loghost source-port](cmdqueryname=info-center+loghost+source-port) source-port
   ```
   
   By default, the source port number is 38514.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   You can run the [**undo info-center loghost character-set**](cmdqueryname=undo+info-center+loghost+character-set) command to configure the character set used by the device to send logs to the log server to be the same as that used by the log server. This prevents garbled characters from being displayed on the log server. By default, the character set used for sending logs to the server is UTF-8.