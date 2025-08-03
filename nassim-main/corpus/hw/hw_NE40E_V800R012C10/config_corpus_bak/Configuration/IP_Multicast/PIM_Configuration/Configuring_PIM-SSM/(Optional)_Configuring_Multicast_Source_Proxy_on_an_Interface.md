(Optional) Configuring Multicast Source Proxy on an Interface
=============================================================

(Optional)_Configuring_Multicast_Source_Proxy_on_an_Interface

#### Context

When an interface of a device receives multicast data from an indirectly connected upstream multicast source and the RP corresponding to the multicast group is not the device, the multicast data cannot be forwarded. To enable downstream hosts to receive the data in such a case, deploy multicast source proxy, which enables the egress to send a Register message to the RP in the PIM domain. The data is then forwarded along an RPT.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**acl**](cmdqueryname=acl) { **name** *advance-acl-name* [ **advance** | [ **advance** ] **number** *advance-acl-number* ] | [ **number** ] *advance-acl-number* } [ **match-order** { **config** | **auto** } ] command to create an advanced ACL and enter the corresponding ACL view.
3. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **deny** | **permit** } **ip** [ **destination** { *destination-ip-address* { *destination-wildcard* | **0** } | **any** } | **source** { *source-ip-address* { *source-wildcard* | **0** } | **any** } ] \* command to configure a rule for the advanced ACL.
   
   
   
   In the [**rule**](cmdqueryname=rule) command, the **source** parameter is used to specify a multicast source address, and the **destination** parameter is used to specify a multicast group address.
4. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
5. Run the [**interface**](cmdqueryname=interface) *interface-type* *interface-number* command to enter the interface view.
6. Run the [**pim source-proxy enable**](cmdqueryname=pim+source-proxy+enable) [ **policy** { *advanced-acl-number* | **acl-name** *acl-name* } ] command to configure multicast source proxy.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   * If no ACL is configured, multicast source proxy is enabled for all multicast entries.
   * If an ACL is configured, the device filters multicast entries based on rules of the ACL and enables multicast source proxy accordingly.
     + If a multicast entry matches a rule of the ACL and the action is **permit**, multicast source proxy is enabled for the multicast entry.
     + If a multicast entry matches a rule of the ACL and the action is **deny**, multicast source proxy is not enabled for the multicast entry.
     + If a multicast entry does not match any rule of the ACL, multicast source proxy is not enabled for the multicast entry.
7. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.