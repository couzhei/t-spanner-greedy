# t-spanner-greedy algorithm

This is a repository for my Python implementation of a [t-spanner greedy algorithm](https://en.wikipedia.org/wiki/Greedy_geometric_spanner). I used the adjancency list representations of Graph. Implemented Node and Edge classes separately. A careful algorithm geek might suspect a lot of space is going to be taken, so a little tweaking might be in great need. Nonetheless, I hope the implementation drives the point home, in order to show that these kinds of algorithms are all about. Which is, as t gets bigger and bigger, the t-spanner, precisely resembles a *minimum weight spanning tree*.

To run the application, you need to first check if you meet the `requirements.txt`(pun intended!), or if you prefer using Anaconda, the `.yml` file under the same name. I'm not a pro PyQt user, so I'm guessing you find my implemenation annoying, but I marked the algorithm in the main.py by comments, and abstracted away the graph, vertex, etc. implementations away on a `digraph` package. Ultimately, running `python main.py` will run the program.

If you want to find a quick overview on the subject, and graph spanners in general, [this](https://arxiv.org/abs/1909.03152) paper would be a great starter. For a special analysis on the subject, check [this](https://arxiv.org/abs/1702.05900) article on the same matter.

Early 90s [researchs](https://www.researchgate.net/publication/220983492_A_Fast_Algorithm_for_Constructing_Sparse_Euclidean_Spanners) of professors [Narasimhan](https://www.researchgate.net/profile/Giri_Narasimhan) and [Das](https://en.wikipedia.org/wiki/Gautam_Das_(computer_scientist)) are invaluable to this end, and I highly recommend checking them.
#### Other references:
* For diving deeper into the [Weighted Graph Algorithms with Python](https://core.ac.uk/download/pdf/230921366.pdf)
* [networkx](https://networkx.org/documentation/stable//reference/algorithms/shortest_paths.html) is a great package if you're not really into implementing things by yourself.
* [Edith Cohen, Fast algorithms for constructing t-spanners and paths with stretch t, *AT&T Bell Laboratories Murray  Hill, NJ 07974, 1993*](https://www.computer.org/csdl/pds/api/csdl/proceedings/download-article/12OmNy3AgqG/pdf)

