set license threshold alarm disable
===================================

set license threshold alarm disable

Function
--------



The **set license threshold alarm disable** command disables the function of reporting an alarm when resources of a single license item or all license items are insufficient.

The **undo set license threshold alarm disable** command enables the function of reporting an alarm when resources of all license items or a single license item are insufficient.



By default, a device reports an alarm indicating that license resources are insufficient.


Format
------

**set license threshold alarm** { **all** | **item** *item-name* } **disable**

**undo set license threshold alarm** { **all** | **item** *item-name* } **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Specifies information about all license items registered on the device. | - |
| **item** *item-name* | Specifies the license resource item registered in the system. | The value is a string of 1 to 31 characters. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

By default, when the resource usage of a license item exceeds the threshold, the device reports an alarm indicating insufficient license resources. You can run the **set license threshold alarm disable** command to disable this function.

**Configuration Impact**

After the **set license threshold alarm disable** command is executed, the alarm indicating insufficient resources for the license control item will be cleared and will not be reported again.


Example
-------

# Disable the function of reporting an alarm when resources of all license items are insufficient.
```
<HUAWEI> system-view
Enter system view, return user view with return command.
[~HUAWEI] set license threshold alarm all disable

```

# Disable the function of reporting an alarm when resources of a specified license item are insufficient.
```
<HUAWEI> system-view
Enter system view, return user view with return command.
[~HUAWEI] set license threshold alarm item LCR5XXXXXXXXX disable

```