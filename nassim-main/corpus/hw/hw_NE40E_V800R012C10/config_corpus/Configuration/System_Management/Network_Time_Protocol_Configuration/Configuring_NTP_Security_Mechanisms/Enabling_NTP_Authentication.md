Enabling NTP Authentication
===========================

Both the NTP server and the NTP client must be enabled with NTP authentication and configured with the same authentication key, and the authentication key must be declared as reliable on the client side. Otherwise, NTP authentication will fail.

#### Context

NTP client synchronizes to authenticated NTP servers to ensure that time service is reliable across the network. You must enable NTP authentication, and then configure basic NTP functions and specify the authentication key. Otherwise, the NTP authentication fails.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ntp-service authentication enable**](cmdqueryname=ntp-service+authentication+enable)
   
   
   
   NTP authentication is enabled.
3. Run [**ntp-service authentication-keyid**](cmdqueryname=ntp-service+authentication-keyid) *key-Id* **authentication-mode** { **md5** | **hmac-sha256** | **aes-128-cmac** | **aes-256-cmac** } { *password* | **cipher** *password* }
   
   
   
   The NTP authentication key is configured.
   
   
   
   Using the HMAC-SHA256 algorithm for NTP key authentication is recommended.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   The algorithm specified using **md5** in the command is a weak security algorithm, which is not recommended. To use such an algorithm, run the **undo crypto weak-algorithm disable** command to enable the weak security algorithm function. To avoid security risks, you are advised to use a more secure algorithm.
4. (Optional) Run [**ntp-service authentication-password complexity-check enable**](cmdqueryname=ntp-service+authentication-password+complexity-check+enable)
   
   
   
   Password strength check is enabled for NTP authentication.
   
   
   
   After this command is configured, the system automatically verifies the strength of an entered password. Only the password that meets the strength requirements can be configured. You are advised to run this command on a network that requires high security.
5. Run [**ntp-service reliable authentication-keyid**](cmdqueryname=ntp-service+reliable+authentication-keyid) *key-id*
   
   
   
   The authentication key is declared to be reliable.
   
   
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * A device that attempts to synchronize its clock must declare its key as reliable.
   * When the client synchronizes to an authenticated server, the authentication key must be declared as reliable only on the client side.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.