radius-server authorization
===========================

radius-server authorization

Function
--------

The **radius-server authorization** command configures the RADIUS authorization server.

The **undo radius-server authorization** command deletes the configured RADIUS authorization server.

By default, no RADIUS authorization server is configured.



Format
------

**radius-server authorization** *ip-address* [ **vpn-instance** *vpn-instance-name* ] { **server-group** *group-name* **shared-key** **cipher** *key-string* | **shared-key** **cipher** *key-string* [ **server-group** *group-name* ] } [ **protect** **enable** ]

**undo radius-server authorization** { **all** | *ip-address* [ **vpn-instance** *vpn-instance-name* ] }



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies the IP address of a RADIUS authorization server. | The value is a unicast address in dotted decimal notation. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. This parameter is supported only in the RADIUS server template view. | The value must be an existing VPN instance name. |
| **server-group** *group-name* | Specifies the name of a RADIUS group corresponding to a RADIUS server template. | The value is a string of 1 to 32 characters, including letters (case-sensitive), digits (0 to 9), periods (.), hyphens (-), and underscores (\_). The value cannot be - or --. |
| **shared-key** | Specifies the shared key. | - |
| **cipher** *key-string* | Specifies the shared key of a RADIUS server. | The value is a string of 1 to 128 case-sensitive characters in plaintext or a string of 128 to 268 case-sensitive characters in ciphertext. The string can contain spaces if it is enclosed in double quotation marks ("). |
| **protect** | Indicates the security hardening function. | - |
| **enable** | Enables the security hardening function. | - |
| **all** | Deletes all RADIUS authorization servers. | - |




Views
-----

System view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

To better control user rights, the RADIUS protocol supports authorization of online users through an independent RADIUS authorization server. RADIUS provides two authorization methods: Change of Authorization (CoA) and Disconnect Message (DM).

* CoA: After a user is successfully authenticated, you can modify the rights of the online user through the RADIUS authorization server. For example, a VLAN ID can be delivered to access users of a certain department through CoA packets, so that they belong to the same VLAN no matter which interfaces they connect to.
* DM: The administrator can actively disconnect a user through the RADIUS authorization server.After the parameters such as IP address and shared key are configured for the RADIUS authorization server, the device can receive authorization requests from the server and grant rights to users according to the authorization information. After authorization is complete, the device returns authorization response packets carrying the results to the server.After the security hardening function is enabled by specifying the protect enable parameter:
* When a CoA or DM request packet carries the Message-Authenticator attribute, the device checks the attribute. If the check fails, the device discards the request packet and does not respond to the packet. If the check succeeds, the device sends a CoA or DM response packet (ACK or NAK) that carries the Message-Authenticator attribute.
* When a CoA or DM request packet does not carry the Message-Authenticator attribute, the device does not check the attribute and sends a CoA or DM response packet (ACK or NAK) that does not carry the Message-Authenticator attribute.NOTE:When a CoA or DM request packet carries the Message-Authenticator attribute, if the **radius-attribute disable message-authenticator receive** command is configured, the device does not check the attribute and sends a response packet that does not carry the Message-Authenticator attribute; if the **radius-attribute disable message-authenticator send** command is configured, the device sends a response packet that does not carry the Message-Authenticator attribute even if the attribute check succeeds.

**Precautions**

To improve security, it is recommended that the password contains at least three types of lowercase letters, uppercase letters, digits, and special characters, and contains at least 16 characters.

To implement this function, the
**radius local-ip** command must be used to configure a local IP address of the UDP socket with the local port number in the range of 1024-55535.

Example
-------

# Specify a RADIUS authorization server.
```
<HUAWEI> system-view
[~HUAWEI] radius-server authorization 10.1.1.116 shared-key cipher YsHsjx_202206YsHsjx_202206

```