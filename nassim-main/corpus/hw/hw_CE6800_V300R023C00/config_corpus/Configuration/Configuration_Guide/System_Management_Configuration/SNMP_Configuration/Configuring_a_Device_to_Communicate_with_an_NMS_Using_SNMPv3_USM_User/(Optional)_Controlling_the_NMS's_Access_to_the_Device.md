(Optional) Controlling the NMS's Access to the Device
=====================================================

(Optional) Controlling the NMS's Access to the Device

#### Context

This section describes how to specify an NMS and manageable MIB objects for SNMPv3-based communication between the NMS and managed device to improve communication security.

If a device is managed by multiple NMSs that are in the same SNMPv3 user group, note the following points:

* If all the NMSs are required to access the objects in the ViewDefault view, skip the following steps.
* If some of the NMSs are required to access the objects in the ViewDefault view, skip steps [7](#EN-US_TASK_0000001512830850__en-us_task_0275866366_step377246470) and [8](#EN-US_TASK_0000001512830850__step_dc_vrp_snmp_cfg_001706).
* If all the NMSs are required to manage specified objects on the device, skip steps [2](#EN-US_TASK_0000001512830850__step951225411811), [3](#EN-US_TASK_0000001512830850__step6515162616910), and [4](#EN-US_TASK_0000001512830850__step_dc_vrp_snmp_cfg_001704).
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
8. Configure an SNMP user group.
   
   
   ```
   [snmp-agent group](cmdqueryname=snmp-agent+group) v3 group-name { authentication | privacy | noauthentication } [ read-view read-view | write-view write-view | notify-view notify-view ] * [ acl { acl-number | acl-name } ]
   ```
   
   If the NMS and network devices are in an insecure environment (for example, the network is vulnerable to attacks), **authentication** or **privacy** can be configured in the command to enable data authentication or privacy.
   
   The available authentication and privacy modes are as follows:
   * No authentication and no privacy: Neither **authentication** nor **privacy** or **noauthentication** is configured in the command. This mode is applicable to secure networks managed by a specified administrator.
   * Authentication without privacy: Only **authentication** is configured in the command. This mode is applicable to secure networks managed by many administrators who may frequently perform operations on the same device. In this mode, only the authenticated administrators can access the managed device.
   * Authentication and privacy: Both **authentication** and **privacy** are configured in the command. This mode is applicable to insecure networks managed by many administrators who may frequently perform operations on the same device. In this mode, only the authenticated administrators can access the managed device, and transmitted data is encrypted to guard against tampering and data leaking.
   
   If the NMS administrator needs the read permission in a specified view, configure **read-view** in this command. For example, a low-level administrator needs to read certain data.
   
   If the NMS administrator needs the read and write permissions in a specified view, configure **write-view** in this command. For example, a high-level administrator needs to read and write certain data.
   
   **notify-view** needs to be configured in the command if you want to filter out irrelevant alarms and configure the managed device to send only the alarms of specified MIB objects to the NMS. If the parameter is configured, only the alarms of the MIB objects specified by **notify-view** are sent to the NMS.
9. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```