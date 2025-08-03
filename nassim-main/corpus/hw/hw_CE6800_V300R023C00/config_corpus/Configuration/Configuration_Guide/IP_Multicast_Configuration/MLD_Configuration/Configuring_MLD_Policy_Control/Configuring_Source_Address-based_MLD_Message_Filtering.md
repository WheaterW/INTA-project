Configuring Source Address-based MLD Message Filtering
======================================================

Configuring Source Address-based MLD Message Filtering

#### Prerequisites

Before configuring source address-based MLD message filtering, configure a basic ACL6 or an advanced ACL6.


#### Context

To prevent other devices on a network from affecting normal multicast services by forging MLD messages, and thereby improve security, you can configure source address-based MLD message filtering on the interfaces connecting the device to user hosts.

By default, source address-based MLD message filtering is not configured on a device.

After you configure source address-based MLD message filtering on a device's interface connected to user hosts, the interface filters MLD messages based on the ACL6 configuration.


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
4. Configure source address-based MLD Report or Done message filtering.
   
   
   ```
   [mld ip-source-policy](cmdqueryname=mld+ip-source-policy) { basic-acl6-number | acl6-name acl6-name }
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * If an MLD Report or Done message matches an ACL6 rule and the action is **permit**, the interface accepts this message.
   * If an MLD Report or Done message matches an ACL6 rule and the action is **deny**, the interface rejects this message.
   * If an MLD Report or Done message does not match any ACL6 rule, the interface rejects this message.
   * If a specified ACL6 does not exist or does not contain rules, the interface rejects all MLD Report or Done messages.
5. Configure source address-based MLD Query message filtering.
   
   
   ```
   [mld query ip-source-policy](cmdqueryname=mld+query+ip-source-policy) { basic-acl6-number | acl6-name acl6-name }
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * If an MLD Query message matches an ACL6 rule and the action is **permit**, the interface accepts this message.
   * If an MLD Query message matches an ACL6 rule and the action is **deny**, the interface rejects this message.
   * If an MLD Query message does not match any ACL6 rule, the interface rejects this message.
   * If a specified ACL6 does not exist or does not contain rules, the interface rejects all MLD Query messages.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```