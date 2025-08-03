Disabling the IP Address Conflict Detection Function and Configuring the Preemption Function
============================================================================================

This section describes how to configure conflicting IP addresses for different interfaces after the IP address conflict detection function is disabled as well as to configure the preemption function so that conflicting IP addresses take effect on the interfaces with higher priorities.

#### Usage Scenario

In scenarios of upgrade and capacity expansion on the live network, existing interfaces need to be replaced. If a customer has limited IP address resources and therefore is unwilling to assign new IP addresses for replacement interfaces, disable the IP address conflict detection function so that conflicting IP addresses can be configured on different interfaces. Configure IP addresses of the to-be-replaced interfaces for new interfaces. The IP addresses take effect on the new interfaces after the to-be-replaced interfaces are shut down or their IP addresses are deleted.

If the IP address or broadcast address of an interface is the same as that of another interface, IP address conflict occurs. After the IP address conflict detection function is disabled and the preemption function for conflicting IP addresses is enabled, conflicting IP addresses take effect on the interfaces with higher priorities.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ip address conflict check disable**](cmdqueryname=ip+address+conflict+check+disable)
   
   
   
   The IP address conflict detection function is disabled.
3. Run [**ip address conflict preempt enable**](cmdqueryname=ip+address+conflict+preempt+enable)
   
   
   
   The preemption function for conflicting IP addresses is enabled.
   
   
   
   After the preemption function for conflicting IP addresses is enabled, IP addresses take effect on the interfaces with higher priorities in IP address conflict scenarios.
   
   If the primary IP address of an interface does not take effect due to IP address conflict, its secondary IP address also becomes invalid. If the primary IP address of an interface takes effect, its secondary IP address takes effect only when no duplicate IP address exists on the network.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.