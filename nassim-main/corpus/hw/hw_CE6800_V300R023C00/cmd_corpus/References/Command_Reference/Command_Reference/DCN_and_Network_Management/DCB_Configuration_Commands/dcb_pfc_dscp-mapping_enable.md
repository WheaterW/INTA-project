dcb pfc dscp-mapping enable
===========================

dcb pfc dscp-mapping enable

Function
--------



The **dcb pfc dscp-mapping enable** command enables PFC to perform backpressure based on internal priorities.

The **undo dcb pfc dscp-mapping enable** command disables PFC from performing backpressure based on the internal priority. PFC performs backpressure based on the 802.1p priority.



By default, a PFC-enabled device performs backpressure based on the 802.1p priority.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**dcb pfc dscp-mapping enable slot** *slot-id*

**undo dcb pfc dscp-mapping enable slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **slot** *slot-id* | Specifies the slot ID. | The value is an integer. You can enter a question mark (?) and select a value from the displayed value range. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

You can run the **dcb pfc dscp-mapping enable** command to enable PFC to perform backpressure based on internal priorities, for example, internal priorities mapped from DSCP values.


Example
-------

# Enable PFC to perform backpressure based on internal priorities.
```
<HUAWEI> system-view
[~HUAWEI] dcb pfc dscp-mapping enable slot 1

```