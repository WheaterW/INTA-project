(Optional) Configuring an Interface to Statically Join an MLD Group
===================================================================

After an interface on a multicast device is configured to statically join an MLD group, the multicast device considers that the interface has a static multicast group member and forwards multicast packets to this interface, irrespective of whether hosts connected to this interface request the multicast packets.

#### Context

If IPv6 users on a user network segment frequently request multicast data, configure an interface connected to this user network segment to statically join an MLD group. Then, the interface can rapidly respond to users' requests, which shortens the channel switching delay.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**mld static-group**](cmdqueryname=mld+static-group) *ipv6-group-address* [ **inc-step-mask** *ipv6-group-mask-length* **number** *group-number* ] [ **source** *ipv6-source-address* ]
   
   
   
   The interface is configured to statically join an MLD group.
   
   
   
   The [**mld static-group**](cmdqueryname=mld+static-group) command can be run only on interfaces connected to user hosts. The command allows you to add an interface to a single or multiple groups at a time, including source-specific groups.
   
   After an interface is configured to statically join an MLD group, multicast entries generated on this Router interface never time-out. Therefore, the Router keeps forwarding multicast data to the interface. If the interface no longer requires IPv6 multicast data of a group, run the [**undo mld static-group**](cmdqueryname=undo+mld+static-group) command to delete the interface from the group.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.