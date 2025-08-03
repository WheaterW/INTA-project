Verifying the Configuration
===========================

After configuring interface-based HQoS, you can view information about queues and packet statistics on the interface.

#### Context

Run the following commands to check the configuration.


#### Procedure

* Run the [**display qos resource user-queue**](cmdqueryname=display+qos+resource+user-queue) **slot** *slot-id* { **inbound** | **outbound** } command to check the usage of user queues on an interface board.
* Run the [**display traffic buffer usage slot**](cmdqueryname=display+traffic+buffer+usage+slot) *slot-id* command to check the buffer usage.
* Run the [**display qos scheduling-mode**](cmdqueryname=display+qos+scheduling-mode) **slot** *slot-id* command to check the scheduling mode of a board.
* Run the [**display qos default flow-queue statistics interface**](cmdqueryname=display+qos+default+flow-queue+statistics+interface) { *interface-name* | *interface-type* *interface-number* } **outbound** command to check FQ statistics on a specified channelized sub-interface.