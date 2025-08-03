peer-ip
=======

peer-ip

Function
--------



The **peer-ip/peer** command configures the IP address or domain name and TCP port number for the NMS to establish a NETCONF connection with the device, and configures the source IP address and public/private network status of the device, or the source interface of the device.

The **undo peer-ip/peer** command deletes the configuration of the IP address or domain name and TCP port number for the NMS to establish a NETCONF connection with the device, and configures the source IP address and public/private network status of the device, or the source interface of the device.



By default, no IP address, domain name, or TCP port number is configured for the NMS to establish a NETCONF connection with a device, and no source IP address, source interface, or public/private network status is configured for the device.


Format
------

{ **peer-ip** *ip-address* | **peer** { *peerName* **ipv6** | *peerName* } } **port** *port-number* { [ [ **local-address** *source-ip* ] | [ **vpn-instance** *vpn-instance* | **public-net** ] ] \* | [ **source-interface** { *interface-name* | *interface-type* *interface-num* } ] }

**undo** { **peer-ip** *ip-address* | **peer** [ *peerName* **ipv6** | *peerName* ] }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IP address of an NMS. | IPv4 address: The value is in dotted decimal notation.  IPv6 address: The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *peerName* | Specifies the domain name of an NMS. | The value is a string of 1 to 255 case-sensitive characters. It cannot contain spaces. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **ipv6** | Specifies to use IPv6. By default, IPv4 is used. | - |
| **port** *port-number* | Specifies the TCP port number of an NMS. | The value is an integer ranging from 1 to 65535. |
| **local-address** *source-ip* | Specifies the source IP address of a device to be connected with an NMS. | IPv4 address: The value is in dotted decimal notation.  IPv6 address: The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **vpn-instance** *vpn-instance* | Specifies the VPN instance name of a NETCONF connection. | The value is a string of 1 to 31 case-sensitive characters, spaces not supported. In addition, the VPN instance name must not be \_public\_. When double quotation marks are used around the string, spaces are allowed in the string. |
| **public-net** | Establish a NETCONF connection on a public network. | - |
| **source-interface** *interface-name* | Specifies the name of the source interface connected to the NMS. | - |
| **source-interface** *interface-type* *interface-num* | Specifies the type and number of the source interface connected to the NMS. | - |



Views
-----

Endpoint view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

If an NMS does not support automatic device discovery, it cannot manage devices in time. To address this problem, you can configure proactive NETCONF registration for a device to send a NETCONF connection request to the NMS when the device goes online so that the NMS can manage the device.When configuring proactive NETCONF registration, you need to configure the IP address and TCP port number for the NMS with which the device is to establish a NETCONF connection using the peer-ip/peer command in the NETCONF connection instance view.

**Prerequisites**

A logical interface has been created before you specify it as the source interface of a callhome connection. Otherwise, the command cannot be executed.

**Precautions**

A device can establish NETCONF connections with only one NMS, and port-number must be the same as that used on the NMS to establish the NETCONF connection.If you run the command without carrying the vpn-instance or public-net parameter, the network to which the NETCONF connection belongs is the same as the network configured using the set net-manager [ ipv6 ] vpn-instance vpn-instance-name command.


Example
-------

# Set the hostname and TCP port number of the NMS with which the device is to establish a NETCONF connection to huawei.com and 8090, respectively.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] callhome root
[*HUAWEI-netconf-callhome-root] endpoint huawei
[*HUAWEI-netconf-callhome-root-endpoint-huawei] peer huawei.com port 8090

```

# Set the domain name to huawei.com, type to IPv6, TCP port number to 8090, source IPv6 address to 2001:db8:1::2, and VPN instance name to vpn1 for the NMS that sets up a NETCONF connection with the device.
```
<HUAWEI> system-view
[~HUAWEI] netconf
[~HUAWEI-netconf] callhome root
[*HUAWEI-netconf-callhome-root] endpoint huawei
[*HUAWEI-netconf-callhome-root-endpoint-huawei] peer huawei.com ipv6 port 8090 local-address 2001:db8:1::2 vpn-instance vpn1

```