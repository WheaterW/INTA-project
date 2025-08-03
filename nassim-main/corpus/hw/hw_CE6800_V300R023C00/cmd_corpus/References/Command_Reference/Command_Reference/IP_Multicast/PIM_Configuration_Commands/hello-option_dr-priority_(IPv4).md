hello-option dr-priority (IPv4)
===============================

hello-option dr-priority (IPv4)

Function
--------



The **hello-option dr-priority** command configures a designated router (DR) election priority for a Router.

The **undo hello-option dr-priority** command restores the default priority.



By default, the DR election priority of a Router is 1.


Format
------

**hello-option dr-priority** *priority*

**undo hello-option dr-priority**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *priority* | Specifies a DR election priority. A larger value indicates a higher priority. | The value is an integer ranging from 0 to 4294967295. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a PIM-SM shared network segment, a DR is dynamically elected among candidate router interfaces. DR election is based on priorities and IP addresses of interfaces on routers. In a DR election process, routers exchange Hello messages carrying DR election priorities.

* If all routers support Hello messages that carry DR election priorities, the interface with the highest DR election priority wins. If all interfaces have the same DR election priority, the interface with the largest IP address wins.
* If one or more routers do not support Hello messages that carry DR priorities, the interface with the largest IP address wins.To change the DR election priority of an interface, run the pim hello-option dr-priority command.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

If the hello-option dr-priority command is run more than once, the latest configuration overrides the previous one.


Example
-------

# In the public network instance, set the DR election priority to 3 for the Router.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] pim
[*HUAWEI-pim] hello-option dr-priority 3

```