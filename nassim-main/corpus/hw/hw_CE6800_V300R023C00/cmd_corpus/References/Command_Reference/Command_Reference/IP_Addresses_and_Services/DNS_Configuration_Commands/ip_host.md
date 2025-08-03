ip host
=======

ip host

Function
--------



The **ip host** command configures static DNS entries.

The **undo ip host** command deletes static DNS entries.



By default, no static DNS entries are configured.


Format
------

**ip host** *host-name* *ip-address* [ **vpn-instance** *vpn-instance-name* ]

**undo ip host** *host-name* [ *ip-address* [ **vpn-instance** *vpn-instance-name* ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *host-name* | Specifies the host name. | The value is a string of 1 to 255 case-sensitive characters without spaces. The value can contain digits, letters, underscores (\_), periods (.), and hyphens (-), and must contain letters. Each level of domain name can contain a maximum of 63 characters. |
| *ip-address* | Specifies the IP address mapping the host name. | The value is in dotted decimal notation. |
| **vpn-instance** *vpn-instance-name* | Specifies the name of the VPN instance to which the IP address corresponding to a domain name belongs. | The value is a string of 1 to 31 case-sensitive characters. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

A static domain name resolution table is manually set up using the **ip host** command, describing the mappings between host names and IP addresses. In addition, some common host names are added to the table. Then, static host name resolution can be performed according to the static domain name resolution table. When requiring the IP address corresponding to a host name, the client firstly searches the static host name resolution table for the specified host name and obtains the corresponding IP address. In this manner, the efficiency of host name resolution is improved.

**Precautions**

1. You can run the **ip host** command to configure a maximum of 50 static DNS entries. Each host has only one IP address. When multiple IP addresses are assigned to a host, the latest configured IP address overrides the previous ones.
2. A domain name at each level can contain a maximum of 63 characters.
3. The address specified by ip host can be configured as long as it complies with the IPv4 address format, including some special addresses such as 0.0.0.0 and 127.0.0.1. Users can determine how to use these addresses.

Example
-------

# Set the IP address corresponding to the host name test in vpn1 to 10.110.0.2.
```
<HUAWEI> system-view
[~HUAWEI] ip vpn-instance vpn1
[*HUAWEI-vpn-instance-vpn1] ipv4-family
[*HUAWEI-vpn-instance-vpn1-af-ipv4] quit
[*HUAWEI-vpn-instance-vpn1] quit
[*HUAWEI] ip host test 10.110.0.2 vpn-instance vpn1

```

# Configure the IP address 10.110.0.1 for the host test.
```
<HUAWEI> system-view
[~HUAWEI] ip host test 10.110.0.1

```