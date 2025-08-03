DSVPN
=====

DSVPN

#### Security Policy Overview

**NHRP** **Negotiation Authentication**

In DSVPN, NHRP enables a source spoke on a public network to dynamically obtain the public address of a destination spoke. When a spoke uses a physical interface to connect to a public network, the spoke sends NHRP registration request packets to the hub by using the public address of the interface as the source address. The hub creates or updates NHRP peer entries based on the packets received. Two spokes can also exchange NHRP resolution request and reply packets to create or update NHRP peer entries.

To prevent a spoke from registering with the hub without authorization, enable NHRP negotiation authentication between the spoke and hub. After a spoke sends a registration request packet to the hub for registration, the hub determines whether to process the packet based on the authentication string in the packet. If the authentication string configured on the hub is different from that in the registration request packet, the hub does not process the packet. If the authentication string configured on the hub is the same as that in the registration request packet, the hub processes the packet.

**DSVPN IPsec Protection**

Data transmitted between the hub and spokes and between spokes can be encrypted to increase data security. During DSVPN deployment, bind an IPsec profile to DSVPN so that mGRE and IPsec tunnels can be dynamically established between spokes.

* The establishment of an mGRE tunnel immediately triggers the establishment of an IPsec tunnel.
* Typical IPsec technology uses ACLs to identify unicast traffic to be encrypted. An IPsec policy requires complex ACL definition, which is difficult to implement. DSVPN uses both NHRP and mGRE technologies. Deploying DSVPN together with IPsec helps simplify device configurations, ensuring data transmission security and facilitating network deployment.
* Because IPsec tunnels are dynamically established between spokes, IPsec data exchanged between spokes does not need to be decrypted or encrypted by the hub, minimizing data transmission delay.

#### Attack Methods

* Listen to data transmitted between spokes and the hub and between spokes.
* Masquerade as authorized spokes to register with the hub. The hub receives registration request packets from all spokes. When receiving registration request packets from unauthorized spokes, it also creates NHRP entries. After the number of created NHRP entries exceeds the upper limit, excess NHRP entries are discarded.

#### Procedure

* Configure NHRP negotiation authentication.
  
  Perform the following configurations on the hub and spokes.
  1. Configure the hub.
     1. Run **system-view**
        
        The system view is displayed.
     2. Run [**nhrp enable**](cmdqueryname=nhrp+enable)
        
        NHRP is enabled globally.
     3. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
        
        The tunnel interface view is displayed.
     4. Run [**nhrp enable**](cmdqueryname=nhrp+enable)
        
        NHRP is enabled on the interface.
     5. (Optional) Run [**nhrp network-id**](cmdqueryname=nhrp+network-id) *netId*
        
        The NHRP domain to which the interface belongs is configured.
     6. Run [**nhrp entry multicast dynamic**](cmdqueryname=nhrp+entry+multicast+dynamic)
        
        The NHRP multicast member table is configured.
     7. Run [**nhrp authentication**](cmdqueryname=nhrp+authentication) [ **hash** { **sha2-256** | **sha2-384** | **sha2-512** } ] **cipher** *authenString*
        
        An authentication string is configured for NHRP negotiation.
     8. (Optional) Run [**nhrp entry holdtime**](cmdqueryname=nhrp+entry+holdtime) *holdtime*
        
        The hold time of NHRP entries is set.
     9. (Optional) Run [**nhrp redirect**](cmdqueryname=nhrp+redirect)
        
        NHRP redirect is enabled.
        
        This function is required only when DSVPN uses the shortcut mode. After this function is deployed, the hub sends an NHRP Redirect packet to the source spoke when forwarding traffic to another spoke in the same DSVPN as the source spoke, triggering the source spoke to send an NHRP resolution request packet to establish a tunnel for direct communication with the destination spoke.
     10. Run [**commit**](cmdqueryname=commit)
         
         The configuration is committed.
  2. Configure spokes.
     1. Run **system-view**
        
        The system view is displayed.
     2. Run [**nhrp enable**](cmdqueryname=nhrp+enable)
        
        NHRP is enabled globally.
     3. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
        
        The tunnel interface view is displayed.
     4. Run [**nhrp enable**](cmdqueryname=nhrp+enable)
        
        NHRP is enabled on the interface.
     5. (Optional) Run [**nhrp network-id**](cmdqueryname=nhrp+network-id) *netId*
        
        The NHRP domain to which the interface belongs is configured.
     6. (Optional) Run [**nhrp shortcut**](cmdqueryname=nhrp+shortcut)
        
        NHRP shortcut is enabled. This function needs to be enabled on spokes in DSVPN shortcut scenarios.
     7. Run [**nhrp entry multicast dynamic**](cmdqueryname=nhrp+entry+multicast+dynamic)
        
        The NHRP multicast member table is configured.
     8. Run ****nhrp entry**** *protocol-address**nbma-address* [ **register** ]
        
        The NHRP mapping table is configured.
     9. (Optional) Run [**nhrp registration no-unique**](cmdqueryname=nhrp+registration+no-unique)
        
        The device is configured to send NHRP packets carrying the no-unique flag to instruct the peer end to override conflicting NHRP peer entries.
     10. Run [**nhrp authentication**](cmdqueryname=nhrp+authentication) [ **hash** { **sha2-256** | **sha2-384** | **sha2-512** } ] **cipher** *authenString*An authentication string is configured for NHRP negotiation.![](../../../../public_sys-resources/note_3.0-en-us.png) 
         
         If this configuration is performed on the hub, it must be performed on spokes.
     11. (Optional) Run [**nhrp registration interval**](cmdqueryname=nhrp+registration+interval) *regInterval*
         
         The NHRP registration interval is configured.
     12. (Optional) Run [**nhrp entry holdtime**](cmdqueryname=nhrp+entry+holdtime) *holdtime*
         
         The hold time of NHRP entries is set.
     13. Run [**commit**](cmdqueryname=commit)
         
         The configuration is committed.
* Configure DSVPN IPsec protection.
  
  
  1. For details, see [Configuring an IKE Proposal](dc_vrp_ipsec_cfg_all_0011.html).
  2. For details, see [Configuring an IKE Peer](dc_vrp_ipsec_cfg_all_0012.html).
  3. (Optional) Configure an IKE filter set.
     1. Run **system-view**
        
        The system view is displayed.
     2. Run [**ike identity**](cmdqueryname=ike+identity) *name*
        
        A filter set for IKE negotiation is configured, and its view is displayed.
     3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
        
        The IP address of the allowed IKE peer is configured.
     4. Run [**fqdn**](cmdqueryname=fqdn) *fqdn*
        
        The domain name of the allowed IKE peer is configured.
     5. Run [**user-fqdn**](cmdqueryname=user-fqdn) *user-fqdn*
        
        The host domain name of the allowed IKE peer is configured.
     6. Run [**dn**](cmdqueryname=dn) *dn*
        
        A distinguished name (DN) is configured for the digital certificate of the allowed IKE peer.
     7. Run [**quit**](cmdqueryname=quit)
        
        Exit the IKE filter set view.
     8. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
  4. Configure an IPsec profile.
     1. Run **system-view**
        
        The system view is displayed.
     2. Run [**ipsec policy**](cmdqueryname=ipsec+policy) *policy-name* **profile**
        
        The IPsec profile view is displayed.
     3. Run [**proposal**](cmdqueryname=proposal) *proposal-name*
        
        The security proposal for reference is specified.
     4. Run [**ike-peer**](cmdqueryname=ike-peer) *peer-name*
        
        The IKE peer for reference is specified.
     5. (Optional) Run [**pfs**](cmdqueryname=pfs) { **dh-group1** | **dh-group2** | **dh-group5** | **dh-group14** | **group15** | **group16** | **dh-group19** | **dh-group20** | **dh-group21** }
        
        The PFS feature used for negotiation is configured.
        
        If PFS is configured on the local end, the peer end must use PFS during initiating negotiation. The DH groups specified on the local and peer ends must be the same. Otherwise, the negotiation fails.
     6. (Optional) Run [**remote ike-identity**](cmdqueryname=remote+ike-identity) *name*A filter set is configured for the allowed IKE peer.![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        If an IPsec profile references a previously defined IKE filter set (IKE identity), packets are filtered based on the IKE filter set. Otherwise, packets are not filtered.
     7. Run [**quit**](cmdqueryname=quit)
        
        Exit the IPsec profile view.
     8. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
  5. Apply the IPsec profile.
     
     For details, see [Applying an IPsec Policy](dc_vrp_ipsec_cfg_all_0015.html).

#### Verifying the Security Hardening Result

* Run the [**display nhrp peer**](cmdqueryname=display+nhrp+peer) command to check information about the NHRP peer table.
* Run [**display ipsec sa**](cmdqueryname=display+ipsec+sa) to check the configuration of the current SA.