(Optional) Configuring the Client/Server Mode
=============================================

In client/server mode, the clock on the client synchronizes with the master clock on the server.

#### Procedure

* Configure the NTP client.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. (Optional) Run [**ntp-service authentication-keyid**](cmdqueryname=ntp-service+authentication-keyid) *key-Id* **authentication-mode** { **md5** | **hmac-sha256** | **aes-128-cmac** | **aes-256-cmac** } { *password* | **cipher** *password* }
     
     
     
     The NTP authentication key is configured.
     
     
     
     Using the HMAC-SHA256 algorithm for NTP key authentication is recommended.
     
     ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     The algorithm specified using **md5** in the command is a weak security algorithm, which is not recommended. To use such an algorithm, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function. To avoid security risks, you are advised to use a more secure algorithm.
  3. (Optional) Run [**ntp-service authentication-password complexity-check enable**](cmdqueryname=ntp-service+authentication-password+complexity-check+enable)
     
     
     
     Password strength check is enabled for NTP authentication.
     
     
     
     After this command is configured, the system automatically verifies the strength of an entered password. Only the password that meets the strength requirements can be configured. You are advised to run this command on a network that requires high security.
  4. (Optional) Run [**ntp-service**](cmdqueryname=ntp-service) [ **ipv6** ] **source-interface** { **interface-name**| **interface\_type****interface\_num***ber* } [****vpn-instance**** *vpnName* ]
     
     
     
     The source interface for sending NTP packets is specified.
  5. Configure an IP address for the NTP server.
     
     
     + To configure an IP address for the server, run the [**ntp-service unicast-server**](cmdqueryname=ntp-service+unicast-server) *ip-address* [ **version** *number* | **authentication-keyid** *key-id* | **source-interface** *interface-type interface-number* | **vpn-instance** *vpn-instance-name* | **preference** | **maxpoll** *max-number* | **minpoll** *min-number* | **burst** | **iburst** | **preempt** | **port** *port-number*] \* command.
     + To specify an IPv6 address for the server, run the [**ntp-service unicast-server**](cmdqueryname=ntp-service+unicast-server) **ipv6** *ipv6-address* [ **authentication-keyid** *key-id* | **source-interface** *interface-type interface-number* | **vpn-instance** *vpn-instance-name* | **preference** | **maxpoll** *max-number* | **minpoll** *min-number* | **burst** | **iburst** | **preempt**] \*command.
     
     *ip-address* is the NTP server IP address. It can be a host address, but not a broadcast address, a multicast address, or the IP address of the reference clock. If a source interface to send NTP packets is specified on the server, the server IP address specified on the client must be this specified source interface address. Otherwise, the client cannot process NTP packets sent from the server and clock synchronization fails.
     
     Specifying the IPv6 address of the server is optional. If the step for specifying the IPv6 address of the server is performed, and the **source-interface** parameter is configured in this step to specify the source interface, the specified source interface is preferentially used.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     When the unicast NTP server is specified, the local Router functions as the client automatically. No additional configurations are required on the server except the NTP master clock.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.