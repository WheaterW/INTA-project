(Optional) Configuring a CPE to Use the IP Address Obtained by the LNS User to Establish a BGP Connection with a BRAS
=====================================================================================================================

A client connects to the LNS through a CPE and LAC. The CPE obtains an IP address through L2TP user access. In this way, the CPE's downstream devices or other IP addresses can communicate with the LNS.

#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**aaa**](cmdqueryname=aaa)
   
   
   
   The AAA view is displayed.
3. (Optional) Run [**bgp over lns enable**](cmdqueryname=bgp+over+lns+enable)
   
   
   
   The CPE is enabled to use the IP address obtained by the LNS user to establish a BGP connection with the BRAS during L2TP user access.
   
   
   
   The CPE obtains an IP address through L2TP user access. However, after the CPE and LNS learn BGP routes through BGP, traffic cannot be forwarded through such routes between these devices. To solve this problem, run this command.
4. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.