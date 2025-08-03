(Optional) Configuring the RADIUS Server to Dynamically Deliver ACLs
====================================================================

(Optional) Configuring the RADIUS Server to Dynamically Deliver ACLs

#### Context

The RADIUS server can dynamically deliver ACLs based on the HW-Data-Filter attribute. The RADIUS server delivers a traffic classifier-behavior (C-B) pair through the HW-Data-Filter attribute (No. 26-82). The traffic classifier attribute carries the classifier name, behavior name, and rule information, whereas the traffic behavior attribute carries the behavior name and behavior information. In this way, ACL information is dynamically delivered. The HW-Data-Filter attribute is disabled by default and can be used only after being enabled using a command.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. (Optional) Run [**remote-download user-group enable**](cmdqueryname=remote-download+user-group+enable)
   
   
   
   The RADIUS server is configured to create dynamic user groups.
4. (Optional) Run [**remote-download user-group check interval**](cmdqueryname=remote-download+user-group+check+interval) *interval*
   
   
   
   The interval at which the device checks whether dynamic user groups created by the RADIUS server are used by online users or dynamic ACLs is configured.
   
   
   
   The device checks one dynamic user group at each interval. If the user group is not used, the device deletes the user group.
5. Run [**remote-download acl enable**](cmdqueryname=remote-download+acl+enable)
   
   
   
   The RADIUS server is configured to create dynamic ACLs. It can deliver C-B pairs for dynamic ACLs through the HW-Data-Filter attribute.
6. (Optional) Run [**remote-download acl warning-threshold**](cmdqueryname=remote-download+acl+warning-threshold) *warning-threshold*
   
   
   
   The alarm threshold for the usage of C-B pairs dynamically delivered by the RADIUS server is configured.
7. (Optional) Run [**recycle remote-download acl classifier**](cmdqueryname=recycle+remote-download+acl+classifier) { *name* | ****classifier-id*****classifier-id* }
   
   
   
   The device is configured to reclaim C-B pairs of dynamic ACLs that are not in use on the device.
8. (Optional) Configure the device to ignore a RADIUS attribute if the device fails to parse this attribute.
   
   
   1. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
   2. Run the [**radius-server group**](cmdqueryname=radius-server+group) *groupname* command to enter the RADIUS server group view.
   3. (Optional) Run the [**radius-attribute decode-error-policy ignore hw-data-filter**](cmdqueryname=radius-attribute+decode-error-policy+ignore+hw-data-filter) command to configure the device to ignore a RADIUS attribute if the device fails to parse this attribute.
      
      Currently, only the HW-Data-Filter attribute is supported.
9. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.