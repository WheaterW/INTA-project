active port-license
===================

active port-license

Function
--------



The **active port-license** command activates a hardware license for an interface.



By default, the license is not activated.


Format
------

**active port-license** *license-type* **interface** { { *interface-name1* | *interface-type1* *interface-number1* } [ **to** { *interface-name2* | *interface-type2* *interface-number2* } ] } &<1-12>

**undo active port-license** *license-type* **interface** { { *interface-name1* | *interface-type1* *interface-number1* } [ **to** { *interface-name2* | *interface-type2* *interface-number2* } ] } &<1-12>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *license-type* | Specifies the license type of an interface. | The options are as follows:   * 25G * 50G * 200G * 400G |
| **interface** | Indicates an interface. | - |
| *interface-name1* | Specifies the name of an interface. | You can enter a question mark (?) and select a value based on the prompt. |
| *interface-type1* | Specifies the interface type. | The value must be set according to the device configuration. |
| *interface-number1* | Specifies an interface number. | You can enter a question mark (?) and select a value based on the prompt. |
| **to** | Indicates a value range. | - |
| *interface-name2* | Specifies the name of an interface. | - |
| *interface-type2* | Specifies the type of an interface. | - |
| *interface-number2* | Specifies an interface number. | The value of interface-number2 must not be less than that of interface-number1. |



Views
-----

License view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**



You can purchase hardware licenses on demand to reduce the initial investment. In the future, you can purchase hardware licenses for capacity expansion as services increase, facilitating flexible consumption.



You can purchase hardware licenses on demand to reduce the initial investment. In the future, you can purchase hardware licenses for capacity expansion as services increase, facilitating flexible consumption.For example, the 8\*100G+24\*25G license is enabled on the CE6860-SAN(8\*100G+48\*25G) board by default.

* You can purchase one 24\*25G port enabling RTU to enable the remaining 24 ports.
* You can purchase one more 24/\*50G capacity upgrade RTU to upgrade the capacity of 24 ports from 25G to 50G.
* You can purchase one more 24/\*50G capacity upgrade RTU to upgrade the capacity of the remaining 24 ports from 25G to 50G.
* You can purchase another 8\*200G capacity upgrade RTU to pugrade the capacity of eight ports from 100G to 200G.

**Precautions**



The device activates licenses by interface group. The specific interface group is related to the license control item.If only some interfaces are specified during the configuration, the device automatically supplements the interfaces in the same group and delivers the configuration, and displays the range of activated interfaces.




Example
-------

# Activate the 200G capability on a port after the license is purchased.
```
<HUAWEI> system-view
[~HUAWEI] license
[~HUAWEI-license] active port-license 200G interface 100ge1/0/1

```