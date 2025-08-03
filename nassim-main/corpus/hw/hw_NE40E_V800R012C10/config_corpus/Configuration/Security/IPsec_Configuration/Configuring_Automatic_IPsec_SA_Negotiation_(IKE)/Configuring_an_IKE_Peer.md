Configuring an IKE Peer
=======================

Through IKE peers, a series of attribute data can be defined to describe parameters required by IKE negotiation, including quoting IKE proposals, and configuring the negotiation mode, NAT traversal, and IKE version.

#### Context

During the configuration of an IKE peer, note the following:

* When IPsec is deployed, the path from the local to the peer and its return path can be the same or different. If they are different, they must work in load balancing mode.
* If the pre-shared key authentication mode is adopted, you need to configure the same authentication key for both ends of the IPsec tunnel.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ike peer**](cmdqueryname=ike+peer) *peer-name*
   
   
   
   An IKE peer is created and the IKE peer view is displayed.
3. Run [**ike-proposal**](cmdqueryname=ike-proposal+default) { *proposal-number* | **default** }
   
   
   
   The IKE proposal is applied in the IKE peer.
   
   ![](../../../../public_sys-resources/notice_3.0-en-us.png) 
   
   If the **default** parameter in the format is used, the default IKE proposal is used. The system provides three default IKE proposals. If no IKE proposal is created, default1, default2, and default3 are used. The default IKE proposals contain insecure algorithms. To ensure better security, you are advised not to use the default IKE proposals.
4. Run [**local-id-type**](cmdqueryname=local-id-type+ip+fqdn+dn+user-fqdn) { **ip** | **fqdn** | **dn** | **user-fqdn** [ *user-fqdn* ] }
   
   
   
   An IKE peer ID type is set.
5. Configure the ID of the IKE peer.
   
   
   * If the ID type is configured as the IP address format, run [**remote-address**](cmdqueryname=remote-address+authentication-address+vpn-instance) [ **authentication-address** | **vpn-instance** *vpn-instance-name* ] *remote-low-address* [ *remote-high-address* ]
     
     The IP address or IP address segment of the peer end is specified.
     
     **authentication-address** indicates the authentication address of the peer end. **authentication-address** is valid only when the ID type is configured as the IP address format.
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     If the IKE peer is referred to by the IPsec policy template, the IP address of the peer end can be also specified as an IP address segment.
   * If the ID type is configured as the **fqdn**, perform the following operations:
     
     + Run [**remote-id**](cmdqueryname=remote-id) *remote-id*
       
       The ID of the peer is specified.
     + Run [**remote-address**](cmdqueryname=remote-address+authentication-address+vpn-instance) [ **authentication-address** | **vpn-instance** *vpn-instance-name* ] *remote-low-address* [ *remote-high-address* ]
       
       The IP address or IP address segment of the peer end is specified.
       
       ![](../../../../public_sys-resources/note_3.0-en-us.png) 
       
       If the IKE peer is referred to by the IPsec policy, the IP address of the peer end must be specified, but cannot be specified as an IP address segment.
       
       If the IKE peer is referred to by the IPsec policy template, the IP address of the peer end may not be specified, or the IP address of the peer end may not be specified as an IP address segment. If the IP address of the peer end is not specified, it indicates that the IP address of the peer end can be any IP address.![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   If a local device corresponds to multiple IKE peers and two IKE peers are allocated the same IP address, the system prompts an address conflict, regardless of whether one is a private IP address and the other is a public IP address. If an IKE peer is allocated an IP address and another IKE peer is allocated an IP address segment that contains the IP address, the system does not prompt an address conflict.
6. (Optional) Run [**sa binding**](cmdqueryname=sa+binding+vpn-instance) **vpn-instance** *vpn-instance-name*
   
   
   
   A VPN instance is associated with an SA.
7. Run [**quit**](cmdqueryname=quit),
   
   
   
   Return to the system view.
8. (Optional) Run [**ike local-name**](cmdqueryname=ike+local-name) *local-name*
   
   
   
   The local end name used for IKE negotiation is configured.
9. Perform either of the following operations to configure an authentication mode for the peer.
   
   
   * The authentication mode is set to **pre-shared key (pre-share)**.
     1. Run the [**ike peer**](cmdqueryname=ike+peer) *peer-name*, command to enter the IKE peer view.
     2. Run the [**pre-shared-key**](cmdqueryname=pre-shared-key+cipher) [ **cipher** ] *key* command to configure a pre-shared key.
   * The authentication mode is set to **certificate (rsa-sig or rsassa-pss)**.
     
     1. Run the [**ike peer**](cmdqueryname=ike+peer) *peer-name*, command to enter the IKE peer view.
     2. Run the [**certificate local pki-domain**](cmdqueryname=certificate+local+pki-domain) *domain-name* command to bind a PKI domain with a specified domain name to an IKE peer
        
        The digital certificate must be configured in advance. For details, see PKI Configuration, see Configuring Offline Certificate Application or Configuring CMPv2-based Certificate Application.
     3. (Optional) Run the [**certificate local-filename**](cmdqueryname=certificate+local-filename) *filename* command to configure the name of a certificate used by the local end.
        
        The digital certificate must be configured in advance. For details, see PKI Configuration, see Configuring Offline Certificate Application or Configuring CMPv2-based Certificate Application.
        
        ![](../../../../public_sys-resources/note_3.0-en-us.png) 
        
        In the IKE peer view, the [**certificate pki-domain**](cmdqueryname=certificate+pki-domain) command and [**certificate local-filename remote-filename**](cmdqueryname=certificate+local-filename+remote-filename) command are mutually exclusive. The [**certificate pki-domain**](cmdqueryname=certificate+pki-domain) command is recommended.
     4. (Optional) Run the [**ike verification pki enable**](cmdqueryname=ike+verification+pki+enable) command to enable PKI certificate-related file verification.
        
        By default, PKI certificate-related file verification is enabled. Perform this step if the function needs to be enabled again after being disabled.
10. Run [**commit**](cmdqueryname=commit)
    
    
    
    The configuration is committed.