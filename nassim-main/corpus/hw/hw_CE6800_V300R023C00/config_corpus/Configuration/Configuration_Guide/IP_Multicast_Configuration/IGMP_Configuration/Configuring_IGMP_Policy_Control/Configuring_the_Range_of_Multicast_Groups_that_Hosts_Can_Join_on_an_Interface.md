Configuring the Range of Multicast Groups that Hosts Can Join on an Interface
=============================================================================

Configuring the Range of Multicast Groups that Hosts Can Join on an Interface

#### Prerequisites

Before configuring the range of multicast groups that hosts can join on an interface, you need to configure a basic ACL or an advanced ACL.


#### Context

To limit the range of multicast groups that hosts can join, configure a filtering policy on a multicast device's interface connected to the user network segment.


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
5. Configure the range of multicast groups that hosts can join on the interface.
   
   
   ```
   [igmp group-policy](cmdqueryname=igmp+group-policy) { acl-number | acl-name acl-name } [ 1 | 2 | 3 ]
   ```
   
   
   ![](public_sys-resources/note_3.0-en-us.png) 
   * If a multicast group matches an ACL rule and the action is **permit**, the interface allows hosts to join this group.
   * If a multicast group matches an ACL rule and the action is **deny**, the interface does not allow hosts to join this group.
   * If a multicast group does not match any ACL rule, the interface does not allow hosts to join this group.
   * If a specified ACL does not exist or contain rules, the interface does not allow hosts to join any multicast group.
6. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```