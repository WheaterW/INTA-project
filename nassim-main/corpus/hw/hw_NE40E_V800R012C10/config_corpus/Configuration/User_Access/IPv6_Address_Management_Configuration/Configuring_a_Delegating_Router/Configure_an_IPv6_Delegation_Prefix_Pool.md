Configure an IPv6 Delegation Prefix Pool
========================================

When the NE40E functions as a delegating router, an IPv6 delegation prefix pool must be configured to manage prefixes.

#### Context

Only one prefix and its mask can be configured in a prefix pool. After a prefix pool is locked, the leases of addresses that have been assigned cannot be renewed, and new addresses cannot be assigned.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ipv6 prefix**](cmdqueryname=ipv6+prefix) *prefix-name* **delegation** command to create an IPv6 prefix pool and enter its view.
3. Run the [**prefix**](cmdqueryname=prefix) *prefix-address/prefix-length* [ **delegating-prefix-length** *delegating-prefix-length* ] command to configure an IPv6 address prefix.
   
   
   
   The *prefix-length* parameter specifies the length of a prefix. The assignable prefix length indicates the length of the IPv6 prefix which is assigned by a device that functions as a delegating router to the requesting router. The assignable prefix length configured in a prefix pool must be greater than the prefix length configured in the prefix pool. Otherwise, prefixes in the prefix pool cannot be assigned to users.
4. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
5. (Optional) Run the [**lock**](cmdqueryname=lock) command to lock an IPv6 prefix pool.
   
   
   
   After this command is run, no prefix in the locked prefix pool can be assigned, preventing new users from going online using prefixes in the prefix pool.
   
   This method is typically used when a prefix pool cannot be deleted because its prefixes are in use by online users. You can lock the prefix pool first to stop it from assigning prefixes. After all users go offline, the prefixes in the prefix pool are all released, and the prefix pool can then be deleted.
6. (Optional) Run the [**vpn-instance**](cmdqueryname=vpn-instance) *vpn-instance-name* command to bind a VPN instance to the prefix pool.
7. (Optional) Run the [**lifetime preferred-lifetime**](cmdqueryname=lifetime+preferred-lifetime) { **days** *days-value* [ **hours** *hours-value* [ **minutes** *minutes-value* ] ] | **infinite** } **valid-lifetime** { **days** *days-value* [ **hours** *hours-value* [ **minutes** *minutes-value* ] ] | **infinite** } command to configure the lifetime of IPv6 prefixes.
   
   
   
   The **preferred-lifetime** parameter is used to calculate the lease renewal time and rebinding time of the IPv6 prefix pool. The time value must be no less than 1 minute. The default value is two days.
   
   The **valid-lifetime** parameter specifies the validity period of a specified IPv6 prefix. The user using the prefix will be logged out after the validity period expires. The time value must be no less than 1 minute and the **preferred-lifetime** value. The default value is three days.
8. (Optional) Run the [**reserved prefix**](cmdqueryname=reserved+prefix) { **duid** | **mac** } [ **lease** ] command to configure the reservation type of user prefixes in the prefix pool.
   
   
   
   This command can be run only in the local and delegation prefix pools.
9. (Optional) Run the [**recycle prefix**](cmdqueryname=recycle+prefix) *start-prefix* [ *end-prefix* ] command to configure the prefix status as idle.
10. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
11. (Optional) Run the [**pd-unshare-only**](cmdqueryname=pd-unshare-only) command to configure the DHCPv6 IA\_PD prefix assignment mode for the delegation prefix pool.
    
    
    
    After the [**pd-unshare-only**](cmdqueryname=pd-unshare-only) command is run in the delegation prefix pool, this prefix pool can be used for prefix assignment only in DHCPv6 IA\_PD mode and is preferred in DHCPv6 IA\_PD prefix assignment.
12. (Optional) Run the [**recycle reserved ipv6-prefix**](cmdqueryname=recycle+reserved+ipv6-prefix) command to reclaim all reserved IPv6 prefixes in the prefix pool.
13. (Optional) Run the [**dhcpv6-unshare-only**](cmdqueryname=dhcpv6-unshare-only) command to configure the prefix pool to assign only addresses, not prefixes.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    This command is mutually exclusive with the following commands:
    
    * [**slaac-unshare-only**](cmdqueryname=slaac-unshare-only)
    * [**pd-unshare-only**](cmdqueryname=pd-unshare-only)
    * [**client-duid client-duid bind prefix**](cmdqueryname=client-duid+client-duid+bind+prefix) *prefix-address*
14. (Optional) Run the [**frame-ipv6 lease manage**](cmdqueryname=frame-ipv6+lease+manage) command to configure lease management for the RADIUS-delivered IPv6 addresses in an address pool which is supported by the device.
    
    ![](../../../../public_sys-resources/note_3.0-en-us.png) 
    
    To configure lease management for the RADIUS-delivered IPv6 addresses in an address pool which is not supported by the device, run the [**access frame-ipv6 lease manage pool-exclude**](cmdqueryname=access+frame-ipv6+lease+manage+pool-exclude) command in the system view.
15. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.