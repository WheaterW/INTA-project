bandwidth-reference (IS-IS view)
================================

bandwidth-reference (IS-IS view)

Function
--------



The **bandwidth-reference** command sets a bandwidth reference value that is used when the system automatically calculates the interface cost.

The **undo bandwidth-reference** command deletes the bandwidth reference value.

The **ipv6 bandwidth-reference** command sets a bandwidth reference value used in interface cost calculation.

The **undo ipv6 bandwidth-reference** command restores the default value.



By default, the bandwidth reference value is 100 Mbit/s.


Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN, CE6885-LL (low latency mode):

**bandwidth-reference** *value*

**undo bandwidth-reference**

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**ipv6 bandwidth-reference** *value*

**undo ipv6 bandwidth-reference**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *value* | Specifies a bandwidth reference value. | The value is an integer ranging from 1 to 2147483648, in Mbit/s. |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

You can configure a link cost for all interfaces or enable automatic interface cost calculation. To enable automatic interface cost calculation, you need to set a proper bandwidth reference value.

**Prerequisites**



An IS-IS process has been created.



**Configuration Impact**



You can run this command to set a proper reference bandwidth value. After automatic interface cost calculation is enabled, if the cost type is wide or wide-compatible, the system automatically calculates the interface cost based on the bandwidth reference value set using this command. The formula for calculating the interface cost is as follows: Interface cost = (Bandwidth-reference/Interface bandwidth) x 10. If the interface cost calculated through this formula is greater than 16777214, 16777214 is used as the interface cost for route calculation. That is, the interface cost will never be greater than 16777214.To enable automatic interface cost calculation, run the **auto-cost enable** command. To set the cost style, run the **cost-style** command.You can run this command to set a proper reference bandwidth value. After automatic interface cost calculation is enabled, the system automatically calculates the interface cost based on the bandwidth reference value set using the bandwidth-reference command.



**Precautions**



Set a proper bandwidth reference value.




Example
-------

# Set IPv6 reference bandwidth used in interface cost calculation to 200 Mbit/s.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] ipv6 enable
[*HUAWEI-isis-1] ipv6 bandwidth-reference 200

```

# Set the bandwidth reference value to 1000 Mbit/s.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] bandwidth-reference 1000

```