ntp unicast-peer
================

ntp unicast-peer

Function
--------



The **ntp unicast-peer** command configures the NTP peer mode.

The **undo ntp unicast-peer** command cancels the NTP peer mode.



By default, no NTP peer or NTP server is configured.


Format
------

**ntp unicast-peer** { *ipv4Addr* [ **version** *number* | **port** *port-number* | **authentication-keyid** *key-id* | **source-interface** { *ifName* | *interface-type* *interface-number* } | **vpn-instance** *vpn-instance-name* | **preferred** | **maxpoll** *max-number* | **minpoll** *min-number* | **preempt** ] \* | **ipv6** *ipv6Addr* [ **authentication-keyid** *key-id* | **port** *port-number* | **source-interface** { *ifName* | *interface-type* *interface-number* } | **vpn-instance** *vpn-instance-name* | **preferred** | **maxpoll** *max-number* | **minpoll** *min-number* | **preempt** ] \* | **domain** *domain-name* [ **version** *number* | **port** *port-number* | **authentication-keyid** *key-id* | **source-interface** { *ifName* | *interface-type* *interface-number* } | **vpn-instance** *vpn-instance-name* | **preferred** | **maxpoll** *max-number* | **minpoll** *min-number* | **preempt** ] \* }

**undo ntp unicast-peer** { *ipv4Addr* | **ipv6** *ipv6Addr* | **domain** *domain-name* } [ **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4Addr* | Specifies the IPv4 address of a remote server. | The value is an IPv4 address in dotted decimal notation. |
| **version** *number* | Specifies the NTP version number. | The value is an integer ranging from 1 to 4. The default value is 3. |
| **port** *port-number* | Specifies the destination port of NTP unicast packets. | The value is 123 or an integer ranging from 1025 to 65535. The default value is 123. |
| **authentication-keyid** *key-id* | Specifies the authentication key ID used when transmitting messages to the remote peer. | The value is an integer ranging from   * 1â4294967295 (versions 1 to 3) * 1â65535 (version 4) |
| **source-interface** *ifName* | Specifies the source interface. | The value is a string of 1 to 47 case-sensitive characters. It cannot contain spaces. |
| *interface-type* | Specifies the type of an interface. | - |
| *interface-number* | Specifies an interface number. | The value is a string of 1 to 47 case-sensitive characters. It cannot contain spaces. |
| **vpn-instance** *vpn-instance-name* | Specifies the VPN instance name. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **maxpoll** *max-number* | Specifies the maximum NTP polling interval. The polling interval is the nth power of 2, in seconds. For example, if maxpoll is set to 11, the maximum polling interval is 2048 seconds. | The value is an integer ranging from 10 to 17, in seconds. The default value is 10. |
| **minpoll** *min-number* | Specifies the minimum NTP polling interval. The polling interval is the nth power of 2, in seconds. For example, if minpoll is set to 5, the minimum polling interval is 32 seconds. | The value is an integer ranging from 3 to 6, in seconds. The default value is 6. |
| **preempt** | Specifies that a peer can be preempted. | - |
| **ipv6** *ipv6Addr* | Indicates the IPv6 address of the remote server. ipv6-address is a host address and cannot be a multicast address, loopback address, or reference clock address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **preferred** | Specifies the remote server as the preferred one. By default, the remote server is not preferred. | - |
| **domain** *domain-name* | Specifies a domain name. | The value is a string of 1 to 255 characters. It cannot contain spaces. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A remote node with a specified IP address or NEID can be configured as the peer of a local device. The local device runs in the symmetric active mode. The local and remote devices can be synchronized to each other.

**Configuration Impact**

If a key ID is configured using NTPv1, authentication may fail because of non-standard NTPv1 authentication.

**Precautions**

* If this command is the first NTP configuration command, the system automatically adds the ntp [ ipv6 ] server disable command to the configuration file to disable the NTP service. To enable the NTP service, run the undo ntp [ ipv6 ] server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp [ ipv6 ] server disable command from the configuration file when you delete this command.
* If a VPN instance is specified for the NTP peer, the instance must have been created using the **ip vpn-instance** command, and the corresponding address family must have been enabled using the ipv4-family (VPN instance view) or ipv6-family (VPN instance view) command based on the IPv4 or IPv6 service configured for the NTP peer. Otherwise, this command fails to be executed.
* If a source interface is specified for the NTP peer, the interface must exist. Otherwise, this command fails to be executed.
* If an NTP IPv6 peer is configured and a source interface is specified, IPv6 must be enabled on the interface. Otherwise, this command fails to be executed.
* If both the VPN instance and source interface are specified, the source interface must be bound to the VPN instance. Otherwise, this command fails to be executed.
* If the VPN instance or source interface specified in the command is deleted, the corresponding NTP peer is also deleted.
* If the IPv4 or IPv6 address family of the VPN instance specified in the command is disabled, the corresponding NTP peer is deleted.
* If a source interface is specified for the NTP IPv6 peer and the IPv6 function is disabled on the source interface, the corresponding NTP peer is deleted.
* If the preference field is specified in this command, the clock source configured with the preference field is selected as the synchronization clock source of the device only when the following conditions are met: (1) The **display ntp sessions** command output shows that the clock status of the clock source contains the selected field. (2) The **display ntp sessions** command output shows that the clock stratum value of any clock source that contains the selected field is not smaller than that of this clock source.


Example
-------

# Configure the IPv6 peer 2001:db8::1 to provide the synchronization time for the local device. The local peer can also provide the synchronization time for the peer. The IP address of the NTP packet is obtained from Vlanif 100.
```
<HUAWEI> system-view
[~HUAWEI] vlan batch 100
[~HUAWEI] interface Vlanif 100
[~HUAWEI-Vlanif100] ipv6 enable
[~HUAWEI-Vlanif100] quit
[~HUAWEI] ntp unicast-peer ipv6 2001:db8::1 source-interface Vlanif 100

```

# Configure the remote node with the domain name www.example.com as the peer of the local device.
```
<HUAWEI> system-view
[~HUAWEI] ntp unicast-peer domain www.example.com

```

# Configure the peer 10.10.1.1 to provide the synchronizing time for the local device. The local device can also provide synchronizing time for the peer. Set the version number to 3.
```
<HUAWEI> system-view
[~HUAWEI] ntp unicast-peer 10.10.1.1 version 3

```