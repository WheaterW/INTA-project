Configuring the Function of Clearing the MAC Addresses of Specific PWs
======================================================================

After you configure the function, a VSI deletes the MAC
address of the PW carried in a received MAC Withdraw message carrying
0x404 TLV but retains the MAC addresses of the other PWs and AC interfaces.

#### Context

In the scenario where a CE accesses an L2VPN network,
when the AC between the CE and its connected PE becomes faulty frequently,
the PE will generate a large number of MAC Withdraw messages carrying
0x404 TLV. After receiving these MAC Withdraw messages, the VSI of
the remote PE will frequently clear MAC address information. If the
VSI has many PWs, traffic will be broadcast for a long period, wasting
device bandwidth. To resolve the issue, configure the function of
clearing the MAC addresses of specific PWs.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**vsi**](cmdqueryname=vsi) *vsi-name*
   
   
   
   The VSI view is displayed.
3. Run [**local-mac remove all-from-me**](cmdqueryname=local-mac+remove+all-from-me)
   
   
   
   The function
   of clearing the MAC addresses of specific PWs is configured.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.