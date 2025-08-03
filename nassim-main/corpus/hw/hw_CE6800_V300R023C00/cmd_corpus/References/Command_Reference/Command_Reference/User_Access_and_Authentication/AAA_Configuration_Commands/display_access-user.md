display access-user
===================

display access-user

Function
--------



The **display access-user** command displays information about online users (including access users and administrators).




Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display access-user username** *user-name* [ **detail** ]

**display access-user access-type** { **admin** [ **ftp** | **ssh** | **telnet** | **terminal** | **http** ] } [ **username** *user-name* ]

**display access-user** [ **username** *user-name* ]

**display access-user** [ **service-scheme** *service-scheme-name* ]

**display access-user** [ **service-scheme** *service-scheme-name* | **user-id** *user-id* ]

**display access-user authentication-mode** { **ldap** | **all** | **hwtacacs** | **local** | **radius** }

**display access-user access-type** { **admin** [ **ftp** | **ssh** | **telnet** | **terminal** | **http** | **md-cli** | **snmp** ] } [ **username** *user-name* ]

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**display access-user** [ **domain** *domain-name* | **ip-address** *ip-address* [ **vpn-instance** *vpn-instance-name* ] | **ipv6-address** *ipv6-address* ] [ **detail** ]

**display access-user** [ **domain** *domain-name* | **ip-address** *ip-address* ] [ **detail** ]

For CE6820H, CE6820H-K, CE6820S, CE6881H, CE6881H-K:

**display access-user** { **access-slot** *slot-id* } [ **detail** ]

For CE6885-LL (low latency mode):

**display access-user** [ **domain** *domain-name* | **ip-address** *ip-address* [ **vpn-instance** *vpn-instance-name* ] ] [ **detail** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Displays information about all users. | - |
| **hwtacacs** | Displays information about HWTACACS authentication users. | - |
| **ldap** | Displays information about LDAP authentication users. | - |
| **local** | Displays information about Local authentication users. | - |
| **radius** | Displays information about RADIUS authentication users. | - |
| **detail** | Displays detailed information. | - |
| **username** *user-name* | Displays information about the user with a user name. | The value must be an existing user name and is case sensitive. |
| **access-type** | Displays information about users using a specified authentication mode. | - |
| **admin** | Displays information about the administrators using the specified authentication mode. | - |
| **ftp** | Indicates FTP users. | - |
| **ssh** | Indicates SSH users. | - |
| **telnet** | Indicates Telnet users. | - |
| **terminal** | Indicates terminal users. | - |
| **http** | Indicates HTTP authentication users. | - |
| **service-scheme** *service-scheme-name* | Displays information about users connecting to a specified LPU. | The service scheme must already exist. |
| **user-id** *user-id* | Displays user information with the specified user index. If this parameter is specified, detailed information about the user is displayed. | The user index must exist. |
| **authentication-mode** | Displays information about users using a specified authentication mode. | - |
| **md-cli** | Indicates the MD-CLI user. | - |
| **snmp** | Indicates SNMP users. | - |
| **domain** *domain-name* | Displays information about users in a specified domain. | The value is a string of 1 to 64 case-sensitive characters, and cannot contain spaces. |
| **ip-address** *ip-address* | Displays information about the user with a specified IP address. | The value is in dotted decimal notation. |
| **vpn-instance** *vpn-instance-name* | Indicates the name of a VPN instance to which the specified IP address belongs. | The VPN instance must exist. |
| **ipv6-address** *ipv6-address* | Displays information about the user with a specified IPv6 address.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | The value is a 32-digit hexadecimal number, in the format of X:X:X:X:X:X:X:X. |
| **access-slot** *slot-id* | Specifies a slot ID.  NOTE:  This parameter is supported only on the CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | The value is an integer. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

This command displays information about user sessions on the device.

**Precautions**

If the character string of the user name contains spaces (for example, a b), you can run the display access-user username "a b" command to view online users.If the character string of the user name contains both spaces and quotation marks (""), you cannot use the user name to view online users. In this case, you can run the display access-user | include username command to view the user ID of the online user, and then run the display access-user user-id user-id command to view the user. Alternatively, you can run the cut access-user user-id user-id command to disconnect the user.When displaying VPN user entries based on user IP address, you need to set the vpn-instance vpn-instance-name parameter to specify the VPN instance to which the IP address belongs.If user-id is specified, detailed information about the specified user is displayed. If user-id is not specified, brief information about all online users is displayed, including the user ID, user name, IP address, and MAC address of each user.When an interface is specified, the device displays the connection information of online wired users on the interface.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about the administrator with the user name huawei.
```
<HUAWEI> display access-user access-type admin username huawei
 Total: 4                                                                                                                           
 ------------------------------------------------------------------------------------------------------                             
 UserID  Username               IP address                               MAC            Status                                      
 ------------------------------------------------------------------------------------------------------                             
 8211    huawei                     10.1.1.1                            -              Success                                     
 8213    huawei                     10.1.1.2                            -              Success                                     
 8219    huawei                     10.1.1.3                            -              Success                                     
 8220    huawei                     10.1.1.4                            -              Success                                     
 ------------------------------------------------------------------------------------------------------

```

# Display the user with the user ID being 36.
```
<HUAWEI> display access-user user-id 36
  ------------------------------------------------------------------------------  
                                                                                  
 Basic:                                                                           
   User ID                         : 11                                           
   User name                       : user1                                        
   Domain-name                     : huawei.com                                   
   User MAC                        : -                                            
   User IP address                 : 10.1.1.10                                
   User IPv6 address               : -                                            
   User access time                : 2019/07/10 09:15:02                          
   User accounting session ID      : huawei255255000000000f****2016009                                                  
   User access type                : SSH
   User Privilege                  : -                                           
                                                                                  
 AAA:                                                                             
   User authentication type        : Administrator authentication
   Current authentication method   : HWTACACS
   Current authorization method    : HWTACACS
   Current accounting method       : HWTACACS
                                                                                  
  ------------------------------------------------------------------------------

```

**Table 1** Description of the **display access-user** command output
| Item | Description |
| --- | --- |
| IP address | IP address of the user. |
| MAC | User MAC address. |
| Status | User state. |
| User ID | Index of a user. |
| User name | User name. |
| User MAC | User MAC address. |
| User IPv6 address | IPv6 address of the user. |
| User access time | Time when a user goes online.  If the time zone is configured and the daylight saving time is used, the time is in YYYY-MM-DD HH:MM:SS UTC±HH:MM DST format. |
| User accounting session ID | ID of an accounting session. |
| User access type | User access type. IPoE indicates an IP session user. For the related command, see local-user service-type. |
| User Privilege | User privilege level. |
| User authentication type | Authentication type of a user, which depends on the access type of the user. |
| User IP address | IP address of the user. |
| Domain-name | User domain. |
| Current authentication method | Authentication method used for a user. |
| Current authorization method | Current authorization mode. |
| Current accounting method | Current accounting mode. |
| Basic | Basic information of a user. |
| Option82 information | Option 82 of a user. |
| AAA | AAA information related to a user. |