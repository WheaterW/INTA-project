display isis statistics updated-lsp
===================================

display isis statistics updated-lsp

Function
--------



The **display isis statistics updated-lsp** command displays statistics about updated LSPs on the network.




Format
------

**display isis** *process-id* **statistics** **updated-lsp** [ **history** ] [ **level-1** | **level-2** | **level-1-2** ]

**display isis statistics updated-lsp** [ **history** ] [ **level-1** | **level-2** | **level-1-2** ] [ *process-id* | **vpn-instance** *vpn-instance-name* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an IS-IS process ID. | The value is an integer ranging from 1 to 4294967295. |
| **updated-lsp** | Displays statistics of updated LSPs. | - |
| **history** | Displays statistics of recorded updated LSPs. | - |
| **level-1** | Displays statistics about an IS-IS Level-1 router. | - |
| **level-2** | Displays statistics of IS-IS Level-2. | - |
| **level-1-2** | Displays statistics of IS-IS Level-1-2. | - |
| **vpn-instance** *vpn-instance-name* | Displays mesh-group information about a specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To monitor the device status or locate faults, run the display isis statistics updated-lsp command to check statistics about updated LSPs on the network. The statistics help you diagnose faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the number of times that LSPs are updated on the current network.
```
<HUAWEI> display isis statistics updated-lsp

                      Updated-lsp statistics for ISIS( 1 )
                      ------------------------------------

                               Level-1 Statistics

Begin time: 2021-11-08 07:46:26

LSPID                         Count
----------------------------------------
2222.2222.2222.00-00          2
3333.3333.3333.00-00          4

Total LSP(s): 2
    *(By LSPID)-Self LSP, +-Self LSP(Extended)


                               Level-2 Statistics

Begin time: 2021-11-08 07:46:26

LSPID                         Count
----------------------------------------
2222.2222.2222.00-00          2
3333.3333.3333.00-00          4

Total LSP(s): 2
    *(By LSPID)-Self LSP, +-Self LSP(Extended)

```

**Table 1** Description of the **display isis statistics updated-lsp** command output
| Item | Description |
| --- | --- |
| Begin time | Start time. |
| Count | Number of LSP updates. |
| Total LSP(s) | Total number of LSPs. |