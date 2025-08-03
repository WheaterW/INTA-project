Verifying the Configuration
===========================

After configuring SRv6 TE Policies, verify the configuration.

#### Prerequisites

SRv6 TE Policies have been configured.


#### Procedure

1. Run the [**display srv6-te policy**](cmdqueryname=display+srv6-te+policy) [ **endpoint** *endpoint-ip* **color** *color-value* | **policy-name** *name-value* | **binding-sid** *binding-sid* ] command to check SRv6 TE Policy details.
2. Run the [**display srv6-te policy statistics**](cmdqueryname=display+srv6-te+policy+statistics) command to check SRv6 TE Policy statistics.
3. Run the [**display srv6-te policy status**](cmdqueryname=display+srv6-te+policy+status) { **endpoint** *endpoint-ip* **color** *color-value* | **policy-name** *name-value* | **binding-sid** *binding-sid* } command to check SRv6 TE Policy status to determine the reason why a specified SRv6 TE Policy cannot go up.
4. Run the [**display srv6-te policy last-down-reason**](cmdqueryname=display+srv6-te+policy+last-down-reason) { **endpoint** *endpoint-ip* **color** *color-value* | **policy-name** *name-value* | **binding-sid** *binding-sid* } command to check records about events where SRv6 TE Policies or segment lists in SRv6 TE Policies go down.
5. Run the [**ping srv6-te policy**](cmdqueryname=ping+srv6-te+policy) { **policy-name** *policyname* | **endpoint-ip** *endpointipv6* **color** *colorid* | **binding-sid** *bsid* } [ **end-op** *endop* ] [ **-a** *sourceaddr6* | **-c** *count* | **-m** *interval* | **-s** *packetsize* | **-t** *timeout* | **-tc** *tc* | **-h** *hoplimit* ] \* command with the **policy-name** *policyname*, **endpoint-ip** *endpointipv6* **color** *colorid*, or **binding-sid** *bsid* parameter configured to ping the specified SRv6 TE Policy to check its connectivity.
6. Run the [**display srv6-te flow-group**](cmdqueryname=display+srv6-te+flow-group) command to check SRv6 TE flow group details.