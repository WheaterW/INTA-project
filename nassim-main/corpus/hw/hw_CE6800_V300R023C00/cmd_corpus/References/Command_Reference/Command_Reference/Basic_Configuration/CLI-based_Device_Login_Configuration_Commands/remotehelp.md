remotehelp
==========

remotehelp

Function
--------



The **remotehelp** command displays help of a particular FTP command from a remote FTP server.




Format
------

**remotehelp** [ *command* ]


Parameters
----------

| Parameter | Description | Value |
| --- | --- | --- |
| *command* | Specifies the FTP command. | The value is a string of 1 to 16 case-sensitive characters, spaces not supported. |



Views
-----

FTP client view


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

The following FTP commands support help information.

| Command | Help Information |
| --- | --- |
| USER | "USER <sp> <username>" |
| PASS | "PASS <sp> password" |
| ACCT\* | "ACCT <sp> account-information" |
| CWD | "CWD [ <sp> directory-name ]" |
| CDUP | "CDUP <change to parent directory>" |
| SMNT\* | "SMNT <sp> <structure mount>, Unimplemented" |
| QUIT | "QUIT <terminate service>" |
| REIN\* | "REIN <reinitialize server state>; Unimplemented" |
| PORT | "PORT <sp> b0, b1, b2, b3, b4, b5" |
| PASV | "PASV <set server in passive mode>" |
| TYPE | "TYPE <sp> [ A | I ]" |
| STRU\* | "STRU <specify file structure>; Unimplemented" |
| MODE\* | "MODE <specify transfer mode>; Unimplemented" |
| RETR | "RETR <sp> file-name" |
| STOR | "STOR <sp> file-name" |
| STOU\* | "STOU <sp> file-name; Unimplemented" |
| APPE | "APPE <sp> file-name" |
| ALLO\* | "ALLO allocate storage <vacuously>; Unimplemented" |
| REST\* | "REST <restart command>; Unimplemented" |
| RNFR | "RNFR <sp> file-name" |
| RNTO | "RNTO <sp> file-name" |
| ABOR\* | "ABOR <abort operation>; Unimplemented" |
| DELE | "DELE <sp> file-name" |
| RMD | "RMD <sp> path-name" |
| MKD | "MKD <sp> path-name" |
| PWD | "PWD <return current directory>" |
| LIST | "LIST [ <sp> path-name ]" |
| NLST | "NLST [ <sp> path-name ]" |
| SITE\* | "SITE; Unimplemented" |
| SYST | "SYST <get type of operating system>" |
| STAT\* | "STAT [ <sp> <pathname> ]" |
| HELP | "HELP [ <sp> <string> ]" |
| NOOP\* | "NOOP; Unimplemented" |
| XCUP | "XCUP <change to parent directory>" |
| XCWD | "XCWD [ directory-name ]" |
| XMKD | "XMKD <sp> path-name" |
| XPWD | "XPWD <return current directory>" |
| XRMD | "XRMD <sp> path-name" |
| EPSV | "EPSV <sp> <net-prt>" |
| EPRT | "EPRT <sp> <d><net-prt><d><net-addr><d><port><d>" |
| FEAT\* | "FEAT; Unimplemented" |

"\*" indicates that the entered command is incomplete.In addition to the commands listed in the preceding table, the help information of other commands is "Unknown command".


Example
-------

# Get help on a command.
```
<HUAWEI> ftp 10.1.1.2
[ftp] remotehelp port

```