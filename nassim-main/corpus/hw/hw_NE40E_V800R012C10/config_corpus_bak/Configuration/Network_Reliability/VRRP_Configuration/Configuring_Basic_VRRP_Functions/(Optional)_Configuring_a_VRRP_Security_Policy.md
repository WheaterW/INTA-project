(Optional) Configuring a VRRP Security Policy
=============================================

A VRRP security policy can be configured to protect a network requiring high security against attacks.

#### Context

When the master device periodically sends VRRP Advertisement packets to a backup device, an attacker may simulate the master device's packets to initiate attacks. To improve network security, configure a VRRP security policy. [Table 1](#EN-US_TASK_0172361756__tab_dc_vrp_vrrp_cfg_010701) describes VRRP security functions.

**Table 1** VRRP security functions
| Basic Function | Usage Scenario |
| --- | --- |
| Configuring an authentication mode for VRRP Advertisement packets | Different authentication modes can be used for different security requirements.   * None authentication is a default mode and is used on a secure network. If none authentication is used, the master device sends VRRP Advertisement packets without authentication information. After receiving the packets, a backup device considers all received packets authentic and valid, without attempting to authenticate them. * Simple authentication or HMAC-MD5 authentication can be used to improve VRRP communication security. HMAC-MD5 authentication is more secure than simple authentication. |



#### Procedure

* Configure an authentication mode for VRRP Advertisement packets.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
     
     
     
     The view of the interface on which the VRRP group is configured is displayed.
  3. Run [**vrrp vrid**](cmdqueryname=vrrp+vrid) *virtual-router-id* **authentication-mode** { **simple** { [ **plain** ] *key* | **cipher** *cipher-key* } | **md5** *md5-key* }
     
     
     
     An authentication mode is configured for VRRP Advertisement packets.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     + For security purposes, you are advised to configure a ciphertext password and change the password periodically.
     + The same authentication key must be configured on the master and backup devices in a VRRP group.
     + For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the **[**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable)** command to enable the weak security algorithm function first.
     + It is recommended that the new password be at least eight characters long and contain at least two of upper-case letters, lower-case letters, digits, and special characters.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.