(Optional) Controlling the NMS's Access to the Device
=====================================================

This section describes how to specify an NMS and manageable MIB objects for SNMPv3-based communication between the NMS and managed device to improve communication security.

#### Context

If a device is managed by multiple NMSs that are in the same SNMPv3 user group, note the following points:

* If all the NMSs need to have permission to access the objects in the Viewdefault view, skip the following steps.
* If some of the NMSs need to have permission to access the objects in the Viewdefault view, skip 8 and 10.
* If all the NMSs are required to manage specified objects on the device, skip 2, 4, 6, and 7.
* If some of the NMSs are required to manage specified objects on the device, perform all the following steps.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**acl**](cmdqueryname=acl) { **name** *basic-acl-name* { **basic** | [ **basic** ] **number** *basic-acl-number* } | [ **number** ] *basic-acl-number* } [ **match-order** { **config** | **auto** } ] command to create a basic ACL to filter NMS users that manage the device.
   
   ![](../../../../public_sys-resources/note_3.0-en-us.png) 
   
   SNMP supports only basic ACLs whose numbers range from 2000 to 2999.
3. Run the [**rule**](cmdqueryname=rule) [ *rule-id* ] [ **name** *rule-name* ] { **permit** | **deny** } [ [ **fragment-type** { **fragment** | **fragment-subseq** | **non-fragment** | **non-subseq** | **fragment-spe-first** } ] | **source** { *source-ip-address* { *source-wildcard* | **0** | *src-netmask* } | **any** } | **time-range** *time-name* | [ **vpn-instance** *vpn-instance-name* | **vpn-instance-any** ] ] \* command to configure a basic ACL rule.
   
   
   * If the address of a login user matches an ACL rule in which the specified action is **permit**, the user is allowed to log in to the device.
   * If the address of a login user matches an ACL rule in which the specified action is **deny**, the user is not allowed to log in to the device.
   * If the address of a login user is not within the address range specified in the configured ACL rule, the user is not allowed to log in to the device.
   * If the referenced ACL does not contain any rules or does not exist, the login of users is not subject to the ACL, and any users can log in to the device.
4. Run the **commit** command to commit the configuration.
5. Run the [**quit**](cmdqueryname=quit) command to return to the system view.
6. Run the [**snmp-agent mib-view**](cmdqueryname=snmp-agent+mib-view) *type* *view-name* *oid-tree* command to create a MIB view and specify manageable MIB objects.
   
   
   * **excluded**: If a few MIB objects on the device or some objects in the current MIB view do not or no longer need to be managed by the NMS, configure **excluded** in the command to exclude these MIB objects.
   * **included**: If a few MIB objects on the device or some objects in the current MIB view need to be managed by the NMS, configure **included** in the command to include these MIB objects.
7. (Optional) Run the [**snmp-agent acl**](cmdqueryname=snmp-agent+acl) { *acl-number* | *aclName* } command to configure an ACL for SNMP.
8. Run the [**snmp-agent group**](cmdqueryname=snmp-agent+group) **v3** *group-name* { **authentication** | **privacy** | **noauthentication** } [ **read-view** *read-view* | **write-view** *write-view* | **notify-view** *notify-view* ] \* [ **acl** { *acl-number* | *acl-name* } ] command to configure an SNMPv3 user group.
   
   
   
   If the NMS and network devices are in an insecure environment (for example, the network is vulnerable to attacks), **authentication** or **privacy** can be configured in the command to enable data authentication or privacy.
   
   The available authentication and privacy modes are as follows:
   * No authentication and no privacy: Neither **authentication** nor **privacy** or **noauthentication** is configured in the command.
   * Authentication without privacy: Only **authentication** is configured in the command. In this mode, only the authenticated administrators can access the managed device.
   * Authentication and privacy: Both **authentication** and **privacy** are configured in the command. In this mode, only the authenticated administrators can access the managed device, and transmitted data is encrypted to guard against tampering and data leaking.
   
   **read-view** needs to be configured in the command if the NMS administrator needs the read permission in a specified view. For example, a low-level administrator needs to read certain data.
   
   **write-view** needs to be configured in the command if the NMS administrator needs the read and write permissions in a specified view. For example, a high-level administrator needs to read and write certain data.
   
   **notify-view** needs to be configured in the command if you want to filter out irrelevant alarms and configure the managed device to send only the alarms of specified MIB objects to the NMS. If the parameter is configured, only the alarms of the MIB objects specified by **notify-view** are sent to the NMS.
9. Run the **commit** command to commit the configuration.

#### Follow-up Procedure

After the access permission is configured, especially after the IP address of the NMS is specified, if the IP address changes (for example, the NMS changes its location, or IP addresses are reallocated due to network adjustment), you need to change the IP address of the NMS in the ACL. Otherwise, the NMS cannot access the device.