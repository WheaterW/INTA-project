Configuring IGMP Static-Group Join
==================================

After an interface on a multicast device is configured to statically join an IGMP group, the multicast device considers that the interface has static multicast group member and forwards multicast packets to this interface, irrespective of whether hosts connected to this interface request the multicast packets.

#### Usage Scenario

If users on a user network segment frequently request multicast data, configure an interface connected to this network segment to statically join an IGMP group. Then, the interface can rapidly respond to users' requests, which shortens the channel switching delay.


#### Pre-configuration Tasks

Before configuring an IGMP user to statically join a multicast group, configure a unicast routing protocol to ensure that unicast routes are reachable.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**interface**](cmdqueryname=interface) *interface-type* *interface-number*
   
   
   
   The interface view is displayed.
3. Run [**igmp static-group**](cmdqueryname=igmp+static-group) *group-address* [ **inc-step-mask** { *group-mask* | *group-mask-length* } **number** *group-number* ] [ **source** *source-address* ]
   
   
   
   The interface is configured to statically join an IGMP group.
   
   The [**igmp static-group**](cmdqueryname=igmp+static-group) command can be run only on interfaces that connect to user hosts. The command allows you to add an interface to a single or multiple groups at a time, including source-specific groups.
   
   After an interface is configured to statically join a multicast group, multicast entries generated on this interface never expire. Therefore, the Router keeps forwarding multicast data to the interface. If the interface no longer requires multicast data of a group, run the [**undo igmp static-group**](cmdqueryname=undo+igmp+static-group) command to delete the interface from the group.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

Run the [**display igmp**](cmdqueryname=display+igmp) [ **vpn-instance** *vpn-instance-name* | **all-instance** ]  **group** [ *group-address* | **interface** *interface-type* *interface-number* ] \* [ **static** ] [ **verbose** ] command to check information about IGMP group members.

Run the [**display igmp group static**](cmdqueryname=display+igmp+group+static) command. The command output shows information about the multicast groups that interfaces in the public network instance statically join.