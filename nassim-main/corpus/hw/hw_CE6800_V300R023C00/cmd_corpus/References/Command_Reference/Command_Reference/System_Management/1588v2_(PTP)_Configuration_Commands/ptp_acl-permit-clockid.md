ptp acl-permit-clockid
======================

ptp acl-permit-clockid

Function
--------



The **ptp acl-permit-clockid** command enables a 1588v2 device to use a clock with the specified clock ID to calculate the local best master clock (BMC).

The **undo ptp acl-permit-clockid** command disables a 1588v2 device from using a clock with the specified clock ID to calculate the local BMC.



By default, after access control of clock sources is enabled, no clock source participates in clock source selection if the clock ID range allowed to participate in clock source selection is not configured.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H-48S6CQ, CE6881H-48S6CQ-K, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

**ptp acl-permit-clockid** *clockid-value*

**undo ptp acl-permit-clockid** *clockid-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *clockid-value* | Specifies a clock source ID. | The value is an 8-byte hexadecimal integer ranging from 0 to ffffffffffffffff. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To prevent network-wide clock flapping caused by malicious clock attacks or incorrect configurations, you can specify the clock source selection range for 1588v2 devices in advance. Then, the 1588v2 clock source is selected only from the configured clock ID list.

**Prerequisites**

Access control of clock sources has been enabled using the **ptp acl enable** command.

**Precautions**

Run the **display ptp all** command on the device to view clock IDs of clock sources.


Example
-------

# Allow the local device to use the clock source with the clock ID 0000000000001234 to calculate the local BMC.
```
<HUAWEI> system-view
[~HUAWEI] ptp acl enable
[*HUAWEI] ptp acl-permit-clockid 0000000000001234

```