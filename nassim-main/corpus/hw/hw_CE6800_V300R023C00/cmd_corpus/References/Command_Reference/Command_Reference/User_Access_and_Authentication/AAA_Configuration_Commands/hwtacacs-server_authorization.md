hwtacacs-server authorization
=============================

hwtacacs-server authorization

Function
--------

The **hwtacacs-server authorization** command configures the HWTACACS authorization server.

The **undo hwtacacs-server authorization** command deletes configurations of the HWTACACS authorization server.

By default, no HWTACACS authorization server is configured.



Format
------

**hwtacacs-server authorization** *ipv4-address* [ *port* ] [ **public-net** | **vpn-instance** *vpn-instance-name* ] [ **secondary** | **third** | **fourth** ] [ **shared-key** **cipher** *cipher-string* ] [ **mux-mode** ]

**undo hwtacacs-server authorization** [ *ipv4-address* [ *port* ] [ **public-net** | **vpn-instance** *vpn-instance-name* ] [ **secondary** | **third** | **fourth** ] [ **mux-mode** ] ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of an HWTACACS authorization server. | The value is in dotted decimal notation. The value must be a valid unicast address. |
| *port* | Specifies the port number of the HWTACACS authorization server. | The value is an integer that ranges from 1 to 65535. The default port number is 49. |
| **public-net** | Indicates that the HWTACACS authorization server is connected to the public network. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. This parameter is supported only in the HWTACACS server template view. | The value is a string of 1 to 31 case-sensitive characters. |
| **secondary** | Configures the second HWTACACS authorization server as the secondary server. If no secondary HWTACACS authorization server is configured, the primary HWTACACS authorization server is specified. | - |
| **third** | Configures the third HWTACACS authorization server as the secondary server. If no secondary HWTACACS authorization server is configured, the primary HWTACACS authorization server is specified. | - |
| **fourth** | Configures the fourth HWTACACS authentication server as the secondary server. If no secondary HWTACACS accounting server is configured, the primary HWTACACS accounting server is configured. | - |
| **shared-key** | Specifies the shared key of the HWTACACS authorization server. | - |
| **cipher** *cipher-string* | Specifies the shared key of the HWTACACS authorization server. | The value is a string of 1 to 255 case-sensitive characters in plaintext or a string of 128 to 428 case-sensitive characters in ciphertext. The string can contain spaces if it is enclosed in double quotation marks ("). |
| **mux-mode** | Indicates that the HWTACACS server works in multiplex mode. | - |




Views
-----

HWTACACS server template view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

To authorize users in HWTACACS mode, you must configure the HWTACACS authorization server.

**Precautions**

You can modify this configuration only when the device does not set up a TCP connection with the specified server.

The IP addresses of the primary and secondary servers must be different. Otherwise, the server configuration fails.

Example
-------

# Configure the primary HWTACACS authorization server.
```
<HUAWEI> system-view
[~HUAWEI] hwtacacs-server template test1
[*HUAWEI-hwtacacs-test1] hwtacacs-server authorization 10.163.155.12 49

```