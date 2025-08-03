node-id(IFIT-dcn-instance view)
===============================

node-id(IFIT-dcn-instance view)

Function
--------



The **node-id** command sets an NE ID for IFIT.

The **undo node-id** command deletes an NE ID for IFIT.



By default, no node ID is set in the IFIT view.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**node-id** *node-id-value*

**undo node-id** [ *node-id-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **node-id** *node-id-value* | Specifies the node ID of IFIT. | The value is an integer ranging from 0 to 65535. By default, it is 0. |



Views
-----

IFIT dcn-instance view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Before configuring IFIT, you can run this command to configure an NE ID. A network-wide flow ID consists of an NE ID and a flow ID of the NE. The flow ID is automatically generated or statically configured. You need to run the **node-id** command to configure an NE ID to ensure that the generated network-wide flow ID is unique on the network.

**Prerequisites**

IFIT has been enabled.

**Precautions**

The node ID can be modified only after all IFIT policies are deleted.The NE IDs of the devices on the network must be different.


Example
-------

# Specify the NE ID for IFIT.
```
<HUAWEI> system-view
[~HUAWEI] ifit
[*HUAWEI-ifit] dcn-instance
[*HUAWEI-ifit-dcn-instance] node-id 200

```