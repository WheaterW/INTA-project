(Optional) Binding an IPv6 Address Pool to a BAS Interface
==========================================================

When different users go online through the same domain and different IPv6 address segments need to be configured for these users, you can bind an IPv6 address pool to the BAS interface from which the users go online so that the IPv6 address range for the users in the domain can be limited based on the BAS interface.

#### Prerequisites

The specified address pool has been created and bound to a prefix pool.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**interface**](cmdqueryname=interface) { *interface-name* | *interface-type* *interface-number* } command to enter the view of the interface to which an address pool needs to be bound.
3. Run the [**bas**](cmdqueryname=bas) command to enter the BAS interface view.
4. Run the [**access-type layer2-subscriber**](cmdqueryname=access-type+layer2-subscriber) command to configure the BAS interface as a Layer 2 user interface.
5. Run the [**authentication-method-ipv6**](cmdqueryname=authentication-method-ipv6) **bind** command to configure the IPv6 user authentication mode as binding authentication for the BAS interface.
6. Run the [**ipv6-pool**](cmdqueryname=ipv6-pool) *pool-name* command to bind a specified IPv6 address pool to the BAS interface.
7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.