system resource
===============

system resource

Function
--------



The **system resource** command configures the system forwarding resource mode.

The **undo system resource** command cancels the current system resource mode.



By default, the card forwarding resource mode is standard.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ.



Format
------

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE6860-SAN, CE6866, CE6860-HAM, CE6866K:

**system resource** { **standard** | **large-mac** | **user-defined** { **mac** *mac-value* } | **large-multicast** }

For CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K:

**system resource** { **standard** | **large-mac** | **large-route** | **balance** }

For CE8851-32CQ8DQ-P, CE8850-HAM, CE8850-SAN, CE8851K, CE8855, CE8851-32CQ4BQ, CE6860-SAN, CE6866, CE6860-HAM, CE6866K, CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**undo system resource**

For CE8855, CE8851-32CQ4BQ, CE6855-48XS8CQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode), CE6863E-48S8CQ, CE6885-SAN:

**system resource** { **standard** | **large-mac** | **large-route** | **large-multicast** | **large-flow** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **standard** | Sets the forwarding resource mode to standard. | - |
| **large-mac** | Sets the forwarding resource mode to large-mac. | - |
| **large-route** | Set the forwarding resource mode to large-route.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6881H, CE6881H-K, CE6820H, CE6820H-K, CE6820S, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **user-defined** | Sets the forwarding resource mode to user-defined.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM. | - |
| **mac** *mac-value* | Specifies the number of MAC addresses when the forwarding resource mode is user-defined.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM. | The value is an integer that ranges from 32 to 800. |
| **large-multicast** | Sets the forwarding resource mode to large multicast mode.  NOTE:  This parameter is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE6855-48XS8CQ, CE6885-SAN, CE8850-SAN, CE8855, CE8851-32CQ4BQ, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |
| **balance** | Sets the forwarding resource mode to load balancing.  NOTE:  This parameter is supported only on the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S. | - |
| **large-flow** | Set the forwarding resource mode to large-flow.  NOTE:  This parameter is supported only on the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ. | - |



Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

Typically, entry resources in a board are shared among services. If the standard or MAC address entries cannot meet service requirements, you can adjust the entry resource mode to obtain more configuration entries.

* large-mac: The large-mac mode increases the number of MAC address entries.
* large-route: The large routing table mode increases the routing table capacity.
* standard: standard is the default mode.
* user-defined: user-defined mode. You can configure a proper number of MAC address entries as required.
* balance: load balancing mode. After the load balancing mode is configured, elephant and mice flows can be configured on the corresponding board to differentiate elephant and mice flows in queues. In this manner, packets in mice flows are preferentially scheduled, and the delay of mice flows is not affected by elephant flows.
* large-multicast: The large multicast mode increases the capacity of the multicast forwarding table.
* large-flow: The large flow table mode increases the flow table capacity.
* large-user: The large-user mode increases the number of access users.

**Precautions**

* After changing the forwarding resource mode, run the save command to save the configuration and restart the device for the change to take effect.
* For the CE6820H, CE6820H-K, CE6820S, CE6863H, CE6863H-K, CE6881H, and CE6881H-K, elephant and mice flow scheduling can be configured only after the load balancing mode takes effect. To switch to another resource mode, you must delete the elephant and mice flow scheduling configuration and then delete the balancing mode configuration.
* In the following situations, the device is reset one more time to restore the resource mode consistency:
* After the mode is changed, the configuration is not saved to the configuration file, and then the device is restarted.
* After the configuration file is switched, the device is restarted, and the resource modes in the old and new configuration files are different.


Example
-------

# Set the system resource mode to standard.
```
<HUAWEI> system-view
[~HUAWEI] system resource standard
Info: Please save configuration before restart. The new resource mode will take effect after the system reboot, but resetting only one board will cause exceptions in resource allocation.

```