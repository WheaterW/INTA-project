Configuring Interface MSD Advertisement (IPv4)
==============================================

Interface maximum SID depth (MSD) advertisement allows IS-IS to advertise the MSD of Segment Routing (SR) interfaces.

#### Usage Scenario

When calculating paths for SR-TE Policies in an SR scenario, the controller needs to determine paths and calculate binding SIDs based on the MSD advertised by an IGP. When the link MSDs of multiple interfaces on a device are different, the node MSD advertised by IS-IS is the smallest value among all link MSDs. Comparing with advertising node MSDs only, advertising link MSDs provides more accurate MSD information, allowing the controller to calculate paths more efficiently.


#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**segment-routing**](cmdqueryname=segment-routing)
   
   
   
   The SR view is displayed.
3. Run [**quit**](cmdqueryname=quit)
   
   
   
   Return to the system view.
4. Run [**isis**](cmdqueryname=isis) [ *process-id* ]
   
   
   
   An IS-IS process is created, and the IS-IS view is displayed.
5. Run [**cost-style**](cmdqueryname=cost-style) { **wide** | **wide-compatible** | **compatible** }
   
   
   
   An IS-IS cost style is set.
6. Run [**segment-routing mpls**](cmdqueryname=segment-routing+mpls)
   
   
   
   Segment Routing is enabled for IS-IS.
7. Run **[**link-msd advertisement enable**](cmdqueryname=link-msd+advertisement+enable)** [ **level-1** | **level-2** | **level-1-2** ]
   
   
   
   Interface MSD advertisement is enabled.
8. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.

#### Verifying the Configuration

After the configuration is complete, verify it.

* Run the [**display isis lsdb**](cmdqueryname=display+isis+lsdb) **verbose** command to check IS-IS LSDB information.
* Run the **display isis traffic-eng advertisements** command to check the TE information advertised by IS-IS.