Configuring IGP GR Helper on the Backbone Network
=================================================

You can configure IGP GR Helper based on the specific IGP running on the backbone network.

#### Context

By default, a device running IS-IS supports the IS-IS GR Helper function. If IS-IS is running on a backbone network, you do not need to perform this configuration. If OSPF is running on a backbone network, perform the following operations to configure the OSPF GR Helper function.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**ospf**](cmdqueryname=ospf) [ *process-id* ]
   
   
   
   The OSPF view is displayed.
3. Run [**opaque-capability enable**](cmdqueryname=opaque-capability+enable)
   
   
   
   The opaque-LSA capability is enabled.
   
   
   
   The opaque-LSA capability of OSPF needs to be enabled first because OSPF supports GR through Type 9 LSAs.
4. Run [**graceful-restart**](cmdqueryname=graceful-restart) [ **helper-role** { { { { **ip-prefix** *ip-prefix-name* | **acl-number** *acl-number* | **acl-name** *acl-name* } | **ignore-external-lsa** | **planned-only** } \* } | **never** } ]
   
   
   
   GR Helper is enabled.
   
   
   
   You can use the **ignore-external-lsa** parameter to configure the GR Helper not to check AS-external LSAs.
   
   You can use the **planned-only** parameter to configure the GR Helper to support only planned GR.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) To specify **acl-number** *acl-number* or **acl-name** *acl-name*, perform the following steps in the system view:
   1. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   2. Run the [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ] command to enter the ACL view.
   3. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } [ **fragment-type** { **fragment** | **non-fragment** | **non-subseq** | **fragment-subseq** | **fragment-spe-first** } | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | **vpn-instance** *vpn-instance-name* ] \* command to configure ACL rules.
5. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.