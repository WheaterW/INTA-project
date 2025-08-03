Configuring BGP Message Extension
=================================

With the enhancement of BGP capabilities, a BGP session needs to negotiate multiple capabilities and use BGP messages to carry information about the routes and route attributes to be advertised. However, the length of BGP messages is limited. You can enable BGP message extension to remove the limit on the length of BGP messages.

#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**bgp**](cmdqueryname=bgp) *as-number* command to enter the BGP view.
3. Run the **[**peer**](cmdqueryname=peer+extended-open-message)** { **peerIpv4Addr** | **peerGroupName** } **[**extended-open-message**](cmdqueryname=peer+extended-open-message)** command to enable the BGP Open message extension function so that the length of an Open message can be greater than 255 bytes.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.