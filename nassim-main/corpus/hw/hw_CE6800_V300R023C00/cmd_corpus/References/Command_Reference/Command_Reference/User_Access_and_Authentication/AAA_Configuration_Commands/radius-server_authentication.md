radius-server authentication
============================

radius-server authentication

Function
--------

The **radius-server authentication** command configures a RADIUS authentication server.

The **undo radius-server authentication** command deletes the configured RADIUS authentication server.

By default, no RADIUS authentication server is specified.



Format
------

**radius-server authentication** *ip-address* *port* [ **shared-key** **cipher** *share-key* | **vpn-instance** *vpn-instance-name* | **source** { *interface-type* *interface-number* | **ip-address** *source-ip-address* } | **weight** *weight-value* ] \*

**undo radius-server authentication** [ *ip-address* [ *port* [ **shared-key** | **vpn-instance** *vpn-instance-name* | **source** { *interface-type* *interface-number* | **ip-address** *source-ip-address* } | **weight** ] \* ] ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip-address** *source-ip-address* | Specifies the source IPv4 address in RADIUS packets sent from the device to a RADIUS authentication server.  If this parameter is specified, ensure that the value of this parameter is the same as the client's IPv4 address specified on the RADIUS authentication server.  If this parameter is not specified, the IPv4 address of the outbound interface is used as the source IPv4 address in RADIUS packets sent from the device to a RADIUS authentication server. | The value must be a valid unicast address in dotted decimal notation. |
| *ip-address* | Specifies the IPv4 address of a RADIUS authentication server. | The value is in dotted decimal notation and must be a valid unicast address. |
| *port* | Specifies the port number of a RADIUS authentication server. | The value is an integer ranging from 1 to 65535. |
| *share-key* | Specifies the shared key of a RADIUS server. | The value is a string of 1 to 128 case-sensitive characters in plaintext or 128 to 268 case-sensitive characters in ciphertext. The value can be letters or digits. The character string can contain spaces if it is enclosed in double quotation marks ("). |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. This parameter is supported only in the RADIUS server template view. | The value is a string of 1 to 31 case-sensitive characters. |
| **source** | Specifies the source interface or source IP address. | - |
| *interface-type* | Specifies the RADIUS server source interface. | - |
| *interface-number* | Specifies the source interface number. The value is an integer. | The value must be an existing interface number. |
| **weight** *weight-value* | Specifies the weight of a RADIUS authentication server.  When multiple servers are available, the device uses the server with the highest weight to perform authentication. If the servers have the same weights, the device uses the server configured first to perform authentication. | The value is an integer that ranges from 0 to 100. The default value is 80. |




Views
-----

RADIUS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

To perform RADIUS authentication, configure a RADIUS authentication server in a RADIUS server template. The device uses the RADIUS protocol to communicate with a RADIUS authentication server to obtain authentication information, and authenticates users based on the authentication information. The device sends authentication packets to the RADIUS authentication server only after the IP address and port number of the RADIUS authentication server are specified in the RADIUS server template.

When the
**radius-server algorithm master-backup** command has been executed to specify the master/backup algorithm on the RADIUS server and both the primary and secondary authentication servers are configured, the device sends an authentication request packet to the secondary authentication server in either of the following situations:

* The primary authentication server does not send an authentication response packet.
* The number of authentication request packet retransmissions reaches the maximum.For the RADIUS server in down state, if configuration parameters except weight of the RADIUS server are modified, the server state will change from down to up.

**Precautions**

You are advised to configure different RADIUS servers for the source VLANIF interface, source IP address, and source loopback interface and bind them to the same RADIUS template. Otherwise, the device creates multiple RADIUS servers even if the source and destination IP addresses of RADIUS request packets sent by different RADIUS templates are the same. As a result, the device finds only the first created RADIUS server after receiving RADIUS response packets, and other created RADIUS servers cannot receive RADIUS response packets. You can run the display radius-server item ip-address { ipv4-address | ipv6-address } authentication command to view the RADIUS server configuration.



Example
-------

# Configure the IP address of the secondary RADIUS authentication server to 10.163.155.15, the port number to 1812 and the weigh to 50.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template group1
[*HUAWEI-radius-group1] radius-server authentication 10.163.155.15 1812 weight 50

```

# Configure the IP address of the primary RADIUS authentication server to 10.163.155.13 and the port number to 1812.
```
<HUAWEI> system-view
[~HUAWEI] radius-server template group1
[*HUAWEI-radius-group1] radius-server authentication 10.163.155.13 1812

```