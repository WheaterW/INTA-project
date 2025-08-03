Disabling Local Protection for SRv6 TE Policies
===============================================

Local protection for SRv6 TE Policies can be disabled to prevent SRv6 traffic from bypassing key value-added service (VAS) devices.

#### Prerequisites

Before disabling local protection for SRv6 TE Policies, complete the following task:

* Configure an SRv6 TE Policy.

#### Context

If the segment lists of an SRv6 TE Policy's primary candidate path all fail and a local protection path (for example, a TI-LFA or TE FRR path) exists, data traffic is switched to the TI-LFA or TE FRR path for forwarding.

In SRv6 TE Policy-based SFC scenarios, the SIDs in the segment lists of an SRv6 TE Policy belong to dedicated devices such as firewalls and traffic cleaning devices. For this reason, traffic steered into the SRv6 TE Policy is not allowed to bypass any of the SIDs during forwarding.

In this case, you need to disable local protection for SRv6 TE Policies, so that data traffic will not be switched to the TI-LFA or TE FRR path when the segment lists of the primary candidate path fail, preventing the traffic from bypassing dedicated devices such as firewalls and traffic cleaning devices.


#### Procedure

* On the headend, disable local protection for SRv6 TE Policies.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
     
     
     
     SRv6 is enabled, and the SRv6 view is displayed.
  3. Run [**srv6-te policy**](cmdqueryname=srv6-te+policy) *name-value* [ **endpoint** *endpoint-ip* **color** *color-value* ]
     
     
     
     The SRv6 TE Policy view is displayed.
  4. Run [**forward no-bypass**](cmdqueryname=forward+no-bypass)
     
     
     
     Local protection for SRv6 TE Policies is disabled.
  5. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.
* On the SFF of an SFC, disable local protection for SRv6 TE Policies.
  1. Run [**system-view**](cmdqueryname=system-view)
     
     
     
     The system view is displayed.
  2. Run [**segment-routing ipv6**](cmdqueryname=segment-routing+ipv6)
     
     
     
     SRv6 is enabled, and the SRv6 view is displayed.
  3. Run [**locator**](cmdqueryname=locator) *locator-name* [ **ipv6-prefix** *ipv6-address* *prefix-length* [ **static** *static-length* | **args** *args-length* ] \* [ **default** ] ]
     
     
     
     The SRv6 locator view is displayed.
  4. Run [**opcode**](cmdqueryname=opcode) *func-opcode1* **end-as**
     
     
     
     An opcode for static End.AS SIDs is configured, and the static SRv6 SFC proxy view is displayed.
  5. Run [**cache forward no-bypass**](cmdqueryname=cache+forward+no-bypass)
     
     
     
     A bypass protection path is configured to protect traffic against SF service failures.
     
     
     
     If the [**forward no-bypass**](cmdqueryname=forward+no-bypass) command is run on the headend of an SRv6 TE Policy to disable local protection, you need to run the [**cache forward no-bypass**](cmdqueryname=cache+forward+no-bypass) command on the SFF of the SFC to prevent the loss of the No-bypass flag during packet forwarding.
  6. Run [**commit**](cmdqueryname=commit)
     
     
     
     The configuration is committed.