Locking the Tunnel Configuration
================================

Tunnel configurations can be locked by the controller when the configurations are sent to a NE40E.

#### Usage Scenario

In service delivery, a controller delivers tunnel configurations to a NE40E. The NE40E uses the obtained configurations to create a tunnel or modify an existing tunnel. To prevent users from modifying such tunnel configurations, the controller delivers the [**mpls te lock**](cmdqueryname=mpls+te+lock) command to lock the configurations, in addition to configurations to the NE40E. Before you modify the configuration of a tunnel, run the [**undo mpls te lock**](cmdqueryname=undo+mpls+te+lock) command to unlock the tunnel configuration on the tunnel interface.


#### Pre-configuration Tasks

Before locking the tunnel configuration, complete the following tasks:

* Configure the controller to deliver tunnel configurations to a NE40E.
* Assign a user management right.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface tunnel**](cmdqueryname=interface+tunnel) *interface-number*
   
   
   
   The tunnel interface view of an MPLS TE tunnel is displayed.
3. Run [**mpls te lock**](cmdqueryname=mpls+te+lock)
   
   
   
   The configuration of the MPLS TE tunnel is locked.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

After locking the tunnel configurations, verify that no command can be run on the tunnel interface to modify configurations and commands can be run only after the [**undo mpls te lock**](cmdqueryname=undo+mpls+te+lock) command is run to unlock the configurations.