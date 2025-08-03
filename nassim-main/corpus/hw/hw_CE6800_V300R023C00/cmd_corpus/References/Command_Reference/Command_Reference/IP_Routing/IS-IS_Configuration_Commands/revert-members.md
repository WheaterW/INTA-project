revert-members
==============

revert-members

Function
--------



The **revert-members** command configures the number of available member links that triggers a link cost restoration for a link group.

The **undo revert-members** command restores the default configuration.



By default, the number equals the configured number that triggers a link cost adjustment.


Format
------

**revert-members** *revert-num*

**undo revert-members**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *revert-num* | Specifies the number of available member links that triggers a link cost restoration in a link group. | The value is an integer ranging from 2 to 64. |



Views
-----

IS-IS link-group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After the link cost of the member links in a link group is increased due to a link failure, traffic is switched to a backup link. You can run the **revert-members** command to configure the number of available member links that triggers a link cost restoration so that the original link cost is restored when the link failure is cleared and the number of available member links reaches or exceeds revert-num. Then, routes are recalculated, and traffic is forwarded along the optimal route.

**Prerequisites**

A link group has been created using the **link-group** command.

**Precautions**

The value of revert-num must be greater than or equal to that of min-members configured in the **min-members** command.


Example
-------

# Set the number of available member links that triggers a link cost restoration to 6 in the link group named link-a.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] link-group link-a
[*HUAWEI-isis-link-group-link-a] revert-members 6

```