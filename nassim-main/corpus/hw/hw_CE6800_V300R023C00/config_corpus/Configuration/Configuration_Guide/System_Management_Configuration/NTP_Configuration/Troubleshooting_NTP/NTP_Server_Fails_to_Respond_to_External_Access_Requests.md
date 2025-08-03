NTP Server Fails to Respond to External Access Requests
=======================================================

NTP Server Fails to Respond to External Access Requests

#### Fault Symptom

The NTP server does not respond to external access requests. As a result, the NTP client fails to synchronize its clocks with the NTP server.


#### Possible Causes

1. No listening interface is configured on the NTP server.
2. The server IP address specified on the NTP client is not the IP address of the source interface for sending NTP packets.

#### Procedure

1. Check the NTP configurations on the client and server.
   
   
   ```
   [display current-configuration interface](cmdqueryname=display+current-configuration+interface) [ interface-type [ interface-number ] | interface-name ] [ include-default ]
   ```
2. Configure a listening interface for the NTP server.
   
   
   * Configure a listening interface for an IPv4 NTP server.
     ```
     [ntp server source-interface](cmdqueryname=ntp+server+source-interface) { interface-name |interface-type interface-number }
     ```
     
     By default, an NTP IPv4 server does not listen to any interface. If the [**ntp server source-interface**](cmdqueryname=ntp+server+source-interface) **all enable** command is run, the device functions as an NTP IPv4 server and listens to all interfaces.
   * Configure a listening interface for an IPv6 NTP server.
     ```
     [ntp ipv6 server source-address](cmdqueryname=ntp+ipv6+server+source-address) ipv6Addr [ vpn-instance vpnName ]
     ```
     
     By default, an NTP IPv6 server does not listen to any interface. If the [**ntp ipv6 server source-interface**](cmdqueryname=ntp+ipv6+server+source-interface) **all enable** command is run, the device functions as an NTP IPv6 server and listens to all interfaces.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
4. Reconfigure the server IP address on the NTP client.
   
   
   
   Reconfigure the server IP address on the NTP client based on the NTP operating mode. The server IP address must be the IP address of the source interface for sending NTP packets.