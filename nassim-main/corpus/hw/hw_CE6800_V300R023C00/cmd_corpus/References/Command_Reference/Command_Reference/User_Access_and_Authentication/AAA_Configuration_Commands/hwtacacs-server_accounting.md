hwtacacs-server accounting
==========================

hwtacacs-server accounting

Function
--------

The **hwtacacs-server accounting** command configures an HWTACACS accounting server.

The **undo hwtacacs-server accounting** command cancels the configuration.

By default, no HWTACACS accounting server is configured.



Format
------

**hwtacacs-server accounting** *ipv4-address* [ *port* ] [ **public-net** | **vpn-instance** *vpn-instance-name* ] [ **secondary** | **third** | **fourth** ] [ **shared-key** **cipher** *cipher-string* ] [ **mux-mode** ]

**undo hwtacacs-server accounting** [ *ipv4-address* [ *port* ] [ **public-net** | **vpn-instance** *vpn-instance-name* ] [ **secondary** | **third** | **fourth** ] [ **mux-mode** ] ]



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ipv4-address* | Specifies the IPv4 address of an HWTACACS accounting server. | The value is a valid unicast address in dotted decimal notation. |
| *port* | Specifies the port number of an HWTACACS accounting server. | The value is an integer that ranges from 1 to 65535. The default value is 49. |
| **public-net** | Indicates that the HWTACACS accounting server is connected to the public network. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. This parameter is supported only in the HWTACACS server template view. | The value is a string of 1 to 31 case-sensitive characters. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **secondary** | Configures the second HWTACACS accounting server as the secondary server. If no secondary server is configured, the primary HWTACACS accounting server is specified. | - |
| **third** | Specifies the third HWTACACS accounting server as the secondary server. If no secondary server is configured, the primary HWTACACS accounting server is specified. | - |
| **fourth** | Configures the fourth HWTACACS authentication server as the secondary server. If no secondary HWTACACS accounting server is configured, the primary HWTACACS accounting server is configured. | - |
| **shared-key** | Specifies the shared key of an HWTACACS accounting server. | - |
| **cipher** *cipher-string* | Specifies the shared key of an HWTACACS accounting server. | The value is a string of 1 to 255 case-sensitive characters in plaintext or a string of 128 to 428 case-sensitive characters in ciphertext. The string can contain spaces if it is enclosed in double quotation marks ("). |
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

The device does not support local accounting; therefore, you need to configure an HWTACACS accounting server to perform accounting. The device sends accounting packets to an HWTACACS accounting server only after the accounting server is specified in an HWTACACS server template.

**Precautions**

You can modify this configuration only when the device does not set up a TCP connection with the specified server.

The IP addresses of the primary and secondary servers must be different. Otherwise, the server configuration fails.

Example
-------

# Configure the primary HWTACACS accounting server.
```
<HUAWEI> system-view
[~HUAWEI] hwtacacs-server template test1
[*HUAWEI-hwtacacs-test1] hwtacacs-server accounting 10.163.155.12 52

```