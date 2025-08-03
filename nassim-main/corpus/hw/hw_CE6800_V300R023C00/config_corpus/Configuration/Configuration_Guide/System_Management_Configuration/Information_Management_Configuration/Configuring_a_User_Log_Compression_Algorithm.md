Configuring a User Log Compression Algorithm
============================================

Configuring a User Log Compression Algorithm

#### Context

Two algorithms can be used to compress user logs: Deflate and Lempel-Ziv-Markov chain algorithm (LZMA). Deflate focuses on fast compression, and LZMA focuses on a high compression ratio and fast decompression. For an 8 MB log file, Deflate can compress the file to about 600 KB, and LZMA can compress the file to about 150 KB. Deflate takes about 150 ms to complete compression, and LZMA takes about 588 ms. You can choose the user log compression algorithm that best suits your needs. If you require faster compression, use Deflate. If you want to store more logs within a limited space, use LZMA.


#### Procedure

1. Enter the system view.
   
   
   ```
   [system-view](cmdqueryname=system-view)
   ```
2. Configure LZMA as the user log compression algorithm.
   
   
   ```
   [info-center logfile compression lzma](cmdqueryname=info-center+logfile+compression+lzma)
   ```
   
   By default, Deflate is used to compress user logs.
3. Commit the configuration.
   
   
   ```
   [commit](cmdqueryname=commit)
   ```