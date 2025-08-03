(Optional) Configuring an IPsec Profile
=======================================

Configure an IPsec profile to encrypt transmitted data to improve network security.

#### Context

Data transmitted between the HQ and branches, and between branches can be encrypted to increase data security. Bind an IPsec profile to DSVPN so that an mGRE tunnel and an IPsec tunnel are dynamically established between branches.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

For security purposes, you are advised not to use weak security algorithms in this feature. If you need to use such an algorithm, run the [**undo crypto weak-algorithm disable**](cmdqueryname=undo+crypto+weak-algorithm+disable) command to enable the weak security algorithm function.



#### Procedure

1. For details, see [Configuring an IKE Proposal](dc_vrp_ipsec_cfg_all_0011.html).
2. For details, see [Configuring an IKE Peer](dc_vrp_ipsec_cfg_all_0012.html).
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   You do not need to run the [**remote-id**](cmdqueryname=remote-id) *remote-id* command to set a peer ID or the [**remote-address**](cmdqueryname=remote-address) [ **authentication-address** | **vpn-instance** *vpn-instance-name* ] *remote-low-address* [ *remote-high-address* ] command to set a peer IP address for DSVPN.
   
   You do not need to run the **sa binding** **vpn-instance** **vpn-instance-name** command for DSVPN. The IPsec tunnel uses the reserved VPN instance \_\_VPN\_MGRE\_IPSEC\_\_ by default.
3. For details, see [Configuring an IPsec Proposal](dc_vrp_ipsec_cfg_all_0013.html).
4. (Optional) Configure an IKE filter set.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**ike identity**](cmdqueryname=ike+identity) *name*
      
      
      
      The local filter set is configured for IKE negotiation, and the IKE filter set view is displayed.
   3. Run [**ip address**](cmdqueryname=ip+address) *ip-address* { *mask* | *mask-length* }
      
      
      
      An IP address is configured for the IKE peer that is allowed to access the local device.
   4. Run [**fqdn**](cmdqueryname=fqdn) *fqdn*
      
      
      
      The domain name of the IKE peer that is allowed to access the device is configured.
   5. Run [**user-fqdn**](cmdqueryname=user-fqdn) *user-fqdn*
      
      
      
      A host domain name is configured for the IKE peer that is allowed to access the device.
   6. Run [**dn**](cmdqueryname=dn) *dn*
      
      
      
      The identifiable name of a digital certificate is configured for the IKE peer that is allowed to access the device.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the IKE filter set view.
   8. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
5. Configure an IPsec profile.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**ipsec policy**](cmdqueryname=ipsec+policy) *policy-name* **profile**
      
      
      
      The IPsec profile view is displayed.
   3. Run [**proposal**](cmdqueryname=proposal) *proposal-name*
      
      
      
      An IPsec proposal is applied in the IPsec profile.
   4. Run [**ike-peer**](cmdqueryname=ike-peer) *peer-name*
      
      
      
      An IKE peer is applied in the IPsec profile.
   5. (Optional) Run [**pfs**](cmdqueryname=pfs) { **dh-group1** | **dh-group2** | **dh-group5** | **dh-group14** | **group15** | **group16** | **dh-group19** | **dh-group20** | **dh-group21** }
      
      
      
      PFS used for negotiation is configured.
      
      
      
      If the local end uses PFS, the peer must perform PFS exchange when initiating a negotiation. The DH groups specified on the local and peer ends must be consistent. Otherwise, the negotiation fails.
   6. (Optional) Run [**remote ike-identity**](cmdqueryname=remote+ike-identity) *name*
      
      
      
      A filter set that allows matching IKE peers to access the local device is configured.
      
      
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If the IPsec profile applies the previously defined IKE filter set (IKE identity), the negotiation is performed based on the IKE filter set. Otherwise, filter is not performed.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Exit the IPsec profile view.
   8. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
6. Apply the IPsec profile.
   
   
   
   For details, see [Applying an IPsec Policy](dc_vrp_ipsec_cfg_all_0015.html).