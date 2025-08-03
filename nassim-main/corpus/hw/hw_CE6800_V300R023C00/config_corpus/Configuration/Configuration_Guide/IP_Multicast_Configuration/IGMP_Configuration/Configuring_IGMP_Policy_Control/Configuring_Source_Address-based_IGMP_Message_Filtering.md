Configuring Source Address-based IGMP Message Filtering
=======================================================

Configuring Source Address-based IGMP Message Filtering

#### Prerequisites

Before configuring source address-based IGMP message filtering, configure a basic ACL or an advanced ACL.


#### Context

To improve security and prevent other devices on a network from forging IGMP messages to affect normal multicast services, you can configure source address-based IGMP message filtering on the interfaces connecting the device to user hosts.

By default, source address-based IGMP message filtering is not configured on a device.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Return to the system view.
   
   
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
5. Configure source address-based IGMP Report or Leave message filtering.
   
   
   ```
   [igmp ip-source-policy](cmdqueryname=igmp+ip-source-policy) [ basic-acl-number | acl-name acl-name ]
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   If this command is run but no ACL rule is configured, the device processes only the IGMP Report or Leave messages whose source address is 0.0.0.0 or on the same network segment as the address of the interface receiving the messages.
   
   If an ACL is configured on an interface, the interface performs source address-based filtering for IGMP Report or Leave messages according to the following rules:
   * If an IGMP Report or Leave message matches an ACL rule and the action is **permit**, the interface accepts this message.
   * If an IGMP Report or Leave message matches an ACL rule and the action is **deny**, the interface rejects this message.
   * If an IGMP Report or Leave message does not match any ACL rule, the interface rejects this message.
   * If a specified ACL does not exist or contain rules, the interface rejects all IGMP Report and Leave messages.
6. Configure source address-based IGMP Query message filtering.
   
   
   ```
   [igmp query ip-source-policy](cmdqueryname=igmp+query+ip-source-policy) { basic-acl-number | acl-name acl-name }
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   
   After this command is run, the processing rules are as follows:
   
   * If an IGMP Query message matches an ACL rule and the action is **permit**, the interface accepts this message.
   * If an IGMP Query message matches an ACL rule and the action is **deny**, the interface rejects this message.
   * If an IGMP Query message does not match any ACL rule, the interface rejects this message.
   * If a specified ACL does not exist or contain rules, the interface rejects all IGMP Query messages.
7. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```