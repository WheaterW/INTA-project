Understanding IS-IS Fast Convergence
====================================

IS-IS fast convergence is an extended feature used to speed up route convergence based on the incremental shortest path first (I-SPF) algorithm, partial route calculation (PRC) algorithm, fast LSP flooding, and intelligent timers.

#### I-SPF

In ISO 10589, the Dijkstra algorithm (SPF algorithm) is used to calculate routes. When a node changes on the network, this algorithm recalculates all routes, which takes a long time and consumes too many CPU resources, reducing the convergence speed.

I-SPF improves the algorithm. Except for the first time the algorithm is run to calculate all nodes on the network, only the nodes that have changed are used in subsequent calculations, significantly decreasing CPU usage and speeding up network convergence. In addition, the SPT generated using I-SPF is the same as that generated using the Dijkstra algorithm.


#### PRC

Similar to I-SPF, PRC only recalculates the routes that have changed. PRC, however, does not calculate the shortest path. Instead, it updates routes based on the SPT calculated by I-SPF. If the SPT changes after I-SPF calculation, PRC only processes the routing information on the changed routing device. If the SPT remains unchanged, PRC only processes the changed routing information.

For example, if IS-IS is newly enabled on an interface of a device, the SPT calculated remains unchanged. In this case, PRC only updates the routes to this interface, consuming fewer CPU resources. PRC works with I-SPF to improve network convergence performance. As a result, PRC and I-SPF have replaced the SPF algorithm.


#### Fast LSP Flooding

When an IS-IS device receives updated LSPs, it updates the corresponding LSPs in its LSDB and periodically floods the updated LSPs based on a timer. Therefore, the synchronization of all LSDBs is slow.

With fast LSP flooding, when a device receives LSPs that trigger route calculation or route update, it floods these LSPs before route calculation occurs to speed up network convergence and LSDB synchronization throughout the entire network.

![](public_sys-resources/note_3.0-en-us.png) 

LSP fast flooding is supported by default and does not need to be configured.



#### Intelligent Timers

Even with an improved route calculation algorithm, a long interval required to trigger route calculation still impacts the convergence speed. As such, a millisecond-level timer is needed to shorten this interval. However, excessive CPU resources will be consumed when frequent network changes occur. The intelligent timer for SPF calculation addresses these problems.

In normal cases, an IS-IS network that runs normally is stable, and frequent network topology changes are rare. As such, IS-IS does not frequently calculate routes, and a short period (milliseconds) can be configured as the first interval for route calculation. If the network topology changes frequently, the interval set by the intelligent timer will increase with the calculation count to reduce CPU resource consumption.

In addition to the intelligent timer for SPF calculation, there is the intelligent timer for LSP generation. When the intelligent timer for LSP generation expires, the system generates a new LSP based on the current topology. However, the interval set by the timer is fixed and cannot meet the requirements for fast convergence and low CPU resource consumption. Therefore, an intelligent timer for LSP generation is designed to quickly respond to emergencies (for example, when an interface goes up or down) and speed up network convergence. In addition, if the network topology changes frequently, the interval set by the intelligent timer automatically increases to reduce CPU resource consumption.