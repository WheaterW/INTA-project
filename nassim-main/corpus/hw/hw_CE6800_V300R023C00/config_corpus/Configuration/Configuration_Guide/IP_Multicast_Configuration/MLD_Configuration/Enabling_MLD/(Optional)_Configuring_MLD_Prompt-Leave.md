(Optional) Configuring MLD Prompt-Leave
=======================================

(Optional) Configuring MLD Prompt-Leave

#### Context

Typically, after receiving a Multicast Listener Done message for a multicast group from an interface, a device sends a last-member query message to check whether this multicast group has other members. To minimize the response delay and conserve network bandwidth, configure prompt-leave on the interface. After receiving a Multicast Listener Done message for a multicast group from the interface, the device with prompt-leave configured immediately deletes the downstream interface from the entry corresponding to the multicast group, without sending a last-member query message.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Enter the view of the interface connected to the user network segment.
   
   
   ```
   [interface](cmdqueryname=interface) interface-type interface-number
   ```
3. Switch the interface working mode from Layer 2 to Layer 3.
   
   
   ```
   [undo portswitch](cmdqueryname=undo+portswitch)
   ```
   
   
   
   Determine whether to perform this step based on the current interface working mode.
4. Configure MLD prompt-leave.
   
   
   ```
   [mld prompt-leave](cmdqueryname=mld+prompt-leave) [ group-policy { basic-acl6-number | acl6-name acl6-name } ]
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If **group-policy** is not specified, the interface implements prompt-leave for all Done requests.
   
   If **group-policy** is specified:
   * If a multicast group matches the **permit** action in an ACL6 rule, the interface implements prompt-leave for this group's Done requests.
   * If a multicast group matches the **deny** action in an ACL6 rule, the interface does not implement prompt-leave for this group's Done requests.
   * If a multicast group does not match any ACL6 rule, the interface does not implement prompt-leave for this group's Done requests.
   * If a specified ACL6 does not exist or does not contain rules, the interface does not implement prompt-leave for any Done requests.
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```