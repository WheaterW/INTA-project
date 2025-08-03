Disabling the IPv6 Address Conflict Detection Function and Configuring the Preemption Function
==============================================================================================

This section describes how to configure conflicting IPv6 addresses for different interfaces after the IPv6 address conflict detection function is disabled as well as to configure the preemption function so that conflicting IPv6 addresses take effect on interfaces with higher priorities.

#### Context

In scenarios of upgrade and capacity expansion on the live network, existing interfaces need to be replaced. If a customer has limited IPv6 address resources and therefore is unwilling to assign new IPv6 addresses for replacement interfaces, disable the IPv6 address conflict detection function so that conflicting IPv6 addresses can be configured on different interfaces. Configure IPv6 addresses of the to-be-replaced interfaces for new interfaces. The IP addresses take effect on the new interfaces after the to-be-replaced interfaces are shut down or their IPv6 addresses are deleted.

If the IPv6 address or broadcast address of an interface is the same as that of another interface, IPv6 address conflict occurs. After the IPv6 address conflict detection function is disabled and the preemption function for conflicting IP addresses is enabled, conflicting IPv6 addresses take effect on interfaces with higher priorities.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ipv6 address conflict check disable**](cmdqueryname=ipv6+address+conflict+check+disable)
   
   
   
   The IPv6 address conflict detection is disabled.
3. Run [**ipv6 address conflict preempt enable**](cmdqueryname=ipv6+address+conflict+preempt+enable)
   
   
   
   The preemption function for conflicting IPv6 addresses is enabled.
   
   
   
   After the preemption function for conflicting IPv6 addresses is enabled, IPv6 addresses take effect on interfaces with higher priorities in IPv6 address conflict scenarios.
   
   If the primary IPv6 address of an interface does not take effect due to IPv6 address conflict, its secondary IPv6 address also becomes invalid. If the primary IPv6 address of an interface takes effect, its secondary IP address takes effect only when no duplicate IPv6 address exists on the network.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.