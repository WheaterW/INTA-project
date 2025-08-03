(Optional) Controlling the NMS's Access to the Device
=====================================================

(Optional) Controlling the NMS's Access to the Device

#### Context

To enhance SNMP communication security, restrict the NMSs that are allowed to access the device and restrict the MIB objects to be managed.

If a device is managed by multiple NMSs that use the same community name, note the following points:

* If all the NMSs are required to access the objects in the ViewDefault view (1.3.6.1), skip the following steps.
* If some of the NMSs are required to access the objects in the ViewDefault view (1.3.6.1), skip steps [7](#EN-US_TASK_0000001563990617__step377246470) and [8](#EN-US_TASK_0000001563990617__step7471162894818).
* If all the NMSs are required to manage specified objects on the device, skip steps [2](#EN-US_TASK_0000001563990617__step115233263716), [3](#EN-US_TASK_0000001563990617__step10996144834214), and [4](#EN-US_TASK_0000001563990617__step10176563447).
* If some of the NMSs are required to manage specified objects on the device, perform all the following steps.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Create a basic ACL to filter network administrators.
   
   
   ```
   [acl](cmdqueryname=acl+name+%28basic+ACL%29) { name basic-acl-name { basic | [ number ] basic-acl-number } | [ number ] basic-acl-number }
   ```
   
   After the access permissions are configured and the NMS's IP address is specified in the ACL rule, if the IP address changes (for example, the network management station changes its location, or IP addresses are re-allocated due to network adjustment), you need to change the IP address in the ACL. Otherwise, the NMS cannot access the device.
3. Configure a basic ACL rule.
   
   
   ```
   [rule](cmdqueryname=rule+%28basic+ACL+view%29) [ rule-id ] [ name rule-name ] { permit | deny }
   ```
   
   
   * If the address of a login user matches an ACL rule in which the specified action is **permit**, the user is allowed to log in to the device.
   * If the address of a login user matches an ACL rule in which the specified action is **deny**, the user is not allowed to log in to the device.
   * If the address of a login user is not within the address range specified in the configured ACL rule, the user is not allowed to log in to the device.
   * If the referenced ACL does not contain any rules or does not exist, the login of users is not subject to the ACL, and any users can log in to the device.
4. Return to the system view.
   
   
   ```
   [quit](cmdqueryname=quit)
   ```
5. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```
6. (Optional) Configure an ACL for SNMP.
   
   
   ```
   [snmp-agent acl](cmdqueryname=snmp-agent+acl) { acl-number | aclName }
   ```
7. Create a MIB view and specify the MIB objects that can be monitored and managed by the NMS.
   
   
   ```
   [snmp-agent mib-view](cmdqueryname=snmp-agent+mib-view) type view-name oid-tree
   ```
   
   By default, the NMS has the permission to access the ViewDefault view (1.3.6.1).
   
   The value of *type* can be **included** or **excluded**. The **included** parameter specifies the MIB objects that the NMS needs to manage. If some MIB objects do not need to be managed, you can specify the **excluded** parameter to exclude them.
8. Control the NMS's access to the device.
   
   
   ```
   [snmp-agent community](cmdqueryname=snmp-agent+community) { read | write } { community-name | cipher host-string } [ mib-view security-string-cipher | acl { acl-number | acl-name } | alias alias-name ]
   ```
   * **read**: If the NMS administrator needs the read permission in a specified view, configure **read** in this command. For example, a low-level administrator needs to read certain data.
   * **write**: If the NMS administrator needs the read and write permissions in a specified view, configure **write** in this command. For example, a high-level administrator needs to read and write certain data.
   * **mib-view**: If some of the NMSs that use the community name need to have permission to access the objects in the ViewDefault view (1.3.6.1), you do not need to configure **mib-view** *view-name* in the command.
   * **acl**: If all the NMSs that use the community name need to manage specified objects on the device, you do not need to configure **acl** *acl-number* in the command.
   * If some of the NMSs that use the community name need to manage specified objects on the device, configure both **mib-view** and **acl** in the command.
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```