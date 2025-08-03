Configuring RIP GTSM
====================

To apply RIP GTSM, you need to enable GTSM on both ends of the corresponding RIP connection.

#### Context

On a RIP network requiring high security, you can configure GTSM to improve the security of the network. GTSM checks TTL values to defend against attacks. Attackers may simulate RIP messages and continuously send them to a device. After receiving these messages, an interface board on the device sends them directly to the control plane for RIP processing, without validating them, if they are destined for the device. Consequently, the device becomes extremely busy, and CPU usage is high because the control plane needs to process these unverified messages. GTSM protects the device by checking whether the TTL value in the IP header is within a predefined range, thereby improving system security.


#### Pre-configuration Tasks

Before configuring RIP GTSM, complete the following task:

* [Configure basic RIP functions](dc_vrp_rip_cfg_0003.html).

Perform the following steps on both ends of the RIP connection for which GTSM is to be enabled:


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**rip valid-ttl-hops**](cmdqueryname=rip+valid-ttl-hops) *valid-ttl-hops-value* [ **vpn-instance** *vpn-instance-name* ] command to configure RIP GTSM.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   The valid TTL range of checked messages is [255 â *valid-ttl-hops-value* + 1, 255].
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
4. Set a default action for the messages that do not match the specified GTSM policy.
   
   
   
   GTSM checks the TTL values of only the messages that match the specified GTSM policy. For messages that do not match the policy, you can set the default action taken on them as either pass or drop.
   
   To facilitate fault locating, you can enable the device to log information about dropped messages.
   
   Perform the following steps on a GTSM-enabled Router:
   
   
   
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**gtsm default-action**](cmdqueryname=gtsm+default-action) { **drop** | **pass** } command to set a default action for the messages that do not match the GTSM policy.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      
      If the default action is configured but no GTSM policy is configured, GTSM does not take effect.
      
      This command is supported only on the Admin-VS and cannot be configured in other VSs. This command takes effect on all VSs.
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.

#### Verifying the Configuration

After the configuration is complete, verify the configuration.

* Run the [**display gtsm statistics**](cmdqueryname=display+gtsm+statistics) { *slot-id* | **all** } command to check GTSM statistics.
  
  ![](../../../../public_sys-resources/note_3.0-en-us.png) 
  
  In VS mode, this command is supported only by the admin VS.