display user-interface
======================

display user-interface

Function
--------



The **display user-interface** command displays the information about the specified user interface.




Format
------

**display user-interface** [ *ui-number* | { { **console** | **vty** | **nca** | **rpc** } *ui-number1* | *ui-name* } ] [ **summary** ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *ui-number* | Specifies the absolute user interface ID. | The minimum value is 0. The maximum value is smaller by 1 than the number of the user interfaces that the system supports. |
| **console** | Display information about the console user interface. | - |
| **vty** | Display the information of the current VTY user interface. | - |
| **nca** | Display the information of the NETCONF user interface. | - |
| **rpc** | Display the information of the rpc interface. | - |
| *ui-number1* | Specifies the relative user interface ID or information about the user interface. | The value is a string of 1 to 11 case-sensitive characters, spaces not supported. |
| *ui-name* | Display the information of the interface. | The value is a string ranging from 1 to 11. |
| **summary** | Introduces the user interface briefly. | - |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

By executing this command displays the configuration details of the specified user interface view.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the details on the user interface.
```
<HUAWEI> display user-interface
  Idx  Type     Tx/Rx      Modem Privi ActualPrivi Auth  Int
+ 0    CON 0    9600       -     3     3           P     1                   
+ 34   VTY 0               -     3     3           N     -                   
+ 35   VTY 1               -     3     3           N     -                   
+ 36   VTY 2               -     3     3           N     -                   
+ 37   VTY 3               -     3     3           N     -                   
+ 38   VTY 4               -     3     3           N     -                   
+ 39   VTY 5               -     3     3           N     -                   
  40   VTY 6               -     3     -           N     -                   
  41   VTY 7               -     3     -           N     -                   
  42   VTY 8               -     3     -           N     -                   
  43   VTY 9               -     3     -           N     -                   
  44   VTY 10              -     3     -           N     -                   
  45   VTY 11              -     3     -           N     -                   
  46   VTY 12              -     3     -           N     -                   
  47   VTY 13              -     3     -           N     -                   
  48   VTY 14              -     3     -           N     -                   
  49   VTY 15              -     3     -           N     -                   
  50   VTY 16              -     3     -           N     -                   
  51   VTY 17              -     3     -           N     -                   
  52   VTY 18              -     3     -           N     -                   
  53   VTY 19              -     3     -           N     -                   
  54   VTY 20              -     3     -           N     -                   
  100  NCA 0               -     -     -           A     -                   
  101  NCA 1               -     -     -           A     -                   
  102  NCA 2               -     -     -           A     -                   
  103  NCA 3               -     -     -           A     -                   
  104  NCA 4               -     -     -           A     -                   
  150  RPC 0               -     -     -           A     -                   
  151  RPC 1               -     -     -           A     -                   
  152  RPC 2               -     -     -           A     -                   
  153  RPC 3               -     -     -           A     -                   
  154  RPC 4               -     -     -           A     -      
UI(s) not in async mode -or- with no hardware support:
21-32
  +    : Current UI is active.
  F    : Current UI is active and work in async mode.
  Idx  : Absolute index of UIs.
  Type : Type and relative index of UIs.
  Privi: The privilege of UIs.
  ActualPrivi: The actual privilege of user-interface.
  Auth : The authentication mode of UIs.
      A: Authenticate use AAA.
      N: Current UI need not authentication.
      P: Authenticate use current UI's password.
  Int  : The physical location of UIs.

```

**Table 1** Description of the **display user-interface** command output
| Item | Description |
| --- | --- |
| Idx | Absolute number of the user interface. |
| Type | Type and relative number of the user interface:   * Console. * VTY. * NCA. * RPC. |
| Tx/Rx | Speed of the user interface. |
| Modem | Modem mode. |
| Privi | Privilege configured for the user interface. |
| ActualPrivi | Actual privilege of the user interface. |
| Auth | Authentication mode of the user interface:   * A: AAA authentication. * P: Current user interface's password. * N: The current user interface needs no authentication. |
| Int | Physical location of the user interface. |
| P | Current UI's password. |
| N | The current user interface does not require identity authentication. |
| A | AAA authentication. |
| + | Flag indicating that the user interface is active. |
| F | Flag indicating that the user interface is active and working in asynchronous mode. |