display aaa-bind administrator ip
=================================

display aaa-bind administrator ip

Function
--------



The **display aaa-bind administrator ip** command displays the IP addresses of trusted hosts.




Format
------

**display aaa-bind administrator ip**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

This command allows you to view the configured IP addresses of trusted hosts.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the configured IP addresses of trusted hosts.
```
<HUAWEI> display aaa-bind administrator ip
 -------------------------------------------------------------------------------                                                    
 Admin IpBind List (Total: 1)                                                                                                       
 -------------------------------------------------------------------------------                                                    
 2001:db8:1::1/64                                                                                                                           
 -------------------------------------------------------------------------------

```

**Table 1** Description of the **display aaa-bind administrator ip** command output
| Item | Description |
| --- | --- |
| Admin IpBind List | Management IP address binding list. |