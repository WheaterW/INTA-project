display ospf lsdb brief
=======================

display ospf lsdb brief

Function
--------



The **display ospf lsdb brief** command displays brief information about the OSPF Link-State Database (LSDB).




Format
------

**display ospf** [ *process-id* ] **lsdb** **brief**


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *process-id* | process-id. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

The **display ospf lsdb brief** command displays brief information about the OSPF LSDB, which helps you locate faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Displays OSPF LSDB brief information.
```
<HUAWEI> display ospf lsdb brief
2020-03-09 15:52:18.616

          OSPF Process 1 with Router ID 10.33.33.33
                  LS Database Statistics

 Area ID         Stub   Router   Network  S-Net   S-ASBR   Type-7   | Subtotal
 0.0.0.0         0      1        0        0       0        0        | 1
 0.0.0.1         0      0        0        0       0        0        | 0
 Total           0      1        0        0       0        0        |
 -------------------------------------------------------------------+---------
 Area ID         Opq-9  Opq-10                                      | Subtotal
 0.0.0.0         0      0                                           | 0
 0.0.0.1         0      0                                           | 0
 Total           0      0                                           |
 -------------------------------------------------------------------+---------
                 ASE      Opq-11                                    | Subtotal
 Total           12       0                                         | 12
 -------------------------------------------------------------------+---------
                                                                    | Total
                                                                    | 13

```

**Table 1** Description of the **display ospf lsdb brief** command output
| Item | Description |
| --- | --- |
| Router | Number of Router-LSAs. |
| Area ID | Area ID. |
| Network | Number of Network-LSAs. |
| S-Net | Number of Summary-Net-LSAs. |
| S-ASBR | Number of Summary-ASBR-LSAs. |
| Type-7 | Number of Type-7 LSAs. |
| Subtotal | Total number of horizontal items in the displayed information. |
| Total | Total number of vertical items in the displayed information. |
| Opq-9 | Number of Opaque-9 LSAs. |
| Opq-10 | Number of Opaque-10 LSAs. |
| ASE | Number of AS-External LSAs. |
| Opq-11 | Number of Opaque-11 LSAs. |