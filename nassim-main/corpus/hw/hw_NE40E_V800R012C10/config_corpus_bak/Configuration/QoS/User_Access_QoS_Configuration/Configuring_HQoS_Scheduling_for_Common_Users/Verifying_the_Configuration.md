Verifying the Configuration
===========================

After HQoS scheduling is configured for common users, you can view the configuration and application information about the specified QoS profile.

#### Procedure

1. Run the [**display qos-profile configuration**](cmdqueryname=display+qos-profile+configuration) [ *profile-name* ] command to check the configuration about a QoS profile.
2. Run the [**display qos-profile application**](cmdqueryname=display+qos-profile+application) *profile-name* command to check application of a QoS profile.
3. Run the [**display qos scheduling-mode**](cmdqueryname=display+qos+scheduling-mode) **slot** *slot-id* command to check the scheduling mode of a board.
4. Run the [**display qos resource sub-port-queue**](cmdqueryname=display+qos+resource+sub-port-queue) **slot** *slot-id* **outbound** command to check the usage of sub-interface queues.
5. Run the [**display queue-4cos-mapping configuration**](cmdqueryname=display+queue-4cos-mapping+configuration) [ **verbose** [ *queue-4cos-mapping-name* ] ] command to check the configurations of 4-CoS mapping profiles, including the number of profiles, profile names, mappings, and reference relationships.