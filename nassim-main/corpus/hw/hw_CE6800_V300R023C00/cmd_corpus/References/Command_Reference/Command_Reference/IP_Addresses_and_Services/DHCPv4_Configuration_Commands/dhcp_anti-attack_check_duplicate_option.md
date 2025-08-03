dhcp anti-attack check duplicate option
=======================================

dhcp anti-attack check duplicate option

Function
--------



The **dhcp anti-attack check duplicate option** command enables the device to check and discard DHCP messages with duplicate options.

The **undo dhcp anti-attack check duplicate option** command disables the device from checking and discarding DHCP messages with duplicate options.



By default, the device is disabled from checking and discarding DHCP messages with duplicate options.


Format
------

**dhcp anti-attack check duplicate option** [ *option-start* [ **to** *option-end* ] ] &<1-254>

**undo dhcp anti-attack check duplicate option** [ *option-start* [ **to** *option-end* ] ] &<1-254>


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *option-start* | Specifies the option value.  option-start: Specifies the start value of an option in a DHCP packet. | The value is an integer ranging from 1 to 254. For an option, the end value must be larger than the start value. |
| **to** *option-end* | Specifies the option value.  option-end: Specifies the end value of an option in a DHCP packet. | The value is an integer ranging from 1 to 254. For an option, the end value must be larger than the start value. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The dhcp anti-attack check duplicate option command applies to DHCP servers, DHCP relay agents, and DHCP clients. To discard DHCP messages with duplicate options 1 to 254, run the dhcp anti-attack check duplicate option command.

**Prerequisites**

DHCP has been enabled using the **dhcp enable** command.


Example
-------

# Configure the device to discard DHCP messages with duplicate options.
```
<HUAWEI> system-view
[~HUAWEI] dhcp enable
[*HUAWEI] dhcp anti-attack check duplicate option

```