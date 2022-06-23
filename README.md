AR gene == 901-919 amino acids

Among the normal methods, only composition-based binning makes sense (if that).

The curse of dimensionality (clustering very affected): addressed by shortening regions maximally

Hierachical clustering chosen as the method because:

1. Underlying clusters cannot be assumed to be globular.
2. No need to specify number of clusters

Reference genome selected according to https://lh3.github.io/2017/11/13/which-human-reference-genome-to-use
(why?)

https://www.open-mpi.org/software/ompi/v4.1/

CUDA install
Download from homepage (version 4.x unless you don't mind symlinking manually), compile from source

-   to symlink manually, run:
    sudo find / -iname "libmpi\.so\*"

./configure && make && sudo make install

LD_LIBRARY_PATH=/usr/local/lib cluster/cluster i testData.fasta o result.fasta
For LD_LIBRARY_PATH, you should use the most sensible result of `sudo find / -iname "libmpi\.so*"`. Use the full path to the folder, but **without** the filename (the 'libmpi whatever' bit).

If stuck on an Intel (= not NVIDIA) GPU architecture, follow the instructions at https://github.com/vosen/ZLUDA.

If you get libstdc++.so.6: version `GLIBCXX_3.4.26' not found, install /usr/lib/x86_64-linux-gnu

Link to CUDA compatability table
