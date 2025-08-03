Verifying the Configuration
===========================

After HQoS is configured for family users, you can view information about the online users with specified IDs and the bandwidth consumed by them and applications of the QoS profile.

#### Context

Run the following commands to check the configuration.


#### Procedure

1. Run the [**display qos-profile configuration**](cmdqueryname=display+qos-profile+configuration) [ *profile-name* ] command to check the configuration about a QoS profile.
2. Run the [**display qos-profile application**](cmdqueryname=display+qos-profile+application) *profile-name* command to check application of a QoS profile.
3. Run the [**display qos scheduling-mode**](cmdqueryname=display+qos+scheduling-mode) **slot** *slot-id* command to check the scheduling mode of a board.
4. Run the [**display qos resource sub-port-queue**](cmdqueryname=display+qos+resource+sub-port-queue) **slot** *slot-id* **outbound** command to check the usage of sub-interface queues.
5. Run the [**display sub-port-queue configuration**](cmdqueryname=display+sub-port-queue+configuration) [ **verbose** [ *sub-port-queue-name* ] ] command to check information about sub-interface queues.
6. Run the [**display sub-port-queue statistics**](cmdqueryname=display+sub-port-queue+statistics) **interface** *interface-type* *interface-number* **outbound** command to check statistics about sub-interface queues.