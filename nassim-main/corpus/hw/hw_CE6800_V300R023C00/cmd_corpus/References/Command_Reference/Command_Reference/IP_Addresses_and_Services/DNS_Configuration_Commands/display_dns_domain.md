display dns domain
==================

display dns domain

Function
--------



The **display dns domain** command displays the configuration and sequence of domain name suffixes.




Format
------

**display dns domain** [ **vpn-instance** *vpn-instance-name* ] [ **verbose** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |
| **verbose** | Displays the detail information of domain name suffixes. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run the **display dns domain** command to view the configuration and sequence of domain name suffixes.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the list of domain name suffixes.
```
<HUAWEI> display dns domain
Type:                                                                            
D:Dynamic     S:Static                                                           
                                                                                 
NO.  Type    Domain name                        TTL                           
1     S      com                                -                                
2     S      net                                -

```

# Display the list of domain name suffixes in vpn1.
```
<HUAWEI> display dns domain vpn-instance vpn1
Type:                                                                            
D:Dynamic     S:Static                                                           
                                                                                 
NO.  Type    Domain name               TTL
1     S      com                       - 
2     S      net                       -

```

**Table 1** Description of the **display dns domain** command output
| Item | Description |
| --- | --- |
| NO. | Domain name suffix numbers, that is, the configuration sequence of domain name suffixes. |
| Type | Domain name suffixes type, including dynamic and static domain name suffix. |
| Domain name | Configured domain name suffix.  In this example, two domain name suffixes are displayed. During DNS resolution, the first suffix "com" is added and sent to the DNS server. If the DNS server gives no response, the query message is resent. If the DNS server still gives no response, the query message is resent for a third time. If the DNS server still does not respond, the second suffix "net" is added and sent to the DNS server for searching for the mapped address. |
| TTL | Domain name suffix TTL. |