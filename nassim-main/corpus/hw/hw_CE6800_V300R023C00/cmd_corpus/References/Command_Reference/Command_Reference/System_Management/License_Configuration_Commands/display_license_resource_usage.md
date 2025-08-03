display license resource usage
==============================

display license resource usage

Function
--------



The **display license resource usage** command displays the usage of active resource items in a license file.




Format
------

**display license resource usage**

**display license resource usage verbose**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **verbose** | Displays detailed resource usage, including the usage of sales items and control items. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

To check the usage of active resource items in a GTL file, run the **display license resource usage** command.Resource usage indicates the ratio of used resources to those authorized by the GTL file.

**Precautions**

If the sales code is the same as the control code, the item is both a control item and a sales item.If the license file does not support the consistency between license sales items and displayed license items, the license resource usage cannot be viewed by running the **display license resource usage verbose** command.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the resource usage of both license sales items and control items when the license supports the consistency between license sales items and displayed license items.
```
<HUAWEI> display license resource usage verbose
Info: Active license on master board: flash:/LICXXXX.
-------------------------------------------------------
ItemName              ItemType            ResourceUsage
-------------------------------------------------------
LCR5S40VA1C00         --                            0/1
LCR5S40VA1C00         Resource                      0/1
LCR5S40VA5C00         --                            0/1
LCR5S40VA5C00         Resource                      0/1
-------------------------------------------------------

```

# Display the resource usage of license control items when the license does not support the consistency between license sales items and displayed license items.
```
<HUAWEI> display license resource usage
Info: Active license on master board: flash:/LICXXXX.
--------------------------------------------------------------------------------
FeatureName              ConfigureItemName                         ResourceUsage
--------------------------------------------------------------------------------
CRFEA1                   LCR5S40VA1C00                                       0/1
CRFEA1                   LCR5S40VA5C00                                       0/1
--------------------------------------------------------------------------------

```

# Display the usage of license sales items when the license supports the consistency between license sales items and displayed license items.
```
<HUAWEI> display license resource usage
Info: Active license on master board: flash:/LICXXXX.
-------------------------------------------------------
SalesItemName                             ResourceUsage
-------------------------------------------------------
LCR5S40VA1C00                                       0/1
LCR5S40VA5C00                                       0/1
-------------------------------------------------------

```

**Table 1** Description of the **display license resource usage** command output
| Item | Description |
| --- | --- |
| Info: Active license on master board | Resource usage. |
| ItemName | Name of a license item. |
| ItemType | Type of a license item.  If the value is --, the license is a sales item.  If the value is Function or Resource, the license is a control item. |
| ResourceUsage | Resource usage.  Resource usage = Usage value of a resource item/Authorized value of a resource item.  The authorized value of a resource item corresponds to the quota value applied for in the license file.  The usage value of a resource item corresponds to the quota that has been configured for the service.  For example, if eight ports are applied for in the license file and six ports have been allocated and used, the resource usage is 6/8. |
| FeatureName | Feature name. |
| ConfigureItemName | Configuration item name. |
| SalesItemName | Sales item name. |