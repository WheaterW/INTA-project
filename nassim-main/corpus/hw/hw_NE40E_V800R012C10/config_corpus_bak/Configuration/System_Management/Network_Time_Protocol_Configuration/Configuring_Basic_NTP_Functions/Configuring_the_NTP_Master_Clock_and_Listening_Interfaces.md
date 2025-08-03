Configuring the NTP Master Clock and Listening Interfaces
=========================================================

The master clock on the server must have a smaller stratum number (higher stratum) than that of the clock on the client. Otherwise, the clock on the client cannot synchronize with the master clock on the server. Perform the following steps on the server.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ntp-service refclock-master**](cmdqueryname=ntp-service+refclock-master) [ *ip-address* ] [ *stratum* ]
   
   
   
   An NTP master clock is configured.
3. Configure a listening interface for the NTP server.
   
   
   * To specify a listening interface for the NTP IPv4 server, run the [**ntp-service server source-interface**](cmdqueryname=ntp-service+server+source-interface) { **interface-name**| **interface-type****interface-number** } command.
   * To specify a listening IPv6 address for the NTP IPv6 server, run the [**ntp-service ipv6 server source-address**](cmdqueryname=ntp-service+ipv6+server+source-address) *ipv6Addr* [ **vpn-instance** *vpnName* ] command.
   
   
   
   If the [**ntp-service server source-interface**](cmdqueryname=ntp-service+server+source-interface) **all enable** or [**ntp-service ipv6 server source-interface**](cmdqueryname=ntp-service+ipv6+server+source-interface) **all enable** command is run, the device listens to all interfaces.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.