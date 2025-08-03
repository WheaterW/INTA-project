Verifying the Configuration
===========================

Verifying the Configuration

#### Procedure

| Operation | Command |
| --- | --- |
| Check the configured traffic classifiers. | [**display traffic classifier**](cmdqueryname=display+traffic+classifier) [ *classifier-name* ] |
| Check the configured traffic behaviors. | [**display traffic behavior**](cmdqueryname=display+traffic+behavior) [ *behavior-name* ] |
| Check the configured traffic policy. | [**display traffic policy**](cmdqueryname=display+traffic+policy) [ *policy-name* [ **classifier** *classifier-name* ] ] |
| Check the traffic policy application records. | [**display traffic-policy applied-record**](cmdqueryname=display+traffic-policy+applied-record) |
| Check TCAM delivery failures. | [**display system tcam fail-record**](cmdqueryname=display+system+tcam+fail-record) [ **slot** *slot-id* ] |
| Check the group indexes and rule counts occupied by different services. | [**display system tcam service brief**](cmdqueryname=display+system+tcam+service+brief) [ **slot** *slot-id* ]  [**display system tcam service**](cmdqueryname=display+system+tcam+service) { [**cpcar**](cmdqueryname=cpcar) [**slot**](cmdqueryname=slot) *slot-id* | *service-name* [**slot**](cmdqueryname=slot) *slot-id* [ [**chip**](cmdqueryname=chip) *chip-id* ] } |
| Check the traffic policy application records. | [**display system tcam service traffic-policy**](cmdqueryname=display+system+tcam+service+traffic-policy) |
| Check information about matched rules. | [**display system tcam match-rules**](cmdqueryname=display+system+tcam+match-rules) **slot** *slot-id* |
| Check statistics on packets that match a traffic policy. | **[**display traffic-policy statistics**](cmdqueryname=display+traffic-policy+statistics)** |
| Check statistics on packets matching hardware-based ACLs. | [**display acl hardware statistics**](cmdqueryname=display+acl+hardware+statistics)  NOTE:  The device can display only the statistics on the packets matching the hardware-based ACL referenced by MQC. To implement this, you need to first run the [**statistics enable**](cmdqueryname=statistics+enable) command in the traffic behavior view to enable traffic statistics collection. |
| Check matching fields and actions supported by a traffic policy in each view. | [**display system tcam acl group-information**](cmdqueryname=display+system+tcam+acl+group-information) |
| Check information about the resources occupied by the traffic policy to be applied to determine whether the traffic policy can be successfully applied after the configuration is committed. | [**display traffic-policy pre-state**](cmdqueryname=display+traffic-policy+pre-state) |

For details about the display commands, see the *Command Reference*.