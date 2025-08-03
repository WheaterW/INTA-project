Resetting the Address Pool Status
=================================

Resetting the Address Pool Status

#### Context

If an IPv6 address conflict occurs because two clients are assigned the same IPv6 address or if new IPv6 addresses or prefixes need to be assigned to clients due to network planning, you can set IPv6 addresses or prefixes in the IPv6 address pool to idle so that clients can re-apply for these IPv6 addresses or prefixes.

![](../../../../public_sys-resources/notice_3.0-en-us.png) 

If a user's IPv6 address or prefix is within the range specified using the [**reset dhcpv6 pool**](cmdqueryname=reset+dhcpv6+pool) command, the user cannot continue to use the IPv6 address or prefix. In this case, the user needs to send an IPv6 address application request again.

The address pool status cannot be restored after this command is run. Therefore, exercise caution when running this command.



#### Procedure

* Run the [**reset dhcpv6 pool**](cmdqueryname=reset+dhcpv6+pool) *pool-name* [ **binding** [ *duid* ] | { **conflict** | **allocated** } **address** | *ipv6-address* [ **to** *ipv6-address* ] | **allocated** **prefix** | *ipv6\_prefix* [ **to** *ipv6\_prefix\_end* ] ] command to clear a specified IPv6 address pool.