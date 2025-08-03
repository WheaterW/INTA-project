Configuring an RSVP Authentication Mode
=======================================

RSVP authentication modes are configured between RSVP neighboring nodes or between the interfaces of RSVP neighboring nodes. The keys on both ends to be authenticated must be the same; otherwise, RSVP authentication fails, and RSVP neighboring nodes discard received packets.

#### Context

RSVP authentication in the key mode is used to prevent an unauthorized node from establishing an RSVP neighbor relationship with a local node. It can also prevent a remote node from constructing forged packets to establish an RSVP neighbor relationship with the local node.

The NE40E supports three RSVP key authentication modes, as shown in [Figure 1](#EN-US_TASK_0172368159__fig_dc_vrp_te-p2p_cfg_001901).**Figure 1** RSVP key authentication networking  
![](images/fig_dc_vrp_te-p2p_cfg_001901.png)  

* Local interface-based authentication
  
  Local interface-based authentication is performed between interfaces connecting a point of local Repair (PLR) and a merge point (MP) in an inter-domain MPLS TE FRR scenario.
  
  + Local interface-based authentication is recommended on a network configured with inter-domain MPLS TE FRR.
  + Local interface- or neighbor interface-based authentication can be used on a network that is not configured with inter-domain MPLS TE FRR.
* Neighbor node-based authentication
  
  Neighbor node-based authentication takes effect on an entire device. It is usually performed between a PLR and an MP based on LSR IDs.
  
  This authentication mode is recommended on a network with non-inter-domain MPLS TE FRR.
* Neighbor interface-based authentication
  
  Neighbor interface-based authentication is performed between interfaces connecting two LSRs. For example, neighbor interface-based authentication is performed between interfaces connecting LSRA and LSRB shown in the [Figure 1](#EN-US_TASK_0172368159__fig_dc_vrp_te-p2p_cfg_001901).
  
  Local interface- or neighbor interface-based authentication can be used on a network that is not configured with inter-domain MPLS TE FRR.

Each pair of RSVP neighbors must use the same key; otherwise, RSVP authentication fails, and all received RSVP messages are discarded.

[Table 1](#EN-US_TASK_0172368159__tab_dc_vrp_te-p2p_cfg_001901) describes differences between local interface-, neighbor node-, and neighbor address-based authentication modes.

**Table 1** Rules for RSVP authentication mode selection
| RSVP Key Authentication | Local Interface-based Authentication | Neighbor Node-based Authentication | Neighbor Interface-based Authentication |
| --- | --- | --- | --- |
| Authentication mode | Local interface-based authentication | RSVP neighbor-based authentication | RSVP neighbor interface-based authentication |
| Priority | High | Medium | Low |
| Applicable environment | Any network | Non-inter-area network | Networks on which MPLS TE FRR is enabled and primary CR-LSPs are in the FRR in-use state |
| Advantages | N/A | Simplex configuration | N/A |




#### Procedure

* Configure RSVP key authentication in neighbor address-based mode.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface on which the MPLS TE tunnel is established is displayed.
  3. Run [**mpls rsvp-te authentication**](cmdqueryname=mpls+rsvp-te+authentication) { { **cipher** | **plain** } *auth-key* | **keychain** *keychain-name* }
     
     
     
     The key for RSVP authentication is configured.
     
     HMAC-MD5 or keychain authentication can be configured based on the selected parameter:
     
     + **cipher**: HMAC-MD5 authentication is used, and a key is displayed in ciphertext.
     + **plain**: HMAC-MD5 authentication is used, and a key is displayed in simple text.
     + **keychain**: Keychain authentication is used, and a globally configured keychain is referenced.![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     If you select the **plain** mode in authentication key configuration, the password is saved in the configuration file in plaintext. Because this mode has high security risks, you are advised to select the **cipher** mode. To improve the device security, periodically change the password.
     
     It is recommended that the password contain uppercase letters, lowercase letters, digits, and special characters.
     
     HMAC-MD5 authentication provides low security. To ensure high security, you are advised to use keychain authentication and a high-security algorithm, such as HMAC-SHA-256.
     
     The configuration must be completed on the two directly connected interfaces within three update periods. If the configuration is not completed after three update periods elapse, the session goes down.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure RSVP key authentication in neighbor-based mode.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**mpls**](cmdqueryname=mpls)
     
     
     
     The MPLS view is displayed.
  3. (Optional) Run [**mpls rsvp-te challenge-lost**](cmdqueryname=mpls+rsvp-te+challenge-lost) *max-miss-times*
     
     
     
     The maximum number of Challenge messages allowed to be dropped when being sent from the authenticated end to the authenticator end during RSVP-TE authentication is configured.
  4. (Optional) Run [**mpls rsvp-te retrans-timer challenge**](cmdqueryname=mpls+rsvp-te+retrans-timer+challenge) *retransmission-interval*
     
     
     
     The interval at which challenge messages are retransmitted is set.
  5. Run [**mpls rsvp-te peer**](cmdqueryname=mpls+rsvp-te+peer) *peer-address*
     
     
     
     The RSVP neighbor view is displayed.
  6. Run [**mpls rsvp-te authentication**](cmdqueryname=mpls+rsvp-te+authentication) { { **cipher** | **plain** } *auth-key* | **keychain** *keychain-name* }
     
     
     
     The key for RSVP authentication is configured.
     
     HMAC-MD5 or keychain authentication can be configured based on the selected parameter:
     
     + **cipher**: HMAC-MD5 authentication is used, and a key is displayed in ciphertext.
     + **plain**: HMAC-MD5 authentication is used, and a key is displayed in simple text.
     + **keychain**: Keychain authentication is used, and a globally configured keychain is referenced.![](../../../../public_sys-resources/notice_3.0-en-us.png) 
     
     If you select the **plain** mode in authentication key configuration, the password is saved in the configuration file in plaintext. Because this mode has high security risks, you are advised to select the **cipher** mode. To improve the device security, periodically change the password.
     
     HMAC-MD5 authentication provides low security. To ensure high security, you are advised to use keychain authentication and a high-security algorithm, such as HMAC-SHA-256.
     
     It is recommended that the password contain uppercase letters, lowercase letters, digits, and special characters.
     
     The configuration must be completed on the two neighboring nodes within three update periods. If the configuration is not completed after three update periods elapse, the session goes down.
  7. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.