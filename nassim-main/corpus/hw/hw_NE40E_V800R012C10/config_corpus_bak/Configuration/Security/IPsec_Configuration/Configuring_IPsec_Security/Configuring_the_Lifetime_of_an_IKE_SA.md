Configuring the Lifetime of an IKE SA
=====================================

By configuring the lifetime of an SA, you can prevent potential security risks if a key is used for a long period of time. The long-term use of keys increases the risk of theft and cracking. The longer the use time, the higher the risk of theft and cracking.

#### Procedure

* Set the lifetime of an IKE SA.
  
  
  
  For configuration details, see [Configuring the IKE Proposal](dc_vrp_ipsec_cfg_all_0011.html).
* Set the lifetime of an IPsec SA (global SA lifetime).
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. (Optional) Run [**ipsec sa global-duration**](cmdqueryname=ipsec+sa+global-duration+traffic-based+traffic-based+disable) { **traffic-based** *kilobytes* | **traffic-based** **disable** | **time-based** *seconds* }
     
     
     
     The global SA lifetime is set.
     
     Pay attention to the following aspects when configuring the global SA lifetime:
     
     + If the lifetime is not specified for a specific SA, the SA uses the global SA lifetime.
     + When the global SA lifetime is changed, the policies for which the lifetime is independently configured are not affected, and the established SAs are not affected. In subsequent IKE negotiations, the new global SA lifetime is used to establish new SAs.
  3. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Set the lifetime of the IPsec SA (per-SA lifetime).
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Enter the IPsec policy view or IPsec policy template view based on actual requirements.
     
     
     + Run the [**ipsec policy**](cmdqueryname=ipsec+policy+isakmp) *policy-name* *policy-seqnum* **isakmp** command to enter the IPsec policy view.
     + Run the [**ipsec policy-template**](cmdqueryname=ipsec+policy-template) *template-name* *seq-number* command to enter the IPsec policy template view.
  3. (Optional) Run [**sa duration**](cmdqueryname=sa+duration+traffic-based+traffic-based+disable+time-based) { **traffic-based** *kilobytes* | **traffic-based** **disable** | **time-based** *seconds* }
     
     
     
     The lifetime of the current IPsec SA is set.
     
     Pay attention to the following aspects when setting the lifetime of an IPsec SA:
     
     + When the IPsec SA is established through IKEv2 negotiation, the lifetime is not negotiated. Both ends of the tunnel can use the respective lifetime. The lifetime configured on both ends is not required to be consistent. When the lifetime on one end expires, this end proactively initiates the negotiation, and the peer end responds to the negotiation.
     + If the lifetime is changed, the established SAs are not affected. In subsequent IKE negotiations, the new SA lifetime is used to establish new SAs.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.

#### Follow-up Procedure

Run the [**display ipsec sa duration**](cmdqueryname=display+ipsec+sa+duration) command to check the global IPsec SA lifetime.