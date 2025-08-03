set said-node disable(System view)
==================================

set said-node disable(System view)

Function
--------



The **set said-node disable** command disables a specified SAID node or all SAID nodes.

The **undo set said-node disable** command restores the default SAID node configuration.



By default, all SAID nodes are enabled.


Format
------

**set said-node** *said-node-name* **disable**

**undo set said-node** *said-node-name* **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *said-node-name* | Specifies the name of a SAID node. | The value is a string of 1 to 30 case-sensitive characters without spaces. |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

After the SAID node function is enabled, you can run the **display said-node status** command to check the SAID node status.


Example
-------

# Disable the SAID node named said\_ping.
```
<HUAWEI> system-view
[~HUAWEI] set said-node said_ping disable

```