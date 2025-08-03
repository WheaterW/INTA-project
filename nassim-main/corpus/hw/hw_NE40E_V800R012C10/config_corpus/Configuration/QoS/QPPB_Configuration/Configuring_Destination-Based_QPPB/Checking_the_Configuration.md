Checking the Configuration
==========================

After QPPB is configured, you can view QPPB information.

#### Context

You can run the **display** commands in any view to check QPPB running information. For details about QPPB running information, see the chapter "QoS Commands" in the *HUAWEI NE40E-M2 series Universal Service Router Command Reference*.


#### Procedure

1. Run the [**display qppb local-policy configuration**](cmdqueryname=display+qppb+local-policy+configuration) *policy-name* command to check the configuration of a specific QPPB local policy.
2. Run the [**display qppb local-policy statistics**](cmdqueryname=display+qppb+local-policy+statistics) **interface** *interface-type* *interface-number* [ **qos-local-id** *qos-local-id* ] { **inbound** | **outbound** } command to check the statistics about a specific QPPB local policy.