snmp-agent proxy community
==========================

snmp-agent proxy community

Function
--------



The **snmp-agent proxy community** command creates an SNMP proxy community.

The **undo snmp-agent proxy community** command deletes an SNMP proxy community.



By default, no SNMP proxy community is configured.


Format
------

**snmp-agent proxy community** *community-name* **remote-engineid** *remote-engineid* [ **acl** { *acl-number* | *acl-name* } | **alias** *alias-name* ] \*

**snmp-agent proxy community cipher** *cipher-name* **remote-engineid** *remote-engineid* [ **acl** { *acl-number* | *acl-name* } | **alias** *alias-name* ] \*

**undo snmp-agent proxy community** *community-name*

**undo snmp-agent proxy community cipher** *cipher-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **remote-engineid** *remote-engineid* | Specifies the engine ID of the managed device.  The engine ID of the managed device must be different from the engine ID of the SNMP proxy. | The value is a string of 10 to 64 case-insensitive characters without spaces.  The value is a hexadecimal integer ranging from 0 to F. All 0s or all Fs are invalid. |
| **acl** | Indicates that a created community is bound to a basic ACL.  The basic ACL defines whether NMSs with specified source IP addresses can access SNMP agents. | - |
| *acl-number* | Specifies the number of a basic ACL. | The value is an integer ranging from 2000 to 2999. |
| *acl-name* | Specifies the name of a named basic ACL.  If no matching rule is configured for the referenced ACL, the matching rule is permit by default. | The value is a string of 1 to 32 case-sensitive characters, and spaces are not supported. |
| **alias** *alias-name* | Specifies a community alias.  The community alias will be saved in simple text format in the configuration file.  A community alias must be unique and differs from the community. Only one alias can be configured for a community. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  If quotation marks are used at both ends of an entered character sting, you can enter spaces in the character string. |
| **cipher** *cipher-name* | Specifies the name of an SNMP proxy community to be stored in ciphertext.The cipher-name value is displayed in ciphertext, no matter whether you specify it in ciphertext or simple text. | The value is a string of 1 to 168 consecutive characters, spaces not supported. Ciphertext passwords with various lengths configured in an earlier version are also supported in the existing version. |
| **cipher** *community-name* | Specifies the name of an SNMP proxy community.  The community-name parameter applies to only SNMPv1 and SNMPv2c entities. | The value is a string of case-sensitive characters, spaces not supported. The length range depends on whether the complexity check of community names is enabled:   * If it is enabled, the length ranges from 8 to 32. * If it is disabled, the length ranges from 1 to 32.   When quotation marks are used around the string, spaces are allowed in the string. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

An SNMP community is used to define the relationships between multiple NMSs and a managed device. The community name acts as a password to regulate access to the managed device. An NMS can access a managed device only if the community name carried in the SNMP request sent by the NMS matches the community name configured on the managed device. The snmp-agent proxy community command creates an SNMP community on an SNMP proxy, enabling communication between the NMS and managed device.

**Configuration Impact**

If a device receives a packet with a null community name, the device drops the packet without filtering the packet based on ACL rules. In addition, the community name error is logged. A device filters a received packet based on ACL rules only if the packet has a valid community name.

**Follow-up Procedure**

After you run the snmp-agent proxy community command, run the **display snmp-agent proxy community** command to check SNMPv1 or SNMPv2c proxy community information.

**Precautions**

The snmp-agent proxy community command applies only to SNMPv1 and SNMPv2c. After the weak password dictionary maintenance function is enabled, the passwords defined in the weak password dictionary cannot be used. You can run the **display security weak-password-dictionary** command to view the passwords.


Example
-------

# Create an SNMP proxy community, set the community name to proxy\_public, and bind the community to a basic ACL numbered 2000.
```
<HUAWEI> system-view
[~HUAWEI] acl 2000
[*HUAWEI-acl4-basic-2000] quit
[*HUAWEI] snmp-agent proxy community proxy_public remote-engineid 800007DB03360607111100 acl 2000

```