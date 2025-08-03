cut access-user
===============

cut access-user

Function
--------

The **cut access-user** command terminates one or multiple access user connections, that is, disconnecting online users.



Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**cut access-user** { **domain** *domain-name* | **ip-address** *ip-address* [ **vpn-instance** *vpn-instance-name* ] | **ipv6-address** *ipv6-address* | **service-scheme** *service-scheme-name* | **user-id** *begin-number* [ *end-number* ] | **username** *user-name* }

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**cut access-user access-type** { **admin** [ **ftp** | **ssh** | **telnet** | **terminal** | **http** ] } [ **username** *user-name* ]

**cut access-user access-type** { **admin** [ **ftp** | **ssh** | **telnet** | **terminal** | **http** | **md-cli** | **snmp** ] } [ **username** *user-name* ]

**cut access-user authentication-mode** { **all** | **hwtacacs** | **local** | **radius** | **ldap** }

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**cut access-user** { **mac-address** *mac-address* | **access-slot** *slot-number* }

**cut access-user interface** { *interface-name* | *interface-type* *interface-number* } [ **vlan** *vlan-id* ]

**cut access-user mac-address** *mac-address*

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6885-LL (low latency mode):

**cut access-user** { **domain** *domain-name* | **ip-address** *ip-address* | **service-scheme** *service-scheme-name* | **user-id** *begin-number* [ *end-number* ] | **username** *user-name* }



Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Indicates all authentication modes. | - |
| **hwtacacs** | Indicates the HWTACACS authentication mode. | - |
| **local** | Indicates the local authentication mode. | - |
| **radius** | Indicates the RADIUS authentication mode. | - |
| **authentication-mode** | Indicates the user authentication mode. | - |
| **ldap** | Indicates the LDAP authentication mode. | - |
| **domain** *domain-name* | Disconnects sessions in a specified domain. | The domain must already exist. |
| **ip-address** *ip-address* | Disconnects sessions initiated by a specified IP address. | The value is in dotted decimal notation. |
| **vpn-instance** *vpn-instance-name* | Indicates the name of a VPN instance to which the specified IP address belongs.     NOTE:   This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a string of 1 to 31 case-sensitive characters without spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **ipv6-address** *ipv6-address* | Displays information about the user with a specified IPv6 address.     NOTE:   This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number in the format X:X:X:X:X:X:X:X. |
| **service-scheme** *service-scheme-name* | Terminates connections based on the service scheme. | The value is a string of 1 to 32 case-sensitive characters. It cannot contain spaces. |
| **user-id** *begin-number* | Specifies the start ID of the session to be disconnected. | The user-id must exist on the device. |
| *end-number* | Specifies the end ID of the session to be disconnected. | The user-id must exist on the device. |
| **username** *user-name* | Displays information about the users using the specified authentication mode. | The value is a string of 1 to 253 case-sensitive characters. |
| **access-type** | Indicates the user access type. | - |
| **admin** | Indicates information about the administrators using the specified authentication mode. | - |
| **ftp** | Indicates FTP users. | - |
| **ssh** | Indicates SSH users. | - |
| **telnet** | Indicates Telnet users. | - |
| **terminal** | Indicates terminal users. | - |
| **http** | Indicates HTTP authentication users. | - |
| **md-cli** | Indicates MD-CLI users. | - |
| **snmp** | Indicates SNMP users. | - |
| **mac-address** *mac-address* | Disconnects sessions initiated by a specified MAC address.     NOTE:   This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | The value is in the format of H-H-H, in which each H is a hexadecimal number of 1 to 4 digits, such as 00e0 and fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. The MAC address cannot be set to FFFF-FFFF-FFFF. |
| **access-slot** *slot-number* | Specifies a slot ID.     NOTE:   This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | The value is an integer. |
| *interface-name* | Displays 802.1X authentication information of a specified interface.     NOTE:   This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | The value is a string of 1 to 255 case-sensitive characters. It cannot contain spaces. |
| *interface-type* | Specifies an interface name.     NOTE:   This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |
| *interface-number* | Specifies the source interface number.     NOTE:   This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |
| **vlan** *vlan-id* | Indicates the user VLAN.     NOTE:   This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | The value is an integer ranging from 1 to 4094. |




Views
-----

AAA view



Default Level
-------------

3: Management level



Usage Guidelines
----------------

**Usage Scenario**

Performing some configurations, such as AAA, on the device, requires that no users be online. You can run the **cut access-user** command to disconnect sessions.

**Precautions**

The **cut access-user** command interrupts all services of the user whose session is torn down. If the character string of the user name contains spaces (for example, a b), you can run the display access-user username "a b" command to view online users.If the character string of the user name contains spaces and quotation marks ("") simultaneously, you cannot use the user name to view online users. In this case, you can run the display access-user | include username command to view the user ID of the online user, and then run the display access-user user-id user-id command to view the user. Alternatively, you can run the cut access-user user-id user-id command to log out the user.



Example
-------

# Tear down the session initiated by the IP address 10.1.1.1.
```
<HUAWEI> system-view
[~HUAWEI] aaa
[~HUAWEI-aaa] cut access-user ip-address 10.1.1.1

```