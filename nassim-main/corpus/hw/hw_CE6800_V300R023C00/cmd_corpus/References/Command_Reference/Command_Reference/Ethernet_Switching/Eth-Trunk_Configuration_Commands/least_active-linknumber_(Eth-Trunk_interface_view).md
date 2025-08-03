least active-linknumber (Eth-Trunk interface view)
==================================================

least active-linknumber (Eth-Trunk interface view)

Function
--------



The **least active-linknumber** command sets the minimum number of active member links of an Eth-Trunk interface.

The **undo least active-linknumber** command restores the default minimum number of active member links.



By default, the minimum number of active member links on an Eth-Trunk interface is 1.


Format
------

**least active-linknumber** *link-number*

**undo least active-linknumber**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *link-number* | Specifies the minimum number of active member links. | The value is a decimal integer ranging from 1 to 256. |



Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The number of active member links on an Eth-Trunk interface affects the status and bandwidth of the Eth-Trunk interface. The bandwidth of an Eth-Trunk interface equals the total bandwidth of all member interfaces in the Up state.To ensure the status and bandwidth of an Eth-Trunk interface, you can set the following thresholds to reduce the impact of changes in member link status:

* Minimum number of active member linksWhen the number of active member links decreases below the threshold, the Eth-Trunk interface goes Down. Setting the minimum number of active member links ensures the minimum bandwidth of an Eth-Trunk interface.For example, each member link can provide the bandwidth of 1 Gbit/s, and the trunk interface needs to provide the minimum bandwidth of 2 Gbit/s. In this case, the lower threshold must be set to 2 or a larger value. If the number of active member links decreases below 2, the Eth-Trunk interface goes Down.
* Maximum number of active member linksAfter the number of active member links reaches the upper threshold, the bandwidth of the Eth-Trunk interface does not increase even if more member links go Up. Setting the maximum number of active member links improves network reliability on the basis of sufficient bandwidth.To delete the configured minimum number of active member links or restore the setting to the default value, run the undo least active-linknumber command or least active-linknumber 1 command.

**Configuration Impact**

If you run the least active-linknumber command more than once, the latest configuration overrides the previous one.After the minimum number of active member links is configured,

* the Eth-Trunk interface goes Down when the number of active member links falls below the configured lower threshold.
* the Eth-Trunk interface goes Up when the number of active member links reaches the configured lower threshold.

**Precautions**



If the **lacp max active-linknumber** command has been configured before you run the least active-linknumber command, ensure that the minimum number of active member links does not exceed the maximum number of active member links.




Example
-------

# Set the minimum number of active member links to 3.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 1
[*HUAWEI-Eth-Trunk1] least active-linknumber 3

```