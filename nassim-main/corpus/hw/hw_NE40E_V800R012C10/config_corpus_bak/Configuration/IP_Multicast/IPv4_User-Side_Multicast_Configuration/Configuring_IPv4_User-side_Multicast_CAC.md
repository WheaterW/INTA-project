Configuring IPv4 User-side Multicast CAC
========================================

To implement refined bandwidth control for users, configure user-side multicast CAC, which helps improve multicast service quality.

#### Usage Scenario

A conventional method to ensure multicast service quality is to limit the maximum number of multicast groups that users can join. This method becomes incompetent due to the increase of IPTV service volume, and carriers require a more refined method to manage and control bandwidth resources. User-side multicast CAC, working with the preceding conventional method, resolves these issues by allowing user-based and interface-based bandwidth limiting.


#### Pre-configuration Tasks

Before configuring user-side multicast CAC, complete the tasks shown in [Figure 1](#EN-US_TASK_0172367641__fig_dc_ne_bras-multicast_cac_cfg_000103). For configuration details, see [Table 1](#EN-US_TASK_0172367641__table_dc_ne_bras-multicast_cac_cfg_000101).

**Figure 1** Pre-configuration tasks for user-side multicast CAC configurations  
![](images/fig_dc_ne_bras-multicast_cac_cfg_000103.png)

**Table 1** Description of each pre-configuration task
| Item | Description |
| --- | --- |
|  | Configure an IPv4 Address Pool to Assign IP Addresses to Online Users. |
|  | Configure Authentication, Authorization and Accounting (AAA) schemes. |
|  | Configure a domain to implement AAA functions and manage access users. |
|  | Configure the PPPoE or IPoE access mode.   * [Configure the PPPoE access mode.](dc_ne_pppoe_cfg_0004.html) * Configure the IPoE access mode. |
|  | Configure basic multicast functions.   1. Configure multicast static routes. 2. Enable PIM-SM. 3. Enable IGMP. |
|  | Configure a BAS interface. |





#### Procedure

1. Configure a global multicast bandwidth limit policy.
   1. Run [**system-view**](cmdqueryname=system-view)
      
      
      
      The system view is displayed.
   2. Run [**multicast bas-policy**](cmdqueryname=multicast+bas-policy)
      
      
      
      A multicast BAS policy view is created and displayed.
   3. Run [**policy**](cmdqueryname=policy) *policy-name*
      
      
      
      A multicast bandwidth limit policy is created, and the policy view is displayed.
   4. (Optional) Run [**unspecified-channel permit**](cmdqueryname=unspecified-channel+permit)
      
      
      
      Users are allowed to join multicast groups that are not specified in a channel, and the device is configured not to count the bandwidth consumed by such groups.
   5. Run [**channel**](cmdqueryname=channel) *channel-name*
      
      
      
      A multicast channel is configured, and the channel view is displayed.
   6. Run [**group**](cmdqueryname=group) *group-address* **mask** { *group-mask-length* | *group-mask* } [ **source** *source-address* **mask** { *source-mask-length* | *source-mask* } ] { **per-bandwidth** *traffic-rate* { **level-1** | **level-2** } }
      
      
      
      A (\*, G) or (S, G) multicast group range, the bandwidth occupied by each group, and the level of bandwidth resources that a group consumes are specified.
   7. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the multicast bandwidth limit policy view.
   8. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the multicast BAS policy view.
   9. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
2. Configure a multicast bandwidth limit policy for each user in a specific domain.
   1. Run [**aaa**](cmdqueryname=aaa)
      
      
      
      The AAA view is displayed.
   2. Run [**domain**](cmdqueryname=domain) *domain-name*
      
      
      
      The AAA domain view is displayed.
   3. Run [**commit**](cmdqueryname=commit)
      
      
      
      The configuration is committed.
   4. Run [**multicast**](cmdqueryname=multicast) **bas-policy** *policy-name* **out** **bandwidth** *traffic-rate* **level-1** *level-1-traffic-rate* **interface** **gigabitethernet**
      
      
      
      A user-side multicast bandwidth policy, the total maximum bandwidth for each user in the domain, and the maximum level-1 bandwidth for each user are specified in the AAA domain view.
   5. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the AAA view.
   6. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
3. Configure a multicast bandwidth limit policy for users on a specific interface.
   1. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
      
      
      
      The GE interface view is displayed.
   2. Run [**multicast**](cmdqueryname=multicast) **bas-policy** *policy-name* **out** **bandwidth** *traffic-rate* **level-1** *level-1-traffic-rate*
      
      
      
      A user-side multicast bandwidth policy is bound to the GE interface, the interface-level bandwidth limit is enabled, and the bandwidth limit is specified for the program ordered by users.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the GE interface view.
   4. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.
4. Enable multicast user-side CAC on the interface board.
   1. Run [**slot**](cmdqueryname=slot) *slot-id*
      
      
      
      The slot view is displayed.
   2. Run [**multicast**](cmdqueryname=multicast) **bas-policy** **out** **enable** **interface** **gigabitethernet**
      
      
      
      Multicast user-side CAC is enabled on the interface board.
   3. Run [**quit**](cmdqueryname=quit)
      
      
      
      Return to the system view.

#### Verifying the Configuration

Run the [**display multicast bas-policy policy**](cmdqueryname=display+multicast+bas-policy+policy) *policy-name* **slot** *slot-id* command to check information about global policy entries delivered to an interface board.

Run the [**display multicast bas-policy out user**](cmdqueryname=display+multicast+bas-policy+out+user) *user-id* command to check information about the multicast BAS policy of a specific user, as well as bandwidth statistics.

Run the [**display multicast bas-policy out interface**](cmdqueryname=display+multicast+bas-policy+out+interface) *interface-type interface-number* command to check information about the multicast BAS policy and bandwidth statistics of a specified interface.