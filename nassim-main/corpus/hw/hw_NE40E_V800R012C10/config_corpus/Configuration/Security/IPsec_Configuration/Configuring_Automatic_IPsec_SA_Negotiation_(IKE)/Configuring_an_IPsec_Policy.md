Configuring an IPsec Policy
===========================

IPsec policies include common policies and policy templates. You can either use IPsec policies at both ends of an IPsec tunnel or use the IPsec policy at one end and IPsec policy template at the other end.

#### Prerequisites

Before configuring an IPsec policy, complete the following tasks:

* [Defining Data Flows to Be Protected](dc_vrp_ipsec_cfg_all_0009.html)
* [Configuring an IKE Proposal](dc_vrp_ipsec_cfg_all_0011.html)
* [Configuring an IKE Peer](dc_vrp_ipsec_cfg_all_0012.html)
* [Configuring an IPsec Proposal](dc_vrp_ipsec_cfg_all_0013.html)

#### Context

You can configure the IPsec policy or IPsec policy template according to actual network environments. IPsec policy templates are mainly applied when the peer-end IP address is unfixed. [Table 1](#EN-US_TASK_0172372432__table_03A3A7EF) describes configuration rules and precautions.

**Table 1** Configuration rules and precautions
| Item | IPsec Policy Template | IPsec Policy |
| --- | --- | --- |
| Configuration rules | * Only one end of an IPsec tunnel can use an IPsec policy in template mode. The other end of the tunnel must use an IPsec policy in IKE mode. * Only one policy in an IPsec policy group can be created using the IPsec policy template, and the IPsec policy number must be larger than that of other IPsec policies. Otherwise, other IPsec policies may become invalid. * The ACL, IPsec proposal, and IKE peers must be configured in the IPsec policy template. Other parameters are optional.  In an IKE negotiation, parameters defined in the IPsec policy template must match those defined by the peer end. Parameters that are not defined in the IPsec policy template are determined by the initiating party, and the response party can accept the suggestions of the initiating party. * One policy template can use multiple IPsec proposals to match different IPsec proposals sent by different peer ends that initiate connection requests. * One policy template can use only one ACL. If a new ACL needs to be quoted, the original ACL must be canceled. | Rules for configuring IPsec policies in IKE mode are as follows:   * The ACL, IPsec proposal, and IKE peers must be configured in the IPsec policy in IKE mode. Other parameters are optional. * One IPsec policy can use multiple IPsec proposals to match different IPsec proposals sent by different peer ends that initiate connection requests. * One IPsec policy can use only one ACL. If a new ACL needs to be used, the original ACL must be canceled. |
| Precautions | A single tunnel interface can use only one security policy group. Before configuring another security policy group for the interface, you must delete the original security policy group. One security policy group can be applied only to one interface.  When a security policy group is applied to a tunnel interface, new policies cannot be added to this security policy group, and existing policies cannot be deleted from this security policy group. If you need to change the IPsec policies, you can run the **undo ipsec policy** command in the tunnel interface view to unbind the IPsec policy group and then modify the policies.  After a security policy group is applied to an interface, an SA is not immediately established. IKE negotiation is triggered to establish an SA only when the data flow that complies with an IPsec policy is transmitted over this interface.  When an interface sends a packet, the interface matches the packet against policies in the security policy group based on the sequence number in an ascending order. If the packet matches an ACL rule defined in a policy, the packet is processed based on the policy. If the packet does not match any ACL defined in the policy, the interface continues to match the packet against the next policy. If the packet does not match any ACL defined in all policies, the packet is directly sent (no protection measure is taken).  You can run the **undo ipsec policy** command in the interface view to delete all IKE and IPsec SAs. | |




#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. You can enter the IPsec policy view or IPsec policy template view according to actual network environments.
   
   
   
   **Table 2** Security policy configuration
   | Step/Item | IPsec Policy | IPsec Policy Template |
   | --- | --- | --- |
   | 1. Enter the IPsec policy view or IPsec policy template view. | [**ipsec policy**](cmdqueryname=ipsec+policy+isakmp) *policy-name* *sequence-number* **isakmp** | [**ipsec policy-template**](cmdqueryname=ipsec+policy-template) *template-name* *sequence-number* |
   | (Optional) Configure a local IP address. | [**local-address**](cmdqueryname=local-address) *ip-address* | [**local-address**](cmdqueryname=local-address+binding+interface+vlan) *localaddr* [ **binding** **interface** *interface-type* *interface-num* **vlan** [ *start-vlan-id1* *end-vlan-id1* [ *start-vlan-id2* *end-vlan-id2* [ *start-vlan-id3* *end-vlan-id3* ] ] ] ] |
   | To conserve IP address resources, IPsec supports an IP address that is borrowed from an interface. Therefore, the IP address of the local peer can be the same as that of another interface.  If the IP address of the local peer is the same as that of another interface on the device and the IPsec policy is configured on a tunnel interface, the device automatically generates the **binding tunnel ipsec** command configuration on the interface. This indicates that the interface has the IPsec policy bound to, and therefore cannot be used for other services. | |
   | 3. Configure an ACL in a policy. | [**security acl**](cmdqueryname=security+acl+name) { *acl-number* | **name** *acl-name* } | |
   | 4. Define a proposal. | [**proposal**](cmdqueryname=proposal) *proposal-name* &<1-6>  When you set up an SA by IKE negotiation, an IPsec policy or an IPsec policy template can use up to six IPsec proposals. IKE negotiation searches for completely matched IPsec proposals at the two ends of the security tunnel. If no completely matching IPsec proposal is found, the SA cannot be set up and the packets that need protection are discarded. | |
   | 5. Define an IKE peer. | [**ike-peer**](cmdqueryname=ike-peer) *peer-name*  NOTICE:  Ensure that the IKE peer has applied the IKE proposal that contains a security algorithm. If the IKE Peer does not apply an IKE proposal, the default IKE proposal containing an insecure algorithm may be used during IKE negotiation, which poses security risks. | |
   | 6. (Optional) Configure the PFS feature used for negotiation. | [**pfs**](cmdqueryname=pfs+dh-group1+dh-group2+dh-group5+dh-group14+dh-group19) { **dh-group1** | **dh-group2** | **dh-group5** | **dh-group14** | **group-15** | **group-16** | **dh-group19** | **dh-group20** | **dh-group21** }  If the local end uses PFS, the peer must perform PFS exchange when initiating a negotiation. The DH groups specified on the local end and the peer must be consistent. Otherwise, the negotiation fails. | |
   | 7. (Optional) Configure the QoS Priority of MPLS Packets | [**set service-class**](cmdqueryname=set+service-class+af1+af2+af3+af4+be+cs6+cs7+ef+inbound+outbound) { **af1** | **af2** | **af3** | **af4** | **be** | **cs6** | **cs7** | **ef** } { **inbound** | **outbound** }  NOTE:  The DSCP in the IP packet header and the EXP in the MPLS packet header map the internal service class of the packet, that is, the QoS priority of the packet.  To enable the EXP value in an MPLS packet header to inherit the DSCP value in the plaintext packet header, run the [**set service-class**](cmdqueryname=set+service-class+inherit-plain+inbound) **inherit-plain** **inbound** command. | |
   | 8. Define a policy template. | - | [**ipsec policy**](cmdqueryname=ipsec+policy+isakmp+template) *policy-name* *seq-number* **isakmp** [ **template** *template-name* ]  The IPsec policy is bound to the IPsec policy template. Then you can implement the IPsec policy template function by applying the IPsec policy to an interface.  NOTE:  In an IPsec policy group, only one IPsec policy can reference the IPsec policy template.  The name of the policy template cannot be identical with that of the IPsec policy. |
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.