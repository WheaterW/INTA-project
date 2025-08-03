Configuring IPsec Anti-Replay
=============================

IPsec anti-replay prevents IPsec from replay attacks and improves the reliability of IPsec tunnels.

#### Context

You can configure the IPsec anti-replay window using either of the following methods:

* Global configuration
  
  A globally configured IPsec anti-replay window takes effect on all existing IPsec policies (except those who have local anti-replay windows), and therefore enhances configuration efficiency. You can configure a global parameter for all the IPsec policies that need a same window size instead of manually executing commands for each IPsec policy.
* Local configuration
  
  You can set an anti-replay window separately for a single IPsec policy. A separately configured anti-replay window has precedence over the global anti-replay window.

For details about the IPsec anti-replay feature, see [Configuring IPsec Security](dc_vrp_ipsec_cfg_all_0017.html).

![](../../../../public_sys-resources/note_3.0-en-us.png) 

To ensure proper service operation, any configuration of the IPsec anti-replay window takes effect only on the IPsec policies being negotiated right after being created or that being renegotiated, but not on the negotiated IPsec policies.



#### Procedure

* Global configuration
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ipsec sa global anti-replay**](cmdqueryname=ipsec+sa+global+anti-replay+disable) **disable**
     
     
     
     The anti-replay function is globally disabled.
     
     Disable the anti-replay function if packets are discarded on a lot of IPsec tunnels due to anti-replay protection. If packets are discarded on a few IPsec tunnels due to anti-replay protection, you can enable the anti-replay function for a specific IPsec policy.
     
     If the current network is subjected to replay attacks, you can enable the anti-replay function. If the existing network scenario is more complex, so that the packet sequence may be out of order, you can disable the anti-replay function.
  3. (Optional) Run [**ipsec sa global anti-replay**](cmdqueryname=ipsec+sa+global+anti-replay+window) **window** *window-size*
     
     
     
     The IPsec anti-replay window size is globally set.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Partial configuration
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Enter the IPsec policy view or IPsec policy template view based on actual requirements.
     
     
     + Run the [**ipsec policy**](cmdqueryname=ipsec+policy) *policy-name* *policy-seqnum* command to enter the IPsec policy view.
     + Run the [**ipsec policy-template**](cmdqueryname=ipsec+policy-template) *template-name* *seq-number* command to enter the IPsec policy template view.
  3. (Optional) Run [**sa anti-replay**](cmdqueryname=sa+anti-replay+enable+disable) { **enable** | **disable** }
     
     
     
     The anti-replay function is started in an IPsec policy or an IPsec policy template.
  4. (Optional) Run [**sa anti-replay**](cmdqueryname=sa+anti-replay+window) **window** *window-size*
     
     
     
     The anti-replay window size is set.
     
     If the anti-replay window size is not separately set for an IPsec policy after the anti-replay window in the IPsec policy is enabled, the global anti-replay window size takes effect in the IPsec policy.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.