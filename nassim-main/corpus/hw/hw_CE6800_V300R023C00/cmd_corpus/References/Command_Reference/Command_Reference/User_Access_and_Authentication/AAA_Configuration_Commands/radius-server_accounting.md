radius-server accounting
========================

radius-server accounting

Function
--------

The **radius-server accounting** command configures the RADIUS accounting server.

The **undo radius-server accounting** command deletes the configuration.

By default, no RADIUS accounting server is configured.



Format
------

**radius-server accounting** *ip-address* *port* [ **shared-key** **cipher** *share-key* | **vpn-instance** *vpn-instance-name* | **source** { *interface-type* *interface-number* | **ip-address** *source-ip-address* } | **weight** *weight-value* ] \*

**undo radius-server accounting** [ *ip-address* [ *port* [ **shared-key** | **vpn-instance** *vpn-instance-name* | **source** { *interface-type* *interface-number* | **ip-address** *source-ip-address* } | **weight** ] \* ] ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip-address** *source-ip-address* | Specifies the source IPv4 address in RADIUS packets sent from the device to a RADIUS accounting server.  If this parameter is specified, ensure that the value of this parameter is the same as the client's IPv4 address specified on the RADIUS accounting server.  If this parameter is not specified, the IPv4 address of the outbound interface is used as the source IPv4 address in RADIUS packets sent from the device to a RADIUS accounting server. | The value must be a valid unicast address in dotted decimal notation. |
| *ip-address* | Specifies the IPv4 address of a RADIUS accounting server. | The value is in dotted decimal notation and must be a valid unicast address. |
| *port* | Specifies the port number of a server. | The value is an integer ranging from 1 to 65535. |
| *share-key* | Specifies the shared key of a RADIUS server. | The value is a string of 1 to 128 case-sensitive characters in plaintext or 128 to 268 case-sensitive characters in ciphertext. The value can be letters or digits. The character string can contain spaces if it is enclosed in double quotation marks ("). |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. This parameter is supported only in the RADIUS server template view. | The VPN instance name must exist. |
| **source** | Specifies the source interface or source IP address. | - |
| *interface-type* | Specifies the RADIUS server source interface. | - |
| *interface-number* | Specifies the source interface number. The value is an integer. | - |
| **weight** *weight-value* | Specifies the weight of a RADIUS accounting server.  When multiple servers are available, the device uses the server with the highest weight to perform accounting. If the servers have the same weights, the device uses the server configured first to perform accounting. | The value is an integer ranging from 0 to 100. |




Views
-----

RADIUS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

To perform accounting for users, configure a RADIUS accounting server. The device communicates with a RADIUS accounting server to obtain accounting information, and performs accounting for users based on the accounting information. The device sends accounting packets to the RADIUS accounting server only after the IP address and port number of the RADIUS accounting server are specified in the RADIUS server template.

**Precautions**

The IP address of the primary accounting server must be different from the IP address of the secondary accounting server; otherwise, the configuration fails. For the RADIUS server in down state, if configuration parameters except weight of the RADIUS server are modified, the server state will change from down to up.



Example
-------

# Configure the secondary RADIUS accounting server.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template group1
[*HUAWEI-radius-group1] radius-server accounting 10.163.155.15 1813 weight 50

```

# Configure the primary RADIUS accounting server.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template group1
[*HUAWEI-radius-group1] radius-server accounting 10.163.155.12 1813

```