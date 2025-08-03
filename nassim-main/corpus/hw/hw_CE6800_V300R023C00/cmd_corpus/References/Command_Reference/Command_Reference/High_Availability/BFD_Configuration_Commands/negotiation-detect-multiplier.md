negotiation-detect-multiplier
=============================

negotiation-detect-multiplier

Function
--------



The **negotiation-detect-multiplier** command sets the detection multiplier during BFD negotiation.

The **undo negotiation-detect-multiplier** command cancels the specified detection multiplier during BFD negotiation.



By default, the detection multiplier for BFD packet sending is not specified. The default value is 50.


Format
------

**negotiation-detect-multiplier** *detect-multiplier-value*

**undo negotiation-detect-multiplier** *detect-multiplier-value*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *detect-multiplier-value* | Specifies the detection multiplier during BFD negotiation. | The value is an integer ranging from 3 to 50. The default value is 50, indicating that the default detection multiplier 50 is used during BFD negotiation. |



Views
-----

BFD view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

In scenarios where Huawei devices interwork with non-Huawei devices, the default detection multiplier is 50. Some non-Huawei devices cannot identify packets with the detection multiplier of 50. In this scenario, you need to manually configure the detection multiplier supported by the non-Huawei device so that the Huawei device can communicate with the non-Huawei device.


Example
-------

# Set the BFD detection multiplier to 15.
```
<HUAWEI> system-view
[~HUAWEI] bfd
[*HUAWEI-bfd] negotiation-detect-multiplier 15

```