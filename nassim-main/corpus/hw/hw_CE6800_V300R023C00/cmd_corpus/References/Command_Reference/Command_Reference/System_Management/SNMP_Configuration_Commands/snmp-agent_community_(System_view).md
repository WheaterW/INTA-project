snmp-agent community (System view)
==================================

snmp-agent community (System view)

Function
--------



The **snmp-agent community** command configures an SNMPv1 or SNMPv2c read/write community name (either in ciphertext or simple text) and specifies a MIB view and an ACL.

The **undo snmp-agent community** command deletes the community name configuration.



By default, no community name is configured.


Format
------

**snmp-agent community** { **read** | **write** } *community-name* [ **mib-view** *security-string-cipher* | **acl** { *acl-number* | *acl-name* } | **alias** *alias-name* ] \*

**snmp-agent community** { **read** | **write** } **cipher** *host-string* [ **mib-view** *security-string-cipher* | **acl** { *acl-number* | *acl-name* } | **alias** *alias-name* ] \*

**undo snmp-agent community** { **read** | **write** } *community-name*

**undo snmp-agent community** { **read** | **write** } **cipher** *host-string*

**undo snmp-agent community** *host-string*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **read** | Indicates that a community with a specified name has read-only permission in the specified view. | - |
| **write** | Indicates that a community with a specified name has read-write permission in the specified view. | - |
| *community-name* | Specifies the name of a community. | * If community name complexity check is enabled, the value is a string of 8 to 32 case-sensitive characters, spaces not supported. * If the complexity check of a community name is disabled, the value is a string of 1 to 32 case-sensitive characters, spaces not supported.   If spaces are used, the string must start and end with double quotation marks ("). |
| **mib-view** *security-string-cipher* | Specifies a MIB view that a community with the specified name can access. The view must have been created using the snmp-agent mib-view { excluded | included } view-name oid-tree command. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |
| **acl** *acl-name* | Specifies the name of a named basic ACL.  If no matching rule is configured for the referenced ACL, the matching rule is permit by default. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported. |
| **acl** *acl-number* | Specifies the number of an access control list (ACL) mapped to a community with a specified name. | The value is an integer ranging from 2000 to 2999. |
| **alias** *alias-name* | Specifies a community alias.  The community alias will be saved in plaintext format in the configuration file.  A community alias must be unique and differs from the community. Only one alias can be configured for a community. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  If quotation marks are used at both ends of an entered character sting, you can enter spaces in the character string. |
| **cipher** *host-string* | Indicates that the SNMP community name is stored in ciphertext.  The community name is displayed in ciphertext regardless of whether it is entered in ciphertext or non-cipher text. | Enter a community name in ciphertext. The community name is a string of consecutive characters.  The non-cipher text is a string of 8 to 32 characters, and the cipher text is a string of 32, 44, 56, 80, 88, 88-168 characters. During the upgrade, ciphertext passwords of different lengths supported by the source version are automatically compatible. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The **snmp-agent community** command is used on SNMPv1 and SNMPv2C networks. A community is a combination of the NMS and SNMP agent and is identified by a community name. The community name functions as a password for authentication during device communication in a community. Devices can communicate if the community name of the NMS matches that of the SNMP agent. The **snmp-agent community** command configures a community name on a device so that the NMS can communicate with the device. Parameters in the **snmp-agent community** command include the access authority, ACL, and accessible MIB views mapped to a community name.

**Precautions**

* The NMS can access a device only when the community name of the NMS matches that of the device.Note:If receiving a packet with the community name field being null, a device discards the packet without filtering the packet based on ACL rules. In addition, a log about the community name error is generated. A device filters a received packet based on ACL rules only if the packet has a valid community name.By default, complexity check is enabled for community names. If a community name fails the complexity check, the community name cannot be configured. To disable the complexity check for a community name, run the **snmp-agent community complexity-check disable** command.After the weak password dictionary maintenance function is enabled, the passwords defined in the weak password dictionary cannot be used. You can run the **display security weak-password-dictionary** command to view the passwords.
* If ip-pool or port-pool in an ACL rule is empty, the rule cannot match any IP address or port.
* After a community name is configured, it is displayed in ciphertext. The alias parameter is used to distinguish different communities. If the alias parameter is not configured, it is automatically generated in the configuration file. The automatic generation rule is \_\_CommunityAliasName\_Sequence number\_Random number. The sequence number is a consecutive value generated based on the configuration sequence of community names.

Example
-------

# Set the community name to YsHsjx\_202206 in ciphertext and allow read-only access using the community name.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent community read cipher YsHsjx_202206

```