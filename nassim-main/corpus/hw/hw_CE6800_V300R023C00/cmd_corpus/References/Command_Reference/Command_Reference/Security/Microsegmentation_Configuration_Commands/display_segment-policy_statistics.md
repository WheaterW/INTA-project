display segment-policy statistics
=================================

display segment-policy statistics

Function
--------



The **display segment-policy statistics** command displays microsegmentation policy statistics.



![](../public_sys-resources/note_3.0-en-us.png) 

This command is supported only on the CE6860-SAN, CE6866K, CE6866, CE6860-HAM, CE8850-SAN, CE8851K, CE8851-32CQ8DQ-P and CE8850-HAM.



Format
------

**display segment-policy statistics** *policy-name* [ **classifier-base** [ *class-name* ] | **rule-base** [ **class** *class-name* ] ] **slot** *slot-id*


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *policy-name* | Specifies the name of a microsegmentation grouping policy. | The value is a string of 1 to 31 characters. |
| **classifier-base** | Based on classifiers. | - |
| **rule-base** | Based on rules. | - |
| **class** *class-name* | Specifies the name of a microsegmentation classifier. | The value is a string of 1 to 31 characters. |
| **slot** *slot-id* | Displays statistics about microsegmentation policies in a specified slot. | The value is a string of characters. The value is a slot ID. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

To check microsegmentation policy statistics, run the **display segment-policy statistics** command. The command output helps you learn packet statistics after a segment policy is applied, analyze and determine whether the segment policy is properly applied, and locate faults.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display statistics based on rules.
```
<HUAWEI> display segment-policy statistics p1 rule-base slot 1
Policy: p1
--------------------------------------------------------------------------------
  Classifier: abc, Behavior: abc
    No rule(s) exist.
    ----------------------------------------------------------------------------
  Classifier: c2, Behavior: abc
    rule 5 permit source-segment 1
    Passed Packets                       0, Passed Bytes                       0
    Dropped Packets                      0, Dropped Bytes                      0
    ----------------------------------------------------------------------------
    rule 10 permit source-segment 32768 destination-segment 32768 protocol tcp source-port range 1 65534 destination-port range 1 65534
    Passed Packets                       0, Passed Bytes                       0
    Dropped Packets                      0, Dropped Bytes                      0
    ----------------------------------------------------------------------------

```

# Display statistics based on classifiers.
```
<HUAWEI> display segment-policy statistics p1 classifier-base c2 slot 1
Policy: p1
--------------------------------------------------------------------------------                                                    
Classifier: c2, Behavior: b1
 Item                  Packets                        Bytes                                                                         
 -------------------------------------------------------------------------------                                                    
 Matched                     0                            0                                                                         
  Passed                     0                            0                                                            
  Dropped                    0                            0              
 -------------------------------------------------------------------------------

```

# Display statistics based on policies.
```
<HUAWEI> display segment-policy statistics p1 slot 1
Policy: p1
-------------------------------------------------------------------------------- 
 Item                  Packets                        Bytes                                                                         
 -------------------------------------------------------------------------------                                                    
 Matched                     0                            0                                                                         
  Passed                     0                            0                                                            
  Dropped                    0                            0             
 -------------------------------------------------------------------------------

```

**Table 1** Description of the **display segment-policy statistics** command output
| Item | Description |
| --- | --- |
| rule 5 permit source-segment 1 | Rules matching the segment classifier. |
| rule 10 permit source-segment 32768 destination-segment 32768 protocol tcp source-port range 1 65534 destination-port range 1 65534 | Rules matching the segment classifier. |
| Passed | Numbers of forwarded packets and bytes that match segment classification rules. All statistics from the last time segment policy statistics are cleared to the current time are displayed. |
| Passed Packets | Number of forwarded packets matching segment classification rules. |
| Passed Bytes | Number of forwarded bytes matching segment classification rules. |
| Packets | Number of packets. |
| Bytes | Number of bytes. |
| Dropped | Numbers of discarded packets and bytes that match segment classification rules. All statistics from the last time segment policy statistics are cleared to the current time are displayed. |
| Dropped Packets | Number of discarded packets matching segment classification rules. |
| Dropped Bytes | Number of discarded bytes that match segment classification rules. |
| Item | Statistical items. |
| Matched | Numbers of packets and bytes that match segment classification rules. All statistics from the last time segment policy statistics are cleared to the current time are displayed. |
| Policy | Microsegmentation grouping policy name. |
| Classifier | Name of a segment classifier. |
| Behavior | Name of a segment behavior. |