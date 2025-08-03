undo mac-address limit all
==========================

undo mac-address limit all

Function
--------



The **undo mac-address limit all** command deletes all MAC address limiting rules.




Format
------

**undo mac-address limit all**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **mac-address** | MAC address. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



To delete all MAC address limiting rules, run the **undo mac-address limit all** command in the system view.



**Precautions**



Before using **undo mac-address limit all** command, run the **display mac-address limit** command to check the MAC address limiting rules and confirm your operation.




Example
-------

# Delete all MAC address limiting rules.
```
<HUAWEI> system-view
[~HUAWEI] undo mac-address limit all

```