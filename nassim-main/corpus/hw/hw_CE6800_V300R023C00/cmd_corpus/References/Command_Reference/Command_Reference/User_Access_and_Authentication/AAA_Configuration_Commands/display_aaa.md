display aaa
===========

display aaa

Function
--------



The **display aaa** command displays information about normal logout, abnormal logout, and login failures.




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display aaa** { **offline-record** | **abnormal-offline-record** | **online-fail-record** } { **all** | **reverse-order** | **domain** *domain-name* | **ip-address** *ip-address* [ **vpn-instance** *vpn-instance-name* ] | **ipv6-address** *ipv6-address* | **time** *start-time* *end-time* [ **date** *start-date* *end-date* ] | **username** *user-name* [ **time** *start-time* *end-time* [ **date** *start-date* *end-date* ] ] } [ **brief** ]

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**display aaa** { **offline-record** | **abnormal-offline-record** | **online-fail-record** } { **all** | **reverse-order** | **access-slot** *slot-number* | **domain** *domain-name* | **ip-address** *ip-address* [ **vpn-instance** *vpn-instance-name* ] | **ipv6-address** *ipv6-address* | **mac-address** *mac-address* | **time** *start-time* *end-time* [ **date** *start-date* *end-date* ] | **username** *user-name* [ **time** *start-time* *end-time* [ **date** *start-date* *end-date* ] ] } [ **brief** ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display aaa** { **offline-record** | **abnormal-offline-record** | **online-fail-record** } **statistics**

For CE6885-LL (low latency mode):

**display aaa** { **offline-record** | **abnormal-offline-record** | **online-fail-record** } { **all** | **reverse-order** | **domain** *domain-name* | **ip-address** *ip-address* [ **vpn-instance** *vpn-instance-name* ] | **time** *start-time* *end-time* [ **date** *start-date* *end-date* ] | **username** *user-name* [ **time** *start-time* *end-time* [ **date** *start-date* *end-date* ] ] } [ **brief** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **offline-record** | Displays normal logout records. | - |
| **abnormal-offline-record** | Displays abnormal logout records. | - |
| **online-fail-record** | Displays login failure records. | - |
| **all** | Displays all login and logout records. | - |
| **reverse-order** | Displays the records in a sequence reverse to the sequence in which they were generated. | The value is a string of 1 to 253 case-sensitive characters, spaces and Chinese characters supported. |
| **domain** *domain-name* | Specifies a domain name. | The value is a string of 1 to 64 case-insensitive characters, excluding spaces, \*, ?, and ". |
| **ip-address** *ip-address* | Specifies an IP address. | The value is in dotted decimal notation. |
| **mac-address** *mac-address* | Specifies a MAC address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | The value is in H-H-H format. H is a 4-digit hexadecimal number, such as 00e0 and fc01. If an H contains fewer than 4 digits, the left-most digits are padded with zeros. For example, e0 is displayed as 00e0. The MAC address cannot be set to FFFF-FFFF-FFFF. |
| **time** *start-time* | Specifies a time range. | The format is HH:MM:SS, indicating hour:minute:second. |
| **time** *end-time* | Specifies a time range. | The format is HH:MM:SS, indicating hour:minute:second. |
| **date** *start-date* | Specifies a date. | The value is in the format of YYYY/MM/DD. YYYY/MM/DD indicates year/month/day. YYYY ranges from 2000 to 2099, MM ranges from 1 to 12, and DD ranges from 1 to 31. |
| **date** *end-date* | Specifies a date. | The value is in the format of YYYY/MM/DD. YYYY/MM/DD indicates year/month/day. YYYY ranges from 2000 to 2099, MM ranges from 1 to 12, and DD ranges from 1 to 31. |
| **username** *user-name* | Specifies a user. | The value is a string of 1 to 253 case-sensitive characters, spaces and Chinese characters supported. |
| **brief** | Displays brief records. | - |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **ipv6-address** *ipv6-address* | Displays information about the user with a specified IPv6 address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-bit hexadecimal string in format X:X:X:X:X:X:X:X. |
| **access-slot** *slot-number* | Specifies the slot ID of an interface board.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | The value is an integer. The value range depends on the model of the device. |
| **statistics** | Displays statistics. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



This command allows you to view information about user normal logouts, abnormal logouts, and login failures based on the domain name, interface, IP address, VPN instance, MAC address, or slot ID.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about normal user logouts.
```
<HUAWEI> display aaa offline-record all
  ------------------------------------------------------------------------------
  User name             : admin                                                 
  Domain name           :                                                       
  User MAC              : -                                                     
  User access type      : Telnet                                                
  User IP address       : 10.177.19.212 
  User IPV6 address     : -                                      
  User ID               : 3                                                     
  User login time       : 2015/04/14 20:20:25                                   
  User offline time     : 2015/04/14 20:28:42                                   
  User offline reason   : user request to offline                               
  ------------------------------------------------------------------------------
  Are you sure to display some information [Y/N]:y

```

**Table 1** Description of the **display aaa** command output
| Item | Description |
| --- | --- |
| User name | User name. |
| User MAC | User MAC address. |
| User access type | Access type of a user. |
| User IP address | IP address of the user. |
| User ID | User ID. |
| User login time | Time when a user goes online. |
| User offline time | User access time. |
| User offline reason | Logout reason of a user. |
| User IPv6 address | IPv6 address of the user. |
| Domain name | Authentication domain of a user. |