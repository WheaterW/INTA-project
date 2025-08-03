encoding
========

encoding

Function
--------



The **encoding** command configures an encoding format for data packets to be sent.

The **undo encoding** command restores the default encoding format for data packets to be sent.



By default, the encoding format is GPB.


Format
------

**encoding** { **gpb** | **json** }

**undo encoding**

**undo encoding** { **gpb** | **json** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **gpb** | Configures the GPB encoding format for data packets to be sent. | - |
| **json** | Configures the JSON encoding format for data packets to be sent. | - |



Views
-----

Subscription view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



When you create a gRPC-based static subscription, run the encoding command to configure an encoding format for data packets to be sent.



**Precautions**

When the encoding format of data packets to be sent is set to JSON:

* If the **json only-content** command is run and takes effect, the telemetry layer and service data layer of the data packets to be sent use the GPB and JSON encoding formats, respectively.
* If the **json only-content** command is not run, both the telemetry layer and service data layer of the data packets to be sent use the JSON encoding format.


Example
-------

# Configure the JSON encoding format for data packets to be sent.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] subscription test
[*HUAWEI-telemetry-subscription-test] encoding json

```