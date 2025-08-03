confederation nonstandard
=========================

confederation nonstandard

Function
--------



The **confederation nonstandard** command enables devices to be compatible with the devices that do not support standard AS confederation.

The **undo confederation nonstandard** command disables the configuration.



By default, the Device is not compatible with the devices that do not support standard AS confederation.


Format
------

**confederation nonstandard**

**undo confederation nonstandard**


Parameters
----------

None

Views
-----

BGP view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To ensure that the devices can communicate with other devices that do not support standard AS confederation, run the command on all devices in a confederation.

**Configuration Impact**

After the confederation ID is configured, running the confederation nonstandard command will disconnect the sessions between a device and its IBGP peers as well as its confederation EBGP peers. Then, new connections are re-established.


Example
-------

# Enable the devices to be compatible with devices that do not support standard AS confederation. The AS 100 contains two sub-ASs, 64000 and 65000.
```
<HUAWEI> system-view
[~HUAWEI] bgp 64000
[*HUAWEI-bgp] confederation id 100
[*HUAWEI-bgp] confederation peer-as 65000
[*HUAWEI-bgp] confederation nonstandard

```