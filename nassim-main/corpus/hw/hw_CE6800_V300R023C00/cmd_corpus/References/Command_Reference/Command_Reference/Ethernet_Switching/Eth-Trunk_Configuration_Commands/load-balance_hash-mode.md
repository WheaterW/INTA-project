load-balance hash-mode
======================

load-balance hash-mode

Function
--------



The **load-balance hash-mode** command configures the hash algorithm for load balancing on an Eth-Trunk interface.

The **undo load-balance hash-mode** command restores the default hash algorithm for load balancing on an Eth-Trunk interface.



By default, the hash algorithm value for load balancing on an Eth-Trunk interface is 1.

![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**load-balance hash-mode** *hash-mode-value*

**undo load-balance hash-mode** [ *hash-mode-value* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *hash-mode-value* | The value of hash mode. | The value is an integer that ranges from 1 to 9. The default value is 1. |



Views
-----

Eth-Trunk interface view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

The load-balance hash-mode command configures the hash algorithm for load balancing on an Eth-Trunk interface. The **undo load-balance** command restores the default hash algorithm for load balancing on an Eth-Trunk interface.

* If source IP and MAC addresses in packets change frequently, you are advised to set hash-mode to 8.
* If source or destination MAC addresses in packets change frequently, you are advised to set hash-mode to 9.
* If source and destination IP addresses in packets change frequently, you are advised to set hash-mode to 8.
* If destination MAC and IP addresses in packets change frequently, you are advised to set hash-mode to 1 or 7.
* If source MAC addresses in packets change frequently, you are advised to set hash-mode to 1, 2, or 7.
* If destination IP addresses in packets change frequently, you are advised to set hash-mode to 7.
* If source IP addresses in packets change frequently, you are advised to set hash-mode to 1, 7, or 9.Other values of hash-mode-id are used when incoming traffic is uneven. In this case, the default hash algorithm is recommended.

Example
-------

# Configure a hash algorithm for load balancing on an Eth-Trunk interface.
```
<HUAWEI> system-view
[~HUAWEI] interface Eth-Trunk 1
[*HUAWEI-Eth-Trunk1] load-balance hash-mode 2

```