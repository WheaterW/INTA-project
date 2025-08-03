snmp-agent target-host inform
=============================

snmp-agent target-host inform

Function
--------



The **snmp-agent target-host inform** command configures a target host for receiving Inform messages.

The **undo snmp-agent target-host** command deletes a target host configured to receive Inform messages.



By default, no proxy target host is configured.


Format
------

**snmp-agent target-host** [ **host-name** *host-name* ] **inform** **address** **udp-domain** *ip-address* [ [ **udp-port** *server-port* ] | [ { **vpn-instance** *vpn-instance-name* | **public-net** } ] | [ **source** { *interface-name* | *interface-type* *interface-number* } ] ] \* **params** **securityname** { *security-name* { **v2c** | **v3** [ **authentication** | **privacy** ] } | **cipher** *cipher-name* **v2c** } [ [ **private-netmanager** | **ext-vb** | **notify-filter-profile** *profile-name* | **heart-beat** **enable** ] \* ] \*

**snmp-agent target-host host-name** *host-name* **inform** **address** **udp-domain** *ip-address* [ [ **udp-port** *server-port* ] | [ { **vpn-instance** *vpn-instance-name* | **public-net** } ] | [ **source** { *interface-name* | *interface-type* *interface-number* } ] ] \* **params** **securityname** { *security-name* { **v2c** | **v3** [ **authentication** | **privacy** ] } | **cipher** *cipher-name* **v2c** } [ [ **private-netmanager** | **ext-vb** | **notify-filter-profile** *profile-name* | **heart-beat** **enable** ] \* ] \*

**snmp-agent target-host** [ **host-name** *host-name* ] **inform** **ipv6** **address** **udp-domain** *ipv6-address* [ [ **udp-port** *server-port* ] | [ **vpn-instance** *vpn-instance-name* | **public-net** ] | [ **source** { *interface-name* | *interface-type* *interface-number* } ] ] \* **params** **securityname** { *security-name* { **v2c** | **v3** [ **authentication** | **privacy** ] } | **cipher** *cipher-name* **v2c** } [ [ **private-netmanager** | **ext-vb** | **notify-filter-profile** *profile-name* ] \* ] \*

**undo snmp-agent target-host** { **host-name** *host-name* | *ip-address* **securityname** { *security-name* | **cipher** *cipher-name* } [ **vpn-instance** *vpn-instance-name* | **public-net** ] | { **trap** | **inform** } **address** **udp-domain** *ip-address* [ { [ **source** { *interface-name* | *interface-type* *interface-number* } ] | **udp-port** *server-port* | { **vpn-instance** *vpn-instance-name* | **public-net** } } \* ] **params** **securityname** { *security-name* | **cipher** *cipher-name* } }

**undo snmp-agent target-host** { **ipv6** *ipv6-address* **securityname** { *security-name* | **cipher** *cipher-name* } [ **vpn-instance** *vpn-instance-name* | **public-net** ] | **inform** **ipv6** **address** **udp-domain** *ipv6-address* [ { [ **source** { *interface-name* | *interface-type* *interface-number* } ] | **udp-port** *server-port* | { **vpn-instance** *vpn-instance-name* | **public-net** } } \* ] **params** **securityname** { *security-name* | **cipher** *cipher-name* } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **host-name** *host-name* | Specifies an SNMP target host name.  If spaces are used, the string must start and end with double quotation marks ("). By default, the device automatically generates a host name as the host identifier. | The value is a string of 1 to 32 characters without spaces.  If spaces are used, the string must start and end with double quotation marks ("). |
| **inform** | Specifies the inform message. | - |
| **address** | Specifies an IP address of a target host for receiving SNMP Inform messages. | - |
| **udp-domain** *ip-address* | Specifies the IP address of a specified target host within a UDP transmission domain. | The value is in dotted decimal notation and must be a valid unicast address. |
| **udp-port** *server-port* | Specifies the number of a UDP port for receiving Inform messages. | The value is an integer ranging from 0 to 65535. The default value is 162. |
| **vpn-instance** *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string.  On a VPN network, use the VPN instance specified using vpn-instance, IP address, and security name together to identify a target host. |
| **public-net** | Indicates that the host generating a trap message is connected to a public network. | - |
| **source** | Specifies the type and number of a source interface for sending Inform messages. | - |
| *interface-name* | Specifies the name of a source interface for sending Inform messages. | - |
| *interface-type* | Specifies the type of a source interface for sending Inform messages. | - |
| *interface-number* | Specifies the number of a source interface for sending Inform messages. | - |
| **params** | Indicates information about a target host that generates SNMP notifications. | - |
| **securityname** *security-name* | Specifies a user security name displayed on the NMS.  For SNMPv3, securityname must be configured as the user name. securityname configured on the host must be the same as that configured on the NMS, or the NMS cannot receive the trap messages sent by the host.  For SNMPv1 and SNMPv2c, the NMS can receive trap messages from all hosts without having securityname configured. securityname is used to distinguish multiple hosts that generate trap messages. | The value is a string of 1 to 32 characters without spaces.  If spaces are used, the string must start and end with double quotation marks ("). |
| **v2c** | Indicates SNMPv2c and SNMPv3, respectively. | - |
| **v3** | Indicates SNMPv2c and SNMPv3, respectively. | - |
| **authentication** | Indicates that messages are authenticated without being encrypted. authentication takes effect only in SNMPv3. | - |
| **privacy** | Indicates that messages are authenticated and encrypted. privacy takes effect only in SNMPv3. | - |
| **cipher** *cipher-name* | Specifies a password in ciphertext. You can type in the plain text or the ciphertext, and it is displayed as the ciphertext in the configuration file. | The value is a string of 1 to 168 case-sensitive characters without spaces. |
| **private-netmanager** | Specifies the target host as the Huawei NMS. | - |
| **ext-vb** | Indicates that Inform messages sent to the NM station carry extended bound variables. If alarm objects defined in public MIBs are extended on a Huawei data communication device, use.  ext-vb to determine whether the corresponding Inform messages sent by the device to the NM station carry extended bound variables.   * If ext-vb is not specified, the Inform message does not carry extended bound variables.   This parameter is not recommended if the NMS is a third-party NMS. This ensures that the third-party NMS can receive Inform messages from Huawei data communication devices.  By default, an Inform message sent by a Huawei data communication device does not carry extended bound variables.   * If ext-vb is specified, the inform message carries extended bound variables.   This parameter is recommended if the NMS is a Huawei NMS. This allows more abundant information in Inform messages. | - |
| **notify-filter-profile** *profile-name* | Specifies the notification profile name for notification filtering. | The value is a string of 1 to 32 characters without spaces.  If spaces are used, the string must start and end with double quotation marks ("). |
| **heart-beat** | Specify heart beat required or not. | - |
| **enable** | Enables the heartbeat mechanism. | - |
| **ipv6** | Specifies the type of the IPv6 target host for SNMP message transmission. | - |
| *ipv6-address* | Specifies the IP address of an IPv6 target host. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **trap** | Specifies the trap message. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



If the heartbeat mechanism is enabled on the target host and the **snmp-agent trap enable feature-name snmp trap-name hwnmsheartbeat** command is configured, the SNMP agent periodically sends heartbeat traps to the NMS to keep the connection alive. The default interval for sending heartbeat traps is 1 hour. The heartbeat trap message is NMSHeartbeat was sent successfully.



**Configuration Impact**

After the **snmp-agent target-host** command is run, no matter whether a trap message sent by the SNMP agent reaches the NMS, the SNMP agent deletes the trap message to reduce the resource consumption.After the **snmp-agent target-host inform** command is run, the SNMP agent, after sending an Inform message, waits for an Inform ACK message from the NMS and will retransmit the same Inform message only when no Inform ACK message is received from the NMS within the specified period. If the SNMP agent does not receive the Inform ACK message from the NMS during the retransmission period, the SNMP agent deletes this Inform message from the trap message queue. This ensures that the NMS can receive the SNMP trap messages to the maximum extent. The transmission of trap messages, however, consumes less resources than that of Inform messages.

**Precautions**

To enable a device to send Inform messages, you must run the snmp-agent target-host inform and snmp-agent trap enable commands on the device.If you run the **snmp-agent target-host** command to configure a target host for receiving trap messages and then run the **snmp-agent target-host inform** command to configure a target host with the same host name and address, the configurations of the latter command overwrite those of the former command.

* If the VPN instance specified by vpn-instance vpn-instance-name does not exist, Inform messages cannot be sent.
* If the user security name specified by securityname security-name does not exist, Inform messages cannot be sent.
* If notify-view is not specified for the group to which the user specified by securityname security-name belongs, Inform messages cannot be sent.

Example
-------

# Set the alarm sending mode to Inform, host security name to 1, SNMP version to v2c, and IP address of the target host to 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent trap enable
[*HUAWEI] snmp-agent target-host host-name 1 inform address udp-domain 10.1.1.1 source 100GE 1/0/1 params securityname 1 v2c

```

# Set the alarm sending mode to Inform, host security name to public, SNMP version to v2c, and IP address of the target host to 10.1.1.1. Set alarms sent to the target host to carry extended bound variables.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent trap enable
[*HUAWEI] snmp-agent target-host inform address udp-domain 10.1.1.1 params securityname public v2c ext-vb

```

# Set the alarm sending mode to Inform, host security name to 123, SNMP version to v3, and IP address of the target host to 10.1.1.1. Enable authentication and encryption.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent trap enable
[*HUAWEI] snmp-agent target-host inform address udp-domain 10.1.1.1 params securityname 123 v3 privacy

```