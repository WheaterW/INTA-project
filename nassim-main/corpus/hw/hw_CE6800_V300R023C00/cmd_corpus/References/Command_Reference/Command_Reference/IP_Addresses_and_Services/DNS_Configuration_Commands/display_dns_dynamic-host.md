display dns dynamic-host
========================

display dns dynamic-host

Function
--------



The **display dns dynamic-host** command displays dynamic DNS entries saved in the domain name cache.




Format
------

**display dns dynamic-host** [ **ip** ] [ *domain-name* ] [ **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **ip** | Specifies the Class-A and PTR query dynamic DNS entries. | - |
| *domain-name* | Specifies the dynamic DNS entries of a domain name. | The value is a string of 1 to 255 case-sensitive characters. The value must be an existing domain name. |
| **vpn-instance** *vpn-instance-name* | Specifies a VPN instance name. | The value is a string of 1 to 31 case-sensitive characters. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run the **display dns dynamic-host** command to view dynamic DNS entries saved in the domain name cache and check whether domain names match the mapping entries.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the dynamic DNS entries saved in the domain name cache.
```
<HUAWEI> display dns dynamic-host
Host                                    TTL        Type   Address                                                                  
sipx.autosrv.com                        114        IP     192.168.1.1                        
sip.autosrv.com                         237        IP     192.168.1.2                           
sip.autonaptr.com                       117        IP     192.168.1.3                        

Total  :  3

```

# Display the dynamic DNS entries saved in the domain name cache of vpn1.
```
<HUAWEI> display dns dynamic-host vpn-instance vpn1
Host                         TTL    Type   Address                                               
sipx.autosrv.com             151    IP     192.168.2.1                              

Total  :  1

```

**Table 1** Description of the **display dns dynamic-host** command output
| Item | Description |
| --- | --- |
| Host | Domain name.  sipx.autosrv.com: indicates the domain name of the server providing the SIP service. |
| TTL | Time left before dynamic DNS entries saved in the cache age out, in seconds. |
| Type | Query type:  IP: Class-A query, which is used to request the IP address corresponding to a domain name, or Pointer (PTR) query, which is used to request the domain name corresponding to an IP address. |
| Address | IP address mapping the domain name.  192.168.1.1: indicates the IPv4 address. |
| Total | Total number of cached dynamic DNS. |