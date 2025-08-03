display bfd link-bundle session
===============================

display bfd link-bundle session

Function
--------



The **display bfd link-bundle session** command displays information about BFD for link-bundle sessions.




Format
------

**display bfd link-bundle session** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Displays information about BFD for link-bundle sessions on a specified interface. | The interface type can be Layer 3 Eth-Trunk. |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To view information about the main session and sub-sessions of a BFD for link-bundle session, run the **display bfd link-bundle session** command.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about BFD for link-bundle sessions.
```
<HUAWEI> display bfd link-bundle session
(w): State in WTR
(*): State is invalid
Total Up/Down Main Session Number : 1/0
Total Up/Down Sub Session Number  : 1/0
--------------------------------------------------------------------------------
  Name                   : a
  State                  : Up
  Local Discriminator    : 1048577
  Remote Discriminator   : -
  Session Detect Mode    : Asynchronous Mode Without Echo Function
  BFD Bind Type          : Interface(Eth-Trunk0) 
  Bind Session Type      : Static_Auto(Bundle_Main | Compatible)
  Bind Peer IP Address   : 10.1.1.1
  Bind Source IP Address : 10.1.1.2
  FSM Board Id           : -
  TOS-EXP                : 7
  Min Tx Interval (ms)   : 1000
  Min Rx Interval (ms)   : 1000
  Local Detect Multi     : 3
  WTR Interval (ms)      : - 
  Last Local Diagnostic  : Control Detection Time Expired
  Bind Application       : OSPF | ISIS | AUTO
  Sub Session Count      : 1
--------------------------------------------------------------------------------
      Sub Session Number     : 1
      State                  : Up
      Local Discriminator    : 16387
      Remote Discriminator   : 16385
      BFD Bind Type          : Interface(100GE1/0/1) 
      Bind Session Type      : Dynamic(Bundle_Sub | Compatible)
      FSM Board Id           : 9
      Min Tx Interval (ms)   : 1000
      Min Rx Interval (ms)   : 1000
      Local Detect Multi     : 3
      Actual Tx Interval (ms): 1000
      Actual Rx Interval (ms): 1000
      Active Multi           : 3 
      Detect Interval (ms)   : 3000
      Destination Port       : 3784
      Last Local Diagnostic  : Control Detection Time Expired
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display bfd link-bundle session** command output
| Item | Description |
| --- | --- |
| State | Current status of the BFD session. |
| WTR Interval (ms) | WTR time of the BFD session. |
| Total Up/Down Main Session Number | Number of main sessions. |
| Total Up/Down Sub Session Number | Number of sub-sessions. |
| Session Detect Mode | The value is Asynchronous Mode Without Echo Function. |
| Sub Session Count | Number of sub-sessions for the main session. |
| Sub Session Number | Name of the sub-session for the main session. |
| Name | Name of the BFD session. |
| Local Discriminator | Local discriminator of the BFD session. |
| Local Detect Multi | Local detection multiplier. |
| Remote Discriminator | Remote discriminator of the BFD session. |
| Detect Interval (ms) | Detection interval. |
| BFD Bind Type | Binding type of the BFD session. The local Layer 3 Eth-Trunk interface bound to the BFD for link-bundle session is displayed. |
| Bind Session Type | Establishment type of the BFD session. The establishment type of a BFD for link-bundle session is. Static\_Auto, indicating that the BFD session is a statically created BFD session with automatically negotiated discriminators.   * Bundle\_Main: main session. * Bundle\_Sub: sub-session. * Compatible: support for interworking with non-Huawei devices. |
| Bind Peer IP Address | Peer IP address of the BFD session. |
| Bind Source IP Address | Local IP address of the BFD session. |
| Bind Application | Bound application. |
| FSM Board Id | Slot ID of the processing board on which the finite state machine resides:   * "-" is displayed for the main session. * The slot ID of the processing board is displayed for a sub-session. |
| TOS-EXP | Priority of BFD packets. |
| Min Tx Interval (ms) | Configured minimum interval between sending BFD packets. |
| Min Rx Interval (ms) | Configured minimum interval between receiving BFD packets. |
| Last Local Diagnostic | Local diagnostic reason that the BFD session last went Down. |
| Actual Tx Interval (ms) | Actual interval between sending packets. |
| Actual Rx Interval (ms) | Actual interval between receiving packets. |
| Active Multi | Active detection multiplier. |
| Destination Port | Destination port number of session packets:   * 3784 for the compatible mode. * 6784 for the non-compatible mode. |