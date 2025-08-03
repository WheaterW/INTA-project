Enabling Association Between ND Probe and DHCPv6 Snooping
=========================================================

The system periodically performs ND probe on users' IPv6 addresses. If a user cannot be detected for the specified number of probes, the system will delete the DHCPv6 binding entry corresponding to the user and construct a DHCPv6 Release message to notify the DHCPv6 server of releasing the user's IPv6 address.

#### Context

If a user goes offline unexpectedly after obtaining an IPv6 address, the client cannot send a DHCPv6 Release message to release this IPv6 address, causing a waste of IPv6 resources. To avoid this, you can enable association between ND probe and DHCPv6 snooping.


#### Procedure

1. Run the **system-view** command to enter the system view.
2. Run the [**dhcpv6 snooping nd-detect enable**](cmdqueryname=dhcpv6+snooping+nd-detect+enable) command to enable association between ND probe and DHCPv6 snooping.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.