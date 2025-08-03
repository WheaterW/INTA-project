Configuring NHRP
================

Configure the Next Hop Resolution Protocol (NHRP) so that spokes can obtain the peer IP address of each other by exchanging NHRP Resolution Request and Reply packets.

#### Context

In DSVPN, NHRP enables a source spoke on a public network to dynamically obtain the public IP address of a destination spoke. When a spoke connects to the public network, it sends NHRP Registration Request packets to the hub using the public address of the outbound interface as the source address. The hub creates or updates NHRP peer entries based on the packets received. Spokes also exchange NHRP Resolution Request and Reply packets to create or update NHRP peer entries.

Perform the following configurations on the hub and spokes.


#### Procedure

* Configure the hub.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**nhrp enable**](cmdqueryname=nhrp+enable)
     
     
     
     NHRP is enabled globally.
  3. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
     
     
     
     The tunnel interface view is displayed.
  4. Run [**nhrp enable**](cmdqueryname=nhrp+enable)
     
     
     
     NHRP is enabled on the interface.
  5. (Optional) Run [**nhrp network-id**](cmdqueryname=nhrp+network-id) *netId*
     
     
     
     An NHRP domain is configured for the interface.
  6. Run [**nhrp entry multicast dynamic**](cmdqueryname=nhrp+entry+multicast+dynamic)
     
     
     
     Dynamically registered spokes are added to the NHRP multicast member table.
  7. Run [**nhrp authentication**](cmdqueryname=nhrp+authentication) [ **hash** { **sha2-256** | **sha2-384** | **sha2-512** } ] **cipher** *authenString*
     
     
     
     An authentication string is configured for NHRP negotiation.
  8. (Optional) Run [**nhrp entry holdtime**](cmdqueryname=nhrp+entry+holdtime) *holdtime*
     
     
     
     The hold time of NHRP mapping entries is set.
  9. (Optional) Run [**nhrp redirect**](cmdqueryname=nhrp+redirect)
     
     
     
     The NHRP redirect function is enabled.
     
     
     
     This command is configured only when DSVPN uses the shortcut mode. When forwarding traffic from spokes of the same DSVPN, the hub sends an NHRP Redirect packet to the source spoke, triggering the source spoke to send NHRP Resolution Request packets and establish tunnels for spokes to directly communicate with each other.
  10. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
* Configure spokes.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**nhrp enable**](cmdqueryname=nhrp+enable)
     
     
     
     NHRP is enabled globally.
  3. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
     
     
     
     The tunnel interface view is displayed.
  4. Run [**nhrp enable**](cmdqueryname=nhrp+enable)
     
     
     
     NHRP is enabled on the interface.
  5. (Optional) Run [**nhrp network-id**](cmdqueryname=nhrp+network-id) *netId*
     
     
     
     An NHRP domain is configured for the interface.
  6. (Optional) Run [**nhrp shortcut**](cmdqueryname=nhrp+shortcut)
     
     
     
     The NHRP shortcut function is enabled. This step is mandatory in DSVPN shortcut scenarios.
  7. Run [**nhrp entry multicast**](cmdqueryname=nhrp+entry+multicast) **dynamic**
     
     
     
     Dynamically registered spokes are added to the NHRP multicast member table.
  8. Run **[**nhrp entry**](cmdqueryname=nhrp+entry)** *protocol-address**nbma-address* [ **register** ]
     
     
     
     An NHRP mapping entry is configured.
  9. (Optional) Run [**nhrp registration no-unique**](cmdqueryname=nhrp+registration+no-unique)
     
     
     
     The device is enabled to send NHRP packets with the no-unique flag to instruct the remote device to use new NHRP mapping entries to overwrite conflicting NHRP peer entries during NHRP registration.
  10. Run [**nhrp authentication**](cmdqueryname=nhrp+authentication) [ **hash** { **sha2-256** | **sha2-384** | **sha2-512** } ] **cipher** *authenString*
      
      
      
      An authentication string is configured for NHRP negotiation.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If this configuration is performed on the hub, it must also be performed on the spokes.
      
      For security purposes, it is recommended that the authentication string contain at least 6 characters, including at least two types of the following: lowercase letters, uppercase letters, digits, and special characters.
  11. (Optional) Run [**nhrp registration interval**](cmdqueryname=nhrp+registration+interval) *regInterval*
      
      
      
      The NHRP registration interval is set.
  12. (Optional) Run [**nhrp entry holdtime**](cmdqueryname=nhrp+entry+holdtime) *holdtime*
      
      
      
      The hold time of NHRP mapping entries is set.
  13. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.