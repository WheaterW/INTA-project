display bfd perlink session
===========================

display bfd perlink session

Function
--------



The **display bfd perlink session** command displays information about BFD for Per-Link sessions.




Format
------

**display bfd perlink session** [ **interface** { *interface-name* | *interface-type* *interface-number* } ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| **interface** *interface-type* *interface-number* | Displays information about BFD for Per-Link sessions on a specified interface. | - |



Views
-----

All views


Default Level
-------------

1: Monitoring level


Usage Guidelines
----------------

**Usage Scenario**



To view information about the main session and sub-sessions of a BFD for Per-Link session, run the **display bfd perlink session** command.



**Prerequisites**



BFD has been globally enabled using the **bfd** command in the system view.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display information about BFD for Per-Link sessions.
```
<HUAWEI> display bfd perlink session
(w): State in WTR
(*): State is invalid
Total Up/Down Main Session Number : 0/1
Total Up/Down Sub Session Number  : 0/1
--------------------------------------------------------------------------------
  Name                   : pe
  State                  : Down
  Local Discriminator    : 1048577
  Remote Discriminator   : 1048577
  Session Detect Mode    : Asynchronous Mode With Echo Function
  BFD Bind Type          : Interface(Vlanif10)
  Bind Session Type      : Static_Auto
  Bind Peer IP Address   : 10.0.0.1
  Bind Source IP Address : 10.0.0.2
  FSM Board Id           : -
  TOS-EXP                : 7
  Min Tx Interval (ms)   : 1000
  Min Rx Interval (ms)   : 1000
  Local Detect Multi     : 3
  WTR Interval (ms)      : -
  Last Local Diagnostic  : No Diagnostic
  Bind Application       : AUTO
  Sub Session Count      : 1
--------------------------------------------------------------------------------
      Sub Session Number     : 1
      State                  : Down
      Local Discriminator    : 16385
      Remote Discriminator   : 0
      BFD Bind Type          : Interface(100GE1/0/1)
      Bind Session Type      : Dynamic
      FSM Board Id           : 9
      Min Tx Interval (ms)   : 10
      Min Rx Interval (ms)   : 10
      Local Detect Multi     : 3
      Actual Tx Interval (ms): -
      Actual Rx Interval (ms): -
      Active Multi           : -
      Detect Interval (ms)   : -
      Destination Port       : 3784
      Last Local Diagnostic  : No Diagnostic
--------------------------------------------------------------------------------

```

**Table 1** Description of the **display bfd perlink session** command output
| Item | Description |
| --- | --- |
| State | Current status of the BFD session. |
| WTR Interval (ms) | WTR time. |
| Total Up/Down Main Session Number | Number of main sessions. |
| Total Up/Down Sub Session Number | Number of sub-sessions. |
| Session Detect Mode | Detection mode of the BFD session. The value is Asynchronous Mode With Echo Function, indicating the asynchronous mode with the echo function. |
| Sub Session Count | Number of sub-sessions for the main session. |
| Sub Session Number | Number of the BFD sub-session. |
| Name | Name of the BFD session. |
| Local Discriminator | Local discriminator of the BFD session. |
| Local Detect Multi | Configured local detection multiplier. |
| Remote Discriminator | Remote discriminator of the BFD session. |
| Detect Interval (ms) | Detection interval. |
| BFD Bind Type | Binding type of the BFD session.   * For a Bundle\_Main session, this field displays Interface and the bound local VLANIF interface. * For a Bundle\_Sub session, this field displays Interface and the Eth-Trunk member interface. |
| Bind Peer IP Address | Peer IP address of the BFD session. |
| Bind Source IP Address | Local IP address of the BFD session. |
| Bind Application | Bound application. |
| Bind Session Type | Establishment type of the BFD session.  The establishment type of a BFD for Per-Link session is Static\_Auto, indicating that the BFD session is a statically created BFD session with automatically negotiated discriminators.  The establishment type of a BFD for Per-Link session is Dynamic, indicating that the BFD session is a dynamically created BFD session. |
| FSM Board Id | Slot ID of the processing board on which the finite state machine resides:   * "-" is displayed for the main session. * The slot ID of the processing board is displayed for a sub-session. |
| TOS-EXP | Priority of BFD packets. |
| Min Tx Interval (ms) | Configured minimum interval between sending packets. |
| Min Rx Interval (ms) | Configured minimum interval between receiving packets. |
| Last Local Diagnostic | Local diagnostic reason that the BFD session last went Down. |
| Actual Tx Interval (ms) | Actual interval between sending packets. |
| Actual Rx Interval (ms) | Actual interval between receiving packets. |
| Active Multi | Active detection multiplier. |
| Destination Port | Destination port number of session packets. The value can be only 3784. |