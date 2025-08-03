Configuring the Maximum Number of IGMP Entries on an Interface
==============================================================

Configuring the Maximum Number of IGMP Entries on an Interface

#### Context

IGMP-limit is configured on an interface to limit the number of multicast groups or source-specific groups. This improves the clarity and stability of programs for users who have joined multicast groups.

To configure the maximum number of IGMP entries based on ACL rules, you need to configure a basic ACL or an advanced ACL in advance.


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
4. Configure the maximum number of IGMP entries on the interface.
   
   
   ```
   [igmp access-limit](cmdqueryname=igmp+access-limit) number [ except { acl-number | acl-name acl-name } ]
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```