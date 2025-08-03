(Optional) Configuring IGMP Prompt-Leave
========================================

(Optional) Configuring IGMP Prompt-Leave

#### Context

In some applications, an IGMP querier's interface connects to only one receiver host. If the host frequently switches between multiple multicast groups, you can configure IGMP prompt-leave on the IGMP querier so that it quickly responds to Leave messages sent from the host.

After IGMP prompt-leave is configured, the querier does not send a Group-Specific Query message after receiving a Leave message from the host. Instead, it directly deletes the IGMP group entry corresponding to the host. This reduces the response delay and saves network bandwidth.

IGMP prompt-leave is applicable only to IGMPv2.

To configure IGMP prompt-leave based on ACL rules, you need to configure a basic ACL or an advanced ACL in advance.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. (Optional) Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
3. Enter the view of the interface connected to the user network segment.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
4. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   Determine whether to perform this step based on the current interface working mode.
5. Configure IGMP prompt-leave.
   
   
   ```
   [igmp prompt-leave](cmdqueryname=igmp+prompt-leave) [ group-policy { acl-number | acl-name acl-name } ]
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If **group-policy** is not specified, the interface implements prompt-leave for all Leave requests.
   
   If **group-policy** is specified:
   * If a multicast group matches the **permit** action in an ACL rule, the interface implements prompt-leave for this group's Leave requests.
   * If a multicast group matches the **deny** action in an ACL rule, the interface does not implement prompt-leave for this group's Leave requests.
   * If a multicast group does not match any ACL rule, the interface does not implement prompt-leave for this group's Leave requests.
   * If a specified ACL does not exist or contain rules, the interface does not implement prompt-leave for any Leave requests.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```