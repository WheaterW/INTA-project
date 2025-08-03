display dns application cache
=============================

display dns application cache

Function
--------



The **display dns application cache** command displays the cache of application domain name resolution.




Format
------

**display dns application cache**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

You can run the **display dns application cache** command to display the cache of application domain resolution.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the cache of application domain name resolution.
```
<HUAWEI> display dns application cache
 Host                                     TTL    Type  IP Address 
 test.excample.com                        114    IP     192.168.2.1 
 Total :  1

```

**Table 1** Description of the **display dns application cache** command output
| Item | Description |
| --- | --- |
| Host | Domain name. |
| TTL | Remaining lifetime of the dynamic domain name in the cache, in seconds. |
| Type | Query types:  IP: Class-A query (obtaining the IP address based on the domain name) or PTR query (obtaining the domain name based on the IP address). |
| IP Address | IP address corresponding to the domain name. |
| Total | Total number of entries in the cache of application domain name resolution. |