Referencing an SRv6 TE Policy Attribute Template
================================================

After creating an SRv6 TE Policy attribute template, you can reference it to create an SRv6 TE Policy.

#### Context

An SRv6 TE Policy attribute template can be used in scenarios where SRv6 TE Policies are manually configured or dynamically delivered by a controller. In scenarios where SRv6 TE Policies are manually configured, you can directly reference such an attribute template to configure related functions in batches. In scenarios where SRv6 TE Policies are dynamically delivered by a controller, you can configure the desired attribute template to be referenced before SRv6 TE Policy delivery.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6) command to enable SRv6 and enter its view.
3. Run the [**srv6-te policy**](cmdqueryname=srv6-te+policy) *name-value* command to enter the SRv6 TE Policy view.
4. Run the [**candidate-path preference**](cmdqueryname=candidate-path+preference) *preference* command to enter the candidate path view of the SRv6 TE Policy.
5. Run the [**template**](cmdqueryname=template) *template-value* command to specify the SR Policy attribute template to be referenced by the candidate path.
6. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.