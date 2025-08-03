isis lsp seq-overflow auto-recover disable
==========================================

isis lsp seq-overflow auto-recover disable

Function
--------



The **isis lsp seq-overflow auto-recover disable** command prevents an IS-IS system from changing its system ID when it receives a locally generated LSP with the maximum sequence number (0xFFFFFFFF).

The **undo isis lsp seq-overflow auto-recover disable** command restores the default configuration.



By default, an IS-IS system changes its system ID when it receives a locally generated LSP with the maximum sequence number.


Format
------

**isis lsp seq-overflow auto-recover disable**

**undo isis lsp seq-overflow auto-recover disable**


Parameters
----------

None

Views
-----

System view


Default Level
-------------

2: Configuration level


Usage Guidelines
----------------

On an IS-IS network, if a device receives a locally generated LSP and finds that the sequence number of the LSP is later than that of the existing LSP, IS-IS increases the sequence number of the LSP by 1 and floods the LSP. If malicious attack packets exist on the network, the device sets the sequence number of IS-IS LSPs to the maximum value 0xFFFFFFFF, encapsulates the system ID of the target device, and sends the LSPs to the target device. After the target device receives the LSPs with the sequence number 0xFFFFFFFF, because the system ID in the LSP is the same as that of the local device, the IS-IS system considers that the locally generated LSP is received. In addition, the sequence number of the LSP is newer than that of the local LSP. In this case, the IS-IS system increases the sequence number of the LSP by 1 because the sequence number of the LSP reaches the maximum value; if the value is increased by 1, the IS-IS system sleeps for a maximum of 18 hours and 1 minute, affecting the normal operation of the network. To solve this problem, when IS-IS detects that the sequence number of the local LSP is 0xFFFFFFFF, IS-IS automatically changes the system ID of the local device. If the local device still generates the LSP after three changes, IS-IS does not change the system ID and directly enters the sleep state. The system ID can be changed three times every 24 hours.The preceding situations also apply to CSNPs and PSNPs.By default, this function is enabled for IS-IS. If this function is not required, run the **isis lsp seq-overflow auto-recover disable** command to disable it. If this function is disabled, services may be interrupted.


Example
-------

# Prevent an IS-IS system from changing its system ID when it receives a locally generated LSP with the maximum sequence number (0xFFFFFFFF).
```
<HUAWEI> system-view
[~HUAWEI] isis lsp seq-overflow auto-recover disable

```