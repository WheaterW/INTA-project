source
======

source

Function
--------



The **source** command configures the source address used in TCP connection setup.

The **undo source** command restores the default setting.



By default, the device uses an outbound interface's IP address as the source IP address used in TCP connection setup.


Format
------

**source** { **interface** *interface-type* *interface-number* | *ipv4-address* | *ipv6-address* }

**source interface** *interface-name*

**undo source**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Specifies an interface's IP address as the source IP address used in TCP connection setup.   * interface-type indicates the type of the interface. * interface-number indicates the number of the interface. | - |
| *ipv4-address* | Specifies the source address used in TCP connection setup. | An IPv4 address is in dotted decimal notation, |
| *ipv6-address* | whereas an IPv6 address is in colon-separated hexadecimal notation.  The CMP session view does not support the configuration of an IPv6 address. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| *interface-name* | Specifies the name of an interface. | - |



Views
-----

PKI CMP session view,PKI domain view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When the device establishes a TCP connection with the certificate server, you are advised to run the **source** command to specify the source address used to establish the TCP connection.In a scenario with multiple outbound interfaces, when the interfaces for sending and receiving TCP packets are different, the IP address of the received TCP packet is different from that of the receiving interface. As a result, the device discards the received TCP packet, causing the TCP connection to be interrupted. In this case, you can run this command to specify the loopback interface address.

**Precautions**

If an interface is specified, ensure that the interface is a Layer 3 interface and has an IP address configured.If an interface is specified, only the primary IP address is used when the interface is configured with primary and secondary IP addresses.If an interface is specified, do not run the **ip address unnumbered** command on the interface. Otherwise, the source IP address borrowed by the interface does not take effect.


Example
-------

# Configure the IP address as the source address used in TCP connection setup.
```
<HUAWEI> system-view
[HUAWEI] interface 100GE 1/0/1
[HUAWEI-100GE1/0/1] ip address 10.136.2.25 24
[HUAWEI-100GE1/0/1] quit
[HUAWEI] pki realm abc
[HUAWEI-pki-realm-abc] source interface 100GE 1/0/1

```