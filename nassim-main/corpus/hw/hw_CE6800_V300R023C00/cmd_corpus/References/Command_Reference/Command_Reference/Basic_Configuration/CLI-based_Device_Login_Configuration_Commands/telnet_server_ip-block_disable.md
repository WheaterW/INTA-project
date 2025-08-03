telnet server ip-block disable
==============================

telnet server ip-block disable

Function
--------



The **telnet server ip-block disable** command disables the function of locking IP addresses in VTY access scenarios.

The **undo telnet server ip-block disable** command restores the default configuration.



By default, the function of locking IP addresses in telnet connection scenarios is enabled.


Format
------

**telnet server ip-block disable**

**undo telnet server ip-block disable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

* If the function of blocking IP addresses in telnet connection scenarios is enabled, the device blocks IP addresses that fail to be authenticated and rejects telnet connect requests that use the blocked IP addresses. The device also records the blocked IP addresses in a list.
* After the function is disabled, the device deletes the blocked IP addresses from the list and does not record new IP addresses that fail to be authenticated. To disable the function, run the **telnet server ip-block disable** command.
* In telnet connection scenarios, IP addresses that fail to be authenticated are blocked only when the function of blocking IP addresses is enabled.

**Precautions**

The Telnet protocol has security risks. You are advised to use the SSH v2 protocol.


Example
-------

# Enable the function of locking IP addresses in telnet connection scenarios.
```
<HUAWEI> system-view
[~HUAWEI] undo telnet server ip-block disable

```

# Disable the function of locking IP addresses in telnet connection scenarios.
```
<HUAWEI> system-view
[~HUAWEI] telnet server ip-block disable
Warning: It is not recommended to disable ip block feature. This operation may result in system becoming vulnerable to security threats.

```