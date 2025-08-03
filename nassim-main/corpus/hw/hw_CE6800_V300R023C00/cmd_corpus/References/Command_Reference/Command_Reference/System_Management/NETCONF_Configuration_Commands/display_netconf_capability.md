display netconf capability
==========================

display netconf capability

Function
--------



The **display netconf capability** command displays the capabilities that the NETCONF supports.




Format
------

**display netconf capability**


Parameters
----------

None

Views
-----

All views


Default Level
-------------

3: Management level


Usage Guidelines
----------------

**Usage Scenario**

NETCONF defines base and standard capabilities. Huawei defines private capabilities. Operations are defined in various capabilities.To view operations supported by capabilities, run the display netconf capability command. This command improves maintainability.Hello messages exchanged between the server and client describe the public and private capabilities supported by a NETCONF session.


Example
-------

![](../public_sys-resources/note_3.0-en-us.png) 

The actual command output varies according to the device. The command output here is only an example.


# Display server capabilities supported.
```
<HUAWEI> display netconf capability
--------------------------------------------------
Capability
--------------------------------------------------
urn:ietf:params:netconf:base:1.0
urn:ietf:params:netconf:base:1.1
urn:ietf:params:netconf:capability:schema-sets:1.0?list=huawei-yang@2.0.0
urn:ietf:params:netconf:capability:writable-running:1.0
urn:ietf:params:netconf:capability:candidate:1.0
urn:ietf:params:netconf:capability:confirmed-commit:1.0
urn:ietf:params:netconf:capability:confirmed-commit:1.1
urn:ietf:params:netconf:capability:rollback-on-error:1.0
urn:ietf:params:netconf:capability:validate:1.0
urn:ietf:params:netconf:capability:validate:1.1
urn:ietf:params:netconf:capability:startup:1.0
urn:ietf:params:netconf:capability:url:1.0?scheme=file,ftp,sftp,http,https
urn:ietf:params:netconf:capability:xpath:1.0
urn:ietf:params:netconf:capability:notification:1.0
urn:ietf:params:netconf:capability:interleave:1.0
urn:ietf:params:netconf:capability:with-defaults:1.0?basic-mode=report-all&also-supported=report-all-tagged,trim
urn:ietf:params:netconf:capability:yang-library:1.0?revision=2016-06-21&module-set-id=3457064700
urn:ietf:params:netconf:capability:notification:2.0
http://www.huawei.com/netconf/capability/sync/1.0
http://www.huawei.com/netconf/capability/sync/1.1
http://www.huawei.com/netconf/capability/sync/1.2
http://www.huawei.com/netconf/capability/sync/1.3
http://www.huawei.com/netconf/capability/exchange/1.0
http://www.huawei.com/netconf/capability/exchange/1.2
http://www.huawei.com/netconf/capability/active/1.0
http://www.huawei.com/netconf/capability/action/1.0
http://www.huawei.com/netconf/capability/discard-commit/1.0
http://www.huawei.com/netconf/capability/execute-cli/1.0
http://www.huawei.com/netconf/capability/update/1.0
http://www.huawei.com/netconf/capability/commit-description/1.0
http://www.huawei.com/netconf/capability/schema/1.0
--------------------------------------------------

```

**Table 1** Description of the **display netconf capability** command output
| Item | Description |
| --- | --- |
| Capability | "urn:ietf:params:netconf:base:X" uniquely identifies a base capability defined by NETCONF. "X" indicates the capability version supported.  "Base" indicates the NETCONF basic capabilities used to run a basic set of operations. NETCONF supports the following basic operations:   * get-config: obtains all or specified configuration data from the running, candidate, and startup configuration databases. * get: obtains some or all running configuration data and status data. * edit-config: creates, modifies, or deletes configuration data. * lock: locks a configuration database. A locked configuration database cannot be modified by other users. The locks eliminate errors caused by simultaneous modifications of the database by NETCONF managers or SNMP or CLI scripts. * unlock: cancels the lock operation performed by the specified user, rather than the lock operation performed by other users. * copy-config: replaces the target configuration database with the source configuration database. If no target configuration database has been created, this operation directly creates one. If a target configuration database has been created, the source configuration database directly replaces the target configuration database. * delete-config: deletes a configuration database. The running configuration database cannot be deleted using this operation. * close-session: closes a NETCONF session. * kill-session: forcibly closes a NETCONF session. Only an administrator can perform this operation.   "urn:ietf:params:netconf:capability:Name:X" uniquely identifies a standard capability defined by NETCONF. "X" indicates the capability version supported.  "Name" indicates the standard capability of NETCONF. NETCONF supports the following standard capabilities:   * Writable-Running: indicates that a device supports writes to the running configuration database. Specifically, the device supports edit-config and copy-config operations on the running configuration database. * Candidate: indicates that a device supports the candidate configuration database. This capability enables a device to perform operations on configuration data without affecting configuration data that is being used. * Confirmed Commit: indicates that a device supports updates to the latest configuration if the configuration is committed before the confirm-timeout period elapses. * Distinct Startup: indicates that a device can perform a distinct startup. The server checks parameter availability and consistency. * Rollback on Error: indicates that a device supports a rollback if an error occurs. If an error occurs and the rpc-error element is generated, the server stops processing the edit-config operation and restores the specified configuration to the status before the edit-config operation is performed. * Notification: indicates that traps or events generated on a device can be sent in notification messages to an NMS. * Interleave: indicates that a device supports NETCONF session reuse for multiple purposes. A user can maintain a device and manage traps and events using the same NETCONF session. * url: indicates that a device can add URL elements to the source and target tags of packets. * xpath: indicates that a device supports xpath expressions in the filter node of the subtree. * validate: indicates that a device supports the validate operation and syntax verification. * with-defaults: indicates that a device supports the get/get-config/copy-config operation with the with-defaults node. The options are as follows: * report-all: queries nodes with default values as well as nodes without default values. * report-all-tagged: queries nodes with default values as well as nodes without default values, and tags the nodes with default values. * trim: queries nodes without default values. * yang-library: enables the NETCONF client to obtain basic information about the YANG module supported by the server, such as the module name, version, namespace, and sub-module list. |