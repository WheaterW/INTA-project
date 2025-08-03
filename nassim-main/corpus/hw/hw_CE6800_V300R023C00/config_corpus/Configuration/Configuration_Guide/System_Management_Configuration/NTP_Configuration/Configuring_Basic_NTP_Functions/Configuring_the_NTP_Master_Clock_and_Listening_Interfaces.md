Configuring the NTP Master Clock and Listening Interfaces
=========================================================

Configuring the NTP Master Clock and Listening Interfaces

#### Context

An NTP master clock can be configured on the server (which can be a unicast server, broadcast server, multicast server, manycast server, or symmetric passive peer) to provide the reference time for other devices. In addition, an interface that listens for external NTP packets needs to be specified. Otherwise, the server fails to respond to client requests.

An NTP master clock does not need to be configured when the local server has been synchronized with an NTP master clock at a higher stratum. When this is the case, if the NTP master clock at a higher stratum fails, the local server cannot provide the reference time for lower-level clients. To resolve this problem, you are advised to configure an NTP master clock on the local server and set its clock stratum to that of the upper-level server plus 1.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure the NTP master clock.
   
   
   ```
   [ntp refclock-master](cmdqueryname=ntp+refclock-master) [ ip-address ] [ stratum ]
   ```
   
   Configure the local clock as the NTP master clock to provide the reference time for other devices. The value of *stratum* must be smaller than the stratum value of a client. Otherwise, the client cannot synchronize with the clock on the server.
3. Configure a listening interface for the NTP server.
   
   
   
   | Listening interface of the NTP server | Command | Description |
   | --- | --- | --- |
   | The device functions as an NTP IPv4 server to listen to all interfaces. | [**ntp server source-interface**](cmdqueryname=ntp+server+source-interface) **all enable** | By default, the device functions as an NTP IPv4 server and does not listen to any address. If all three commands are configured, the [**ntp server source-interface**](cmdqueryname=ntp+server+source-interface) **all enable** command takes precedence. The device functions as an NTP IPv4 server to receive and process packets received by all interfaces and addresses. |
   | The device functions as an NTP IPv4 server to listen to a specified interface. | [**ntp server source-interface**](cmdqueryname=ntp+server+source-interface) { *interface-name* |*interface-type interface-number* } |
   | The device functions as an NTP IPv4 server to listen to a specified interface and address. | [**ntp server**](cmdqueryname=ntp+server) ****physic-isolate** [**source-interface**](cmdqueryname=source-interface)** { *interface-name* | *interface-type interface-number* } **source-address** *ipv4Addr* |
   | The device functions as an NTP IPv6 server to listen to all interfaces. | [**ntp ipv6 server source-interface**](cmdqueryname=ntp+ipv6+server+source-interface) **all enable** | By default, the device functions as an NTP IPv6 server and does not listen to any address. If all three commands are configured, the [**ntp ipv6 server source-interface**](cmdqueryname=ntp+ipv6+server+source-interface) **all enable** command takes precedence. The device functions as an NTP IPv6 server to receive and process packets received by all interfaces and addresses. |
   | The device functions as an NTP IPv6 server to listen to a specified address. | [**ntp ipv6 server source-address**](cmdqueryname=ntp+ipv6+server+source-address) *ipv6Addr* [ **vpn-instance** *vpnName* ] |
   | The device functions as an NTP IPv6 server to listen to a specified interface and address. | [**ntp ipv6 server**](cmdqueryname=ntp+ipv6+server) ****physic-isolate** [**source-interface**](cmdqueryname=source-interface)** { *interface-name* | *interface-type interface-number* } **source-address** *ipv6Addr* |
4. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```

#### Follow-up Procedure

For details about how to enable the NTP authentication function, see [Enabling NTP Authentication](vrp_ntp_cfg_0025.html). Before configuring the working mode, ensure that the authentication function has been configured.