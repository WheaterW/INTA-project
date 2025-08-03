snmp-agent proxy target-host
============================

snmp-agent proxy target-host

Function
--------



The **snmp-agent proxy target-host** command configures target host information on an SNMP proxy.

The **undo snmp-agent proxy target-host** command deletes target host information.



By default, no target host information is configured.


Format
------

**snmp-agent proxy target-host** *target-host-name* **address** **udp-domain** *ip-address* **udp-port** *port-number* [ { **source** { *interface-type* *interface-number* | *interface-name* } | { **vpn-instance** *vpn-instance-name* | **public-net** } } | { **timeout** *timeout-value* } ] \* **params** **securityname** { *security-string* { **v1** | **v2c** | **v3** [ **authentication** | **privacy** ] } | **cipher** *security-string-cipher* { **v1** | **v2c** } }

**snmp-agent proxy target-host** *target-host-name* **ipv6** **address** **udp-domain** *ipv6-address* **udp-port** *port-number* [ { **source** { *interface-type* *interface-number* | *interface-name* } | { **vpn-instance** *vpn-instance-name* | **public-net** } } | { **timeout** *timeout-value* } ] \* **params** **securityname** { *security-string* { **v1** | **v2c** | **v3** [ **authentication** | **privacy** ] } | **cipher** *security-string-cipher* { **v1** | **v2c** } }

**undo snmp-agent proxy target-host** *target-host-name*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *target-host-name* | Specifies the name of a target host.  The target host may be either the managed device or the NMS. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |
| **address** | Indicates the destination address carried in SNMP proxy packets. | - |
| **udp-domain** *ip-address* | Uses UDP to transmit SNMP proxy packets.  The ip-address parameter specifies the destination IPv4 address used to receive SNMP proxy packets. | The value is in dotted decimal notation. |
| **udp-port** *port-number* | Specifies the number of a port used by the target host to receive SNMP proxy packets. | The value is an integer ranging from 1 to 65535. |
| **source** | Specifies the type and number of a source interface used by the SNMP proxy to send SNMP proxy packets. | - |
| *interface-type* | Interface Type. | - |
| *interface-number* | Interface Number. | - |
| *interface-name* | Interface Name. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance to which a target host belongs.  If the NMS and managed device need to communicate over a private network, use this parameter. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string.  On a VPN, the VPN instance name, IP address, and security name form a triplet to uniquely identify a host. |
| **public-net** | Indicates that a host generating a trap message is connected to a public network. | - |
| **timeout** *timeout-value* | Specifies the timeout period for a target host to send a response to an SNMP agent after receiving an inform from the SNMP agent. | The value is an integer ranging from 1 to 1800, in seconds. |
| **params** | Displays information about the target host that generates SNMP messages. | - |
| **securityname** *security-string* | Specifies a security name to be displayed on the NMS.  For SNMPv3, securityname must be configured as the user name. securityname configured on the host must be the same as that configured on the NMS, or the NMS cannot receive the trap messages sent by the host.  For SNMPv1 and SNMPv2c, the NMS can receive trap messages from all hosts without having securityname configured. securityname is used to distinguish multiple hosts that generate trap messages. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |
| **v1** | Indicates SNMPv1. | - |
| **v2c** | Indicates SNMPv2c. | - |
| **v3** | Indicates SNMPv3. | - |
| **authentication** | Authenticates SNMPv3 packets without encrypting them.  The authentication function is used to check the integrity and validity of SNMP packets. The authentication password is configured using the snmp-agent usm-user command. | - |
| **privacy** | Authenticates and encrypts SNMPv3 packets.  The encryption function is used to protect packet data against theft. The authentication and encryption passwords are configured using the snmp-agent usm-user command. | - |
| **cipher** *security-string-cipher* | Specifies a security name in ciphertext. You can type in the plain text or ciphertext, and it is displayed as the ciphertext in the configuration file. | The value is a string of case-sensitive characters, spaces not supported. A simple text password is a string of 1 to 32 case-sensitive characters. A ciphertext password is a string of 32, 48, 56 or from 68 to 168 case-sensitive characters.  When quotation marks are used around the string, spaces are allowed in the string.  Ciphertext passwords with various lengths configured in an earlier version are also supported in the existing version. |
| **ipv6** *ipv6-address* | Specifies the IPv6 address of a target host. | The address is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To enable an NMS to effectively manage a managed device, run the snmp-agent proxy target-host command to configure target host information. You can also configure the SNMP proxy to filter undesired SNMP packets.

**Precautions**

* You can run this command multiple times with different parameters set to configure an SNMP proxy to send packets to multiple NMSs or the managed device. An SNMP proxy supports a maximum of 20 target hosts. If the number of target hosts exceeds 20, an error message is displayed.
* If you specify neither authentication nor privacy, SNMPv3 packets are neither authenticated nor encrypted.
* If a VPN instance to which the target host belongs is specified by the vpn-instance vpn-instance-name parameter, make sure the VPN instance has already been created. Otherwise, the SNMP proxy packets cannot be sent to the target host.
* When you configure target host information, ensure that the VPN instance name configured for the target host is the same as the name of the VPN instance to which to the source port of the target host is bound. Otherwise, the target host may fail to receive SNMP proxy packets.

Example
-------

# Configure an SNMP proxy to send packets to a target host with name of 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent proxy target-host snmp-proxy address udp-domain 10.1.1.1 udp-port 162 source 100GE 1/0/1 timeout 45 params securityname public v3

```