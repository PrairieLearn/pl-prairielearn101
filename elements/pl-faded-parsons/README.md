# [The Faded Parsons Element](https://github.com/ace-lab/pl-faded-parsons)
This repository contains the Berkeley Faded Parson's element and is designed to be used as a submodule.
**Note, however, that the PrairieLearn server doesn't handle submodules properly when syncing a GitHub repo,**
so to use this in a course, either the course's `elements/` subdirectory will need to contain a **copy** of this repo,
or the top-level `elements/` directory of the PrairieLearn build itself will need a copy of it.

## Adding to Your Projects (for development only)

This command will add the element to your project in the **properly-named** directory for PrairieLearn to use this element.
``` bash
git submodule add https://github.com/ace-lab/pl-faded-parsons.git ./elements/pl-faded-parsons/
```

The main branch is the most recent public release.

## Pulling Changes into Your Projects

As detailed [in the "Working on a Project with Submodules" section of the git book](https://git-scm.com/book/en/v2/Git-Tools-Submodules), pulling must be done with a different command.

From the top-level of your directory run:
``` bash
git submodule update --remote ./elements/pl-faded-parsons/
```

## Work around `pl-faded-parsons`
[Nathaniel Weinman, Armando Fox, and Marti A. Hearst. 2021. Improving Instruction of Programming Patterns with Faded Parsons Problems. In Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems (CHI '21). Association for Computing Machinery, New York, NY, USA, Article 53, 1–4. https://doi.org/10.1145/3411764.3445228](https://dl.acm.org/doi/10.1145/3411764.3445228)

[Logan Caraco, Nate Weinman, Stanley Ko and Armando Fox. 2022. Automatically Converting Code-Writing Exercises to Variably-Scaffolded Parsons Problems. EECS Department University of California, Berkeley Technical Report No. UCB/EECS-2022-173. June 27, 2022. http://www2.eecs.berkeley.edu/Pubs/TechRpts/2022/EECS-2022-173.pdf](http://www2.eecs.berkeley.edu/Pubs/TechRpts/2022/EECS-2022-173.pdf)

[Nelson Lojo and Armando Fox. 2022. Teaching Test-Writing As a Variably-Scaffolded Programming Pattern. In Proceedings of the 27th ACM Conference on on Innovation and Technology in Computer Science Education Vol. 1 (ITiCSE '22). Association for Computing Machinery, New York, NY, USA, 498–504. https://doi.org/10.1145/3502718.3524789](https://dl.acm.org/doi/10.1145/3502718.3524789)

[Lauren Zhou, Akshit Dewan, Anirudh Kothapalli, Pamela Fox, Michael Ball, and Thomas Joseph. 2023. Implementing Faded Parsons Problems in a Very Large CS1 Course. In Proceedings of the 54th ACM Technical Symposium on Computer Science Education V. 2 (SIGCSE 2023). Association for Computing Machinery, New York, NY, USA, 1356. https://doi.org/10.1145/3545947.3576300](https://dl.acm.org/doi/abs/10.1145/3545947.3576300)

[Slide deck for a CS 194-244 project at University of California, Berkeley around problem autogeneration](https://docs.google.com/presentation/d/1XPSyo1BaQnEEaCSphn9YJi3tg7m5fiIwGa7qGVNdAzg/edit?usp=sharing)
