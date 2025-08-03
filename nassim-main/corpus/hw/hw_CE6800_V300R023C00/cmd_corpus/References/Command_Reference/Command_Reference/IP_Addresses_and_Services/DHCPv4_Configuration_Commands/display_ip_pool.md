display ip pool
===============

display ip pool

Function
--------



The **display ip pool** command displays the configurations of an address pool.




Format
------

**display ip pool**

**display ip pool interface** *interface-pool-name* [ *start-ip-address* [ *end-ip-address* ] | **all** | **conflict** | **expired** | **used** ]

**display ip pool vpn-instance** *vpn-instance-name*

**display ip pool name** *pool-name* [ *start-ip-address* [ *end-ip-address* ] | **all** | **conflict** | **expired** | **used** [ **user-type** **dhcp** ] ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-pool-name* | Displays the configuration of the specified interface address pool.  An interface address pool is specified using the type and number of an interface without spaces between them. | The value is a string of 1 to 64 case-insensitive characters without spaces. It can contain digits, letters, and special characters underscores (\_), hyphens (-), and periods (.). It cannot be set to - or --. |
| *start-ip-address* | Displays the IP addresses within the range specified by the start IP address in the address pool. | The value is in dotted decimal notation. |
| *end-ip-address* | If end-ip-address is set, the end IP address is also specified. | The value is in dotted decimal notation. |
| **all** | Displays all IP addresses in the address pool. | - |
| **conflict** | Displays the conflicting IP addresses in the address pool. (If an IP address that the DHCP server prepares to allocate to a user exists on the network, the IP address will be added to the conflict list. This problem occurs when a static IP address is configured or an active/standby switchover occurs in a VRRP group if the range of IP addresses in the address pools on the master and backup devices overlap.). | - |
| **expired** | Displays the expired and idle IP addresses in the address pool. | - |
| **used** | Display the IP addresses used in the address pool. | - |
| *vpn-instance-name* | Displays information about the address pool in a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **name** *pool-name* | Displays the configuration of the specified global address pool. | The value is a string of 1 to 64 case-insensitive characters without spaces. It can contain digits, letters, and special characters underscores (\_), hyphens (-), and periods (.). It cannot be set to - or --. |
| **user-type** | Display the IP addresses used in the address pool by the specific type of users. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run the **display ip pool** command to view information about a configured address pool and IP addresses in the address pool, including the address pool name, lease, lock status, and status of IP addresses in the address pool.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about conflicting IP addresses in the address pool huawei.
```
<HUAWEI> display ip pool name huawei conflict
  Pool-name        : huawei                                                        
  Pool-No          : 1                                                          
  Lease            : 1 Days 0 Hours 0 Minutes                                   
  Domain-name      : -                                                          
  Option-code      : 60                                                         
    Option-subcode : --                                                         
      Option-type   : cipher                                                     
      Option-value : %^%#5g)NPN1M,$M;pQ-lT\P>Al6QN4#ldIVVjD69XlCN%^%#                                                                                                              
  DNS-server0      : -                                                          
  NBNS-server0     : -                                                          
  Netbios-type     : -                                                          
  Position         : Local           
  Status           : Unlocked              
  Gateway-0        : -                                                          
  Network          : 192.168.0.0                                                   
  Mask             : 255.255.255.0                                              
  VPN instance     : --                                                         
  Bootfile         : 43534                                                      
  Logging          : Enable                                                     
  Conflicted address recycle interval: 1 Days 0 Hours 0 Minutes                 
  Address Statistic: Total       :254       Used        :1                      
                     Idle        :252       Expired     :2                       
                     Conflict    :1         Disabled    :0                      
                                                                                
 -------------------------------------------------------------------------------
  Network section                                                               
         Start           End       Total    Used Idle(Expired) Conflict Disabled
 -------------------------------------------------------------------------------
     192.168.0.1   192.168.0.254     254       1        252(2)       1     0    
 -------------------------------------------------------------------------------
 Client-ID format as follows:                                                   
   DHCP    : mac-address                  
   IPSec   : user-id/portnumber/vrf                
   SSL-VPN : user-id/session-id             
 -------------------------------------------------------------------------------
  Index              IP             Client-ID    Type       Left   Status       
 -------------------------------------------------------------------------------
    109   192.168.0.110                     -       -          -   Conflict     
 -------------------------------------------------------------------------------

```

**Table 1** Description of the **display ip pool** command output
| Item | Description |
| --- | --- |
| Pool-name | Name of an IP address pool.  To configure the IP address pool name, run the ip pool (system view) command. |
| Pool-No | Address pool index. |
| Lease | Lease of the IP address pool. |
| Domain-name | Name of a domain.  To configure the domain name, run the domain-name command. |
| Option-code | Value of a customized option.  To configure the value, run the option command. |
| Option-subcode | Value of a customized sub-option.  To configure the value, run the option command. |
| Option-type | Type of a customized option code:   * ascii: indicates that the customized option code is an ASCII character string. * hex: indicates that the customized option code is a hexadecimal string. * cipher: indicates that the customized option code is a ciphertext character string.   To configure the type, run the option command. |
| Option-value | Content of a customized option.  To configure the content, run the option command. |
| DNS-server0 | Address of the DNS server. Currently, an IP address pool can be configured with up to eight DNS servers. The value 0 indicates the first DNS server address and the value 1 indicates the second DNS server address.  To configure the DNS server address, run the dns-list command. |
| NBNS-server0 | Address of the NetBIOS server. Currently, an address pool can be configured with up to eight NetBIOS server addresses.The value 0 indicates the first NetBIOS server address and the value 1 indicates the second NetBIOS server address.  To configure the NetBIOS server address, run the nbns-list command. |
| Netbios-type | NetBIOS type.  To configure the NetBIOS type, run the netbios-type command. |
| Position | Location of the IP address pool. |
| Status (First) | Status of the address pool.  To configure the address pool status, run the lock (IP address pool view) command. |
| Status (Second) | Status of an IP address:   * Used: indicates that the IP address is used. * Idle: indicates that the IP address is idle. * Expired: indicates that the lease of the IP address expires and the IP address is idle. * Conflict: indicates that the IP address conflicts with another IP address on the network. * Disable: indicates that the IP address cannot be used. * Static-bind: indicates that the IP address is bound to a MAC address. * Static-bind used: indicates that the IP address is bound to a MAC address and used. |
| Gateway-0 | Gateway address. Currently, a maximum of eight gateway addresses can be configured in an IP address pool. The value 0 indicates the first gateway address. |
| Network | Network segment of the address pool. |
| Mask | Subnet mask of the address pool.  To configure the subnet mask of the address pool, run the network (IP address pool view) command. |
| VPN instance | VPN instance name. |
| Bootfile | Name of the startup configuration file configured for the DHCP client.  To configure the name, run the bootfile command. |
| Logging | To configure the status of the logging function, run the logging command. |
| Conflicted address recycle interval | The interval for the automatic reclaim of conflicting IP addresses in the address pool. |
| Address Statistic | Statistics about IP addresses in the address pool. |
| Total | Total number of IP addresses in the address pool.  Total = Used + Idle(Expired) + Conflict + Disable. |
| Used | Number of used IP addresses in the address pool. |
| Conflict | Number of conflicting IP addresses in the address pool.  If there are many conflicting IP addresses in the address pool, it is recommended that you configure the conflict auto-recycle interval command to reclaim conflicting IP addresses periodically. This configuration reduces occupation of idle IP addresses in the address pool and prevents IP address conflicts on the network. |
| Disabled | Number of disabled IP addresses in the address pool. |
| Start | Start IP address of the IP address pool. |
| End | End IP address of the IP address pool. |
| Idle(Expired) | Number of idle(expired) IP addresses in the address pool. |
| Client-ID format as follows | Client ID format. |
| Client-ID | DHCP client ID. |
| Index | Index. |
| Type | DHCP client type. |
| Left | Remaining lease of an IP address.  When the result of the calculation formula ([Lease - Left]/Lease) is 50% or 87.5%, the DHCP client sends a DHCP Request message to the DHCP server to renew the lease. If the renewal succeeds, the value of the Left field is recounted. If the renewal fails, the DHCP client requests an IP address again and the status of its original IP address is set to Expired. |