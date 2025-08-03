snmp-agent proxy rule
=====================

snmp-agent proxy rule

Function
--------



The **snmp-agent proxy rule** command configures proxy rules for SNMP packets.

The **undo snmp-agent proxy rule** command deletes proxy rules for SNMP packets.



By default, no proxy rules are configured for SNMP packets.


Format
------

**snmp-agent proxy rule** *rule-name* { **read** | **write** | **trap** } **remote-engineid** *remote-engineid* **target-host** *target-host-name* **params-in** **securityname** { *security-name* { **v1** | **v2c** | **v3** [ **authentication** | **privacy** ] } | **cipher** *cipher-text* { **v1** | **v2c** } }

**snmp-agent proxy rule** *rule-name* **inform** **remote-engineid** *remote-engineid* **target-host** *target-host-name* **params-in** **securityname** { *security-name* { **v2c** | **v3** [ **authentication** | **privacy** ] } | **cipher** *cipher-text* { **v2c** } }

**undo snmp-agent proxy rule** *rule-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *rule-name* | Specifies the name of a proxy rule for SNMP packets. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **read** | Enables an NMS to send GetRequest packets to a managed device. | - |
| **write** | Enables an NMS to send SetRequest packets to a managed device. | - |
| **trap** | Enables a managed device to send traps to an NMS. | - |
| **remote-engineid** *remote-engineid* | Binds an SNMP proxy rule to the engine ID of a managed device. | The value is a string of 10 to 64 case-insensitive characters without spaces.  The value is a hexadecimal integer ranging from 0 to F. All 0s or all Fs are invalid. |
| **target-host** *target-host-name* | Specifies the name of a target host for receiving SNMP proxy packets.  The target host may be either the managed device or the NMS. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **params-in** | Specifies the parameters to forward received SNMP messages. | - |
| **securityname** *security-name* | Specifies the name of a security user or community, of which SNMP messages are forwarded. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  In SNMPv1 or SNMPv2c, the value is set to an SNMP proxy community name. In SNMPv3, the value is set to an SNMP user name.  When quotation marks are used around the string, spaces are allowed in the string. |
| **v1** | Enables SNMPv1. | - |
| **v2c** | Enables SNMPv2c. | - |
| **v3** | Enables SNMPv3. | - |
| **authentication** | Authenticates SNMPv3 packets without encrypting them.  The authentication function is used to check the integrity and validity of SNMP packets. An authentication password is configured using the snmp-agent usm-user command. | - |
| **privacy** | Authenticates and encrypts SNMPv3 packets.  The encryption function is used to protect packet data against theft. The authentication and encryption passwords are configured using the snmp-agent usm-user command. | - |
| **cipher** *cipher-text* | Specifies a security name in ciphertext. You can type in the plain text or ciphertext, and it is displayed as the ciphertext in the configuration file. | The value is a string of case-sensitive characters, spaces not supported. A simple text password is a string of 1 to 32 case-sensitive characters. A ciphertext password is a string of 32, 48, 56, 68 or 68 to 168 case-sensitive characters.  When quotation marks are used around the string, spaces are allowed in the string.  Ciphertext passwords with various lengths configured in an earlier version are also supported in the existing version. |
| **inform** | Enables a managed device to send informs to an NMS. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The SNMP proxy and the Cabinet Control Unit (CCU) of a managed device are placed in the same outdoor cabinet. The SNMP proxy enables communication between the NMS and managed device and allows you to manage the configurations and system software version of the managed device. The NMS manages the SNMP proxy and managed device as an independent network element, reducing the number of managed network elements and management costs. The NMS monitors the performance of managed devices in real time, helping to improve service quality. After you run the snmp-agent proxy rule command to configure proxy rules, the SNMP proxy can automatically forward SNMP requests from the NMS to the managed device and forward responses from the managed device to the NMS.

**Prerequisites**

The proxy rules configured on an SNMP proxy must be unique.

**Precautions**

* If trap or inform is specified, the proxy rule uniquely identifies a target host for receiving notifications.
* If read or write is specified, the proxy rule uniquely identifies a target host for receiving GetRequest or SetRequest PDUs.
* If you specify neither authentication nor privacy, SNMPv3 packets are neither authenticated nor encrypted.
* If the target host specified by the target-host target-host-name parameter does not exist, the proxy rule configured using this command does not take effect.If the security user or community specified by the securityname security-name parameter does not exist, the proxy rule configured using this command does not take effect.

Example
-------

# Configure a proxy rule for SNMP packets and set the rule name to proxy\_rule\_write@ccu2, target host name to 10.1.1.1, and remote engine ID to 01120025602101.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent proxy rule proxy_rule_write@ccu2 write remote-engineid 01120025602101 target-host 10.1.1.1 params-in securityname hello v3

```