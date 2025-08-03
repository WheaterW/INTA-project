display system osnode-group
===========================

display system osnode-group

Function
--------



The **display system osnode-group** command displays information about an operating system (OS) group on a device.




Format
------

**display system osnode-group**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

An OS group of a device is automatically generated based on a specified board group and used to carry master and slave OS services. To view OS group information of a device, run the display osnode-group command.


Example
-------

# Display OS group information of a device.
```
<HUAWEI> display system osnode-group
OS-group             OS-node    Board-id         Deploy-state      Active-state 
OSG-MMB-BG1-1        273        17               available         active       
OSG-MMB-BG1-1        274        18               available         active

```

**Table 1** Description of the **display system osnode-group** command output
| Item | Description |
| --- | --- |
| OS-group | OS group name. |
| OS-node | OS node ID. |
| Board-id | ID of the board where an OS node resides. |
| Deploy-state | Service deployment status on an OS node:   * unavailable: All boards, including the MMB or MB board are unavailable. * available: Only master and slave MMB or MB boards are available. |
| Active-state | Activation status of an OS node:   * inactive: An OS node does not register with the SEM. * active: An OS node has registered with the SEM. |