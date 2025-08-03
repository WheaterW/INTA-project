c-rp advertisement-interval (VPN instance PIM view/PIM view of a public network instance)
=========================================================================================

c-rp advertisement-interval (VPN instance PIM view/PIM view of a public network instance)

Function
--------



The **c-rp advertisement-interval** command sets an interval at which a candidate-rendezvous point (C-RP) sends an Advertisement message.

The **undo c-rp advertisement-interval** command restores the default setting.



By default, a C-RP sends Advertisement messages at an interval of 60 seconds.


Format
------

**c-rp advertisement-interval** *interval*

**undo c-rp advertisement-interval**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *interval* | Specifies an interval at which a C-RP sends an Advertisement message. | The value is an integer ranging from 1 to 65535, in seconds. |



Views
-----

VPN instance PIM view,PIM view of a public network instance


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

All C-RPs in a PIM-SM domain send Advertisement messages to the same bootstrap router (BSR). An Advertisement message carries the C-RP address, range of multicast groups that the C-RP serves, and priority of the C-RP. In this manner, the BSR can collect complete RP-set information. To set an interval at which a C-RP sends an Advertisement message, run the c-rp advertisement-interval command.

**Prerequisites**

The multicast routing function has been enabled using the **multicast routing-enable** command in the public network instance view or VPN instance view.

**Configuration Impact**

If the c-rp advertisement-interval command is run more than once, the latest configuration overrides the previous one.


Example
-------

# In the public network instance, specify 30 seconds as the interval at which a C-RP sends an Advertisement message.
```
<HUAWEI> system-view
[~HUAWEI] multicast routing-enable
[*HUAWEI] interface LoopBack 0
[*HUAWEI] quit
[*HUAWEI] pim
[*HUAWEI-pim] c-rp loopback 0
[*HUAWEI-pim] c-rp advertisement-interval 30

```