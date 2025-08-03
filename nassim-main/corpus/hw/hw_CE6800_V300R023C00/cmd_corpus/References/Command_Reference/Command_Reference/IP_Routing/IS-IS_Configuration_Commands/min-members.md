min-members
===========

min-members

Function
--------



The **min-members** command configures the number of available member links that triggers a link cost adjustment in a link group.

The **undo min-members** command resumes the number of available member links that triggers a link cost adjustment in a link group to 2.



By default, the minimum number of available member links in the link group is 2.


Format
------

**min-members** *min-num*

**undo min-members**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *min-num* | Specifies the number of available member links that triggers a link cost adjustment in a link group. | The value is an integer ranging from 2 to 64. |



Views
-----

IS-IS link-group view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

After a link group is configured, run the **min-members** command to configure the number of available member links that triggers a link cost adjustment in the link group. If the number of available member links in the link group falls below the configured min-num the link cost of these member links is increased. Consequently, the routes along the member links are not selected, and traffic is switched to a backup link, which prevents traffic loss.

**Prerequisites**

A link group has been created using the **link-group** command.

**Precautions**

When configuring min-num ensure that the bandwidth of the available member links in the link group is sufficient enough to carry the traffic. For example, when the traffic forwarding rate is 250 Gbit/s, and the bandwidth of each link is 100 Gbit/s, the value of min-num must be greater than or equal to 3.


Example
-------

# Set the number of available member links that triggers a link cost adjustment to 3 in the link group named link-a.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] link-group link-a
[*HUAWEI-isis-link-group-link-a] revert-members 6
[*HUAWEI-isis-link-group-link-a] min-members 3

```