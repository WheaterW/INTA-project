display ip host
===============

display ip host

Function
--------



The **display ip host** command displays mappings between hosts and IP addresses.




Format
------

**display ip host** [ **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **vpn-instance** *vpn-instance-name* | Specifies the name of a VPN instance. | The value is a string of 1 to 31 case-sensitive characters. The VPN instance name cannot be \_public\_. The character string can contain spaces if it is enclosed with double quotation marks ("). |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

After configuring static DNS entries, you can run the **display ip host** command to view the mapping between hosts and IP addresses.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display mappings between hosts and IP addresses.
```
<HUAWEI> display ip host
Host                              Age        Flag   IP Address

exampletest                       0          Static 10.1.1.1

example                           0          Static 10.2.2.2

Total    :  2

```

# Display the mappings between the domain names and IP addresses in the VPN named vpn1.
```
<HUAWEI> display ip host vpn-instance vpn1
Host                              Age        Flag   IP Address
exampletestvpn1                   0          Static 10.1.1.1     
examplevpn1                       0          Static 10.2.2.2    
Total    :  2

```

**Table 1** Description of the **display ip host** command output
| Item | Description |
| --- | --- |
| Host | Host name. |
| Age | Aging time.  The value 0 indicates that the static DNS entry need not be aged. |
| Flag | Status of the domain name.  "Static" indicates the static domain name. |
| IP Address | IP address matching the host. |
| Total | Total number of static domain name resolution entries. |