(Optional) Configuring the Manycast Mode
========================================

The NTP manycast mode can be configured to synchronize clocks in a manycast domain.

#### Procedure

* Configure an NTP manycast server.
  
  
  
  Perform the following steps on the Router functioning as an NTP manycast server:
  
  
  
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
  4. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface specified for sending NTP manycast packets is displayed.
  5. Configure an NTP manycast server.
     
     
     + Run the [**ntp-service manycast-server**](cmdqueryname=ntp-service+manycast-server) *ip-address* command to configure the Routeras an NTP manycast server on an IPv4 network.
     + Run the [**ntp-service manycast-server**](cmdqueryname=ntp-service+manycast-server) **ipv6** [ *ipv6-address* ] command to configure the Router as an NTP manycast server on an IPv6 network.
* Configure an NTP manycast client.
  
  
  
  Perform the following steps on the Router functioning as an NTP manycast client:
  
  
  
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
  4. (Optional) Run [**ntp-service max-dynamic-sessions**](cmdqueryname=ntp-service+max-dynamic-sessions) *number*
     
     
     
     The maximum number of dynamic sessions supported by the local device is specified.
     
     
     
     Running this command does not affect the existing NTP sessions. When the number of sessions reaches the maximum number, no more session can be established.
  5. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The interface for receiving NTP manycast packets is specified.
  6. Configure an NTP manycast client.
     
     
     + Run the [**ntp-service manycast-client**](cmdqueryname=ntp-service+manycast-client) *ip-address* [ [ **authentication-keyid** *key-id* ] | **ttl** *ttl-number* | **port** *port-number* ] \* command to configure the Router as an IPv4 NTP manycast client.
     + Run the [**ntp-service manycast-client**](cmdqueryname=ntp-service+manycast-client) **ipv6** [ *ipv6-address* ][ [ **authentication-keyid** *key-id* ] | **ttl** *ttl-number* | **port** *port-number* ] \* command to configure the Router as an NTP manycast client on an IPv6 network.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
     
     
     
     The NTP manycast client receives the NTP manycast packets sent from the server and synchronizes the local clock.