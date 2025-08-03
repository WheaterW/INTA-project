(Optional) Configuring the NTP Manycast Mode
============================================

(Optional) Configuring the NTP Manycast Mode

#### Context

When the manycast mode is used, you need to perform the following configurations on both the manycast server and client.


#### Procedure

* Configure an NTP manycast server.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure the interface used for sending NTP manycast packets.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Configure the local device as the NTP manycast server.
     
     
     
     Run either of the following commands depending on whether the server IP address is an IPv4 or IPv6 address:
     
     ```
     [ntp manycast-server](cmdqueryname=ntp+manycast-server) [ ip-address ]
     ```
     ```
     [ntp manycast-server](cmdqueryname=ntp+manycast-server) ipv6 [ ipv6-address ]
     ```
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure an NTP manycast client.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure the interface used for receiving NTP manycast packets.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Configure the local device as the NTP manycast client.
     
     
     
     Run either of the following commands depending on whether the client IP address is an IPv4 or IPv6 address:
     
     ```
     [ntp manycast-client](cmdqueryname=ntp+manycast-client) [ ip-address ] [ authentication-keyid key-id | ttl ttl-number | port port-number ] *
     ```
     ```
     [ntp manycast-client ipv6](cmdqueryname=ntp+manycast-client+ipv6) [ ipv6-address ] [ authentication-keyid key-id | ttl ttl-number | port port-number ] *
     ```
     
     After the configuration is complete, the NTP manycast client synchronizes the local clock with the server after receiving NTP manycast packets from the server.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```