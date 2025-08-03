snmp-agent group (System view)
==============================

snmp-agent group (System view)

Function
--------



The **snmp-agent group** command creates an SNMP user group by mapping SNMP users to the SNMP view.

The **undo snmp-agent group** command deletes a specified SNMP user group.



By default, the snmp-agent group v3 group-name command does not contain the authentication or privacy parameter.


Format
------

**snmp-agent group v3** *group-name* { **authentication** | **privacy** | **noauthentication** } [ **read-view** *read-view* | **write-view** *write-view* | **notify-view** *notify-view* ] \* [ **acl** { *acl-number* | *acl-name* } ]

**undo snmp-agent group v3** *group-name* { **authentication** | **privacy** | **noauthentication** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *group-name* | Specifies the name of an SNMP user group. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **authentication** | Authenticates packets without encrypting them. | - |
| **privacy** | Indicates that messages are authenticated and encrypted. | - |
| **noauthentication** | Indicates that no encryption or authentication is performed for an SNMP group to be configured. | - |
| **read-view** *read-view* | Specifies a read-only view. The view must have been created using the snmp-agent mib-view { excluded | included } view-name oid-tree command. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. read-view is specified using the snmp-agent mib-view command. The NMS can read a MIB node in the read-view. If read-view is not configured, the NMS will read the ViewDefault by default. You can run display snmp-agent mib-view to view the default view.  When quotation marks are used around the string, spaces are allowed in the string. |
| **write-view** *write-view* | Specifies the name of a read-write view.  The view has been created using the snmp-agent mib-view {excluded | included } view-name oid-tree command. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. write-view is specified by the snmp-agent mib-view command. The NMS can read and write MIB objects in the write view.  If spaces are used, the string must start and end with double quotation marks ("). |
| **notify-view** *notify-view* | Specifies a notify view. The view must have been created using the snmp-agent mib-view { excluded | included } view-name oid-tree command. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. notify-view is specified using the snmp-agent mib-view command. The MIB node information in the notify-view can be carried in alarms and sent to an NMS.  When quotation marks are used around the string, spaces are allowed in the string. |
| **acl** *acl-number* | Specifies the number of a basic ACL, which can be an ACL4 or ACL6 number. | The value is an integer ranging from 2000 to 2999. |
| **acl** *acl-name* | Specifies the name of a named basic ACL.  If no matching rule is configured for the referenced ACL, the matching rule is permit by default. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **v3** | Indicates that the SNMP user group uses the security mode in SNMPv3. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

SNMPv1 and SNMPv2c have serious security defects. The security authentication mechanism used by SNMPv1 and SNMPv2c is based on a community name. In this mechanism, the community name is transmitted in simple text, which is easy to be obtained. You are not advised to use SNMPv1 or SNMPv2c on untrusted networks.<br />
Using the user-based security model (USM), SNMPv3 eradicates security defects in SNMPv1 and SNMPv2c and provides authentication and encryption services. SNMPv3 defines the following three security levels:

* No authentication or encryption (noAuthNoPriv)
* AuthNoPriv: authentication and no encryption
* Authentication and encryptionNote:There is not any security level that defines encryption but no authentication. This is because the passwords used for encryption are associated with users, and the users must be authenticated.The **snmp-agent group** command can be used to configure the following information:
* Certification
* Encryption
* Controlling the access of users in an SNMP group
* Bind an SNMP group to a MIB view.To set the authentication level of an SNMP user group to authentication without encryption and set the view access permission to read-only, run the snmp-agent group v3 <group-name> authentication read-view <read-view> command.To set the authentication level of an SNMP user group to authentication with encryption and set the view access permission to read-write, run the snmp-agent group v3 <group-name> privacy write-view <write-view> command. You can set the authentication mode of SNMP users to Message-Digest Algorithm 5 (MD5) or Secure Hash Algorithm (SHA) and the privacy mode to Data Encryption Standard 56 (DES56), Triple Data Encryption Standard 168 (3DES168), Advanced Encryption Standard 128 (AES128), Advanced Encryption Standard 192 (AES192), or Advanced Encryption Standard 256 (AES256).Note:
* The NMS and the agent must be configured with the same authentication key and encryption password. Otherwise, authentication fails.
* To ensure high security, do not use the MD5 algorithm as the SNMPv3 authentication algorithm.
* To ensure high security, do not use the DES-56 or 3DES168 algorithm as the SNMPv3 encryption algorithm.

**Configuration Impact**



After you run the undo **snmp-agent group** command to delete an SNMP user group, information about all SNMP users in the SNMP user group is deleted.You can run the **snmp-agent usm-user** command to configure an authentication mode and an encrypted string for users in an SNMP user group only after the authentication and encryption functions are enabled for the SNMP user group.



**Follow-up Procedure**



After configuring the SNMP user group, run the **snmp-agent mib-view** command to create a MIB view and the access control for the view. You can run the **snmp-agent usm-user** command to add a user to SNMP user group and configure MIB-view-based access permission for the SNMP user. This is performed to ensure that SNMP users in an SNMP user group have the same security level and access control list.



**Precautions**

To enable the device to receive trap or Inform messages specified in <notify-view>, ensure that the following configurations are complete:

* A target host that receives SNMP trap messages is specified using the **snmp-agent target-host** command.
* A target host that receives SNMP Inform messages is specified using the **snmp-agent target-host inform** command.


Example
-------

# Create an SNMPv3 group named Johngroup and enable a device to authenticate SNMP messages without encrypting them.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent group v3 Johngroup authentication

```

# Create an SNMPv3 group named Johngroup and enable a device to authenticate and encrypt SNMP messages.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent group v3 Johngroup privacy

```

# Create an SNMPv3 user group named Johngroup, authenticate and encrypt SNMP messages, and set the view to publicView.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent mib-view included publicView 1.3.6.1.2.1
[*HUAWEI] snmp-agent group v3 Johngroup privacy read-view publicView

```

# Create an SNMPv3 user group named Johngroup, authenticate and encrypt SNMP messages, and set the write view to privateView.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent mib-view included privateView 1.3.6.1.4
[*HUAWEI] snmp-agent group v3 Johngroup privacy write-view privateView

```