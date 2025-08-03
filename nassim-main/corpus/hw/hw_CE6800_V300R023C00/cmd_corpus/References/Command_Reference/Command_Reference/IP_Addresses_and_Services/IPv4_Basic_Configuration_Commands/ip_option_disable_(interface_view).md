ip option disable (interface view)
==================================

ip option disable (interface view)

Function
--------



The **ip option disable** command disables the system to process IP packets with route options.

The **undo ip option disable** command enables the system from processing IP packets with route options.



By default, the system processes IP packets with route options.


Format
------

**ip option** { **route-alert** | **route-record** | **source-route** | **time-stamp** } **disable**

**ip option** { **route-alert** | **route-record** | **source-route** | **time-stamp** } **inherent-global**

**undo ip option** { **route-alert** | **route-record** | **source-route** | **time-stamp** } **disable**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **route-alert** | Enables the system to process IP packets with the route-alert option. | - |
| **route-record** | Enables the system to process IP packets with the route-record option. | - |
| **source-route** | Enables the system to process IP packets with the source-route option. This option determines the path along which packets are transmitted. | - |
| **time-stamp** | Enables the system to process IP packets with the time-stamp option. This option calculates the time spent on packet transmission and processing. | - |
| **inherent-global** | Clears the configuration on an interface and restores the configuration of processing IP packets with route options on the interface to the system configuration. This parameter can be configured only in the interface view. | - |



Views
-----

100ge sub-interface view,100GE interface view,10GE sub-interface view,10GE interface view,1200ge sub-interface view,200GE sub-interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE sub-interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view,Management interface view


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

**Precautions**

When the network status is normal, you can run the **undo ip option disable** command to enable the system to process IP packets with route options.The route configured in the interface view takes precedence over the route configured in the system view.After the **ip option disable** command is run, the processing of IP packets carrying the corresponding route option may be affected.


Example
-------

# Disable the system to process IP packets with the Route-Alert option.
```
<HUAWEI> system-view
[~HUAWEI] interface 100GE 1/0/1
[~HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] ip option route-alert disable

```