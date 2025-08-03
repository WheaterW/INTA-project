robust-count (MLD view)
=======================

robust-count (MLD view)

Function
--------



The **robust-count** command sets a global robustness variable for a Multicast Listener Discovery (MLD) querier.

The **undo robust-count** command restores the default value.



By default, the robustness variable of an MLD querier is 2.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**robust-count** *robust-value*

**undo robust-count**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *robust-value* | Specifies the robustness variable of an MLD querier. | The value is an integer ranging from 2 to 5. |



Views
-----

MLD view,VPN instance MLD view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

A robustness variable is used to define the following values:

* Number of times for sending general query messages when the MLD querier starts
* Number of times for sending group-specific query messages when the MLD querier receives a Leave messageThe function of this command is the same as that of the mld robust-count command used in the interface view. The configuration in the MLD view is globally valid, whereas the configuration in the interface view is valid only for the current interface. The system prefers the configuration in the interface view. The configuration in the MLD view is used only when the configuration in the interface view is not done.

Example
-------

# Set the robustness variable of an MLD querier to 3 in the MLD view.
```
<HUAWEI> system-view
[~HUAWEI] multicast ipv6 routing-enable
[*HUAWEI] mld
[*HUAWEI-mld] robust-count 3

```