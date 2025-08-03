display wavelength-map
======================

display wavelength-map

Function
--------



The **display wavelength-map** command displays the mapping between the channel number of DWDM optical modules and center wavelength.




Format
------

**display wavelength-map**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**

The system pre-sets 80 channels, each of which has a wavelength value. Before setting the wavelength of an interface, run the **display wavelength-map** command to view the channel number of the wavelength and then run the **wavelength-channel** command to set the channel number of the interface.

**Precautions**

If no colored optical module is installed on a device or the medium type of an interface is not pre-configured as colored optical module using the **device transceiver** command in the interface view, no information is displayed.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the mapping between the channel number of DWDM optical modules and center wavelength.
```
<HUAWEI> display wavelength-map
80 Channel Map:                                                                                                                     
------------------------------------------                                                                                          
 Channel Frequency(MHz)   Wavelength(pm)                                                                                            
------------------------------------------                                                                                          
       1 192100000        1560606                                                                                                  
       2 192150000        1560200                                                                                                  
       3 192200000        1559794                                                                                                  
       4 192250000        1559389                                                                                                  
       5 192300000        1558983                                                                                                  
       6 192350000        1558578                                                                                                  
       7 192400000        1558173                                                                                                  
       8 192450000        1557768                                                                                                  
       9 192500000        1557363                                                                                                  
      10 192550000        1556959                                                                                                  
      11 192600000        1556555                                                                                                  
      12 192650000        1556151                                                                                                  
      13 192700000        1555747                                                                                                  
      14 192750000        1555344                                                                                                  
      15 192800000        1554940                                                                                                  
      16 192850000        1554537                                                                                                  
      17 192900000        1554134                                                                                                  
      18 192950000        1553731                                                                                                  
      19 193000000        1553329                                                                                                  
      20 193050000        1552926                                                                                                  
      21 193100000        1552524                                                                                                  
      22 193150000        1552122                                                                                                  
      23 193200000        1551721                                                                                                  
      24 193250000        1551319                                                                                                  
      25 193300000        1550918                                                                                                  
      26 193350000        1550517                                                                                                  
      27 193400000        1550116                                                                                                  
      28 193450000        1549715                                                                                                  
      29 193500000        1549315                                                                                                  
      30 193550000        1548915                                                                                                  
      31 193600000        1548515                                                                                                  
      32 193650000        1548115                                                                                                  
      33 193700000        1547715                                                                                                  
      34 193750000        1547316                                                                                                  
      35 193800000        1546917                                                                                                  
      36 193850000        1546518                                                                                                  
      37 193900000        1546119                                                                                                  
      38 193950000        1545720                                                                                                  
      39 194000000        1545322                                                                                                  
      40 194050000        1544924                                                                                                  
      41 194100000        1544526                                                                                                  
      42 194150000        1544128                                                                                                  
      43 194200000        1543730                                                                                                  
      44 194250000        1543333                                                                                                  
      45 194300000        1542936                                                                                                  
      46 194350000        1542539                                                                                                  
      47 194400000        1542142                                                                                                  
      48 194450000        1541746                                                                                                  
      49 194500000        1541349                                                                                                  
      50 194550000        1540953                                                                                                  
      51 194600000        1540557                                                                                                  
      52 194650000        1540162                                                                                                  
      53 194700000        1539766                                                                                                  
      54 194750000        1539371                                                                                                  
      55 194800000        1538976                                                                                                  
      56 194850000        1538581                                                                                                  
      57 194900000        1538186                                                                                                  
      58 194950000        1537792                                                                                                  
      59 195000000        1537397                                                                                                  
      60 195050000        1537003                                                                                                  
      61 195100000        1536609                                                                                                  
      62 195150000        1536216                                                                                                  
      63 195200000        1535822                                                                                                  
      64 195250000        1535429                                                                                                  
      65 195300000        1535036                                                                                                  
      66 195350000        1534643                                                                                                  
      67 195400000        1534250                                                                                                  
      68 195450000        1533858                                                                                                  
      69 195500000        1533465                                                                                                  
      70 195550000        1533073                                                                                                  
      71 195600000        1532681                                                                                                  
      72 195650000        1532290                                                                                                  
      73 195700000        1531898                                                                                                  
      74 195750000        1531507                                                                                                  
      75 195800000        1531116                                                                                                  
      76 195850000        1530725                                                                                                  
      77 195900000        1530334                                                                                                  
      78 195950000        1529944                                                                                                  
      79 196000000        1529553                                                                                                  
      80 196050000        1529163                                                                                                  
------------------------------------------

```

**Table 1** Description of the **display wavelength-map** command output
| Item | Description |
| --- | --- |
| 80 Channel Map | Mapping between the channel number of 80 channels and the central wavelength. |
| Channel | Channel number. |
| Frequency(MHz) | Frequency, in MHz. |
| Wavelength(pm) | Center wavelength, in picometers. |