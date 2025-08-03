Enabling NTP Authentication
===========================

Enabling NTP Authentication

#### Context

NTP authentication can be enabled on networks requiring high security. With password authentication configured between the client and server sides, a client synchronize its clocks only with the authenticated server.

When configuring the NTP authentication function, comply with the following rules:

* Enable NTP authentication before configuring the basic NTP functions. Otherwise, NTP authentication will not be performed.
* Configure NTP authentication on both the client and server. Otherwise, NTP authentication does not take effect. In NTP peer mode, the client is the symmetric active peer, and the server is the symmetric passive peer.
* Configure the same key on the client and server.

#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enable NTP authentication.
   
   
   ```
   [ntp authentication enable](cmdqueryname=ntp+authentication+enable)
   ```
3. Configure an NTP authentication key.
   
   
   ```
   [ntp authentication-keyid](cmdqueryname=ntp+authentication-keyid) keyId authentication-mode { md5 | hmac-sha256 | aes-128-cmac | aes-256-cmac } { password | cipher password }
   ```
   
   
   
   MD5 is a weak security algorithm. It can be used only after the weak security algorithm or protocol feature package is installed after the [**install feature-software WEAKEA**](cmdqueryname=install+feature-software+WEAKEA) command is run. You are advised to use other security algorithms for NTP key authentication.
   
   The system automatically verifies the strength of an entered key. Only the key that meets the strength requirements can be configured. To disable key strength check, run the [**ntp authentication-password complexity-check disable**](cmdqueryname=ntp+authentication-password+complexity-check+disable) command.
   
   ![](public_sys-resources/notice_3.0-en-us.png) 
   
   Disabling the key strength check function causes security risks. Therefore, you are advised not to run this command.
4. Declare the authentication key to be reliable.
   
   
   ```
   [ntp trusted authentication-keyid](cmdqueryname=ntp+trusted+authentication-keyid) keyNum
   ```
   ![](public_sys-resources/note_3.0-en-us.png) 
   * A device that attempts to synchronize its clock must declare its key as reliable.
   * When the client synchronizes to an authenticated server, the authentication key must be declared as reliable only on the client side.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```