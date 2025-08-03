Enabling Secondary Authentication
=================================

Secondary authentication prevents service interruptions caused by misoperations.

#### Context

Misoperations of some commands cause the configurations of related features to be deleted, interrupting services and disconnecting the user network. To prevent misoperations, you can enable secondary authentication.

After secondary authentication is enabled, you need to enter the login password for secondary authentication before running the [**reboot**](cmdqueryname=reboot), [**reset saved-configuration**](cmdqueryname=reset+saved-configuration), [**rollback configuration**](cmdqueryname=rollback+configuration), [**undo mpls**](cmdqueryname=undo+mpls), [**undo mpls te**](cmdqueryname=undo+mpls+te), [**undo mpls rsvp**](cmdqueryname=undo+mpls+rsvp), [**undo mpls ldp**](cmdqueryname=undo+mpls+ldp), [**undo mpls l2vpn**](cmdqueryname=undo+mpls+l2vpn), [**undo multicast ipv6 routing-enable**](cmdqueryname=undo+multicast+ipv6+routing-enable), [**undo multicast routing-enable**](cmdqueryname=undo+multicast+routing-enable), [**undo pim**](cmdqueryname=undo+pim), [**undo igmp**](cmdqueryname=undo+igmp), [**undo bgp**](cmdqueryname=undo+bgp), [**undo stp enable**](cmdqueryname=undo+stp+enable) command.![](../../../../public_sys-resources/note_3.0-en-us.png) 

To prevent some services from being unavailable due to misoperations, you are advised to enable secondary authentication.




#### Example

1. Run [**system-view**](cmdqueryname=system-view)
   
   The system view is displayed.
2. Run [**configuration re-authentication enable**](cmdqueryname=configuration+re-authentication+enable)
   
   Secondary authentication is enabled.
3. Run [**commit**](cmdqueryname=commit)
   
   The configuration is committed.