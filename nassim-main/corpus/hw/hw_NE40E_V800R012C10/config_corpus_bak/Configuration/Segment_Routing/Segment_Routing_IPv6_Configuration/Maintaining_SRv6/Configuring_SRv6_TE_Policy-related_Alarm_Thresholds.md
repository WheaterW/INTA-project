Configuring SRv6 TE Policy-related Alarm Thresholds
===================================================

You can configure SRv6 TE Policy-related alarm thresholds, enabling the device to generate an alarm when the number of SRv6 TE Policies, SRv6 TE flow groups, or segment lists reaches the specified threshold. This facilitates O&M.

#### Context

If the number of SRv6 TE Policies, SRv6 TE flow groups, or segment lists exceeds the upper limit, adding new ones may affect existing services. To prevent this, you can configure alarm thresholds for the numbers of SRv6 TE Policies, SRv6 TE flow groups, and segment lists so that alarms are generated when the thresholds are exceeded.

Ensure that the value of **lower-limit** *lowerLimitValue* is less than that of **upper-limit** *upperLimitValue*. *lowerLimitValue* must range from 1 to 99, and *upperLimitValue* must range from 2 to 100. They are both expressed in percentage.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) command to enable SRv6 and enter its view.
3. Run the [**srv6-te-policy segment-list-number threshold-alarm**](cmdqueryname=srv6-te-policy+segment-list-number+threshold-alarm) **upper-limit** *upperLimitValue* **lower-limit** *lowerLimitValue* command to configure an alarm threshold for the number of segment lists.
4. Run the [**srv6-te-policy policy-number threshold-alarm**](cmdqueryname=srv6-te-policy+policy-number+threshold-alarm) **upper-limit** *upperLimitValue* **lower-limit** *lowerLimitValue* command to configure an alarm threshold for the number of SRv6 TE Policies.
5. Run the [**srv6-te flow-group-number threshold-alarm**](cmdqueryname=srv6-te+flow-group-number+threshold-alarm)**upper-limit***upperLimitValue* **lower-limit** *lowerLimitValue* command to configure an alarm threshold for the number of SRv6 TE flow groups.
6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.