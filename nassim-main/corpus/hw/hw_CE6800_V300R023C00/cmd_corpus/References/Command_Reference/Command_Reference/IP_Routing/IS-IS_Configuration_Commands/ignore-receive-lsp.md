ignore-receive-lsp
==================

ignore-receive-lsp

Function
--------



The **ignore-receive-lsp** command configures the device to discard the specified LSP.

The **undo ignore-receive-lsp** command cancels the configuration of configuring the device to discard the specified LSP.



By default, the device is not configured to discard a specified LSP.


Format
------

**ignore-receive-lsp** { **system-id** *sysid* | **lsp-id** *lspid* }

**undo ignore-receive-lsp** { **system-id** *sysid* | **lsp-id** *lspid* }


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **system-id** *sysid* | Specifies an IS-IS system ID. | The value is in dotted decimal notation, ranging from 16 to 20 and in the format of ####.####.####.##, such as 0050.0500.5004.00. |
| **lsp-id** *lspid* | Specifies an LSP ID. | The value is in dotted decimal notation, ranging from 16 to 20 and in the format of ####.####.####.##-##, such as 0050.0500.5004.00-00. |



Views
-----

IS-IS view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

**Usage Scenario**

1. When devices on the entire network restart repeatedly due to abnormal LSPs and you have located the LSP that causes protocol restarts, you can configure this function as a last resort to prevent the device from restarting continuously.
2. If an LSP is identified as an attack packet, which is not supposed to appear in the local area, and the LSP has caused serious problems, such as device restarts, you can configure this function to filter out the LSP under the condition that the attack source cannot be located temporarily and that the LSP does not affect topology path computation.
3. If an LSP is identified as an attack packet, which is not supposed to appear in the local area, and it affects topology path computation and has caused serious problems, such as network-wide device restarts, you can configure this function on each device to discard the LSP to prevent it from participating in network-wide calculation. (Note: To filter out the LSP that affects topology path computation, ensure that it is filtered out of all LSDBs on the entire network. If it is filtered out of only some of LSDBs, routing loops may occur.)

**Configuration Impact**

If this command is incorrectly configured, services cannot be restored even if the **undo** command is run. In this case, you may need to reset the process to restore services.To filter out the LSP that affects topology path computation, you must ensure that it is removed from all the LSDBs on the entire network. Otherwise, routing loops may occur.This command is not recommended for the LSPs that actually exist on the network because normal LSPs may be filtered out.

**Precautions**

This command cannot be used to defend against attacks as it goes against protocol processing rules and affects services.As an attack LSP can have any key, it is difficult to defend against the LSP using this command. Therefore, you are advised to directly isolate the attack source.If the fault is caused by a bug, you are advised to run this command temporarily. After the patch is installed, run the **undo** command immediately and check whether services are affected. If services are affected, re-establish all neighbor relationships to restore services.


Example
-------

# Configure the device to discard a specified LSP.
```
<HUAWEI> system-view
[~HUAWEI] isis 1
[*HUAWEI-isis-1] ignore-receive-lsp lsp-id 0000.0000.0002.00-00

```