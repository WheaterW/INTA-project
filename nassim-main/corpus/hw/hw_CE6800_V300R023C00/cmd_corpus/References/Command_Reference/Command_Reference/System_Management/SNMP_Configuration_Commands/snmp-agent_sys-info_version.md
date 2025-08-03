snmp-agent sys-info version
===========================

snmp-agent sys-info version

Function
--------



The **snmp-agent sys-info version** command enables the corresponding SNMP version.

The **snmp-agent sys-info version disable** command disables the corresponding SNMP version.



By default, the version is SNMPv3.


Format
------

**snmp-agent sys-info version** { { *v1* | *v2c* | *v3* } \* | *all* }

**snmp-agent sys-info version** { { *v1* | *v2c* | *v3* } \* | *all* } **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *v1* | Indicates SNMPv1. | v1 |
| *v2c* | Indicates SNMPv2c. | v2c |
| *v3* | Indicates SNMPv3. | v3 |
| *all* | Enables all SNMP versions, namely, SNMPv1, SNMPv2c, and SNMPv3. | all |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To set an SNMP version, run the **snmp-agent sys-info version** command. SNMP functions provided vary with the SNMP version.SNMPv1:

* Community-name-based access control
* MIB-view-based access controlSNMPv2c:
* Community-name-based access control
* MIB-view-based access controlSNMPv3 inherits basic SNMPv2c operations, defines a new management architecture, and provides more secure access based on the user-based security model (USM):
* User groups
* Group-based access control
* User-based access control
* Authentication and encryption mechanisms
* Inform messagesYou can run the **display snmp-agent sys-info** command to view the system maintenance information, physical location of the device node, and SNMP version.

**Configuration Impact**

Running the **undo snmp-agent** command causes the configurations of all SNMP versions (SNMPv1, SNMPv2c, and SNMPv3) on the device to become invalid.

**Precautions**

* To ensure high security, SNMPv3 is recommended.
* Parameters v1, v2c, and all can be used only after the weak security algorithm/protocol feature package (WEAKEA) has been installed using the **install feature-software WEAKEA** command.


Example
-------

# Set the current SNMP version to v3.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent sys-info version v3

```