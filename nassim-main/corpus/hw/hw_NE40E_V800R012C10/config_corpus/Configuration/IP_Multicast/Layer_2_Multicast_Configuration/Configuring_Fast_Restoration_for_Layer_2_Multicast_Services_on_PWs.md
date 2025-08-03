Configuring Fast Restoration for Layer 2 Multicast Services on PWs
==================================================================

To rapidly restore the Layer 2 multicast services on a PW when the PW goes Down and then Up, delay or disable the deletion of the Layer 2 multicast forwarding entries when the PW goes Down.

#### Usage Scenario

All Layer 2 multicast forwarding entries of a PW outbound interface are deleted after the PW goes Down. The services can be restored only after the PW goes Up and the entries are re-created. To ensure that Layer 2 multicast services are not interrupted or are interrupted for less than 50 ms during PW re-establishment, configure fast restoration for services on PWs by delaying or disabling the deletion of Layer 2 multicast forwarding entries of PW outbound interfaces when PWs go Down.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
   
   
   
   The VSI view is displayed.
3. Run [**l2-multicast pw-fast-control**](cmdqueryname=l2-multicast+pw-fast-control) **holdtime** *interval*
   
   
   
   Fast restoration is configured for Layer 2 multicast services on PWs.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Checking the Configurations

Run the [**display current-configuration**](cmdqueryname=display+current-configuration) [**| include**](cmdqueryname=%7C+include)  [**l2-multicast pw-fast-control**](cmdqueryname=l2-multicast+pw-fast-control) command to check whether fast restoration is configured for Layer 2 multicast services on PWs.

```
<HUAWEI> display current-configuration | include l2-multicast pw-fast-control
 l2-multicast pw-fast-control holdtime 20
```