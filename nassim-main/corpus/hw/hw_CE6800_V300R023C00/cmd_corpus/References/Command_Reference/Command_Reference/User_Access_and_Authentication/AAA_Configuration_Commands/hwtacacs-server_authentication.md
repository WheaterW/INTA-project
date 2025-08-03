hwtacacs-server authentication
==============================

hwtacacs-server authentication

Function
--------

The **hwtacacs-server authentication** command configures the HWTACACS authentication server.

The **undo hwtacacs-server authentication** command deletes configurations of the HWTACACS authentication server.

By default, no HWTACACS authentication server is configured.



Format
------

**hwtacacs-server authentication** *ipv4-address* [ *port* ] [ **public-net** | **vpn-instance** *vpn-instance-name* ] [ **secondary** | **third** | **fourth** ] [ **shared-key** **cipher** *cipher-string* ] [ **mux-mode** ]

**undo hwtacacs-server authentication** [ *ipv4-address* [ *port* ] [ **public-net** | **vpn-instance** *vpn-instance-name* ] [ **secondary** | **third** | **fourth** ] [ **mux-mode** ] ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of an HWTACACS authentication server. | The value is a valid unicast address in dotted decimal notation. |
| *port* | Specifies the port number of an HWTACACS authentication server. | The value is an integer that ranges from 1 to 65535. The default value is 49. |
| **public-net** | Indicates that the HWTACACS authentication server is connected to the public network. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. This parameter is supported only in the HWTACACS server template view. | The value is a string of 1 to 31 case-sensitive characters. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **secondary** | Configures the second HWTACACS authentication server as the secondary server. If no secondary HWTACACS authentication server is configured, the primary HWTACACS authentication server is specified. | - |
| **third** | Configures the third HWTACACS authentication server as the secondary server. If no secondary HWTACACS authentication server is configured, the primary HWTACACS authentication server is specified. | - |
| **fourth** | Configures the fourth HWTACACS authentication server as the secondary server. If no secondary HWTACACS accounting server is configured, the primary HWTACACS accounting server is configured. | - |
| **shared-key** | Specifies the shared key of an HWTACACS authentication server. | - |
| **cipher** *cipher-string* | Specifies the shared key of an HWTACACS authentication server. | The value is a string of 1 to 255 case-sensitive characters in plaintext or a string of 128 to 428 case-sensitive characters in ciphertext. The string can contain spaces if it is enclosed in double quotation marks ("). |
| **mux-mode** | Indicates that the HWTACACS server works in multiplexing mode. | - |




Views
-----

HWTACACS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

To authenticate users using HWTACACS, you must configure the HWTACACS authentication server. When both the primary and secondary authentication servers are configured, the device sends an authentication request packet to the secondary authentication server in any of the following situations:

* The device fails to send a request packet to the primary authentication server.
* The device does not receive any authentication response packet from the primary authentication server.
* The primary authentication server requires re-authentication.
* The primary authentication server considers that the received authentication request packet is incorrect.

**Precautions**

You can modify this configuration only when the device does not set up a TCP connection with the specified server.

The IP addresses of the primary and secondary servers must be different. Otherwise, the server configuration fails.

Example
-------

# Configure the primary HWTACACS authentication server.
```
<HUAWEI> system-view
[~HUAWEI] hwtacacs-server template test1
[*HUAWEI-hwtacacs-test1] hwtacacs-server authentication 10.163.155.12 49

```