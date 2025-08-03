Configuring a Hash Algorithm for Load Balancing
===============================================

Configure a hash algorithm for load balancing on an interface board to ensure even load balancing.

#### Context

Different load balancing results will be achieved using different hash algorithms. You can select an appropriate hash algorithm for load balancing based on a traffic model. In two-level load balancing scenarios, the hash algorithms for level-1 and level-2 load balancing cannot be the same. Otherwise, level-2 load balancing does not take effect on the involved router.

On the network shown in [Figure 1](#EN-US_TASK_0000001219752233__fig_load-balance_feature_02801), traffic is load-balanced on R1 and also load-balanced on R2 and R3. This is called two-level load balancing.

**Figure 1** Two-level load balancing networking (1)  
![](figure/en-us_image_0000001221050581.png)

If R2 and R3 use the same load balancing algorithm as R1, R1 can calculate only two results (for example, a and b) for the same data flow. In the example shown in [Figure 2](#EN-US_TASK_0000001219752233__fig_load-balance_feature_02802), the data flow with result a travels along Link1 to R2, and the data flow with result b travels along Link2 to R3. When the data flow with result a arrives at R2, R2 still calculates result a because it uses the same load balancing algorithm as R1. As such, the data flow still goes through Link1 to arrive at R4. Similarly, when the data flow with result b arrives at R3, R3 still calculates result b. As such, the data flow still goes through Link2 to arrive at R7.

**Figure 2** Two-level load balancing networking (2)  
![](figure/en-us_image_0000001220929145.png)

As such, when Level-1 and Level-2 devices have the same load balancing algorithm, traffic is not equally load-balanced on Level-2 devices, or even traffic is not distributed to some links at all.

![](../../../../public_sys-resources/note_3.0-en-us.png) 

In VS mode, this configuration process is supported only by the admin VS.



#### Procedure

1. Run [**system-view**](cmdqueryname=system-view)
   
   
   
   The system view is displayed.
2. Run [**slot**](cmdqueryname=slot) *slot-id*
   
   
   
   The slot view is displayed.
3. Run [**load-balance hash-arithmetic**](cmdqueryname=load-balance+hash-arithmetic) { **arithmetic1** | **arithmetic2** | **arithmetic3** | **arithmetic4** | **arithmetic5** } [ **second-hash** ]
   
   
   
   A hash algorithm for load balancing is configured on the interface board.
4. Run [**load-balance hash-arithmetic random**](cmdqueryname=load-balance+hash-arithmetic+random)
   
   
   
   The random hash algorithm is configured for load balancing on the interface board.
5. Run [**load-balance hash-arithmetic second-hash**](cmdqueryname=load-balance+hash-arithmetic+second-hash)
   
   
   
   The secondary hash function is configured for the hash algorithm for load balancing on the interface board.
6. Run [**load-balance hash-arithmetic**](cmdqueryname=load-balance+hash-arithmetic) { **arithmetic1** | **arithmetic2** | **arithmetic3** | **arithmetic4** | **arithmetic5** }
   
   
   
   A hash algorithm for load balancing is configured on the interface board.
7. Run [**commit**](cmdqueryname=commit)
   
   
   
   The configuration is committed.