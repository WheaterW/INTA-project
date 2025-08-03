(Optional) MC-LMSP Negotiation and Authentication Parameters
============================================================

MC-LMSP-enabled routers run the Protection Group Protocol (PGP) to exchange control messages. Negotiation and authentication parameters can be set for PGP message transmission, helping use MC-LMSP functions easily and securely.

#### Context

Two MC-LMSP-enabled Routers run the Protection Group Protocol (PGP) to exchange control messages along an outband channel at a specified interval. PGP negotiation messages are exchanged periodically to verify MC-LMSP connectivity. If no response arrives within a specified period, the Router considers its peer Router faulty and does not perform MC-LMSP switching even though a switching trigger condition is met.

In addition to the interval at which negotiation messages are sent, the MC-LMSP connection hold time can also be set on the NE40Es. The local NE40E retains the MC-LMSP connection during the configured hold time. If no negotiation message is received after the hold time elapses, the local NE40E considers the MC-LMSP connection is torn down.

PGP is a Layer 3 Huawei proprietary protocol and operates over a UDP connection. PGP's default authentication mode is none. Messages transmitted in none authentication mode can be easily used to initiate attacks. To protect the NE40E running PGP, an authentication string can be configured so that PGP messages are authenticated. Two MC-LMSP-enabled routers use the authentication string to authenticate PGP messages. Negotiation can be successfully performed only when the two Routers use the same authentication string. Authentication string inconsistency will lead to a negotiation failure.

Perform the following steps on the working and protection interfaces of an LMSP group:


#### Procedure

* Set the interval at which LMSP negotiation messages are sent and the LMSP connection hold time.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run either of the following commands:
     
     
     ```
     [controller cpos](cmdqueryname=controller+cpos) cpos-number
     ```
     
     The working or protection interface view is displayed.
  3. Run [**aps timers**](cmdqueryname=aps+timers) *keep-alive-time hold-time*
     
     
     
     The interval at which MC-LMSP negotiation messages are sent and the hold time of the LMSP connection between the working and protection interfaces are set.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the authentication string for PGP messages.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run either of the following commands:
     
     
     ```
     [controller cpos](cmdqueryname=controller+cpos) cpos-number
     ```
     
     The working or protection interface view is displayed.
  3. Run [**aps authenticate**](cmdqueryname=aps+authenticate) { *simple-key* | **simple** *simple-key* | **cipher** *cipher-key* [ **sha2** | **hmac** ] }
     
     
     
     The authentication string is configured for PGP messages.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     The working or protection interface must be specified before an authentication string is configured for the PGP message.
     
     PGP negotiation can only be performed successfully when the authentication strings configured on both working and protection interfaces are the same.
     
     To ensure higher security, you are advised not to use the MD5 algorithm. In this case, you can run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak-security algorithm function.
     
     When the cipher text mode is used, enable the HMAC abstract algorithm to obtain a higher security level. Ensure that the configurations on the two devices must be consistent.
     
     + The new password is at least eight characters long and contains at least two of upper-case letters, lower-case letters, digits, and special characters.
     + When configuring an authentication password, select the ciphertext mode because the password is saved in configuration files in simple text if you select simple text mode, which has a high risk. To ensure device security, change the password periodically.
  4. (Optional) Run [**aps anti-replay enable**](cmdqueryname=aps+anti-replay+enable)
     
     
     
     APS anti-replay is enabled.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.