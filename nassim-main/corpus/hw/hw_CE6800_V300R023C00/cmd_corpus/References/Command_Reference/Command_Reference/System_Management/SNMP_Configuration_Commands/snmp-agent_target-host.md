snmp-agent target-host
======================

snmp-agent target-host

Function
--------



The **snmp-agent target-host** command sets the target host for receiving SNMP trap messages.

The **undo snmp-agent target-host** command deletes the target host set for receiving SNMP trap messages.



By default, the target host is not set.


Format
------

**snmp-agent target-host** [ **host-name** *host-name* ] **trap** **ipv6** **address** **udp-domain** *ipv6-address* [ [ **udp-port** *port-number* | [ **alarm-udp-port** *alarm-port-number* | **event-udp-port** *event-port-number* ] \* ] | [ **vpn-instance** *vpn-instance-name* | **public-net** ] ] \* **params** **securityname** { *security-name* [ [ **v1** | **v2c** | **v3** [ **authentication** | **privacy** ] ] | **ext-vb** | **notify-filter-profile** *profile-name* | **private-netmanager** ] \* | **cipher** *cipher-name* [ [ **v1** | **v2c** ] | **ext-vb** | **notify-filter-profile** *profile-name* | **private-netmanager** ] \* }

**snmp-agent target-host** [ **host-name** *host-name* ] **trap** **address** **udp-domain** *ip-address* [ [ **udp-port** *port-number* | [ **alarm-udp-port** *alarm-port-number* | **event-udp-port** *event-port-number* ] \* ] | [ { **vpn-instance** *vpn-instance-name* | **public-net** } ] | [ **source** { *interface-name* | *interface-type* *interface-number* } ] ] \* **params** **securityname** { *security-name* [ [ **v1** | **v2c** | **v3** [ **authentication** | **privacy** ] ] | **private-netmanager** | **ext-vb** | **notify-filter-profile** *profile-name* | **heart-beat** **enable** ] \* | **cipher** *cipher-name* [ [ **v1** | **v2c** ] | **private-netmanager** | **ext-vb** | **notify-filter-profile** *profile-name* | **heart-beat** **enable** ] \* }

**snmp-agent target-host host-name** *host-name* **trap** **address** **udp-domain** *ip-address* [ [ **udp-port** *port-number* | [ **alarm-udp-port** *alarm-port-number* | **event-udp-port** *event-port-number* ] \* ] | [ { **vpn-instance** *vpn-instance-name* | **public-net** } ] | [ **source** { *interface-name* | *interface-type* *interface-number* } ] ] \* **params** **securityname** { *security-name* [ [ **v1** | **v2c** | **v3** [ **authentication** | **privacy** ] ] | **private-netmanager** | **ext-vb** | **notify-filter-profile** *profile-name* | **heart-beat** **enable** ] \* | **cipher** *cipher-name* [ [ **v1** | **v2c** ] | **private-netmanager** | **ext-vb** | **notify-filter-profile** *profile-name* | **heart-beat** **enable** ] \* }

**snmp-agent target-host host-name** *host-name* **trap** **ipv6** **address** **udp-domain** *ipv6-address* [ [ **udp-port** *port-number* | [ **alarm-udp-port** *alarm-port-number* | **event-udp-port** *event-port-number* ] \* ] | [ **vpn-instance** *vpn-instance-name* | **public-net** ] | [ **source** { *interface-name* | *interface-type* *interface-number* } ] ] \* **params** **securityname** { *security-name* [ [ **v1** | **v2c** | **v3** [ **authentication** | **privacy** ] ] | **ext-vb** | **notify-filter-profile** *profile-name* | **private-netmanager** ] \* | **cipher** *cipher-name* [ [ **v1** | **v2c** ] | **ext-vb** | **notify-filter-profile** *profile-name* | **private-netmanager** ] \* }

**undo snmp-agent target-host** { **ipv6** *ipv6-address* **securityname** { *security-name* | **cipher** *cipher-name* } | **trap** **ipv6** **address** **udp-domain** *ipv6-address* [ [ **udp-port** *port-number* | [ **alarm-udp-port** *alarm-port-number* | **event-udp-port** *event-port-number* ] \* ] | [ **vpn-instance** *vpn-instance-name* | **public-net** ] | [ **source** { *interface-name* | *interface-type* *interface-number* } ] ] \* **params** **securityname** { *security-name* | **cipher** *cipher-name* } }

**undo snmp-agent target-host** { **host-name** *host-name* | *ip-address* **securityname** { *security-name* | **cipher** *cipher-name* } [ **vpn-instance** *vpn-instance-name* | **public-net** ] | **trap** **address** **udp-domain** *ip-address* [ { [ **source** { *interface-name* | *interface-type* *interface-number* } ] | [ **udp-port** *port-number* | [ **alarm-udp-port** *alarm-port-number* | **event-udp-port** *event-port-number* ] \* ] | { **vpn-instance** *vpn-instance-name* | **public-net** } } \* ] **params** **securityname** { *security-name* | **cipher** *cipher-name* } }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **host-name** *host-name* | Specifies an SNMP target host name. | The value is a string of 1 to 32 characters without spaces.  If spaces are used, the string must start and end with double quotation marks ("). By default, the device automatically generates a host name as the host identifier. |
| **trap** | Specifies the target host for receiving SNMP notifications in the form of trap messages. | - |
| **ipv6** *ipv6-address* | Specifies the target is in IPv6 address. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **address** | Specifies the address of the target host that receives SNMP trap messages. | The IP address specified using address and the username specified using securityname together identify a target host. |
| **udp-domain** *ip-address* | Specifies the IP address of the specified target host within a UDP transmission domain. | The value is in dotted decimal notation. The value must be a valid unicast address. |
| **udp-domain** *ipv6-address* | Specifies the IPv6 address of the specified target host within a UDP transmission domain. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **udp-port** *port-number* | Specifies the number of the port for receiving alarm and event traps. | The value is an integer ranging from 0 to 65535. The default value is 162. |
| **alarm-udp-port** *alarm-port-number* | Specifies the number of the port for receiving alarm traps. | The value is an integer ranging from 0 to 65535. The default value is 162. |
| **event-udp-port** *event-port-number* | Specifies the number of the port for receiving alarm and event traps. | The value is an integer ranging from 0 to 65535. The default value is 162. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, which do not contain spaces. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks (").  On a VPN network, use the VPN instance specified using vpn-instance, IP address, and security name together to identify a target host. |
| **public-net** | Indicates that the host generating a trap message is connected to a public network. | - |
| **source** | Specifies the type and number of a source interface for sending trap messages. | - |
| *interface-name* | Specifies the name of a source interface for sending Inform messages. | - |
| *interface-type* | Interface type. | - |
| *interface-number* | Specifies the number of a source interface. | - |
| **params** | Indicates the user name displayed on the NMS side.  For SNMPv1 and SNMPv2c, the NMS can receive trap messages from all target hosts without using securityname for a check. This parameter is used to distinguish multiple target hosts with the same IP address. | - |
| **securityname** *security-name* | Specifies the user security name displayed on the NMS.  For SNMPv3, securityname must be configured as the user name. securityname configured on the host must be the same as that configured on the NMS, or the NMS cannot receive the trap messages sent by the host.  For SNMPv1 and SNMPv2c, the NMS can receive trap messages from all hosts without having securityname configured. securityname is used to distinguish multiple hosts that generate trap messages. | The name is a string of 1 to 32 characters, spaces not supported.  When quotation marks are used around the string, spaces are allowed in the string. |
| **v1** | Specify security model of SNMPv1 to generate SNMP messages. | - |
| **v2c** | Specify security model of SNMPv2c to generate SNMP messages. | - |
| **v3** | Specify security model of SNMPv3 to generate SNMP messages. | - |
| **authentication** | Specifies that messages are authenticated but not encrypted. | - |
| **privacy** | Indicates that messages are authenticated and encrypted. | - |
| **ext-vb** | Indicates that trap messages sent to a target host carry extended bound variables. If alarm objects defined in public MIBs are extended on a Huawei data communication device, use.  ext-vb to determine whether the trap messages sent by the device to an NMS carry extended bound variables.   * If ext-vb is not specified, the trap message does not carry extended bound variables.   This parameter is not recommended if the NMS is a third-party NMS. This ensures tde the third-party NMS can receive trap messages from Huawei data communication devices.  By default, a trap message sent by a Huawei data communication device does not carry extended bound variables.   * If ext-vb is specified, the trap message carries extended bound variables.   This parameter is recommended if the NMS is a Huawei NMS. This allows more abundant information in trap messages. | - |
| **notify-filter-profile** *profile-name* | Specifies the notification profile name for notification filtering. | The value is a string of 1 to 32 characters without spaces.  If spaces are used, the string must start and end with double quotation marks ("). |
| **private-netmanager** | Indicates that the target host for receiving traps is a Huawei NMS. If a Huawei NMS is used and this parameter is configured, traps sent to the NMS can carry more information, including the trap type, trap sequence number, and trap sending time.  You are advised to set this parameter to enhance the reliability of alarm messages when the device is connected to a Huawei NMS. | - |
| **cipher** *cipher-name* | Specifies a password in ciphertext. You can type in the plain text or the ciphertext, and it is displayed as the ciphertext when the configuration file is viewed. | The value is a string of case-sensitive characters, spaces not supported. A simple text password is a string of 1 to 32 case-sensitive characters. A ciphertext password is a string of 32, 48, 56 or from 68 to 168 case-sensitive characters.  When quotation marks are used around the string, spaces are allowed in the string.  Ciphertext passwords with various lengths configured in an earlier version are also supported in the existing version. |
| **heart-beat** | Indicates the heartbeat . | - |
| **enable** | Enable. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

SNMP notifications can be classified into trap messages and Inform messages. Trap messages are less reliable than Inform messages because the NMS does not send any acknowledgment when it receives a trap message. In this case, the sender cannot verify whether the trap message has been received. Inform messages are configured with an acknowledgment mechanism and are therefore reliable.By default, port 162 receives trap messages, and a random port sends trap messages.

**Configuration Impact**

After the **snmp-agent target-host** command is run, no matter whether a trap message sent by the SNMP agent reaches the NMS, the SNMP agent deletes the trap message to reduce the resource consumption.After the **snmp-agent target-host inform** command is run, the SNMP agent, after sending an Inform message, waits for an Inform ACK message from the NMS and will retransmit the same Inform message only when no Inform ACK message is received from the NMS within the specified period. If the SNMP agent does not receive the Inform ACK message from the NMS during the retransmission period, the SNMP agent deletes this Inform message from the trap message queue. This ensures that the NMS can receive the SNMP trap messages to the maximum extent. The transmission of trap messages, however, consumes less resources than that of Inform messages.

**Precautions**

To enable a device to send trap messages, you must run the snmp-agent target-host and snmp-agent trap enable commands on the device.If the VPN instance specified by vpn-instance does not exist, trap messages cannot be sent.If the user security name specified by securityname does not exist, trap messages cannot be sent.

* If notify-view is not specified for the group to which the user specified by securityname belongs, trap messages cannot be sent.A maximum of 20 target hosts can be configured.

Example
-------

# Configure the SNMP agent to send trap messages that carry source interface information to the target host.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent trap enable
[*HUAWEI] snmp-agent target-host host-name 1 trap address udp-domain 10.0.0.1 source 100GE 1/0/1 params securityname 1

```

# Allow the SNMP agent to send SNMP trap messages notifications to the target host with the IP address of 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent trap enable
[*HUAWEI] snmp-agent target-host trap address udp-domain 10.1.1.1 params securityname comaccess

```

# Enable the device to send SNMP trap messages to the IPv6 address 2001:db8:1::1.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent target-host host-name aaa trap ipv6 address udp-domain 2001:db8:1::1 udp-port 5000 params securityname www

```

# Configure the SNMP agent to send trap messages to the target host and receive trap messages that are destined for Huawei NMSs and carry extended bound variables.
```
<HUAWEI> system-view
[~HUAWEI] snmp-agent trap enable
[*HUAWEI] snmp-agent target-host trap address udp-domain 10.1.1.1 params securityname public v1 ext-vb private-netmanager

```