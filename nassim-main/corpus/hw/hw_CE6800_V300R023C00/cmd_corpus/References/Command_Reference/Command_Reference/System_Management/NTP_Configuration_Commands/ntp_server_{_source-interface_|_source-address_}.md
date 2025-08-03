ntp server { source-interface | source-address }
================================================

ntp server { source-interface | source-address }

Function
--------



The **ntp server source-interface** command configures a listening interface for an NTP IPv4 server.

The **undo ntp server source-interface** command cancels the listening interface of the NTP IPv4 server.

The **ntp ipv6 server source-address** command configures a listening address for an NTP IPv6 server.

The **undo ntp ipv6 server source-address** command deletes the listening IP address of the NTP IPv6 server.



By default, the NTP server does not listen to any interface.


Format
------

**ntp server source-interface** { *interface-name* | *interface-type* *interface-number* }

**ntp ipv6 server source-address** *ipv6Addr* [ **vpn-instance** *vpnName* ]

**ntp server physic-isolate source-interface** { *interface-name* | *interface-type* *interface-number* } **source-address** *ipv4Addr*

**ntp ipv6 server physic-isolate source-interface** { *interface-name* | *interface-type* *interface-number* } **source-address** *ipv6Addr*

**undo ntp server source-interface** { *interface-name* | *interface-type* *interface-number* }

**undo ntp ipv6 server source-address** *ipv6Addr* [ **vpn-instance** *vpnName* ]

**undo ntp server physic-isolate source-interface** { *interface-name* | *interface-type* *interface-number* } **source-address** *ipv4Addr*

**undo ntp ipv6 server physic-isolate source-interface** { *interface-name* | *interface-type* *interface-number* } **source-address** *ipv6Addr*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interface-name* | Specifies the type and number of a local interface that receives NTP packets. | The value is a string of 1 to 47 case-sensitive characters. It cannot contain spaces. |
| *interface-type* | Specifies the type and number of a local interface that receives NTP packets. | The value is a string of 1 to 47 case-sensitive characters. It cannot contain spaces. |
| *interface-number* | Specifies the type and number of a local interface that receives NTP packets. | The value is a string of 1 to 47 case-sensitive characters. It cannot contain spaces. |
| **source-address** *ipv6Addr* | Specifies the IPv6 address that the server listens to. The ipv6-address is a host address and cannot be a multicast address, loopback address, or IP address of a reference clock. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **source-address** *ipv4Addr* | Specifies the IPv4 address listened by the server. ipv4-address is a host address and cannot be a multicast address, loopback address, or reference clock address. | The value is an IPv4 address in dotted decimal notation. |
| **vpn-instance** *vpnName* | Specifies the VPN instance name. | The value is a string of 1 to 31 case-sensitive characters. It cannot be \_public\_. If spaces are used, the string must be enclosed in double quotation marks (" "). |
| **physic-isolate** | Set the isolation attribute of an NTP server interface. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

If you want the NTP server to listen to the packets from a specified interface and IP address, you can specify the interface as the source interface of the NTP server. After this interface is specified, the host can receive only the NTP packets from this interface.

**Precautions**

* If this command is the first NTP configuration command, the system automatically adds the ntp [ ipv6 ] server disable command to the configuration file to disable the NTP server function. To enable the NTP service, run the undo ntp [ ipv6 ] server disable command. If this command is the last NTP configuration command to be deleted, the system automatically deletes the ntp [ ipv6 ] server disable command from the configuration file.
* If an NTP IPv6 source address is specified in a VPN instance, the VPN instance must have been created using the **ip vpn-instance** command and the IPv6 address family must have been enabled using the ipv6-family (VPN instance view) command. Otherwise, the command fails to be executed.
* If an NTP IPv4 source interface is specified, the interface must exist. Otherwise, the command fails to be executed.
* If the VPN instance or source interface specified in the command is deleted, the configuration of the corresponding NTP server source interface is also deleted.
* To enhance system security, the NTP server does not process packets received by any interface or address by default. You can run this command on the NTP server to specify the source interface of the NTP server. The interface and address verification is added. Only the packets from the trusted source specified by the user are received and processed.
* After the IPv4 source interface of the NTP server is specified, the NTP server uses only the primary IP address of the interface as the trusted source address and does not process packets whose destination address is a sub-IP address.
* If the ntp [ipv6] server source-interface all enable, ntp server source-interface, and ntp ipv6 server source-address commands are configured, the ntp [ipv6] server source-interface all enable command takes effect. The server receives and processes the packets received by all interfaces and addresses.


Example
-------

# Configure the NTP server to listen to NTP packets sent from the interface with the IPv6 address 2001:db8:1::1.
```
<HUAWEI> system-view
[~HUAWEI] ntp ipv6 server source-address 2001:db8:1::1

```

# Configure the NTP server to listen to the packets sent from vlanif 100.
```
<HUAWEI> system-view
[~HUAWEI] vlan batch 100
[~HUAWEI] interface Vlanif 100
[~HUAWEI-Vlanif100] quit
[*HUAWEI] ntp server source-interface Vlanif 100

```

# Configure the NTP server to listen to the packets received from VLANIF 100 and destined for 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] vlan batch 100
[~HUAWEI] interface Vlanif 100
[~HUAWEI-Vlanif100] quit
[*HUAWEI] ntp server physic-isolate source-interface Vlanif 100 source-address 10.1.1.1

```

# Configure the NTP server to listen to the packets received from VLANIF 100 and destined for 2001:db8:2::1.
```
<HUAWEI> system-view
[~HUAWEI] vlan batch 100
[~HUAWEI] interface Vlanif 100
[~HUAWEI-Vlanif100] quit
[*HUAWEI] ntp ipv6 server physic-isolate source-interface Vlanif 100 source-address 2001:db8:2::1

```