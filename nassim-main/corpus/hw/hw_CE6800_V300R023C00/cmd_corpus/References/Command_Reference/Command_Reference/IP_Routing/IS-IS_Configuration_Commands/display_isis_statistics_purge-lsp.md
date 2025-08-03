display isis statistics purge-lsp
=================================

display isis statistics purge-lsp

Function
--------



The **display isis statistics purge-lsp** command displays statistics about purge LSPs on the network.




Format
------

**display isis statistics purge-lsp** [ *process-id* | { **vpn-instance** *vpn-instance-name* } ] [ **level-1** | **level-2** ]

**display isis** [ *process-id* ] **statistics** **purge-lsp** [ **level-1** | **level-2** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | Specifies an IS-IS process. If process-id is not specified in the command, statistics about purge LSPs of all IS-IS processes are displayed. | The value is an integer ranging from 1 to 4294967295. |
| **vpn-instance** *vpn-instance-name* | Displays statistics of IS-IS purge LSPs about specified VPN instance. | The value is a string of 1 to 31 case-sensitive characters. It cannot contain spaces. The VPN instance name cannot be \_public\_. If the character string is quoted by double quotation marks, the character string can contain spaces. |
| **level-1** | Displays statistics about IS-IS Level-1 purge LSPs. | - |
| **level-2** | Displays statistics about IS-IS Level-2 purge LSPs. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

When monitoring the device status or locating a fault, you can run the **display isis statistics purge-lsp** command to check statistics about purge LSPs. The statistics help traffic statistics collection and troubleshooting.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics about purge LSPs.
```
<HUAWEI> display isis statistics purge-lsp

                      Statistics of Purge packets Received for ISIS(1)
                    ----------------------------------------------------

                                 Level-1 Statistics

Total Records:2

LSP ID                    Purge Count                                      Last Three Purge Times
--------------------------------------------------------------------------------------------------
0000.0000.0002.01-00                0                                                    --:--:--
0000.0000.0002.00-00                0                                                    --:--:--

                                 Level-2 Statistics

Total Records:2

LSP ID                    Purge Count                                      Last Three Purge Times
--------------------------------------------------------------------------------------------------
0000.0000.0002.01-00                0                                                    --:--:--
0000.0000.0002.00-00                0                                                    --:--:--

```

**Table 1** Description of the **display isis statistics purge-lsp** command output
| Item | Description |
| --- | --- |
| Purge Count | Number of times purge LSPs are received. 0 indicates that no purge LSPs are received. |
| Total Records | Records number. |
| LSP ID | LSP ID. |
| Last Three Purge Times | Time when the system received the latest three purge LSPs. If the system does not receive any purge LSP, --:--:-- is displayed. |