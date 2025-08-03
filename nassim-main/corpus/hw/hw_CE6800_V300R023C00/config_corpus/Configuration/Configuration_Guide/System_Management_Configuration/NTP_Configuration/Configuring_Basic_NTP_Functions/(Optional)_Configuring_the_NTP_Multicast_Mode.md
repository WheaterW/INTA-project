(Optional) Configuring the NTP Multicast Mode
=============================================

(Optional) Configuring the NTP Multicast Mode

#### Context

When the multicast mode is used, you need to perform the following configurations on both the multicast server and client.


#### Procedure

* Configure an NTP multicast server.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Configure an NTP authentication key.
     
     
     ```
     [ntp authentication-keyid](cmdqueryname=ntp+authentication-keyid) keyId authentication-mode { md5 | hmac-sha256 | aes-128-cmac | aes-256-cmac } { password | cipher password }
     ```
     
     
     
     MD5 is a weak security algorithm. It can be used only after the weak security algorithm or protocol feature package is installed after the **install feature-software WEAKEA** command is run. You are advised to use other security algorithms for NTP key authentication.
  3. Enter the view of the interface used for sending NTP multicast packets.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  4. Configure the local device as the NTP multicast server.
     
     
     
     Run either of the following commands depending on whether the server IP address is an IPv4 or IPv6 address:
     
     ```
     [ntp multicast-server](cmdqueryname=ntp+multicast-server) [ ip-address ] [ authentication-keyid key-id | ttl ttl-number | version number | port port-number ] *
     ```
     ```
     [ntp multicast-server ipv6](cmdqueryname=ntp+multicast-server+ipv6) [ ipv6Addr ] [ authentication-keyid keyid | ttl ttl-number | port portNumber ] *
     ```
     
     After the configuration is complete, the local device functions as the NTP multicast server periodically sending clock synchronization packets to the configured destination multicast address from a specified interface.
  5. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```
* Configure an NTP multicast client.
  1. Enter the system view.
     
     
     ```
     [system-view](cmdqueryname=system-view)
     ```
  2. Enter the view of the interface used for receiving NTP multicast packets.
     
     
     ```
     [interface](cmdqueryname=interface) interface-type interface-number
     ```
  3. Configure the local device as the NTP multicast client.
     
     
     ```
     [ntp multicast-client](cmdqueryname=ntp+multicast-client) [ ip-address | ipv6 ipv6-address ]
     ```
     
     After the configuration is complete, the local device functions as the NTP multicast client listening for the NTP multicast packets sent from the server and synchronizing the local clock with the server.
  4. Commit the configuration.
     
     
     ```
     [commit](cmdqueryname=commit)
     ```