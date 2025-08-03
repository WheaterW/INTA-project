Configuring the ETH-Test Function for a VLAN
============================================

The ETH-test function is short for Ethernet test signal. ETH-test instances are performed for a unidirectional on-demand service or during an on-demand-service interruption to calculate parameters, including the maximum bandwidth, frame loss ratio, and bit error rate.

#### Context

In [Figure 1](#EN-US_TASK_0172362106__fig_dc_vrp_y1731_cfg_006901), MEP1 is configured on an AC interface of PE1, and MEP2 is configured on an AC interface of PE2. MEP1 initiates an ETH-test and sends test packets with a specified size and code type at a specified rate and interval. Then check the number of packets MEP1 sends and the number of packets MEP2 receives. If MEP1 sends more packets than MEP2 receives, some packets have been dropped. Then MEP1 is configured to use the bisection method to continue the test and send test packets at a lower rate. The bisection method is used to send test packets at different rates between the upper and lower rate thresholds. The test process repeats until a maximum bandwidth is found when no packets are dropped in a test. In addition, check for bit errors on MEP2 that receives test packets.

**Figure 1** ETH-test function for a VLAN network  
![](images/fig_dc_vrp_y1731_cfg_006901.png)

#### Procedure

1. Perform the following steps on PEs:
   
   
   1. Run [**system-view**](cmdqueryname=system-view)
      
      The system view is displayed.
   2. Run [**cfm enable**](cmdqueryname=cfm+enable)
      
      CFM is enabled.
   3. Run [**cfm md**](cmdqueryname=cfm+md) *md-name*
      
      The MD view is displayed.
   4. Run [**ma**](cmdqueryname=ma) *ma-name*
      
      The MA view is displayed.
   5. Run [**map**](cmdqueryname=map) **vlan** *vlan-id*
      
      The MA is bound to a VLAN.
   6. Run [**mep mep-id**](cmdqueryname=mep+mep-id)
      
      A MEP is configured.
   7. Run [**remote-mep mep-id**](cmdqueryname=remote-mep+mep-id) *mep-id*
      
      An RMEP is configured.
   8. Run [**eth-test enable**](cmdqueryname=eth-test+enable) **mep** *mep-id*
      
      The ETH-test function is enabled.
   9. Run [**eth-test start**](cmdqueryname=eth-test+start) **mep** *mep-id* { **mac** *mac-address* | **remote-mep** *mep-id* } **rate** *rate-value* [ [ **timeout** *timeout-value* ] | [ **pattern** { **zero-no-crc** | **zero-crc** } ] | [ **8021p** *8021p-value* ] | [ **packet-size** *packet-size-value* ] | **out-of-service** { **lck-level** *level-value* } ] \*
      
      The MEP is enabled to send test packets. The rate at which Eth-Test packets are sent is the L2 rate.
   10. (Optional) Run [**eth-test stop**](cmdqueryname=eth-test+stop) **mep** *mep-id*
       
       The MEP is disabled from sending test packets.
   11. Run [**commit**](cmdqueryname=commit)
       
       The configuration is committed.