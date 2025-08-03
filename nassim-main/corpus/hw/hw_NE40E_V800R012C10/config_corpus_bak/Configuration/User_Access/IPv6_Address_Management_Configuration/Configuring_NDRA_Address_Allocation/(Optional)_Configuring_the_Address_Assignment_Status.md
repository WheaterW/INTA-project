(Optional) Configuring the Address Assignment Status
====================================================

You can configure the address assignment status based on the address assignment mode and access mode.

#### Context

If the address assignment mode is NDRA or NDRA+IA\_PD, stateless address assignment (M=0) needs to be configured. By default, the M flag is 0 in the interface view and domain view, and no configuration is required.

If the M flag is 0 and the O flag is 1, clients obtain IPv6 addresses in stateless mode and other configuration information in stateful mode.


#### Procedure

1. Configure the address assignment status on an interface.
   * For IPoE users, configure the address assignment status in the interface view.
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**interface**](cmdqueryname=interface) *interface-type interface-number* [ *sub-interface* ]
        
        The interface view is displayed.
     3. Run [**ipv6 enable**](cmdqueryname=ipv6+enable)
        
        The IPv6 function is enabled for the interface.
     4. Run [**undo ipv6 nd autoconfig managed-address-flag**](cmdqueryname=undo+ipv6+nd+autoconfig+managed-address-flag)
        
        The interface is configured to use stateless autoconfiguration to obtain IPv6 addresses.
     5. Run [**ipv6 nd autoconfig other-flag**](cmdqueryname=ipv6+nd+autoconfig+other-flag)
        
        The interface is configured to use stateful autoconfiguration to obtain other configuration information.
     6. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
     7. (Optional) Configure a unicast destination address for RA messages.
        + Run the [**bas**](cmdqueryname=bas) command to enter the BAS interface view.
        + Run the [**ipv6 nd ra unicast**](cmdqueryname=ipv6+nd+ra+unicast) command to configure the Router to send RA messages that carry a unicast destination address in response to IPoEv6 user access requests.
        + Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
   * For PPPoE users, configure the address assignment status in the domain view.
     1. Run [**system-view**](cmdqueryname=system-view)
        
        The system view is displayed.
     2. Run [**aaa**](cmdqueryname=aaa)
        
        The AAA view is displayed.
     3. Run [**domain**](cmdqueryname=domain) *domain-name*
        
        A domain is created and the AAA domain view is displayed.
     4. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.
     5. Run [**undo ipv6 nd autoconfig managed-address-flag**](cmdqueryname=undo+ipv6+nd+autoconfig+managed-address-flag)
        
        The device is configured to assign IP addresses to PPPoX users in stateless mode.
     6. Run [**ipv6 nd autoconfig other-flag**](cmdqueryname=ipv6+nd+autoconfig+other-flag) { **ndra** | **dhcpv6** | [**dhcpv6-enhance**](cmdqueryname=dhcpv6-enhance) }
        
        The device is configured to assign other configuration information using NDRA or stateless DHCPv6 when IPv6 addresses are assigned in NDRA mode.
     7. (Optional) Run [**prefix-assign-mode unshared**](cmdqueryname=prefix-assign-mode+unshared)
        
        The IPv6 prefix assignment mode is set to unshared. That is, IPv6 users do not share the same IP prefix.
     8. (Optional) Run [**dhcpv6-follow-ipv6cp wait-delay**](cmdqueryname=dhcpv6-follow-ipv6cp+wait-delay) { *time-value* | **infinity** }
        
        The timeout period for waiting for a DHCPv6 connection request from a PPPoE user is configured.
     9. Run [**commit**](cmdqueryname=commit)
        
        The configuration is committed.