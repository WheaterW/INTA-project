Configuring Detection of Overlapping IPsec Flows
================================================

Configuring Detection of Overlapping IPsec Flows

#### Prerequisites

The overlapping IPsec flow detection function takes effect only for template IPsec policies.


#### Context

When IPsec is deployed on a mobile bearer network, new base stations are usually added for network upgrade and capacity expansion, and the device needs to interconnect with these new base stations. This is typically a complex scenario involving a large number of base stations. The data flows configured and negotiated for encryption may overlap with existing data flows, causing IPsec service faults. After these faults occur, queried tunnel status information is normal and packets will still be forwarded without being dropped. Fault location becomes difficult and time-consuming.

To solve this problem, configure detection of overlapping IPsec flows so that the device can detect whether the data flows generated through a new tunnel for encryption overlap with existing ones after IKE negotiation.

* If not, the new tunnel is successfully established.
* If so, the new tunnel cannot be established. This prevents IPsec service faults caused by overlapping of data flows to be encrypted.

This function applies only to new IPsec tunnels and detects overlapping data flows between new IPsec tunnels and existing IPsec tunnels that are established in the same VPN instance as new IPsec tunnels. This function supports the detection of the source IP address/address group, destination IP address/address group, source port range, destination port range, protocol, and DSCP fields. Overlapping flow detection cannot be performed on existing or renegotiated IPsec tunnels or delivered ACL configurations.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**ipsec flow-overlap check enable**](cmdqueryname=ipsec+flow-overlap+check+enable) command to enable detection of overlapping IPsec flows.
   
   
   
   If overlapping flows are detected, re-plan and deliver more refined ACL configurations to prevent IPsec service faults caused by overlapping flows.