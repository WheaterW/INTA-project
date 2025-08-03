Configuring the Maximum Number of MLD Entries on an Interface
=============================================================

Configuring the Maximum Number of MLD Entries on an Interface

#### Context

MLD-limit is configured on an interface to limit the number of multicast groups or source-specific groups. This improves the clarity and stability of programs for users who have joined multicast groups.

To configure the maximum number of MLD entries based on ACL6 rules, you need to configure a basic ACL6 or an advanced ACL6 in advance.


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
4. Configure the maximum number of MLD entries on the interface.
   
   
   ```
   [mld access-limit](cmdqueryname=mld+access-limit) number [ except {  ExceptAclNumValue | acl6-name ExceptAclNameValue } ]
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```