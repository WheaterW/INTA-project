Configuring OSPFv3 GTSM
=======================

To apply OSPFv3 GTSM, you need to enable GTSM on the two ends of the corresponding OSPFv3 connection.

#### Pre-configuration Tasks

Before configuring OSPFv3 GTSM, complete the following task:

* [Configure basic OSPFv3 functions](dc_vrp_ospfv3_cfg_2003.html).


#### Procedure

1. Configure basic OSPFv3 GTSM functions.
   
   
   
   To apply OSPFv3 GTSM, you need to enable GTSM on the two ends of the corresponding OSPFv3 connection.
   
   
   
   1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
   2. Run the [**ospfv3 valid-ttl-hops**](cmdqueryname=ospfv3+valid-ttl-hops) *ttl* [ **vpn-instance** *vpn-instance-name* ] command to enable OSPFv3 GTSM.
      
      ![](../../../../public_sys-resources/note_3.0-en-us.png) 
      * The [**ospfv3 valid-ttl-hops**](cmdqueryname=ospfv3+valid-ttl-hops) command enables OSPFv3 GTSM and configures a TTL value. The **vpn-instance** parameter takes effect only for the latter function.
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