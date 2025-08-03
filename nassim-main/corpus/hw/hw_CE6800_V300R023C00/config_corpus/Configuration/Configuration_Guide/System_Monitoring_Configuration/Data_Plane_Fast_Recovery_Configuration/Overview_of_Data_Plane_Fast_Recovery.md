Overview of Data Plane Fast Recovery
====================================

Overview of Data Plane Fast Recovery

#### Definition

Data Plane Fast Recovery (DPFR) is a sub-millisecond-level fault recovery technology. It provides local or remote fast fault convergence based on the data plane to ensure that service performance is not affected if a link fails.


#### Purpose

Traditional route convergence technologies rely on information exchange and path recomputation being performed by dynamic routing protocols (such as OSPF and BGP) on the control plane. Although Bidirectional Forwarding Detection (BFD) can accelerate the detection of faults when they occur, route convergence still takes hundreds of milliseconds to complete, and can even take seconds for a large-scale DCN.

Online transaction applications, such as high-performance storage services and high-performance database access services, require ultimate performance and high reliability. For such services, taking hundreds of milliseconds to restore service transmission after a link fault occurs is unacceptable. Continuous packet loss may cause transaction failures or even connection timeout of the peer protocol stack. As a result, the application performance deteriorates significantly.

To solve this problem, DPFR is developed. It evolves from the traditional control plane-based fault convergence to the data plane-based fault convergence. Based on the data plane, it can perform fast fault detection, remote fault advertisement, and fast path switching, achieving sub-millisecond-level fault convergence and minimizing the impact on service performance. This technology provides higher reliability and stability for mission-critical applications such as high-performance databases, storage, and supercomputing.