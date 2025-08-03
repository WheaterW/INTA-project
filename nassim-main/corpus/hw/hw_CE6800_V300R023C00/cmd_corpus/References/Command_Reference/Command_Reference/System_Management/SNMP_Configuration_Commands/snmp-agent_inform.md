snmp-agent inform
=================

snmp-agent inform

Function
--------



The **snmp-agent inform address** command sets parameters for sending Inform messages. The parameters include the timeout period for waiting for Inform ACK messages from the NMS and the number of attempts to retransmit an Inform message.

The **undo snmp-agent inform address** command restores the default settings for a particular inform host.



By default, the timeout waiting period for Inform ACK messages is 15 seconds, and the number of attempts to retransmit an Inform message is 3.


Format
------

**snmp-agent inform** { **timeout** *seconds* | **resend-times** *times* } \* { **host-name** *target-host-name* | { **address** **udp-domain** *ip-address* | **ipv6** **address** **udp-domain** *ipv6-address* } [ **vpn-instance** *vpn-instance-name* ] **params** **securityname** { *security-name* | **cipher** *security-name-cipher* } }

**undo snmp-agent inform** { **timeout** [ *seconds* ] | **resend-times** [ *times* ] } \* { **host-name** *target-host-name* | { **address** **udp-domain** *ip-address* | **ipv6** **address** **udp-domain** *ipv6-address* } [ **vpn-instance** *vpn-instance-name* ] **params** **securityname** { *security-name* | **cipher** *security-name-cipher* } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **timeout** *seconds* | Specified the timeout period for waiting for Inform ACK messages from the NMS. | The value is an integer ranging from 1 to 1800, in seconds. The default value is 15, which is equal to the global timeout period configured using the snmp-agent inform command. |
| **resend-times** *times* | Specifies the maximum number of attempts to retransmit an Inform message if no Inform ACK message is returned by the NMS. | The value is an integer ranging from 0 to 10. The default value is 3, which is equal to the global retransmission times configured using the snmp-agent inform command. |
| **host-name** *target-host-name* | Specifies an SNMP target host name. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **address** | Indicates the IP address of a target host for receiving SNMP trap messages. | The IP address specified using address and the security name specified using securityname together identify a host. |
| **udp-domain** *ipv6-address* | Specifies the IP address of the IPv6 target host and the UDP protocol for the transmission domain. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **udp-domain** *ip-address* | Specifies the IP address of a specified target host within a UDP transmission domain. | The value is in dotted decimal notation. The value must be a valid unicast address. |
| **ipv6** | Specifies the type of the IPv6 target host for SNMP message transmission. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string.  The parameter vpn-instance is optional. On a VPN network, use the VPN instance specified using vpn-instance, IP address, and security name together to identify a target host. |
| **params** | Indicates information about a target host that generates SNMP notifications. | - |
| **securityname** *security-name* | Displays the name of a target host for receiving Inform messages on the NMS.  For SNMPv3, securityname must be set to a user name. securityname configured on the host must be the same as that configured on the NMS, or the NMS cannot receive the trap messages sent by the host.  For SNMPv1 and SNMPv2c, the NMS can receive trap messages from all hosts without having securityname configured. securityname is used to distinguish multiple hosts that generate trap messages. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |
| **cipher** | Indicates the password in ciphertext. The simple password or the ciphertext password can be entered. The password in the configuration file is displayed in ciphertext.  If you do not specify the keyword, enter the simple password only. | The value is a string of case-sensitive characters, spaces not supported. A simple text password is a string of 1 to 32 case-sensitive characters. A ciphertext password is a string of 32, 48, 56 or from 68 to 168 case-sensitive characters.  When quotation marks are used around the string, spaces are allowed in the string.  Ciphertext passwords with various lengths configured in an earlier version are also supported in the existing version. |
| **cipher** *security-name-cipher* | Specifies a ciphertext security name. | The value is a string of 1 to 168 case-sensitive characters without spaces. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

You can run the **snmp-agent inform address** command to set the parameters of the Inform mode for the target host. The timeout and resend-times parameters take precedence over the two parameters set by the **snmp-agent inform** command. If the **snmp-agent inform address** command is run on the target host after the global Inform parameters are configured, only the parameter configured using the **snmp-agent inform address** command takes effect.You can use both the **snmp-agent inform address** command and the **snmp-agent inform** command to set parameters based on network conditions.

* When a large number of Inform messages are lost on the network, you are advised to increase the queue length. You are advised to run the snmp-agent inform pending *number*command globally, and then run the **snmp-agent inform address** command to specify the destination address and the user name to be displayed.
* If the network transmission speed is low, you are advised to increase the timeout period. Increasing the timeout period will increase the waiting time of Inform messages in the message queue for confirmation. You are advised to run the snmp-agent inform { timeout *seconds*| pending *number*} \* command globally and then run the **snmp-agent inform address** command to specify the destination address and user name to be displayed.
* If the network transmission speed is high, you are advised to reduce the timeout period. You are advised to run the snmp-agent inform timeout address udp-domain params securityname or **snmp-agent inform timeout ipv6 address udp-domain params securityname** command.
* If Inform messages are transmitted on an unreliable network, you are advised to increase the number of retransmission times. In this case, the Inform messages in the message queue need to wait for a longer time to be confirmed. You are advised to run the snmp-agent inform { resend-times *times*| pending *number*} \* command and then run the **snmp-agent inform address** command to specify the destination address and user name to be displayed.
* When the timeout and resend-times parameters of the target host are configured using parameters such as address, the parameters are converted to the host name of the corresponding host in the configuration file.

**Prerequisites**

Parameters for sending Inform messages take effect only after the IP address of the target host for receiving Inform messages is configured using the **snmp-agent target-host inform** command.The IP address of the target host for receiving Inform messages has been configured using the **snmp-agent target-host inform** command.

**Precautions**

You must set the parameters timeout and resend-times based on network conditions. Setting an inappropriate parameter deteriorates the transmission efficiency of SNMP messages. If the parameters timeout and resend-times are already configured globally using the **snmp-agent inform** command, after the **snmp-agent inform address** command is run on a specified target host, the earlier configuration is overwritten.Note:Only parameters for sending Inform messages need to be configured using the **snmp-agent inform address** command. Parameters for sending trap messages do not need to be configured.


Example
-------

# Set the maximum number of attempts 10 to retransmit an Inform message to a target host with the IP address of 10.1.1.1 and the security name of ABC.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent inform resend-times 10 address udp-domain 10.1.1.1 params securityname ABC

```

# Set the maximum number of attempts 10 to retransmit an Inform message to a target host.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent inform resend-times 10

```