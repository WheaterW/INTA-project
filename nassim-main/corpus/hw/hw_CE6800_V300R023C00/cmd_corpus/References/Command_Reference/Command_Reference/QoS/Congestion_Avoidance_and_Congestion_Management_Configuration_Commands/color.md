color
=====

color

Function
--------



The **color** command sets parameters of a WRED drop profile, including the absolute values of upper and lower drop thresholds, upper drop threshold, lower drop threshold, and maximum drop probability.

The **undo color** command restores the default settings of a WRED drop profile.



By default, the upper drop threshold, lower drop threshold, and maximum drop probability of a WRED drop profile are all 100, and absolute values of upper and lower drop thresholds are not configured.


Format
------

**color** { **green** | **red** | **yellow** } { **buffer-size** **low-limit** *low-buffer-size* **high-limit** *high-buffer-size* | **buffer-size** **cell** **low-limit** *low-buffer-size-cell* **high-limit** *high-buffer-size-cell* | **low-limit** *low-limit-percentage* **high-limit** *high-limit-percentage* } **discard-percentage** *discard-percentage*

**undo color** { **green** | **red** | **yellow** }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **high-limit** *high-buffer-size* | Specifies the absolute value of the upper drop threshold. When the length of packets in a queue reaches this value, all subsequent packets are discarded. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from low-buffer-size to 34078720, in bytes.  For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM:The value is an integer that ranges from low-buffer-size to 16000000, in bytes.  For the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S:The value is an integer that ranges from low-buffer-size to 36000000, in bytes.  For the CE6885-LL (low latency mode):The value is an integer that ranges from low-buffer-size to 10223616, in bytes. |
| **high-limit** *high-buffer-size-cell* | Specifies the absolute value of the upper drop threshold. The unit is cell. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from low-buffer-size-cell to 106496.  For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S:The value is an integer that ranges from low-buffer-size-cell to 125000. |
| **high-limit** *high-limit-percentage* | Specifies the upper drop threshold. When the percentage of the packet count in a queue to the queue length reaches this value, all subsequent packets are discarded. | The value is an integer that ranges from low-limit-percentage to 100. The default value is 100. |
| **discard-percentage** *discard-percentage* | Specifies the maximum drop probability. | The value is an integer that ranges from 1 to 100. The default value is 100. |
| **green** | Indicates WRED parameters for green packets. | - |
| **red** | Indicates WRED parameters for red packets. | - |
| **yellow** | Indicates WRED parameters for yellow packets. | - |
| **low-limit** *low-buffer-size* | Specifies the absolute value of the lower drop threshold. When the length of packets in a queue reaches this value, packets start to be discarded. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 320 to 34078720, in bytes.  For the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM:The value is an integer that ranges from 128 to 16000000, in bytes.  For the CE6863H, CE6863H-K, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S:The value is an integer that ranges from 288 to 36000000, in bytes.  For the CE6885-LL (low latency mode):The value is an integer that ranges from 96 to 10223616, in bytes. |
| **low-limit** *low-buffer-size-cell* | Specifies the absolute value of the lower drop threshold. The unit is cell. | For the CE6855-48XS8CQ, CE6885-SAN, CE8855, CE8851-32CQ4BQ, CE6885-LL (low latency mode), CE6885, CE6885-T, CE6885-LL (standard forwarding mode) and CE6863E-48S8CQ:The value is an integer that ranges from 1 to 106496.  For the CE6863H, CE6863H-K, CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P, CE8850-HAM, CE6881H, CE6881H-K, CE6820H, CE6820H-K and CE6820S:The value is an integer that ranges from 1 to 125000. |
| **low-limit** *low-limit-percentage* | Specifies the lower drop threshold. When the percentage of the packet count in a queue to the queue length reaches this value, packets start to be discarded. | The value is an integer in the range from 0 to 100. The default value is 100. |
| **buffer-size** | Specifies the absolute value of the WRED threshold. | - |
| **cell** | Specifies that the absolute value of the WRED threshold is in cells. If this parameter is not specified, the absolute value of the WRED threshold is in bytes. | - |



Views
-----

Drop profile view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

When packets enter a device, the packets are colored based on the mapping in a DiffServ domain. The system processes packets with different colors based on the WRED configuration.When upper and lower drop thresholds in percentage are used:

* When the queue length reaches the lower drop threshold, some packets are discarded.
* When the queue length is between the lower drop threshold and the upper drop threshold, a longer queue linearly increases the drop probability until the maximum drop probability is reached.
* When the queue length reaches the upper drop threshold, all subsequent packets in the queue are discarded.When absolute values of upper and lower drop thresholds are used:
* When the queue length reaches the absolute value of the lower drop threshold, some packets are discarded.
* When the queue length is between absolute values of lower and upper drop thresholds, a longer queue linearly increases the drop probability until the maximum drop probability is reached.
* When the queue length reaches the absolute value of the upper drop threshold, all subsequent packets in the queue are discarded.When congestion occurs, packets with the highest drop probability are discarded first.

**Precautions**



If you run the **color** command multiple times in the same drop profile view, only the latest configuration takes effect.




Example
-------

# Configure WRED drop profile wred1 in which the lower drop threshold, upper drop threshold, and maximum drop probability are set to 80, 100, and 10 for green packets, to 60, 80, and 20 for yellow packets, and to 40, 60, and 40 for red packets.
```
<HUAWEI> system-view
[~HUAWEI] drop-profile wred1
[*HUAWEI-drop-wred1] color green low-limit 80 high-limit 100 discard-percentage 10
[*HUAWEI-drop-wred1] color yellow low-limit 60 high-limit 80 discard-percentage 20
[*HUAWEI-drop-wred1] color red low-limit 40 high-limit 60 discard-percentage 40

```