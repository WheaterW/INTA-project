Configuring the OSPFv3 GR Helper
================================

To avoid traffic interruption and route flapping caused by the active/standby switchover, you can enable OSPFv3 GR.

#### Context

GR ensures normal traffic forwarding and non-stop forwarding of key services during the restart of routing protocols. GR is one of high availability (HA) technologies. HA technologies comprise a set of comprehensive techniques, such as fault-tolerant redundancy, link protection, faulty node recovery, and traffic engineering. As a fault-tolerant redundancy technology, GR is widely used to ensure non-stop forwarding of key services during master/slave main control board switchover and system upgrade.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

The NE40E supports only the GR Helper.



#### Pre-configuration Tasks

Before configuring OSPFv3 GR, complete the following tasks:

* Configure a link layer protocol.
* Configure IP addresses for interfaces to ensure that neighboring nodes are reachable at the network layer.
* [Configure basic OSPFv3 functions](dc_vrp_ospfv3_cfg_2003.html).

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospfv3**](cmdqueryname=ospfv3) *process-id*
   
   
   
   The OSPFv3 view is displayed.
3. Configure a basic ACL:
   
   
   1. Run [**helper-role**](cmdqueryname=helper-role) [ { **ip-prefix** *ip-prefix-name* | **acl-number** *acl-number* | **acl-name** *acl-name* } | **max-grace-period** *period* | **planned-only** | **lsa-checking-ignore** ] \*
      
      OSPFv3 GR is enabled.
   2. Run [**quit**](cmdqueryname=quit)
      
      Return to the system view.
   3. Run [**acl ipv6**](cmdqueryname=acl+ipv6) { **name** *basic-acl6-name* **basic** | [ **number** ] *basic-acl6-number* } [ **match-order** { **config** | **auto** } ]
      
      The ACL view is displayed.
   4. Run [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *source-ipv6-address*/*prefix-length* | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \*
      
      A rule is configured for the ACL.
      
      When the [**rule**](cmdqueryname=rule) command is used to configure a filtering rule for a named ACL, only the configurations specified by **source** and **time-range** take effect.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

Run the following command to check the preceding configuration:

* Run the [**display ospfv3**](cmdqueryname=display+ospfv3) [ *process-id* ] **graceful-restart-information** command to view the OSPFv3 GR Helper status.