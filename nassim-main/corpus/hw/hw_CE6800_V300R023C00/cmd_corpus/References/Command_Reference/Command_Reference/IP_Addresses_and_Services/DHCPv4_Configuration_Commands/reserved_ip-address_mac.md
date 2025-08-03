reserved ip-address mac
=======================

reserved ip-address mac

Function
--------

The **reserved ip-address mac** command enables the function of reserving IP address allocation records.

The **undo reserved ip-address mac** command disables the function of reserving IP address allocation records.

By default, a device reserves IP address allocation records.



Format
------

**reserved ip-address mac**

**undo reserved ip-address mac**



Parameters
----------

None


Views
-----

IP address pool view



Default Level
-------------

2: Configuration level



Usage Guidelines
----------------

After a user goes offline, the IP address is reclaimed. The status of the IP address then is set to Idle and the device does not reserve allocation records of the IP address. When the user attempts to go online again, the user wants to use the original IP address. However, the device does not reserve any allocation record of the IP address and the original IP address may have been allocated to another user.

To resolve this issue, you can enable the function of reserving IP address allocation records. If a user goes offline after this function is enabled, the status of the IP address is set to Expired and the device reserves allocation records of the IP address based on the user's MAC address. If the user attempts to go online again, the device preferentially allocates the original IP address to the user.

Example
-------

# Enable the function of reserving IP address allocation records in the address pool named test.
```
<HUAWEI> system-view
[~HUAWEI] ip pool test
[*HUAWEI-ip-pool-test] reserved ip-address mac

```