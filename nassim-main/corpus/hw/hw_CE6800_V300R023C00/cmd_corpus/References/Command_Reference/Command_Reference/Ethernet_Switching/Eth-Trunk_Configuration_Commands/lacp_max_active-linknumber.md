lacp max active-linknumber
==========================

lacp max active-linknumber

Function
--------



The **lacp max active-linknumber** command sets the maximum number of active member links on an Eth-Trunk interface.

The **undo lacp max active-linknumber** command restores the maximum number of active member links on an Eth-Trunk interface to the default value.



By default, the maximum number of active member links is 256.


Format
------

**lacp max active-linknumber** *link-number*

**undo lacp max active-linknumber**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **active-linknumber** *link-number* | Specifies the maximum number of active member links. | The value is an integer ranging from 1 to 256. |



Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The number of active member links on an Eth-Trunk interface affects the status and bandwidth of the Eth-Trunk interface. The bandwidth of an Eth-Trunk interface equals the total bandwidth of all member interfaces in the Up state.To ensure the status and bandwidth of an Eth-Trunk interface, you can set the following thresholds to reduce the impact of changes in member link status:

* Setting the maximum number of active member linksAfter the number of active member links reaches the upper threshold, the bandwidth of the Eth-Trunk interface does not increase even if more member links go Up. Setting the maximum number of active member links improves network reliability on the basis of sufficient bandwidth.For example, an Eth-Trunk interface has 10 trouble-free member links, and each of them can provide the bandwidth of 1 Gbit/s. The Eth-Trunk interface needs to provide the maximum bandwidth of 5 Gbit/s. In this case, the upper threshold can be set to 5. Other links automatically enter the backup state. When one or more links of the selected five links go Down, backup links automatically start to work. This ensures the 5 Gbit/s bandwidth of the Eth-Trunk interface and improves the network reliability.
* Setting the minimum number of active member linksWhen the number of active member links decreases below the threshold, the Eth-Trunk interface goes Down. Setting the minimum number of active member links ensures the minimum bandwidth of an Eth-Trunk interface.For how to set the minimum number of active member links, see the **least active-linknumber** command.

**Prerequisites**



The **mode lacp-static** command has been run in the Eth-Trunk interface view to configure the Eth-Trunk interface to work in static Link Aggregation Control Protocol (LACP) mode.



**Configuration Impact**



If you run the lacp max active-linknumber command more than once, the latest configuration overrides the previous one.If the maximum number of active member links is set to a small value but the Eth-Trunk interface has many member interfaces, a majority of member interfaces are backup. This affects the bandwidth of the Eth-Trunk interface.



**Precautions**



If the **least active-linknumber** command has been configured before you run the max active-linknumber command, ensure that the maximum number of active member links is greater than or equal to the minimum number of active member links.In the scenario of interconnection with non-Huawei devices, especially in 1:1 mode, if the configured maximum numbers of active links at the two ends of an Eth-Trunk are both less than the number of active Eth-Trunk member interfaces, the link may be intermittently disconnected. As a result, the LACP negotiation fails and the Down Eth-Trunk cannot automatically go Up. Therefore, you are recommended to enable the priority preemption function at the two ends of an Eth-Trunk and configure a same preemption delay, or disable the limitation on the maximum number of active links.In 1:1 mode, the configured maximum number of active links at the two ends of an Eth-Trunk is 1 and each link has two member interfaces.




Example
-------

# Set the maximum number of active member links of Eth-Trunk 1 to 5.
```
<HUAWEI> system-view
[~HUAWEI] interface eth-trunk 1
[*HUAWEI-Eth-Trunk1] mode lacp-static
[*HUAWEI-Eth-Trunk1] lacp max active-linknumber 5

```