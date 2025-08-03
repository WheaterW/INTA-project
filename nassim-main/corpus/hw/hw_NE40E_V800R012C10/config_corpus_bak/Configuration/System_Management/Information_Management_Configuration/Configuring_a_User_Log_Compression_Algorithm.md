Configuring a User Log Compression Algorithm
============================================

Configuring_a_User_Log_Compression_Algorithm

#### Context

Two algorithms can be used to compress user logs: Deflate and Lempel-Ziv-Markov chain algorithm (LZMA). Deflate focuses on fast compression, and LZMA focuses on a high compression ratio and fast decompression. For an 8 MB log file, Deflate can compress the file to about 600 KB, and LZMA can compress the file to about 150 KB. Deflate takes about 150 ms to complete compression, and LZMA takes about 588 ms. You can choose the user log compression algorithm that best suits your needs. If you require faster compression, use Deflate. If you want to store more logs within a limited space, use LZMA.


#### Procedure

1. Run the [**system-view**](cmdqueryname=system-view) command to enter the system view.
2. Run the [**info-center logfile compression lzma**](cmdqueryname=info-center+logfile+compression+lzma) command to configure LZMA as the user log compression algorithm.
3. Run the [**commit**](cmdqueryname=commit) command to commit the configuration.