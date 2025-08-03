lsp-fragments-extend
====================

lsp-fragments-extend

Function
--------



The **lsp-fragments-extend** command enables LSP fragment extension on an IS-IS device in a specified mode and at a specified level. To enable the device to generate extended LSP fragments, at least one virtual system ID must be configured.

The **undo lsp-fragments-extend** command disables the function.



By default, the LSP fragment extension on an IS-IS device is disabled.


Format
------

**lsp-fragments-extend** [ [ **level-1** | **level-2** | **level-1-2** ] | [ **mode-1** | **mode-2** ] ] \*

**undo lsp-fragments-extend** [ [ **level-1** | **level-2** | **level-1-2** ] | [ **mode-1** | **mode-2** ] ] \*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **level-1** | Enables LSP fragment extension at Level-1. | - |
| **level-2** | Enables LSP fragment extension at Level-2. | - |
| **level-1-2** | Enables LSP fragment extension at Level-1-2. | - |
| **mode-1** | Enables the device to be compatible with a device that does not support LSP fragment extension. | - |
| **mode-2** | Indicates a fragment extension mode that requires LSP fragment extension on all devices.  By default, mode-1 and level-1-2 are used. | - |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

The **lsp-fragment-extend** command enables LSP fragment extension on an IS-IS device in a specified mode and at a specified level. One LSP fragment number occupies only one byte and therefore a maximum of 256 fragments are supported. If there are a great number of LSPs and the number of fragments exceeds 256, some information is lost. Therefore, the fragment extension function is introduced. You can run the **virtual-system** command to configure one or more virtual system nodes for the IS-IS process on the local system so that the number of LSPs exceeds 256.

**Prerequisites**

Virtual systems have been configured using the **virtual-system** command.

**Configuration Impact**

After LSP fragment extension is configured, if the number of LSP fragments exceeds 256, the excessive LSP fragments are forwarded by virtual systems.


Example
-------

# Enable LSP fragment extension in mode-1 at Level-2.
```
<HUAWEI> system-view
[~HUAWEI] isis
[*HUAWEI-isis-1] network-entity 00.1111.1111.1111.00
[*HUAWEI-isis-1] virtual-system 2222.2222.2222
[*HUAWEI-isis-1] lsp-fragments-extend mode-1 level-2

```