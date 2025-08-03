display snmp-agent inform
=========================

display snmp-agent inform

Function
--------



The **display snmp-agent inform** command displays parameters configured for a specific or all target hosts to send Inform messages.




Format
------

**display snmp-agent inform** { **host-name** *host-name* | { **ipv6** **address** **udp-domain** *ipv6-address* | **address** **udp-domain** *ip-address* } [ **vpn-instance** *vpn-instance-name* ] **params** **securityname** { *interface-name* | { **cipher** *protocol-interface-name* } } }

**display snmp-agent inform**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **host-name** *host-name* | Specifies an SNMP target host name. | The name is a string of 1 to 32 characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |
| **ipv6** | Specifies an IPv6 target host. | - |
| **address** | Indicates the address of a target host for receiving SNMP messages. | The IP address specified using address and the security name specified using securityname together identify a host. |
| **udp-domain** *ipv6-address* | Specifies the IP address of the IPv6 target host and uses UDP for transmission. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **udp-domain** *ip-address* | Specifies the IP address of a target host within a User Datagram Protocol (UDP) transmission domain. | The value is in dotted decimal notation. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string.  vpn-instance is optional. To run the display snmp-agent inform command on a VPN network, use the VPN instance name, IP address, and security name together to identify a host. |
| **params** | Indicates information about a target host that generates SNMP messages. | - |
| **securityname** *interface-name* | Specifies the user name or community name displayed on the NMS. | The value is a string of 1 to 32 case-sensitive characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |
| **cipher** *protocol-interface-name* | Specifies the unencrypted or encrypted password of a security name. The simple text password or the ciphertext password can be entered. The password in the configuration file is displayed in ciphertext. | The value is a string of case-sensitive characters, spaces not supported. A simple text password is a string of 1 to 32 case-sensitive characters. A ciphertext password is a string of 48 or from 68 to 168 case-sensitive characters.  When quotation marks are used around the string, spaces are allowed in the string.  Ciphertext passwords with various lengths configured in an earlier version are also supported in the existing version. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

To view the configuration of sending Inform messages on all target hosts, run the **display snmp-agent inform** command. The command output contains the following information:

* Retransmission times configured on all target hosts
* Timeout period
* Maximum number of Inform messages that can be pending in the inform buffer for acknowledgment from the NMS
* Current number of Inform messages pending in the inform buffer waiting for acknowledgment from the NMSTo view the configuration of sending Inform messages on a specified target host and message statistics, run the **display snmp-agent inform** command. The command output contains the following information:
* Retransmission times configured on the specified target host
* Timeout period in seconds after which an inform message is retransmitted from the inform buffer to the NMS.
* Number of times that an Inform message has been retransmitted
* Number of Inform messages to be confirmed
* Number of Inform messages that have been sent
* Number of Inform messages that are dropped because the inform buffer is full
* Number of Inform messages that are dropped because no corresponding acknowledgement messages are returned
* Number of received acknowledgement messages

**Prerequisites**

The IP address of the target host that receives Inform messages and parameters for sending Inform messages has been configured using the **snmp-agent target-host inform** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the parameters configured for a specific or all target hosts to send Inform messages.
```
<HUAWEI> display snmp-agent inform
Global config: resend-times 3, timeout 15s, pending 39
Global status: current notification count 0
Target-host ID: Host name/VPN instance/IP-Address/Security name
targetHost_1_36305/-/10.1.1.1/%#%#[7SCH}$<HX.vZ8%7YS3L:IsCPA^LbRRK-`/6"i"$%#%#:
    Config: resend-times 3, timeout 15s
    Status: retries 0, pending 0, sent 0, dropped 0, failed 0, confirmed 0

```

**Table 1** Description of the **display snmp-agent inform** command output
| Item | Description |
| --- | --- |
| Global config | Global configuration:   * resend-times: number of times for retransmitting Inform messages. * timeout: configured timeout period. * pending: maximum number of informs in the trap queue. |
| Global status | Global packet statistics. |
| Target-host ID | ID of the target host, consisting of the VPN instance name, IP address of the target host, and security name. |
| Config | Configuration of the host where the SNMP agent resides:   * resend-times: number of times for retransmitting Inform messages. * timeout: configured timeout period. |
| Status | Statistics about the Inform messages generated on the host where the SNMP agent resides. The possible types are:   * retries: number of Inform messages retransmitted to the target host. * pending: number of inform messages waiting in the inform buffer for acknowledgment from NMS. * sent: number of Inform messages that are successfully sent. * dropped: number of Inform messages that are dropped because the inform buffer is full. * failed: number of Inform messages that are not confirmed during the retransmission. * confirmed: number of Acknowledgement messages returned by the target host. |