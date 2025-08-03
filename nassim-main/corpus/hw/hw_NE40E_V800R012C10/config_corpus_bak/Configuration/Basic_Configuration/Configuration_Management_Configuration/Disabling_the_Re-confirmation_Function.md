Disabling the Re-confirmation Function
======================================

Some device commands may result in serious consequences if operations are not properly performed. To avoid misoperations, re-confirmation is required by default.

#### Context

Misoperations of some **undo** commands cause the configurations of related features to be deleted, interrupting services and disconnecting the user network. By default, to prevent misoperations, you need to perform re-confirmation before running such **undo** commands. The commands cover [**undo mpls**](cmdqueryname=undo+mpls), [**undo mpls te**](cmdqueryname=undo+mpls+te), [**undo mpls rsvp**](cmdqueryname=undo+mpls+rsvp), [**undo mpls ldp**](cmdqueryname=undo+mpls+ldp), [**undo mpls l2vpn**](cmdqueryname=undo+mpls+l2vpn), [**undo multicast ipv6 routing-enable**](cmdqueryname=undo+multicast+ipv6+routing-enable), [**undo multicast routing-enable**](cmdqueryname=undo+multicast+routing-enable), [**undo pim**](cmdqueryname=undo+pim), [**undo igmp**](cmdqueryname=undo+igmp), [**undo stp enable**](cmdqueryname=undo+stp+enable), and [**undo bfd**](cmdqueryname=undo+bfd).

You are advised to enable the function because misoperations will cause services to be unavailable.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**configuration prevent-misoperation disable**](cmdqueryname=configuration+prevent-misoperation+disable)
   
   
   
   The re-confirmation function is disabled.
3. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.