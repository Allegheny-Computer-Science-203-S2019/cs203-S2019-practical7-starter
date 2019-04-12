<!---

PROFESSOR TASK LIST:

  * Use cp -r to copy all of the files and directories in this repository
    to the starter repository for this assignment
  * Change into the directory for the starter repository
  * Update the header (e.g., #) to only give the name of the assignment
  * Update the first paragraph to include the commented-out content
  * Change the link in the # Problems section to point to this lab's starter
  * Create the assignment in the GitHub Classroom, noting the URL
  * Test the assignment by accepting it with your own GitHub account
  * Check to ensure that your GitHub repository is created correctly
  * Share the assignment link with all of the students using email or Slack

PROFESSOR PROBLEMS?

  * Contact Gregory M. Kapfhammer by email or Slack
  * Raise an issue in the GitHub repository for this assignment starter

-->

# cs203-S2019-practical7-starter

Designed for use with [GitHub Classroom](https://classroom.github.com/), this
repository contains the starter for Practical 7 in Computer Science 203. Since
the Travis builds for this repository will initially fail (as evidenced by a red
&#x2717; appearing in the commit logs instead of a green &#x2714;), the
programmer is responsible for completing all of the steps needed to satisfy the
requirements for the assignment, thus causing a &#x2714; to instead appear in
the commit logs.

## Introduction

This assignment requires a programmer to refactor, document, and automatically
test a Python program called `src/termfrequency/compute_tf_aspects.py`.
In addition to the work that you did for the previous practical assignments
&mdash; exploring different command-line options for Pytest, installing the
`pytest-cov` code coverage calculation package, perform code coverage analysis,
and incrementally increasing the coverage of your test suite &mdash; you will
gain experience with refactoring Python source code so that it meets
well-established standards for source code formatting. A key task for this
practical assignment is the exploration of how the Python programming langauge
supports aspect-oriented programming.

When you use the `git commit` command to transfer your source code to your
GitHub repository, [Travis CI](https://travis-ci.com/) will initialize a build
of your assignment, checking to see if it meets all of the requirements. If both
your source code and writing meet all of the established requirements, then you
will see a green &#x2714; in the listing of commits in GitHub. If your
submission does not meet the requirements, a red &#x2717; will appear instead.
The instructor will reduce a programmer's grade for this assignment if the red
&#x2717; appears on the last commit in GitHub immediately before the
assignment's due date.

## Learning

If you have not done so already, please read all of the relevant [GitHub
Guides](https://guides.github.com/) that explain how to use many of the features
that GitHub provides. In particular, please make sure that you have read the
following GitHub guides: [Mastering
Markdown](https://guides.github.com/features/mastering-markdown/), [Hello
World](https://guides.github.com/activities/hello-world/), and [Documenting Your
Projects on GitHub](https://guides.github.com/features/wikis/). Each of these
guides will help you to understand how to use both [GitHub](http://github.com) and
[GitHub Classroom](https://classroom.github.com/).

To do well on this assignment, you should also read all relevant chapters in
"Think Python". You should also read the Preface and Chapters 1 through 20 in
the "Exercises in Programming Style" book, paying particularly close attention
to the content in Chapter 18. Finally, you should review the first five chapters
in the "Pytest" book, focusing on any relevant content that helps you to write
test cases. Please see the course instructor or one of the teaching assistants
or tutors if you have questions about any of these reading assignments. Students
who want to learn more about how to calculate code coverage for a Pytest test
suite are encouraged to read the documentation for
[Coverage.py](https://coverage.readthedocs.io/).

## Commands

To get started in using the GatorGrader tool, you can change into the directory
for this assignment and type the command `gradle grade` in your terminal.
Running this command will produce a lot of output that you should carefully
inspect. If the output indicates that GatorGrader judges that there are no
mistakes in the assignment, then this means that your source code and writing
are passing all of the automated baseline checks. However, if the output
indicates that there are mistakes, then you will need to understand what they
are and then try to fix them.

This practical assignment also requires students to use
[Pipenv](https://github.com/pypa/pipenv) to create a virtual environment,
install and manage development packages, and to run Python commands. Here is a
sample of the Pipenv commands that you will need to run during this assignment.

- If needed, install and upgrade the `pipenv` command: `pip install pipenv --user`
- Install the development dependencies `pipenv` command: `pipenv install --dev`
- Reformat the program with `black`: `pipenv run black termfrequency/compute_tf_aspects.py`
- Check the program with `pylint`: `pipenv run pylint termfrequency`
- Check the program with `flake8`: `pipenv run flake8 termfrequency`
- Run the program with `pipenv` and `python3` and a small input: `pipenv run python3 termfrequency/compute_tf_aspects.py inputs/input.txt`
- Run the program with `pipenv` and `python3` and a realistic input: `pipenv run python3 termfrequency/compute_tf_aspects.py inputs/pride-and-prejudice.txt`
- Run the test suite with `pytest`: `pipenv run pytest`
- Run the test suite with specialize coverage monitoring: `pipenv run pytest -x -s --cov-config pytest.cov --cov-report term-missing --cov`

To run one of these commands, you must be in the main directory for this
assignment where the configuration files are located. Then, you can type these
commands in the terminal and study the output.

## Output

Running the program with the small input should produce the following output:

```
extract_words(...) took 0.0002429485321044922 secs
frequencies(...) took 5.7220458984375e-06 secs
sort(...) took 1.0967254638671875e-05 secs
live  -  2
mostly  -  2
white  -  1
tigers  -  1
india  -  1
wild  -  1
lions  -  1
africa  -  1
```

Running the program with the realistic input should produce the following output:

```
extract_words(...) took 0.23739409446716309 secs
frequencies(...) took 0.010707616806030273 secs
sort(...) took 0.0026705265045166016 secs
mr  -  786
elizabeth  -  635
very  -  488
darcy  -  418
such  -  395
mrs  -  343
much  -  329
more  -  327
bennet  -  323
bingley  -  306
jane  -  295
miss  -  283
one  -  275
know  -  239
before  -  229
herself  -  227
though  -  226
well  -  224
never  -  220
sister  -  218
soon  -  216
think  -  211
now  -  209
time  -  203
good  -  201
```

Please note that, due to the use of aspect-oriented programming, this program
also outputs the execution time of the functions. Can you explain why it is the
case that the first block of program times is faster than the second?

To start working on this practical assignment, you should refactor the provided
source code so that it adheres to all of the well-established linting standards
for Python source code. Following the strategies that you developed in the
previous assignments, you should add as many test cases as you can to
iteratively increase the coverage of the entire test suite, aiming for at
least 80% code coverage and the overall goal of nearly 100% code coverage.
Make sure that you explore how to use parameterized tests in Python and
Pytest!

## Checks

- termfrequency/compute_tf_aspects.py:
  - Contains the import fragment `if __name__ ==` for the main function
    designation
  - Runs correctly through `pipenv` without crashing or producing an error
  - Runs correctly through `pipenv` and outputs exactly three function timings
  - Produces exactly eleven lines of output in the terminal when run with `inputs/input.txt`
  - Does not contain any markers to indicate work that was not completed

- tests/test_compute_tf_aspects.py:
  - Features the import statement `from termfrequency import compute_tf_aspects`
  - Features at least five test cases that start with `test_`
  - Runs correctly through `pipenv` without crashing or failing a test
  - Does not contain any markers to indicate work that was not completed

- writing/reflection.md:
  - Passes the checks performed by the Markdown linting tool
  - Passes the checks performed by the proselint linting tool
  - Contains exactly five contiguous paragraphs of formatted text
  - Each contiguous paragraphs of formatted text should include at least 100 words

- GitHub repository:
  - Contains five commits beyond the repository's starting number of commits

## Updates

If the course instructor updates the provided material for this assignment and
you would like to receive these updates, then you can type this command in the
main directory for this assignment:

```
git remote add download git@github.com:Allegheny-Computer-Science-203-S2019/cs203-S2019-practical7-starter.git
```

You should only need to type this command once; typing the command additional
times may yield an error message but will not negatively influence the state of
your repository. Now, you are ready to download the updates provided by the
course instructor by typing:

```
git pull download master
```

This second command can be run whenever the course instructor needs to provide
you with new source code for this assignment. However, please note that, if you
have edited the files that the course instructor updated, running the previous
command may lead to Git merge conflicts. If this happens, you may need to
manually resolve them with the help of the instructor or a teaching assistant.

## Travis

This assignment uses [Travis CI](https://travis-ci.com/) to automatically run
the checking programs every time you commit to your GitHub repository. The
checking will start as soon as you have accepted the assignment, thus creating
your own private repository, and the course instructor enables Travis for it. If
you are using Travis for the first time, you will need to authorize Travis CI to
access the private repositories that you created on GitHub.

## Requirements

The GatorGrader software that supports the checking of this assignment was
developed for the following software and versions:

- Gradle 4.6
- Java 1.8.0
- MDL 0.4.0
- Proselint 0.8.0
- Python 3.6

## Problems

If you have found a problem with this assignment's provided source code, then
you can go to the [Computer Science 203 Practical 6
Starter](https://github.com/Allegheny-Computer-Science-203-S2019/cs203-S2019-practical7-starter)
repository and create an issue by clicking the "Issues" tab and then clicking
the green "New Issue" button. If you have found a problem with the [GatorGrader
tool](https://github.com/GatorEducator/gatorgrader) and the way that it checks
you assignment, then you can follow the aforementioned steps to create an issue
in its repository. To ensure that your issue is properly resolved, please
provide as many details as is possible about the problem that you experienced.
If you discover a problem with the laboratory assignment sheet, then please
raise an issue in the
[cs203-S2019-sheets](https://github.com/Allegheny-Computer-Science-203-S2019/cs203-S2019-sheets)
repository and mention this assignment.

Students who find &mdash; and use the appropriate GitHub issue tracker to
correctly document &mdash; a mistake in any aspect of this laboratory assignment
will receive free GitHub stickers and extra credit towards their grade for it.

## Assistance

If you are having trouble completing any part of this project, then please talk
with either the course instructor or a teaching assistant during the laboratory
session. Alternatively, you may ask questions in the Slack workspace for this
course. Finally, you can schedule a meeting during the course instructor's
office hours.
