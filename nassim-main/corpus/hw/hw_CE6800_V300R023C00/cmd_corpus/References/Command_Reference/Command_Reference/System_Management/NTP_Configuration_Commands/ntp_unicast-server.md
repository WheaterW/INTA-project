ntp unicast-server
==================

ntp unicast-server

Function
--------



The **ntp unicast-server** command configures an NTP server on a local device.

The **undo ntp unicast-server** command deletes the NTP server configuration.



By default, no NTP server is set.


Format
------

**ntp unicast-server** { *ipv4-address* [ **version** *number* | **authentication-keyid** *key-id* | **port** *port-number* | **source-interface** { *ifName* | *interface-type* *interface-number* } | **vpn-instance** *vpn-instance-name* | **preferred** | **maxpoll** *max-number* | **minpoll** *min-number* | **burst** | **iburst** | **preempt** ] \* | **ipv6** *ipv6-address* [ **authentication-keyid** *key-id* | **port** *port-number* | **source-interface** { *ifName* | *interface-type* *interface-number* } | **vpn-instance** *vpn-instance-name* | **preferred** | **maxpoll** *max-number* | **minpoll** *min-number* | **burst** | **iburst** | **preempt** ] \* | **domain** *domain-name* [ **version** *number* | **authentication-keyid** *key-id* | **port** *port-number* | **source-interface** { *ifName* | *interface-type* *interface-number* } | **vpn-instance** *vpn-instance-name* | **preferred** | **maxpoll** *max-number* | **minpoll** *min-number* | **burst** | **iburst** | **preempt** ] \* }

**undo ntp unicast-server** { *ipv4-address* | **ipv6** *ipv6-address* | **domain** *domain-name* } [ **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of a remote server. | The value is in dotted decimal notation. |
| **version** *number* | Specifies an NTP version number. | The value is an integer ranging from 1 to 4. The default value is 3. |
| **authentication-keyid** *key-id* | Specifies an authentication key number used when messages are transmitted to a remote server. | The value is an integer and ranges as: 1 to 4294967295 (version 1 to 3), or 1 to 65535 (version 4). |
| **port** *port-number* | Specifies the destination port number to transmit NTP unicast packets. | The value is 123 or an integer ranging from 1025 to 65535. The default value is 123. |
| **source-interface** *ifName* | Specify interface whose address should be used as source. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. |
| *interface-type* | Specify the interface type. | - |
| *interface-number* | Specify the interface number. | The value is a string of 1 to 47 case-sensitive characters, spaces not supported. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **preferred** | Specifies the remote server as a preferred one. By default, the remote server is not preferred. | - |
| **maxpoll** *max-number* | Specifies the maximum NTP polling interval. The value that takes effect is 2 to the power of max-number, in seconds. | The value is an integer ranging from 10 to 17, in seconds. The default value is 10. |
| **minpoll** *min-number* | Specifies the minimum NTP polling interval. The value that takes effect is 2 to the power of min-number, in seconds. | The value is an integer ranging from 3 to 6, in seconds. The default value is 6. |
| **burst** | Specifies that a burst of packets will be sent at every poll interval. This is useful to accurately measure a jitter with long poll intervals. | - |
| **iburst** | Specifies that a burst of packets will be sent when an unreachable server sends a reply. This is useful to rapidly synchronize the clock. | - |
| **preempt** | Enables the preemption mode for the server. The specified server is marked unavailable for selection if any error (authentication failure) is detected on a connection between the local device and reference clock. The server is marked available for selection if no other connections are available and no error is detected on the connection between the local device and reference clock. | - |
| **ipv6** *ipv6-address* | Specifies the IPv6 address of a remote server. The ipv6-address is a host address and cannot be a multicast address, loopback address, or IP address of a reference clock. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **domain** *domain-name* | Specifies a domain name of a remote server. | The value is a string of 1 to 255 characters, spaces not supported. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A specified remote server can be configured as the local time server. The local device works in client mode. The local client can be synchronized to the time of the remote server, and the remote server cannot be synchronized to the time of the local client.

**Precautions**

* If this command is the first NTP configuration command, the system automatically adds the ntp [ ipv6 ] server disable command to the configuration file to disable the NTP server function when you run this command. To enable the NTP server function, run the undo ntp [ ipv6 ] server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp [ ipv6 ] server disable command from the configuration file when you delete this command.
* If a VPN instance is specified for an NTP peer, the VPN instance must have been created using the **ip vpn-instance** command, and the IPv4 or IPv6 address family must have been enabled using the ipv4-family (VPN instance view) or ipv6-family (VPN instance view) command based on the IPv4 or IPv6 service configured for the NTP peer. Otherwise, the command cannot be executed successfully.
* If the source interface of the NTP peer is specified, the interface must exist. Otherwise, the command cannot be executed successfully.
* If an NTP IPv6 peer is configured and a source interface is specified, the IPv6 function must be enabled on the interface. Otherwise, the command cannot be executed.
* If both a VPN instance and a source interface are specified, the specified source interface must be bound to the specified VPN instance. Otherwise, the command cannot be executed successfully.
* If the VPN instance or source interface specified in the command is deleted, the corresponding NTP peer is deleted.
* If the IPv4 or IPv6 address family of the VPN instance specified in the command is disabled, the corresponding NTP peer is deleted.
* If a source interface is specified for an NTP IPv6 peer and the IPv6 function is disabled on the source interface, the corresponding NTP peer is deleted.

Example
-------

# Configure the local device to have time synchronized with the server whose IP address is 10.10.1.1 and version number is 3.
```
<HUAWEI> system-view
[~HUAWEI] ntp unicast-server 10.10.1.1 version 3

```

# Configure the local device to have time synchronized with a server whose VPN instance is named abc and IP address is 10.10.1.1.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance abc
[~HUAWEI-vpn-instance-abc] route-distinguisher 100:1
[*HUAWEI-vpn-instance-abc-af-ipv4] quit
[*HUAWEI-vpn-instance-abc] quit
[*HUAWEI] ntp unicast-server 10.10.1.1 vpn-instance abc

```

# Configure the server 10.10.1.1 to provide time synchronization for the local device, with the NTP version number of V3 and the port number of 5000.
```
<HUAWEI> system-view
[~HUAWEI] ntp unicast-server 10.10.1.1 version 3 port 5000

```

# Configure the server 1.1.1.1 with maxpoll 11, minpoll 4, burst, and preempt options.
```
<HUAWEI> system-view
[~HUAWEI] ntp unicast-server 1.1.1.1 burst iburst maxpoll 11 minpoll 4 preempt

```

# Configure the local device to use the IPv6 server 2001:db8::1 to provide time synchronization.
```
<HUAWEI> system-view
[~HUAWEI] ntp unicast-server ipv6 2001:db8::1

```

# Configure the local device to have time synchronized with the server whose domain name is www.example.com.
```
<HUAWEI> system-view
[~HUAWEI] ntp unicast-server domain www.example.com

```