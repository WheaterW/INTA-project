ip option disable
=================

ip option disable

Function
--------



The **ip option disable** command disables the system from processing IP packets with route options.

The **undo ip option disable** command enables the system to process IP packets with route options.



By default, the system processes IP packets with route options.


Format
------

**ip option** { **route-alert** | **route-record** | **source-route** | **time-stamp** } **disable**

**undo ip option** { **route-alert** | **route-record** | **source-route** | **time-stamp** } **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **route-alert** | Enables the system to process IP packets with the route-alert option. | - |
| **route-record** | Enables the system to process IP packets with the route-record option. | - |
| **source-route** | Enables the system to process IP packets with the source-route option. This option determines the path along which packets are transmitted. | - |
| **time-stamp** | Enables the system to process IP packets with the time-stamp option. This option calculates the time spent on packet transmission and processing. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

IP packets can carry the following route options:

* Route-alert
* Route-record
* Source-route
* Time-stampGenerally, these options are used for diagnosing network paths and temporarily transmitting special services. These options, however, may be used by attackers to spy on the network structure for initiating attacks. Therefore, you need to run the ip option enable command to enable the system to process IP packets with route options or run the undo ip option enable command to disable the system from processing IP packets with route options.By default, the system processes IP packets with route options. To prevent attacks that make use of IP packets with route options, disable the system from processing IP packets with route options.

**Configuration Impact**



After the system is disabled from processing IP packets with route options, the system collects only statistics about discarded packets.



**Precautions**



If the network status is normal and the system is required to process IP packets with route options, run the **undo ip option disable** command.Route priorities configured in the interface view take precedence over those configured in the system view.The execution of the **ip option disable** command may affect the CPU processing of IP packets that carry the corresponding routing entries. For example, after the **ip option route-alert disable** command is run, the CPU processing of RSVP-TE packets is affected.




Example
-------

# Disable the system to process IP packets with the Rqoute-alert option.
```
<HUAWEI> system-view
[~HUAWEI] ip option route-alert disable

```