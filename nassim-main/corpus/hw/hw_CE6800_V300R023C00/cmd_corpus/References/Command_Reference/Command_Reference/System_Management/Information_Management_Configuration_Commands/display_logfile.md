display logfile
===============

Function
--------



The **display logfile** command displays an information file.




Format
------

**display logfile** *path* [ *offset* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *path* | Displays the information file with the specified driver, path, and file name. | The value is a string of 1 to 255 case-insensitive characters, spaces supported. |
| *offset* | Displays the information file with specified offset bytes. | The value is an integer ranging from 1 to 4294967295. |



Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**



If a problem occurs, you can query log information to learn about what happened during device operation. This is helpful for fault location. The file name is generated automatically and the log format is log.log. You can view the content of a specified information file in the flash: directory or view all files in the specified directory. For details, see "Example."If the size of the existing information file reaches the upper limit, the system transfers the information file into a historical compress file with the name of "log\_SlotID\_time.log.zip". The "slot ID" indicates the slot where the log is generated, and "time" indicate the date and time when the log was recorded.




Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display the information file of the log.log format in the specified directory.
```
<HUAWEI> display logfile flash:/logfile/log.log
###############################################################################
#     This logfile is generated at :17                                        #
###############################################################################

Apr 23 2020 17:26:19 "HUAWEI" %%01SOCKET/6/socket_event_log(l):CID=0x80650403;The SOCKET component switch, from state of < SOCK_COMP_FSM_INIT> to < SOCK_COMP_FSM_STANDALONE >, by event < SOCK_COM
P_EVENT_PRI_STARTWORK>.
Apr 23 2020 17:26:18 "HUAWEI" %%01SOCKET/6/socket_event_log(l):CID=0x80652712;The SOCKET component switch, from state of <SOCK_COMP_EVENT_PRI_INIT> to < SOCK_COMP_FSM_STANDALONE>, by event < SOCK
_COMP_EVENT_PRI_STARTWORK>.
Apr 23 2020 17:26:18 "HUAWEI" %%01SOCKET/6/socket_event_log(l):CID=0x80650407;The SOCKET component switch, from state of < SOCK_COMP_FSM_INIT> to < SOCK_COMP_FSM_STANDALONE>, by event < SOCK_COMP
_EVENT_PRI_STARTWORK>.
Apr 23 2020 17:25:53 "HUAWEI" %%01CONFIGURATION/4/CFG_STARTUPWITH_N
ULL_FILE(l):CID=0x80cb001a;
Apr 23 2020 17:26:23 "HUAWEI" %%01GRESM/6/PEER_STATE_CHG(l):CID=0x792715;Peer components Finite State Machine changed. (ComPid=2172723, ComType=33, FSM=0, StateBefore=0, StateAfter=1, Reason=SSP n
otified user HA state is available)

.......

```