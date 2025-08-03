display fwm dldp statistics
===========================

display fwm dldp statistics

Function
--------



The **display fwm dldp statistics** command displays statistics about the DLDP module on a specified board.




Format
------

**display fwm dldp statistics** [ **all** ] **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **all** | Indicates all statistics (including the statistics whose value is 0). | - |
| **slot** *slot-id* | Specifies a slot ID. | The value is a string of case-sensitive characters. It cannot contain spaces. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check service delivery of the DLDP module, run the **display fwm dldp statistics** command. This command displays statistics in a list. Each line indicates a piece of statistics.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display all statistics about the DLDP module in slot 1.
```
<HUAWEI> display fwm dldp statistics all slot 1
Id     Statistic description                    Counter           Last timestamp
--------------------------------------------------------------------------------
1      Write cfg_dldp_entry success                   2  09-26-2022 10:24:04.681
2      Write cfg_dldp_entry fail                      0  00-00-0000 00:00:00.000
3      Read cfg_dldp_entry success                    0  00-00-0000 00:00:00.000
4      Read cfg_dldp_entry fail                       2  09-26-2022 10:24:04.681
5      Update cfg_dldp_entry success                  0  00-00-0000 00:00:00.000
6      Update cfg_dldp_entry fail                     0  00-00-0000 00:00:00.000
7      Remove cfg_dldp_entry success                  0  00-00-0000 00:00:00.000
8      Remove cfg_dldp_entry fail                     0  00-00-0000 00:00:00.000
9      Write dldp_entry success                       2  09-26-2022 10:24:04.682
10     Write dldp_entry fail                          0  00-00-0000 00:00:00.000
11     Read dldp_entry success                        0  00-00-0000 00:00:00.000
12     Read dldp_entry fail                       20596  09-26-2022 10:24:04.681
13     Update dldp_entry success                      0  00-00-0000 00:00:00.000
14     Update dldp_entry fail                         0  00-00-0000 00:00:00.000
15     Remove dldp_entry success                      0  00-00-0000 00:00:00.000
16     Remove dldp_entry fail                         0  00-00-0000 00:00:00.000
17     Write dldp_port_bmp success                    1  09-25-2022 18:27:33.418
18     Write dldp_port_bmp fail                       0  00-00-0000 00:00:00.000
19     Read dldp_port_bmp success                     1  09-26-2022 10:24:04.681
20     Read dldp_port_bmp fail                        1  09-25-2022 18:27:33.418
21     Update dldp_port_bmp success                   1  09-26-2022 10:24:04.681
22     Update dldp_port_bmp fail                      0  00-00-0000 00:00:00.000
23     Remove dldp_port_bmp success                   0  00-00-0000 00:00:00.000
24     Remove dldp_port_bmp fail                      0  00-00-0000 00:00:00.000
25     Write dldp_entry_state success                 2  09-26-2022 10:24:04.681
26     Write dldp_entry_state fail                    0  00-00-0000 00:00:00.000
27     Read dldp_entry_state success                  5  09-26-2022 10:26:51.628
28     Read dldp_entry_state fail                     2  09-26-2022 10:24:04.681
29     Update dldp_entry_state success                2  09-26-2022 10:24:04.682
30     Update dldp_entry_state fail                   0  00-00-0000 00:00:00.000
31     Remove dldp_entry_state success                0  00-00-0000 00:00:00.000
32     Remove dldp_entry_state fail                   0  00-00-0000 00:00:00.000
33     add or update acl success                      2  09-26-2022 10:24:04.682
34     add or update acl fail                         0  00-00-0000 00:00:00.000
35     delete or update acl success                   0  00-00-0000 00:00:00.000
36     delete or update acl fail                      0  00-00-0000 00:00:00.000
37     Rev len msg success                            0  00-00-0000 00:00:00.000
38     Rev len msg fail                               0  00-00-0000 00:00:00.000
39     Rev cnt msg success                            0  00-00-0000 00:00:00.000
40     Rev cnt msg fail                               0  00-00-0000 00:00:00.000
41     Pid age msg success                            0  00-00-0000 00:00:00.000
42     Pid age msg fail                               0  00-00-0000 00:00:00.000
43     Begin smooth msg success                       0  00-00-0000 00:00:00.000
44     Begin smooth msg fail                          0  00-00-0000 00:00:00.000
45     End smooth msg success                         0  00-00-0000 00:00:00.000
46     End smooth msg fail                            0  00-00-0000 00:00:00.000
47     Update dldp msg success                        2  09-26-2022 10:24:04.681
48     Update dldp msg fail                           0  00-00-0000 00:00:00.000
49     Delete dldp msg success                        0  00-00-0000 00:00:00.000
50     Delete dldp msg fail                           0  00-00-0000 00:00:00.000
51     Update dldp compatible msg succe               0  00-00-0000 00:00:00.000
52     Update dldp compatible msg fail                0  00-00-0000 00:00:00.000
53     Ha status change msg success                   6  09-25-2022 18:22:02.286
54     Ha status change msg fail                      0  00-00-0000 00:00:00.000
55     Receive ifm port msg success               20594  09-25-2022 18:22:02.149
56     Receive ifm port msg fail                      0  00-00-0000 00:00:00.000
57     Receive frm res msg success                    0  00-00-0000 00:00:00.000
58     Receive frm res msg fail                       0  00-00-0000 00:00:00.000

```

# Display statistics about the DLDP module in slot 1.
```
<HUAWEI> display fwm dldp statistics slot 1
Id     Statistic description                    Counter           Last timestamp
--------------------------------------------------------------------------------
1      Write cfg_dldp_entry success                   3  09-29-2022 22:47:49.542
2      Read cfg_dldp_entry fail                       3  09-29-2022 22:47:49.542
3      Write dldp_entry success                       3  09-29-2022 22:47:49.543
4      Read dldp_entry success                        2  09-29-2022 22:41:57.282
5      Read dldp_entry fail                           6  09-29-2022 22:47:49.542
6      Write dldp_port_bmp success                    1  09-29-2022 22:41:57.151
7      Read dldp_port_bmp success                     2  09-29-2022 22:47:49.542
8      Read dldp_port_bmp fail                        1  09-29-2022 22:41:57.151
9      Update dldp_port_bmp success                   2  09-29-2022 22:47:49.542
10     Write dldp_entry_state success                 5  09-29-2022 22:47:49.542
11     Read dldp_entry_state success                  5  09-29-2022 22:47:49.542
12     Read dldp_entry_state fail                     5  09-29-2022 22:47:49.542
13     Update dldp_entry_state success                3  09-29-2022 22:47:49.542
14     Remove dldp_entry_state success                2  09-29-2022 22:41:57.282
15     add or update acl success                      3  09-29-2022 22:47:49.542
16     Update dldp msg success                        3  09-29-2022 22:47:49.542
17     Ha status change msg success                   6  09-29-2022 22:42:17.700
18     Receive ifm port msg success                   5  09-29-2022 22:42:17.491

```

**Table 1** Description of the **display fwm dldp statistics** command output
| Item | Description |
| --- | --- |
| Id | Statistics sequence number. |
| Statistic description | Description of the statistics, that is, the specific service. |
| Counter | Number of statistics. |
| Last timestamp | Time when the statistics were last updated. |