ip route-static default-bfd
===========================

ip route-static default-bfd

Function
--------



The **ip route-static default-bfd** command sets the global BFD parameters for a static route.

The **undo ip route-static default-bfd** command cancels the global BFD parameters of a static route.



By default, the minimum intervals at which BFD packets are received and sent is 1000 ms, and the detection time multiplier is 3.


Format
------

**ip route-static default-bfd** { **min-rx-interval** *min-rx-interval* | **min-tx-interval** *min-tx-interval* | **detect-multiplier** *multiplier* } \*

**undo ip route-static default-bfd**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **min-rx-interval** *min-rx-interval* | Specifies the minimum interval at which BFD packets are received. | The value is an integer ranging from 3 to 1000, in milliseconds. |
| **min-tx-interval** *min-tx-interval* | Specifies the minimum interval at which BFD packets are sent. | The value is an integer ranging from 3 to 1000, in milliseconds. |
| **detect-multiplier** *multiplier* | Specifies the detection time multiplier. | The value is an integer ranging from 3 to 50. |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

To modify BFD parameters for static routes, run the **ip route-static default-bfd** command.

**Configuration Impact**

* If BFD parameters are not configured for a static route, the default values set using the **ip route-static default-bfd** command are used.
* After the values of global BFD parameters are changed, you need to change the values of BFD parameters corresponding to all the static routes that use default values of BFD parameters.

**Precautions**

After the values of global BFD parameters are changed, the values of BFD parameters corresponding to all the static routes that use default values of BFD parameters are changed.


Example
-------

# Set the global minimum interval at which BFD packets are received to 300 ms for static routes.
```
<HUAWEI> system-view
[~HUAWEI] ip route-static default-bfd min-rx-interval 300

```