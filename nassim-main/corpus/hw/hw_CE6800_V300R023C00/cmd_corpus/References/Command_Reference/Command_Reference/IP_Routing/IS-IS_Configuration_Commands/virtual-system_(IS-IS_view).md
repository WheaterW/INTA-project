virtual-system (IS-IS view)
===========================

virtual-system (IS-IS view)

Function
--------



The **virtual-system** command configures the virtual system ID for an IS-IS process.

The undo virtual system virtual-system-id command deletes the virtual system ID.



By default, there is no virtual system ID for an IS-IS process.


Format
------

**virtual-system** *virtual-system-id*

**undo virtual-system** *virtual-system-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *virtual-system-id* | Specifies a virtual system ID for an IS-IS process. | The length is 6 bytes (48 bits), and the format is XXXX.XXXX.XXXX. |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **virtual-system** command is used to set a virtual system ID for an IS-IS process. If no virtual system ID exists, no extended LSPs are generated.The virtual ID must be unique in the entire area.The **virtual-system** command is used together with the lsp-fragments-extend command. The configured virtual system ID takes effect only after LSP fragment extension is enabled.If LSP fragment extension is not enabled, virtual system IDs can be configured, but they do not take effect.

**Configuration Impact**

After LSP fragment extension is configured, if information is lost because of LSP overflow, the system restarts the IS-IS process. After the IS-IS process is restarted, the system tries its best to load and package routing information. The excessive routing information that is beyond the forwarding capability of the system is placed into the LSPs of virtual systems. In addition, when a virtual system that is used to load routing information is deleted, the system automatically restarts the IS-IS process.


Example
-------

# Configure virtual system ID 2222.2222.2222 for IS-IS process 1.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] network-entity 10.0001.1010.1020.1030.00
[*HUAWEI-isis-1] virtual-system 2222.2222.2222

```