(Optional) Configuring the Peer Mode
====================================

In peer mode, the two peers synchronize clocks with each other. One end can send the clock synchronization request message to the other and respond to the clock synchronization request message from the peer.

#### Procedure

* Configure the NTP proactive peer end.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ntp-service authentication-keyid**](cmdqueryname=ntp-service+authentication-keyid) *key-Id* **authentication-mode** { **md5** | **hmac-sha256** | **aes-128-cmac** | **aes-256-cmac** } { *password* | **cipher** *password* }
     
     
     
     The NTP authentication key is configured.
     
     
     
     Using the HMAC-SHA256 algorithm for NTP key authentication is recommended.
     
     ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     The algorithm specified using **md5** in the command is a weak security algorithm, which is not recommended. To use such an algorithm, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function. To avoid security risks, you are advised to use a more secure algorithm.
  3. (Optional) Run [**ntp-service authentication-password complexity-check enable**](cmdqueryname=ntp-service+authentication-password+complexity-check+enable)
     
     
     
     Password strength check is enabled for NTP authentication.
     
     
     
     After this command is configured, the system automatically verifies the strength of an entered password. Only the password that meets the strength requirements can be configured. You are advised to run this command on a network that requires high security.
  4. (Optional) Run [**ntp-service**](cmdqueryname=ntp-service) [ **ipv6** ] **source-interface** { **interface-name**| **interface\_type****interface\_num***ber* } [****vpn-instance**** *vpnName* ]
     
     
     
     The local source interface for sending NTP packets is specified.
  5. Configure an IP address for the NTP peer.
     
     
     + To specify an IP address for the remote peer, run the [**ntp-service unicast-peer**](cmdqueryname=ntp-service+unicast-peer) *ip-address* [ **version** *number* | **authentication-keyid** *key-id* | **source-interface** *interface-type interface-number* | **vpn-instance** *vpn-instance-name* | **preference** | **maxpoll** *max-number* | **minpoll** *min-number* | **preempt** | **port** *port-number* ] \* command.
     + To specify an IPv6 address for the remote peer, run the [**ntp-service unicast-peer**](cmdqueryname=ntp-service+unicast-peer)  **ipv6** *ipv6-address* [ **authentication-keyid** *key-id* | **source-interface** *interface-type interface-number* | **vpn-instance** *vpn-instance-name* | **preference** | **maxpoll** *max-number* | **minpoll** *min-number* | **preempt** | **port** *port-number* ] \* command.
     
     Step 3 is optional. If Step 3 is performed, and the **source-interface** parameter is configured in Step 4 to specify the source interface, the source interface specified in Step 4 is preferentially used.
     
     *ip-address* is the NTP peer IP address. It can be a host address, but not a broadcast address, a multicast address, or the IP address of the reference clock.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     After the NTP peer is specified, the local Router runs in proactive peer mode. The passive peer end does not need to be configured.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* (Optional) Configure the NTP passive peer end.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ntp-service authentication-keyid**](cmdqueryname=ntp-service+authentication-keyid) *key-Id* **authentication-mode** { **md5** | **hmac-sha256** } { *password* | **cipher** *password* }
     
     
     
     The NTP authentication key is configured.
     
     
     
     Using the HMAC-SHA256 algorithm for NTP key authentication is recommended.
     
     ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     The algorithm specified using **md5** in the command is a weak security algorithm, which is not recommended. To use such an algorithm, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function. To avoid security risks, you are advised to use a more secure algorithm.
  3. (Optional) Run [**ntp-service authentication-password complexity-check enable**](cmdqueryname=ntp-service+authentication-password+complexity-check+enable)
     
     
     
     Password strength check is enabled for NTP authentication.
     
     
     
     After this command is configured, the system automatically verifies the strength of an entered key. Only the key that meets the strength requirements can be configured. You are advised to run this command on a network that requires high security.
  4. Run [**ntp-service**](cmdqueryname=ntp-service) [ **ipv6** ] **source-interface** { **interface-name**| **interface\_type****interface\_num**} [****vpn-instance**** *vpnName* ]
     
     
     
     The local source interface for sending NTP packets is specified.
     
     
     
     Generally, you only need to specify the IP address of the passive peer end on the proactive peer end. As such, the peer ends can then exchange NTP packets using this IP address.
     
     If the source interface for sending NTP packets is specified on the passive peer end, the peer IP address configured on the proactive peer end must be the same as the IP address of the source interface. Otherwise, the proactive peer end cannot process NTP packets sent from the passive peer end and clock synchronization fails.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.