ip address (ACL address pool view)
==================================

ip address (ACL address pool view)

Function
--------



The **ip address** command adds an IP address to an ACL IP address pool.

The **undo ip address** command deletes an IP address from an ACL IP address pool.



By default, an ACL IP address pool has no IP addresses.


Format
------

**ip address** *ip-address* { *ip-mask* | *mask-length* }

**undo ip address** *ip-address* { *ip-mask* | *mask-length* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ip-address* | Specifies an IP address to be added to an ACL IP address pool. | The value is in dotted decimal notation. |
| *ip-mask* | Specifies the wildcard mask of an IP address to be added to an ACL IP address pool. | The value is in dotted decimal notation. |
| *mask-length* | Specifies the wildcard mask length of an IP address to be added to an ACL IP address pool. | The value is an integer ranging from 1 to 32. |



Views
-----

ACL address pool view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To add an IP address to an ACL IP address pool, run the ip address command.



**Prerequisites**



An ACL IP address pool has been created and its view is displayed using the **acl ip-pool pool-name** command.




Example
-------

# Create an ACL IP address pool named test and add IP address 10.10.10.1 with the wildcard mask length of 24 to test.
```
<HUAWEI> system-view
[~HUAWEI] acl ip-pool test
[*HUAWEI-acl-ip-pool-test] ip address 10.10.10.1 24

```