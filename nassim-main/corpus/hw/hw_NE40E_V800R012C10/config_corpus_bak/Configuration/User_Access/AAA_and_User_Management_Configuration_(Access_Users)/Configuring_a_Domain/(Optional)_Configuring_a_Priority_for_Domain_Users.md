(Optional) Configuring a Priority for Domain Users
==================================================

You can configure a priority for domain users so that users or services with different priorities are offered different services.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. Run [**domain**](cmdqueryname=domain) *domain-name*
   
   
   
   The domain view is displayed.
4. Run [**user-priority**](cmdqueryname=user-priority) { **upstream** | **downstream** } { *priority* | **trust-8021p-inner** | **trust-8021p-outer** | **trust-dscp-inner** | **trust-dscp-outer** | **unchangeable** | **trust-exp-inner** | **trust-exp-outer** }
   
   
   
   A priority is configured for domain users.
   
   
   
   Currently, only one user priority can be configured for a domain.
   
   * *priority*: specifies a user priority. The value ranges from 0 to 7.
   * **trust-8021p-inner**: indicates that the 802.1p value in the inner tag of a Layer 2 user packet is used as the user priority.
   * **trust-8021p-outer**: indicates that the 802.1p value in the outer tag of a Layer 2 user packet is used as the user priority.
   * **trust-dscp-inner**: indicates that the DSCP value in the inner tag of a user packet is used as the user priority.
   * **trust-dscp-outer**: indicates that the DSCP value in the outer tag of a user packet is used as the user priority.
   * **unchangeable**: indicates that the user priority remains unchanged.
   * **trust-exp-inner**: indicates that the EXP value in the inner tag of an MPLS packet is used as the user priority.
   * **trust-exp-outer**: indicates that the EXP value in the outer tag of an MPLS packet is used as the user priority.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.