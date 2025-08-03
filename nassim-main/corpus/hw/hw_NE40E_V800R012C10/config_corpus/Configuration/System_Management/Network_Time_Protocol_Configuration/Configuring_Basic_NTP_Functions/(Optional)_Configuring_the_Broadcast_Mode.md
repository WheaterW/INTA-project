(Optional) Configuring the Broadcast Mode
=========================================

The NTP broadcast mode can be configured on a LAN to synchronize clocks on the LAN.

#### Procedure

* Configure an NTP broadcast server.
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
     
     
     
     The view of the interface specified for sending NTP broadcast packets is displayed.
  5. Run [**ntp-service broadcast-server**](cmdqueryname=ntp-service+broadcast-server) [ **authentication-keyid** *key-id* | **version** *version-number* | **port** *port-number* ] \*
     
     
     
     The local Router is configured as an NTP broadcast server.
     
     
     
     After the configuration is complete, the local Router functions as the NTP broadcast server periodically sending clock synchronization packets to the broadcast address 255.255.255.255 from a specified interface.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The NTP broadcast server functions for a LAN only.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure an NTP broadcast client.
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
     
     
     
     The view of the interface specified for receiving NTP broadcast packets is displayed.
  6. Run [**ntp-service broadcast-client**](cmdqueryname=ntp-service+broadcast-client)
     
     
     
     The local Router is configured as an NTP broadcast client.
     
     
     
     After the configuration is complete, the local Router functions as the NTP broadcast client listening for the NTP broadcast packets sent from the server and synchronizing the local clock with the server.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.