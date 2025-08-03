eq | lt | gt | range (ACL port pool view)
=========================================

eq | lt | gt | range (ACL port pool view)

Function
--------



The **eq** command adds a port number to an ACL port pool.

The **lt** command adds multiple port numbers to an ACL port pool, with the numbers of the ports to be added less than a specific value.

The **gt** command adds multiple port numbers to an ACL port pool, with the numbers of the ports to be added greater than a specific value.

The **range** command adds multiple port numbers to an ACL port pool, with the numbers of the ports to be added ranging from the start port number to the end port number.

The **undo** command deletes the port number range from a created ACL port pool.



By default, no port number exists in an ACL port pool.


Format
------

{ **eq** | **lt** | **gt** } *begin-port-number*

**range** *begin-port-number* *end-port-number*

**undo** { **eq** | **lt** | **gt** } *begin-port-number*

**undo range** *begin-port-number* *end-port-number*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *begin-port-number* | Specify start port number. | The value is an integer ranging from 0 to 65535. |
| *end-port-number* | Specifies the end port. | The value is an integer ranging from 0 to 65535. |



Views
-----

ACL port pool view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



In typical ACL usage scenarios, such as in QoS policy scenarios, a user may need to match both the source and destination port numbers. To match an ACL rule against multiple source and destination port numbers to implement a QoS policy, the user needs to create an ACL port pool and run the eq, gt, lt, or range command to add desired port numbers to the ACL port pool, or run the neq command to rule out unneeded port numbers from the ACL port number. When these port numbers are cohesive, you can run the eq, gt, lt, or range command to add multiple port numbers to the ACL port pool.



**Prerequisites**



An ACL port pool has been created using the **acl port-pool** command.




Example
-------

# Set the port number range to 5-100 for an ACL port pool named p1.
```
<HUAWEI> system-view
[~HUAWEI] acl port-pool p1
[*HUAWEI-acl-port-pool-p1] range 5 100

```