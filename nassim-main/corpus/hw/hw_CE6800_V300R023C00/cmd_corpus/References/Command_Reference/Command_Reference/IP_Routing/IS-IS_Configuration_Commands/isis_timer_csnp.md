isis timer csnp
===============

isis timer csnp

Function
--------



The **isis timer csnp** command configures an interval at which CSNPs are sent on the broadcast network.

The **undo isis timer csnp** command restores the default value.



By default, the interval at which CSNPs are sent is 10 seconds.


Format
------

**isis timer csnp** *csnp-interval* [ **level-1** | **level-2** ]

**undo isis timer csnp** [ *csnp-interval* ] [ **level-1** | **level-2** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *csnp-interval* | Specifies an interval at which CSNPs are sent on a broadcast network. | The value is an integer ranging from 1 to 65535, in seconds. |
| **level-1** | Indicates the interval at which Level-1 CSNPs are sent. | - |
| **level-2** | Indicates the interval at which Level-2 CSNPs are sent.  If neither Level-1 nor Level-2 is specified, by default, the interval at which the CSNPs of the current level are sent is set. | - |



Views
-----

100GE interface view,10GE sub-interface view,10GE interface view,200GE interface view,25GE sub-interface view,25GE interface view,400GE interface view,50GE sub-interface view,50GE interface view,Eth-Trunk sub-interface view,Eth-Trunk interface view,Loopback interface view,Tunnel interface view,VBDIF interface view,VLANIF interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

On a broadcast network, a DIS sends CSNPs periodically to enable all devices to synchronize LSDBs with one another. If a device finds that the local LSDB does not have a specific LSP or an existing LSP is not the latest one after the device has received a CSNP, the device will send a PSNP to request the corresponding LSP.The interval at which CSNPs are sent can be configured using the **isis timer csnp** command.

**Configuration Impact**

The IS-IS route convergence speed depends on the LSDB synchronization speed. Therefore, reducing the interval at which CSNPs are sent can speed up LSDB synchronization and IS-IS route convergence. If the interval is set too small, the DIS will send CSNPs frequently. This causes high CPU, memory, and network bandwidth usage and affects services.

**Precautions**

Only the DIS can periodically send CSNPs. This command is valid only for the device that is elected as the DIS. The DIS can be a Level-1 and Level-2 DIS, and the intervals at which CSNPs are sent must be set respectively.If the **isis circuit-type** command is run to emulate an interface as a P2P interface, the **isis timer csnp** command becomes invalid on the interface; after the **undo isis circuit-type** command is run to restore the broadcast interface, the interval at which CSNPs are sent is restored to the default value.


Example
-------

# Set Level-2 CSNPs to be transmitted every 15 seconds on Gigabit 100GE1/0/1.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] quit
[*HUAWEI] interface 100GE1/0/1
[*HUAWEI-100GE1/0/1] undo portswitch
[*HUAWEI-100GE1/0/1] isis enable 1
[*HUAWEI-100GE1/0/1] isis timer csnp 15 level-2

```