Configuring GR Helper of the Routing Protocol Between PEs and CEs
=================================================================

You can configure GR Helper of a routing protocol according to the specific routing protocol running between the CE and the PE.

#### Context

The precautions for configuring GR Helper of different protocols are as follows:

* The procedure for configuring the BGP GR Helper function on the PE or CE is the same as that for configuring a common BGP GR Helper function.
* By default, a device running IS-IS supports the IS-IS GR Helper function. If IS-IS is running between the PE and CE, you do not need to configure the IS-IS GR Helper function.
* The procedure for configuring the OSPF GR Helper function on the CE is the same as that for configuring a common OSPF GR Helper function. For details, see [Configuring IGP GR Helper on the Backbone Network](dc_vrp_mpls-l3vpn-v6_cfg_2075.html). The following describes how to configure the OSPF GR Helper function on the PE.


#### Procedure

* Configure the BGP GR Helper.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**bgp**](cmdqueryname=bgp) *as-number*
     
     
     
     The BGP view is displayed.
  3. Run [**graceful-restart**](cmdqueryname=graceful-restart)
     
     
     
     BGP GR is enabled.
  4. Run [**graceful-restart timer wait-for-rib**](cmdqueryname=graceful-restart+timer+wait-for-rib) *time*
     
     
     
     The period during which the restarting speaker and receiving speaker wait for End-Of-RIB messages is set.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) 
     
     You can adjust parameter values of a BGP GR session as required. Generally, the default values of parameters are recommended.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* Configure the OSPFv3 GR Helper function on the PE.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**ospfv3**](cmdqueryname=ospfv3) *process-id* **vpn-instance** *vpnname*
     
     
     
     The OSPFv3 multi-instance view is displayed.
  3. Run [**helper-role**](cmdqueryname=helper-role) [ { [**ip-prefix**](cmdqueryname=ip-prefix) *ip-prefix-name* | **acl-number** *acl-number* | **acl-name** *acl-name* } | **max-grace-period** *period* | **planned-only** | **lsa-checking-ignore** ] \*
     
     
     
     OSPFv3 GR Helper is enabled.
     
     
     
     ![](../../../../public_sys-resources/note_3.0-en-us.png) To specify **acl-number** *acl-number* or **acl-name** *acl-name*, perform the following steps in the system view:
     + Run the [**quit**](cmdqueryname=quit) command to return to the system view.
     + Run the [**acl ipv6**](cmdqueryname=acl+ipv6) { **name** *basic-acl6-name* **basic** | [ **number** ] *basic-acl6-number* } [ **match-order** { **config** | **auto** } ] command to enter the ACL view.
     + Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment** | **source** { *source-ipv6-address* { *prefix-length* | *source-wildcard* } | *source-ipv6-address*/*prefix-length* | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \* command to configure ACL rules.
  4. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.