Configuring OSPF GTSM
=====================

To apply OSPF GTSM, you need to enable GTSM on the two ends of the corresponding OSPF connection.

#### Usage Scenario

GTSM checks TTL values to defend against attacks. Attackers may simulate OSPF unicast packets and continuously send them to a Router. Upon reception of the packets, an interface board on the Router sends them directly to the control plane for OSPF processing, without validating them, if they are destined for the device. Consequently, the Router becomes extremely busy, and CPU usage is high because the control plane needs to process these unverified packets.

GTSM protects the Router by checking whether the TTL value in the IP header is within a predefined range, thereby improving system security.


#### Pre-configuration Tasks

Before configuring OSPF GTSM, complete the following task:

* [Configure basic OSPF functions](dc_vrp_ospf_cfg_0003.html).

#### Procedure

1. Configure basic OSPF GTSM functions.
   
   
   
   To apply OSPF GTSM, you need to enable GTSM on the two ends of the corresponding OSPF connection.
   
   Therefore, perform the following steps on the Routers on the two ends of the virtual or sham link for which GTSM is to be enabled:
   
   
   
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**ospf valid-ttl-hops**](cmdqueryname=ospf+valid-ttl-hops) *ttl* [ **nonstandard-multicast** ] [ **vpn-instance** *vpn-instance-name* ] command to enable OSPF GTSM.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      * The [**ospf valid-ttl-hops**](cmdqueryname=ospf+valid-ttl-hops) command enables OSPF GTSM and configures a TTL value. The **vpn-instance** parameter takes effect only for the latter function.
      * The valid TTL range of checked packets is [255 â *hops* + 1, 255].
   3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.
2. Set a default action for the packets that do not match the specified GTSM policy.
   
   
   
   GTSM checks the TTL values of only the packets that match the specified GTSM policy. For packets that do not match the policy, you can set the default action taken on them as either pass or drop.
   
   To facilitate fault locating, you can enable the device to log information about dropped packets.
   
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