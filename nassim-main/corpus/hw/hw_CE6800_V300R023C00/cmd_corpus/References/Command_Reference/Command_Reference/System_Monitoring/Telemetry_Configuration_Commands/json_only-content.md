json only-content
=================

json only-content

Function
--------



The **json only-content** command configures the telemetry layer and service data layer of the data packets to be sent to use the GPB and JSON encoding formats respectively when a telemetry static or dynamic subscription uses the JSON encoding format.

The **undo json only-content** command configures both the telemetry layer and service data layer of the data packets to be sent to use the JSON encoding format when a telemetry static or dynamic subscription uses the JSON encoding format.



By default, when a telemetry static or dynamic subscription uses the JSON encoding format, both the telemetry layer and service data layer of the data packets to be sent use the JSON encoding format.


Format
------

**json only-content**

**undo json only-content**


Parameters
----------

None

Views
-----

Telemetry view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

When a telemetry static or dynamic subscription uses the JSON encoding format to send data packets, you can run the json only-content command to control the encoding format used by the telemetry layer and service data layer of the data packets to be sent.

**Precautions**

When you upgrade the system to a version that contains the json only-content command for the first time and a telemetry static subscription has been configured to use the JSON encoding format:

* If the **encoding json** command is configured for any static subscription in the source version and takes effect, the json only-content command configuration is automatically added to the corresponding system to ensure that the telemetry layer and service data layer of the data packets to be sent use the GPB and JSON encoding formats respectively.
* If the **encoding json** command is not configured for any static subscription in the source version, the json only-content command configuration is not automatically added to the corresponding system. In this case, both the telemetry layer and service data layer of the data packets to be sent use the JSON encoding format.


Example
-------

# Configure the telemetry layer and service data layer of the data packets to be sent to use the GPB and JSON encoding formats respectively when a telemetry static or dynamic subscription uses the JSON encoding format.
```
<HUAWEI> system-view
[~HUAWEI] telemetry
[~HUAWEI-telemetry] json only-content

```