Configuring OSPF GR Helper
==========================

To avoid traffic interruption and route flapping caused by the active/standby switchover, you can enable OSPF GR.

#### Usage Scenario

Graceful Restart (GR) is a technology that ensures normal data forwarding without affecting key services when a routing protocol restarts. GR is one of high availability (HA) technologies. HA technologies comprise a set of comprehensive techniques, such as fault-tolerant redundancy, link protection, faulty node recovery, and traffic engineering. As a fault-tolerant redundancy technology, GR is widely used to ensure non-stop forwarding of key data during the active/standby switchover and system upgrade.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

GR involves two roles: the GR restarter and GR helper. The NE40E supports the GR helper only.



#### Pre-configuration Tasks

Before configuring OSPF GR, complete the following tasks:

* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic OSPF functions](dc_vrp_ospf_cfg_0003.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
3. Run [**opaque-capability enable**](cmdqueryname=opaque-capability+enable)
   
   
   
   The Opaque-LSA capability is enabled.
   
   OSPF supports OSPF GR through Type 9 LSAs. Therefore, before configuring GR, run the [**opaque-capability enable**](cmdqueryname=opaque-capability+enable) command to enable the Opaque-LSA capability.
4. Configure GR session parameters on the helper.
   1. Run [**graceful-restart**](cmdqueryname=graceful-restart) **helper-role** **ignore-external-lsa**
      
      
      
      The helper is configured to ignore AS-external LSAs.
   2. Run [**graceful-restart**](cmdqueryname=graceful-restart) **helper-role** **planned-only**
      
      
      
      The helper is configured to support only planned GR.
   3. Choose either of the following configuration as required:
      
      
      * Based on a basic ACL:
        1. Run [**graceful-restart**](cmdqueryname=graceful-restart) [ **helper-role** { { **acl-number** *acl-number* | **acl-name** *acl-name* } | **never** } ]
           
           GR session parameters on the helper are configured.
        2. Run [**quit**](cmdqueryname=quit)
           
           The system view is displayed.
        3. Run [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ]
           
           The ACL view is displayed.
        4. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \*
           
           An ACL rule is configured.
           
           When the [**rule**](cmdqueryname=rule) command is used to configure a filtering rule for a named ACL, only the configurations specified by **source** and **time-range** take effect.
      * Configure an IP prefix list.
        
        Run [**graceful-restart**](cmdqueryname=graceful-restart) [ **helper-role** { { **ip-prefix** *ip-prefix-name* \* } | **never** } ]
        
        GR session parameters on the helper are configured.
5. Configure GR session parameters on the helper.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   IETF mode and non-IETF mode are mutually exclusive.
   
   
   * Configure GR session parameters on the helper in IETF mode.
     1. Run [**graceful-restart**](cmdqueryname=graceful-restart) **helper-role** **ignore-external-lsa**
        
        The helper does not check AS external LSAs.
     2. Run [**graceful-restart**](cmdqueryname=graceful-restart) **helper-role** **planned-only**
        
        The helper is configured to support only planned GR.
     3. Choose either of the following configuration as required:
        
        + Based on a basic ACL:
          1. Run [**graceful-restart**](cmdqueryname=graceful-restart) [ **helper-role** { { **acl-number** *acl-number* | **acl-name** *acl-name* } | **never** } ]
             
             GR session parameters on the helper are configured.
          2. Run [**quit**](cmdqueryname=quit)
             
             The system view is displayed.
          3. Run [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ]
             
             The ACL view is displayed.
          4. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \*
             
             The rule for the ACL is configured.
             
             When the [**rule**](cmdqueryname=rule) command is run to configure rules for a named ACL, only the source address range specified by **source** and the time period specified by **time-range** are valid as the rules.
        + Configure an IP prefix list.
          
          Run [**graceful-restart**](cmdqueryname=graceful-restart) [ **helper-role** { { **ip-prefix** *ip-prefix-name* } | **never** } ]
          
          GR session parameters on the helper are configured.
   * Enable the non-IETF mode.
     
     Run [**graceful-restart**](cmdqueryname=graceful-restart) **non-ietf**
     
     GR Helper in non-IETF mode is enabled.
6. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the [**display ospf graceful-restart**](cmdqueryname=display+ospf+graceful-restart) command, and you can view the configurations about OSPF GR.