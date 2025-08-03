netstream export ip version
===========================

netstream export ip version

Function
--------



The **netstream export ip version** command configures the version number of the exported packets carrying IPv4 flow statistics.

The **undo netstream export ip version** command restores the default setting.



By default, the version number of the exported packets carrying IPv4 original flow statistics is 9 and no AS option is used.


Format
------

**netstream export ip version 5**

**netstream export ip version 9**

**undo netstream export ip version** [ **5** | **9** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **9** | Sets the version of exported packets carrying IPv4 flow statistics to V9. | - |
| **5** | Sets the version of exported packets carrying IPv4 flow statistics to V5. | - |



Views
-----

System view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The NDE exports NetStream flow statistics to the NSC. In order for the NSC to parse the exported packets, the version of exported packets carrying these statistics must be the same as that configured on the NSC.The exported packets in V5 have fixed format and are difficult to expand. In contrast, the format of exported packets in V9 is defined in templates and is easy to expand. The statistics can be exported flexibly in such packets.Due to its advantages of being template-based and highly extendable, V9 is supported by most NSCs. As such, you are advised to set the version of exported packets to V9.You can set the export version according to the NMS configuration. V9 must be used for the following exported packets:

* Exported packets need to carry IPv4 flexible flow statistics.
* The interface indexes carried in exported packets need to be extended from 16 bits to 32 bits.
* Statistics about MPLS IPv4 packets need to be collected.

**Precautions**

When the exported packets carry 32-bit interface indexes, the export version cannot be changed from V9 to V5.


Example
-------

# Set the version of the exported packets carrying IPv4 flow statistics to V9.
```
<HUAWEI> system-view
[~HUAWEI] netstream export ip version 9

```