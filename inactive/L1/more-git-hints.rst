---
title: Tracking Changes
teaching: 20
exercises: 0
questions:
- "How do I record changes in Git?"
- "How do I check the status of my version control repository?"
- "How do I record notes about what changes I made and why?"
objectives:
- "Go through the modify-add-commit cycle for one or more files."
- "Explain where information is stored at each stage of that cycle."
- "Distinguish between descriptive and non-descriptive commit messages."
keypoints:
- "`git status` shows the status of a repository."
- "Files can be stored in a project's working directory (which users see), the staging area (where the next commit is being built up) and the local repository (where commits are permanently recorded)."
- "`git add` puts files in the staging area."
- "`git commit` saves the staged content as a new commit in the local repository."
- "Write a commit message that accurately describes your changes."
---

First let's make sure we're still in the right directory.
You should be in the `planets` directory.

~~~
$ pwd
~~~
{: .language-bash}
~~~
/home/vlad/Desktop/planets
~~~
{: .output}

If you are still in `moons`, navigate back up to `planets`

~~~
$ pwd
~~~
{: .language-bash}
~~~
/home/vlad/Desktop/planets/moons
~~~
{: .output}
~~~
$ cd ..
~~~
{: .language-bash}

Let's create a file called `mars.txt` that contains some notes
about the Red Planet's suitability as a base.
We'll use `nano` to edit the file;
you can use whatever editor you like.
In particular, this does not have to be the `core.editor` you set globally earlier. But remember, the bash command to create or edit a new file will depend on the editor you choose (it might not be `nano`). For a refresher on text editors, check out ["Which Editor?"](https://swcarpentry.github.io/shell-novice/03-create/) in [The Unix Shell](https://swcarpentry.github.io/shell-novice/) lesson.

~~~
$ nano mars.txt
~~~
{: .language-bash}

Type the text below into the `mars.txt` file:

~~~
Cold and dry, but everything is my favorite color
~~~

`mars.txt` now contains a single line, which we can see by running:

~~~
$ ls
~~~
{: .language-bash}

~~~
mars.txt
~~~
{: .output}

~~~
$ cat mars.txt
~~~
{: .language-bash}

~~~
Cold and dry, but everything is my favorite color
~~~
{: .output}

If we check the status of our project again,
Git tells us that it's noticed the new file:

~~~
$ git status
~~~
{: .language-bash}

~~~
On branch master

Initial commit

Untracked files:
   (use "git add <file>..." to include in what will be committed)

	mars.txt
nothing added to commit but untracked files present (use "git add" to track)
~~~
{: .output}

The "untracked files" message means that there's a file in the directory
that Git isn't keeping track of.
We can tell Git to track a file using `git add`:

~~~
$ git add mars.txt
~~~
{: .language-bash}

and then check that the right thing happened:

~~~
$ git status
~~~
{: .language-bash}

~~~
On branch master

Initial commit

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   mars.txt

~~~
{: .output}

Git now knows that it's supposed to keep track of `mars.txt`,
but it hasn't recorded these changes as a commit yet.
To get it to do that,
we need to run one more command:

~~~
$ git commit -m "Start notes on Mars as a base"
~~~
{: .language-bash}

~~~
[master (root-commit) f22b25e] Start notes on Mars as a base
 1 file changed, 1 insertion(+)
 create mode 100644 mars.txt
~~~
{: .output}

When we run `git commit`,
Git takes everything we have told it to save by using `git add`
and stores a copy permanently inside the special `.git` directory.
This permanent copy is called a [commit]({{ page.root }}/reference#commit)
(or [revision]({{ page.root }}/reference#revision)) and its short identifier is `f22b25e`.
Your commit may have another identifier.

We use the `-m` flag (for "message")
to record a short, descriptive, and specific comment that will help us remember later on what we did and why.
If we just run `git commit` without the `-m` option,
Git will launch `nano` (or whatever other editor we configured as `core.editor`)
so that we can write a longer message.

[Good commit messages][commit-messages] start with a brief (<50 characters) statement about the
changes made in the commit. Generally, the message should complete the sentence "If applied, this commit will" <commit message here>.
If you want to go into more detail, add a blank line between the summary line and your additional notes. Use this additional space to explain why you made changes and/or what their impact will be.

If we run `git status` now:

~~~
$ git status
~~~
{: .language-bash}

~~~
On branch master
nothing to commit, working directory clean
~~~
{: .output}

it tells us everything is up to date.
If we want to know what we've done recently,
we can ask Git to show us the project's history using `git log`:

~~~
$ git log
~~~
{: .language-bash}

~~~
commit f22b25e3233b4645dabd0d81e651fe074bd8e73b
Author: Vlad Dracula <vlad@tran.sylvan.ia>
Date:   Thu Aug 22 09:51:46 2013 -0400

    Start notes on Mars as a base
~~~
{: .output}

`git log` lists all commits  made to a repository in reverse chronological order.
The listing for each commit includes
the commit's full identifier
(which starts with the same characters as
the short identifier printed by the `git commit` command earlier),
the commit's author,
when it was created,
and the log message Git was given when the commit was created.

> ## Where Are My Changes?
>
> If we run `ls` at this point, we will still see just one file called `mars.txt`.
> That's because Git saves information about files' history
> in the special `.git` directory mentioned earlier
> so that our filesystem doesn't become cluttered
> (and so that we can't accidentally edit or delete an old version).
{: .callout}

Now suppose Dracula adds more information to the file.
(Again, we'll edit with `nano` and then `cat` the file to show its contents;
you may use a different editor, and don't need to `cat`.)

~~~
$ nano mars.txt
$ cat mars.txt
~~~
{: .language-bash}

~~~
Cold and dry, but everything is my favorite color
The two moons may be a problem for Wolfman
~~~
{: .output}

When we run `git status` now,
it tells us that a file it already knows about has been modified:

~~~
$ git status
~~~
{: .language-bash}

~~~
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   mars.txt

no changes added to commit (use "git add" and/or "git commit -a")
~~~
{: .output}

The last line is the key phrase:
"no changes added to commit".
We have changed this file,
but we haven't told Git we will want to save those changes
(which we do with `git add`)
nor have we saved them (which we do with `git commit`).
So let's do that now. It is good practice to always review
our changes before saving them. We do this using `git diff`.
This shows us the differences between the current state
of the file and the most recently saved version:

~~~
$ git diff
~~~
{: .language-bash}

~~~
diff --git a/mars.txt b/mars.txt
index df0654a..315bf3a 100644
--- a/mars.txt
+++ b/mars.txt
@@ -1 +1,2 @@
 Cold and dry, but everything is my favorite color
+The two moons may be a problem for Wolfman
~~~
{: .output}

The output is cryptic because
it is actually a series of commands for tools like editors and `patch`
telling them how to reconstruct one file given the other.
If we break it down into pieces:

1.  The first line tells us that Git is producing output similar to the Unix `diff` command
    comparing the old and new versions of the file.
2.  The second line tells exactly which versions of the file
    Git is comparing;
    `df0654a` and `315bf3a` are unique computer-generated labels for those versions.
3.  The third and fourth lines once again show the name of the file being changed.
4.  The remaining lines are the most interesting, they show us the actual differences
    and the lines on which they occur.
    In particular,
    the `+` marker in the first column shows where we added a line.

After reviewing our change, it's time to commit it:

~~~
$ git commit -m "Add concerns about effects of Mars' moons on Wolfman"
$ git status
~~~
{: .language-bash}

~~~
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   mars.txt

no changes added to commit (use "git add" and/or "git commit -a")
~~~
{: .output}

Whoops:
Git won't commit because we didn't use `git add` first.
Let's fix that:

~~~
$ git add mars.txt
$ git commit -m "Add concerns about effects of Mars' moons on Wolfman"
~~~
{: .language-bash}

~~~
[master 34961b1] Add concerns about effects of Mars' moons on Wolfman
 1 file changed, 1 insertion(+)
~~~
{: .output}

Git insists that we add files to the set we want to commit
before actually committing anything. This allows us to commit our
changes in stages and capture changes in logical portions rather than
only large batches.
For example,
suppose we're adding a few citations to relevant research to our thesis.
We might want to commit those additions,
and the corresponding bibliography entries,
but *not* commit some of our work drafting the conclusion
(which we haven't finished yet).

To allow for this,
Git has a special *staging area*
where it keeps track of things that have been added to
the current [changeset]({{ page.root }}/reference#changeset)
but not yet committed.

> ## Staging Area
>
> If you think of Git as taking snapshots of changes over the life of a project,
> `git add` specifies *what* will go in a snapshot
> (putting things in the staging area),
> and `git commit` then *actually takes* the snapshot, and
> makes a permanent record of it (as a commit).
> If you don't have anything staged when you type `git commit`,
> Git will prompt you to use `git commit -a` or `git commit --all`,
> which is kind of like gathering *everyone* for the picture!
> However, it's almost always better to
> explicitly add things to the staging area, because you might
> commit changes you forgot you made. (Going back to snapshots,
> you might get the extra with incomplete makeup walking on
> the stage for the snapshot because you used `-a`!)
> Try to stage things manually,
> or you might find yourself searching for "git undo commit" more
> than you would like!
{: .callout}

![The Git Staging Area](../fig/git-staging-area.svg)

Let's watch as our changes to a file move from our editor
to the staging area
and into long-term storage.
First,
we'll add another line to the file:

~~~
$ nano mars.txt
$ cat mars.txt
~~~
{: .language-bash}

~~~
Cold and dry, but everything is my favorite color
The two moons may be a problem for Wolfman
But the Mummy will appreciate the lack of humidity
~~~
{: .output}

~~~
$ git diff
~~~
{: .language-bash}

~~~
diff --git a/mars.txt b/mars.txt
index 315bf3a..b36abfd 100644
--- a/mars.txt
+++ b/mars.txt
@@ -1,2 +1,3 @@
 Cold and dry, but everything is my favorite color
 The two moons may be a problem for Wolfman
+But the Mummy will appreciate the lack of humidity
~~~
{: .output}

So far, so good:
we've added one line to the end of the file
(shown with a `+` in the first column).
Now let's put that change in the staging area
and see what `git diff` reports:

~~~
$ git add mars.txt
$ git diff
~~~
{: .language-bash}

There is no output:
as far as Git can tell,
there's no difference between what it's been asked to save permanently
and what's currently in the directory.
However,
if we do this:

~~~
$ git diff --staged
~~~
{: .language-bash}

~~~
diff --git a/mars.txt b/mars.txt
index 315bf3a..b36abfd 100644
--- a/mars.txt
+++ b/mars.txt
@@ -1,2 +1,3 @@
 Cold and dry, but everything is my favorite color
 The two moons may be a problem for Wolfman
+But the Mummy will appreciate the lack of humidity
~~~
{: .output}

it shows us the difference between
the last committed change
and what's in the staging area.
Let's save our changes:

~~~
$ git commit -m "Discuss concerns about Mars' climate for Mummy"
~~~
{: .language-bash}

~~~
[master 005937f] Discuss concerns about Mars' climate for Mummy
 1 file changed, 1 insertion(+)
~~~
{: .output}

check our status:

~~~
$ git status
~~~
{: .language-bash}

~~~
On branch master
nothing to commit, working directory clean
~~~
{: .output}

and look at the history of what we've done so far:

~~~
$ git log
~~~
{: .language-bash}

~~~
commit 005937fbe2a98fb83f0ade869025dc2636b4dad5
Author: Vlad Dracula <vlad@tran.sylvan.ia>
Date:   Thu Aug 22 10:14:07 2013 -0400

    Discuss concerns about Mars' climate for Mummy

commit 34961b159c27df3b475cfe4415d94a6d1fcd064d
Author: Vlad Dracula <vlad@tran.sylvan.ia>
Date:   Thu Aug 22 10:07:21 2013 -0400

    Add concerns about effects of Mars' moons on Wolfman

commit f22b25e3233b4645dabd0d81e651fe074bd8e73b
Author: Vlad Dracula <vlad@tran.sylvan.ia>
Date:   Thu Aug 22 09:51:46 2013 -0400

    Start notes on Mars as a base
~~~
{: .output}

> ## Word-based diffing
>
> Sometimes, e.g. in the case of the text documents a line-wise
> diff is too coarse. That is where the `--color-words` option of
> `git diff` comes in very useful as it highlights the changed
> words using colors.
{: .callout}

> ## Paging the Log
>
> When the output of `git log` is too long to fit in your screen,
> `git` uses a program to split it into pages of the size of your screen.
> When this "pager" is called, you will notice that the last line in your
> screen is a `:`, instead of your usual prompt.
>
> *   To get out of the pager, press <kbd>Q</kbd>.
> *   To move to the next page, press <kbd>Spacebar</kbd>.
> *   To search for `some_word` in all pages,
>     press <kbd>/</kbd>
>     and type `some_word`.
>     Navigate through matches pressing <kbd>N</kbd>.
{: .callout}

> ## Limit Log Size
>
> To avoid having `git log` cover your entire terminal screen, you can limit the
> number of commits that Git lists by using `-N`, where `N` is the number of
> commits that you want to view. For example, if you only want information from
> the last commit you can use:
>
> ~~~
> $ git log -1
> ~~~
> {: .language-bash}
>
> ~~~
> commit 005937fbe2a98fb83f0ade869025dc2636b4dad5
> Author: Vlad Dracula <vlad@tran.sylvan.ia>
> Date:   Thu Aug 22 10:14:07 2013 -0400
>
>    Discuss concerns about Mars' climate for Mummy
> ~~~
> {: .output}
>
> You can also reduce the quantity of information using the
> `--oneline` option:
>
> ~~~
> $ git log --oneline
> ~~~
> {: .language-bash}
> ~~~
> * 005937f Discuss concerns about Mars' climate for Mummy
> * 34961b1 Add concerns about effects of Mars' moons on Wolfman
> * f22b25e Start notes on Mars as a base
> ~~~
> {: .output}
>
> You can also combine the `--oneline` options with others. One useful
> combination is:
>
> ~~~
> $ git log --oneline --graph --all --decorate
> ~~~
> {: .language-bash}
> ~~~
> * 005937f Discuss concerns about Mars' climate for Mummy (HEAD, master)
> * 34961b1 Add concerns about effects of Mars' moons on Wolfman
> * f22b25e Start notes on Mars as a base
> ~~~
> {: .output}
{: .callout}

> ## Directories
>
> Two important facts you should know about directories in Git.
>
> 1. Git does not track directories on their own, only files within them.
>    Try it for yourself:
>
>    ~~~
>    $ mkdir directory
>    $ git status
>    $ git add directory
>    $ git status
>    ~~~
>    {: .language-bash}
>
>    Note, our newly created empty directory `directory` does not appear in
>    the list of untracked files even if we explicitly add it (_via_ `git add`) to our
>    repository. This is the reason why you will sometimes see `.gitkeep` files
>    in otherwise empty directories. Unlike `.gitignore`, these files are not special
>    and their sole purpose is to populate a directory so that Git adds it to
>    the repository. In fact, you can name such files anything you like.
>
> 2. If you create a directory in your Git repository and populate it with files,
>    you can add all files in the directory at once by:
>
>    ~~~
>    git add <directory-with-files>
>    ~~~
>    {: .language-bash}
>
{: .callout}

To recap, when we want to add changes to our repository,
we first need to add the changed files to the staging area
(`git add`) and then commit the staged changes to the
repository (`git commit`):

![The Git Commit Workflow](../fig/git-committing.svg)

> ## Choosing a Commit Message
>
> Which of the following commit messages would be most appropriate for the
> last commit made to `mars.txt`?
>
> 1. "Changes"
> 2. "Added line 'But the Mummy will appreciate the lack of humidity' to mars.txt"
> 3. "Discuss effects of Mars' climate on the Mummy"
>
> > ## Solution
> > Answer 1 is not descriptive enough, and the purpose of the commit is unclear;
> > and answer 2 is redundant to using "git diff" to see what changed in this commit;
> > but answer 3 is good: short, descriptive, and imperative.
> {: .solution}
{: .challenge}

> ## Committing Changes to Git
>
> Which command(s) below would save the changes of `myfile.txt`
> to my local Git repository?
>
> 1. ~~~
>    $ git commit -m "my recent changes"
>    ~~~
>    {: .language-bash}
> 2. ~~~
>    $ git init myfile.txt
>    $ git commit -m "my recent changes"
>    ~~~
>    {: .language-bash}
> 3. ~~~
>    $ git add myfile.txt
>    $ git commit -m "my recent changes"
>    ~~~
>    {: .language-bash}
> 4. ~~~
>    $ git commit -m myfile.txt "my recent changes"
>    ~~~
>    {: .language-bash}
>
> > ## Solution
> >
> > 1. Would only create a commit if files have already been staged.
> > 2. Would try to create a new repository.
> > 3. Is correct: first add the file to the staging area, then commit.
> > 4. Would try to commit a file "my recent changes" with the message myfile.txt.
> {: .solution}
{: .challenge}

> ## Committing Multiple Files
>
> The staging area can hold changes from any number of files
> that you want to commit as a single snapshot.
>
> 1. Add some text to `mars.txt` noting your decision
> to consider Venus as a base
> 2. Create a new file `venus.txt` with your initial thoughts
> about Venus as a base for you and your friends
> 3. Add changes from both files to the staging area,
> and commit those changes.
>
> > ## Solution
> >
> > First we make our changes to the `mars.txt` and `venus.txt` files:
> > ~~~
> > $ nano mars.txt
> > $ cat mars.txt
> > ~~~
> > {: .language-bash}
> > ~~~
> > Maybe I should start with a base on Venus.
> > ~~~
> > {: .output}
> > ~~~
> > $ nano venus.txt
> > $ cat venus.txt
> > ~~~
> > {: .language-bash}
> > ~~~
> > Venus is a nice planet and I definitely should consider it as a base.
> > ~~~
> > {: .output}
> > Now you can add both files to the staging area. We can do that in one line:
> >
> > ~~~
> > $ git add mars.txt venus.txt
> > ~~~
> > {: .language-bash}
> > Or with multiple commands:
> > ~~~
> > $ git add mars.txt
> > $ git add venus.txt
> > ~~~
> > {: .language-bash}
> > Now the files are ready to commit. You can check that using `git status`. If you are ready to commit use:
> > ~~~
> > $ git commit -m "Write plans to start a base on Venus"
> > ~~~
> > {: .language-bash}
> > ~~~
> > [master cc127c2]
> >  Write plans to start a base on Venus
> >  2 files changed, 2 insertions(+)
> >  create mode 100644 venus.txt
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

> ## `bio` Repository
>
> * Create a new Git repository on your computer called `bio`.
> * Write a three-line biography for yourself in a file called `me.txt`,
> commit your changes
> * Modify one line, add a fourth line
> * Display the differences
> between its updated state and its original state.
>
> > ## Solution
> >
> > If needed, move out of the `planets` folder:
> >
> > ~~~
> > $ cd ..
> > ~~~
> > {: .language-bash}
> >
> > Create a new folder called `bio` and 'move' into it:
> >
> > ~~~
> > $ mkdir bio
> > $ cd bio
> > ~~~
> > {: .language-bash}
> >
> > Initialise git:
> >
> > ~~~
> > $ git init
> > ~~~
> > {: .language-bash}
> >
> > Create your biography file `me.txt` using `nano` or another text editor.
> > Once in place, add and commit it to the repository:
> >
> > ~~~
> > $ git add me.txt
> > $ git commit -m'Adding biography file'
> > ~~~
> > {: .language-bash}
> >
> > Modify the file as described (modify one line, add a fourth line).
> > To display the differences
> > between its updated state and its original state, use `git diff`:
> >
> > ~~~
> > $ git diff me.txt
> > ~~~
> > {: .language-bash}
> >
> {: .solution}
{: .challenge}

> ## Author and Committer
>
> For each of the commits you have done, Git stored your name twice.
> You are named as the author and as the committer. You can observe
> that by telling Git to show you more information about your last
> commits:
>
> ~~~
> $ git log --format=full
> ~~~
> {: .language-bash}
>
> When committing you can name someone else as the author:
>
> ~~~
> $ git commit --author="Vlad Dracula <vlad@tran.sylvan.ia>"
> ~~~
> {: .language-bash}
>
> Create a new repository and create two commits: one without the
> `--author` option and one by naming a colleague of yours as the
> author. Run `git log` and `git log --format=full`. Think about ways
> how that can allow you to collaborate with your colleagues.
>
> > ## Solution
> >
> > ~~~
> > $ git add me.txt
> > $ git commit -m "Update Vlad's bio." --author="Frank N. Stein <franky@monster.com>"
> > ~~~
> > {: .language-bash}
> > ~~~
> > [master 4162a51] Update Vlad's bio.
> > Author: Frank N. Stein <franky@monster.com>
> > 1 file changed, 2 insertions(+), 2 deletions(-)
> >
> > $ git log --format=full
> > commit 4162a51b273ba799a9d395dd70c45d96dba4e2ff
> > Author: Frank N. Stein <franky@monster.com>
> > Commit: Vlad Dracula <vlad@tran.sylvan.ia>
> >
> > Update Vlad's bio.
> >
> > commit aaa3271e5e26f75f11892718e83a3e2743fab8ea
> > Author: Vlad Dracula <vlad@tran.sylvan.ia>
> > Commit: Vlad Dracula <vlad@tran.sylvan.ia>
> >
> > Vlad's initial bio.
> > ~~~
> > {: .output}
> {: .solution}
{: .challenge}

[commit-messages]: https://chris.beams.io/posts/git-commit/


---
title: Exploring History
teaching: 25
exercises: 0
questions:
- "How can I identify old versions of files?"
- "How do I review my changes?"
- "How can I recover old versions of files?"
objectives:
- "Explain what the HEAD of a repository is and how to use it."
- "Identify and use Git commit numbers."
- "Compare various versions of tracked files."
- "Restore old versions of files."
keypoints:
- "`git diff` displays differences between commits."
- "`git checkout` recovers old versions of files."
---

As we saw in the previous lesson, we can refer to commits by their
identifiers.  You can refer to the _most recent commit_ of the working
directory by using the identifier `HEAD`.

We've been adding one line at a time to `mars.txt`, so it's easy to track our
progress by looking, so let's do that using our `HEAD`s.  Before we start,
let's make a change to `mars.txt`.

~~~
$ nano mars.txt
$ cat mars.txt
~~~
{: .language-bash}

~~~
Cold and dry, but everything is my favorite color
The two moons may be a problem for Wolfman
But the Mummy will appreciate the lack of humidity
An ill-considered change
~~~
{: .output}

Now, let's see what we get.

~~~
$ git diff HEAD mars.txt
~~~
{: .language-bash}

~~~
diff --git a/mars.txt b/mars.txt
index b36abfd..0848c8d 100644
--- a/mars.txt
+++ b/mars.txt
@@ -1,3 +1,4 @@
 Cold and dry, but everything is my favorite color
 The two moons may be a problem for Wolfman
 But the Mummy will appreciate the lack of humidity
+An ill-considered change.
~~~
{: .output}

which is the same as what you would get if you leave out `HEAD` (try it).  The
real goodness in all this is when you can refer to previous commits.  We do
that by adding `~1`
(where "~" is "tilde", pronounced [**til**-d*uh*])
to refer to the commit one before `HEAD`.

~~~
$ git diff HEAD~1 mars.txt
~~~
{: .language-bash}

If we want to see the differences between older commits we can use `git diff`
again, but with the notation `HEAD~1`, `HEAD~2`, and so on, to refer to them:


~~~
$ git diff HEAD~2 mars.txt
~~~
{: .language-bash}

~~~
diff --git a/mars.txt b/mars.txt
index df0654a..b36abfd 100644
--- a/mars.txt
+++ b/mars.txt
@@ -1 +1,4 @@
 Cold and dry, but everything is my favorite color
+The two moons may be a problem for Wolfman
+But the Mummy will appreciate the lack of humidity
+An ill-considered change
~~~
{: .output}

We could also use `git show` which shows us what changes we made at an older commit as well as the commit message, rather than the _differences_ between a commit and our working directory that we see by using `git diff`.

~~~
$ git show HEAD~2 mars.txt
~~~
{: .language-bash}

~~~
commit 34961b159c27df3b475cfe4415d94a6d1fcd064d
Author: Vlad Dracula <vlad@tran.sylvan.ia>
Date:   Thu Aug 22 10:07:21 2013 -0400

    Start notes on Mars as a base

diff --git a/mars.txt b/mars.txt
new file mode 100644
index 0000000..df0654a
--- /dev/null
+++ b/mars.txt
@@ -0,0 +1 @@
+Cold and dry, but everything is my favorite color
~~~
{: .output}

In this way,
we can build up a chain of commits.
The most recent end of the chain is referred to as `HEAD`;
we can refer to previous commits using the `~` notation,
so `HEAD~1`
means "the previous commit",
while `HEAD~123` goes back 123 commits from where we are now.

We can also refer to commits using
those long strings of digits and letters
that `git log` displays.
These are unique IDs for the changes,
and "unique" really does mean unique:
every change to any set of files on any computer
has a unique 40-character identifier.
Our first commit was given the ID
`f22b25e3233b4645dabd0d81e651fe074bd8e73b`,
so let's try this:

~~~
$ git diff f22b25e3233b4645dabd0d81e651fe074bd8e73b mars.txt
~~~
{: .language-bash}

~~~
diff --git a/mars.txt b/mars.txt
index df0654a..93a3e13 100644
--- a/mars.txt
+++ b/mars.txt
@@ -1 +1,4 @@
 Cold and dry, but everything is my favorite color
+The two moons may be a problem for Wolfman
+But the Mummy will appreciate the lack of humidity
+An ill-considered change
~~~
{: .output}

That's the right answer,
but typing out random 40-character strings is annoying,
so Git lets us use just the first few characters:

~~~
$ git diff f22b25e mars.txt
~~~
{: .language-bash}

~~~
diff --git a/mars.txt b/mars.txt
index df0654a..93a3e13 100644
--- a/mars.txt
+++ b/mars.txt
@@ -1 +1,4 @@
 Cold and dry, but everything is my favorite color
+The two moons may be a problem for Wolfman
+But the Mummy will appreciate the lack of humidity
+An ill-considered change
~~~
{: .output}

All right! So
we can save changes to files and see what we've changed—now how
can we restore older versions of things?
Let's suppose we accidentally overwrite our file:

~~~
$ nano mars.txt
$ cat mars.txt
~~~
{: .language-bash}

~~~
We will need to manufacture our own oxygen
~~~
{: .output}

`git status` now tells us that the file has been changed,
but those changes haven't been staged:

~~~
$ git status
~~~
{: .language-bash}

~~~
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   mars.txt

no changes added to commit (use "git add" and/or "git commit -a")
~~~
{: .output}

We can put things back the way they were
by using `git checkout`:

~~~
$ git checkout HEAD mars.txt
$ cat mars.txt
~~~
{: .language-bash}

~~~
Cold and dry, but everything is my favorite color
The two moons may be a problem for Wolfman
But the Mummy will appreciate the lack of humidity
~~~
{: .output}

As you might guess from its name,
`git checkout` checks out (i.e., restores) an old version of a file.
In this case,
we're telling Git that we want to recover the version of the file recorded in `HEAD`,
which is the last saved commit.
If we want to go back even further,
we can use a commit identifier instead:

~~~
$ git checkout f22b25e mars.txt
~~~
{: .language-bash}

~~~
$ cat mars.txt
~~~
{: .language-bash}

~~~
Cold and dry, but everything is my favorite color
~~~
{: .output}

~~~
$ git status
~~~
{: .language-bash}

~~~
# On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#	modified:   mars.txt
#
no changes added to commit (use "git add" and/or "git commit -a")
~~~
{: .output}

Notice that the changes are on the staged area.
Again, we can put things back the way they were
by using `git checkout`:

~~~
$ git checkout HEAD mars.txt
~~~
{: .language-bash}

> ## Don't Lose Your HEAD
>
> Above we used
>
> ~~~
> $ git checkout f22b25e mars.txt
> ~~~
> {: .language-bash}
>
> to revert `mars.txt` to its state after the commit `f22b25e`. But be careful!
> The command `checkout` has other important functionalities and Git will misunderstand
> your intentions if you are not accurate with the typing. For example,
> if you forget `mars.txt` in the previous command.
>
> ~~~
> $ git checkout f22b25e
> ~~~
> {: .language-bash}
> ~~~
> Note: checking out 'f22b25e'.
>
> You are in 'detached HEAD' state. You can look around, make experimental
> changes and commit them, and you can discard any commits you make in this
> state without impacting any branches by performing another checkout.
>
> If you want to create a new branch to retain commits you create, you may
> do so (now or later) by using -b with the checkout command again. Example:
>
>  git checkout -b <new-branch-name>
>
> HEAD is now at f22b25e Start notes on Mars as a base
> ~~~
> {: .error}
>
> The "detached HEAD" is like "look, but don't touch" here,
> so you shouldn't make any changes in this state.
> After investigating your repo's past state, reattach your `HEAD` with `git checkout master`.
{: .callout}

It's important to remember that
we must use the commit number that identifies the state of the repository
*before* the change we're trying to undo.
A common mistake is to use the number of
the commit in which we made the change we're trying to get rid of.
In the example below, we want to retrieve the state from before the most
recent commit (`HEAD~1`), which is commit `f22b25e`:

![Git Checkout](../fig/git-checkout.svg)

So, to put it all together,
here's how Git works in cartoon form:

![https://figshare.com/articles/How_Git_works_a_cartoon/1328266](../fig/git_staging.svg)

> ## Simplifying the Common Case
>
> If you read the output of `git status` carefully,
> you'll see that it includes this hint:
>
> ~~~
> (use "git checkout -- <file>..." to discard changes in working directory)
> ~~~
> {: .language-bash}
>
> As it says,
> `git checkout` without a version identifier restores files to the state saved in `HEAD`.
> The double dash `--` is needed to separate the names of the files being recovered
> from the command itself:
> without it,
> Git would try to use the name of the file as the commit identifier.
{: .callout}

The fact that files can be reverted one by one
tends to change the way people organize their work.
If everything is in one large document,
it's hard (but not impossible) to undo changes to the introduction
without also undoing changes made later to the conclusion.
If the introduction and conclusion are stored in separate files,
on the other hand,
moving backward and forward in time becomes much easier.

> ## Recovering Older Versions of a File
>
> Jennifer has made changes to the Python script that she has been working on for weeks, and the
> modifications she made this morning "broke" the script and it no longer runs. She has spent
> ~ 1hr trying to fix it, with no luck...
>
> Luckily, she has been keeping track of her project's versions using Git! Which commands below will
> let her recover the last committed version of her Python script called
> `data_cruncher.py`?
>
> 1. `$ git checkout HEAD`
>
> 2. `$ git checkout HEAD data_cruncher.py`
>
> 3. `$ git checkout HEAD~1 data_cruncher.py`
>
> 4. `$ git checkout <unique ID of last commit> data_cruncher.py`
>
> 5. Both 2 and 4
{: .challenge}

> ## Reverting a Commit
>
> Jennifer is collaborating on her Python script with her colleagues and
> realizes her last commit to the group repository is wrong and wants to
> undo it.  Jennifer needs to undo correctly so everyone in the group
> repository gets the correct change.  `git revert [wrong commit ID]`
> will make a new commit that undoes Jennifer's previous wrong
> commit. Therefore `git revert` is different than `git checkout [commit
> ID]` because `checkout` is for local changes not committed to the
> group repository.  Below are the right steps and explanations for
> Jennifer to use `git revert`, what is the missing command?
>
> 1. `________ # Look at the git history of the project to find the commit ID`
>
> 2. Copy the ID (the first few characters of the ID, e.g. 0b1d055).
>
> 3. `git revert [commit ID]`
>
> 4. Type in the new commit message.
>
> 5. Save and close
{: .challenge}

> ## Understanding Workflow and History
>
> What is the output of the last command in
>
> ~~~
> $ cd planets
> $ echo "Venus is beautiful and full of love" > venus.txt
> $ git add venus.txt
> $ echo "Venus is too hot to be suitable as a base" >> venus.txt
> $ git commit -m "Comment on Venus as an unsuitable base"
> $ git checkout HEAD venus.txt
> $ cat venus.txt #this will print the contents of venus.txt to the screen
> ~~~
> {: .language-bash}
>
> 1. ~~~
>    Venus is too hot to be suitable as a base
>    ~~~
>    {: .output}
> 2. ~~~
>    Venus is beautiful and full of love
>    ~~~
>    {: .output}
> 3. ~~~
>    Venus is beautiful and full of love
>    Venus is too hot to be suitable as a base
>    ~~~
>    {: .output}
> 4. ~~~
>    Error because you have changed venus.txt without committing the changes
>    ~~~
>    {: .output}
>
> > ## Solution
> >
> > The answer is 2 because `git add venus.txt` was used only before add the line
> > `Venus is too hot to be suitable as a base`
> > which was lost when `git checkout` was executed.
> > Using the flag `-a` with `git commit` would have prevented the lost.
> {: .solution}
{: .challenge}

> ## Checking Understanding of `git diff`
>
> Consider this command: `git diff HEAD~3 mars.txt`. What do you predict this command
> will do if you execute it? What happens when you do execute it? Why?
>
> Try another command, `git diff [ID] mars.txt`, where [ID] is replaced with
> the unique identifier for your most recent commit. What do you think will happen,
> and what does happen?
{: .challenge}

> ## Getting Rid of Staged Changes
>
> `git checkout` can be used to restore a previous commit when unstaged changes have
> been made, but will it also work for changes that have been staged but not committed?
> Make a change to `mars.txt`, add that change, and use `git checkout` to see if
> you can remove your change.
{: .challenge}

> ## Explore and Summarize Histories
>
> Exploring history is an important part of Git, often it is a challenge to find
> the right commit ID, especially if the commit is from several months ago.
>
> Imagine the `planets` project has more than 50 files.
> You would like to find a commit with specific text in `mars.txt` is modified.
> When you type `git log`, a very long list appeared,
> How can you narrow down the search?
>
> Recall that the `git diff` command allow us to explore one specific file,
> e.g. `git diff mars.txt`. We can apply a similar idea here.
>
> ~~~
> $ git log mars.txt
> ~~~
> {: .language-bash}
>
> Unfortunately some of these commit messages are very ambiguous e.g. `update files`.
> How can you search through these files?
>
> Both `git diff` and `git log` are very useful and they summarize a different part of the history for you.
> Is it possible to combine both? Let's try the following:
>
> ~~~
> $ git log --patch mars.txt
> ~~~
> {: .language-bash}
>
> You should get a long list of output, and you should be able to see both commit messages and the difference between each commit.
>
> Question: What does the following command do?
>
> ~~~
> $ git log --patch HEAD~3 *.txt
> ~~~
> {: .language-bash}
{: .challenge}


---
title: Open Science
teaching: 5
exercises: 5
questions:
- "How can version control help me make my work more open?"
objectives:
- "Explain how a version control system can be leveraged as an electronic lab notebook for computational work."
keypoints:
- "Open scientific work is more useful and more highly cited than closed."
---

> The opposite of "open" isn't "closed".
> The opposite of "open" is "broken".
>
> --- John Wilbanks
{: .quotation}

Free sharing of information might be the ideal in science,
but the reality is often more complicated.
Normal practice today looks something like this:

*   A scientist collects some data and stores it on a machine
    that is occasionally backed up by her department.
*   She then writes or modifies a few small programs
    (which also reside on her machine)
    to analyze that data.
*   Once she has some results,
    she writes them up and submits her paper.
    She might include her data—a growing number of journals require this—but
    she probably doesn't include her code.
*   Time passes.
*   The journal sends her reviews written anonymously by a handful of other people in her field.
    She revises her paper to satisfy them,
    during which time she might also modify the scripts she wrote earlier,
    and resubmits.
*   More time passes.
*   The paper is eventually published.
    It might include a link to an online copy of her data,
    but the paper itself will be behind a paywall:
    only people who have personal or institutional access
    will be able to read it.

For a growing number of scientists,
though,
the process looks like this:

*   The data that the scientist collects is stored in an open access repository
    like [figshare](https://figshare.com/) or
    [Zenodo](https://zenodo.org), possibly as soon as it's collected,
    and given its own
    [Digital Object Identifier](https://en.wikipedia.org/wiki/Digital_object_identifier) (DOI).
    Or the data was already published and is stored in
    [Dryad](https://datadryad.org/).
*   The scientist creates a new repository on GitHub to hold her work.
*   As she does her analysis,
    she pushes changes to her scripts
    (and possibly some output files)
    to that repository.
    She also uses the repository for her paper;
    that repository is then the hub for collaboration with her colleagues.
*   When she's happy with the state of her paper,
    she posts a version to [arXiv](https://arxiv.org/)
    or some other preprint server
    to invite feedback from peers.
*   Based on that feedback,
    she may post several revisions
    before finally submitting her paper to a journal.
*   The published paper includes links to her preprint
    and to her code and data repositories,
    which  makes it much easier for other scientists
    to use her work as starting point for their own research.

This open model accelerates discovery:
the more open work is,
[the more widely it is cited and re-used](https://doi.org/10.1371/journal.pone.0000308).
However,
people who want to work this way need to make some decisions
about what exactly "open" means and how to do it. You can find more on the different aspects of Open Science in [this book](https://link.springer.com/book/10.1007/978-3-319-00026-8).

This is one of the (many) reasons we teach version control.
When used diligently,
it answers the "how" question
by acting as a shareable electronic lab notebook for computational work:

*   The conceptual stages of your work are documented, including who did
    what and when. Every step is stamped with an identifier (the commit ID)
    that is for most intents and purposes unique.
*   You can tie documentation of rationale, ideas, and other
    intellectual work directly to the changes that spring from them.
*   You can refer to what you used in your research to obtain your
    computational results in a way that is unique and recoverable.
*   With a version control system such as Git,
    the entire history of the repository is easy to archive for perpetuity.

> ## Making Code Citable
>
> Anything that is hosted in a version control repository (data, code, papers,
> etc.) can be turned into a citable object. You'll learn how to do this in
> [lesson 12: Citation]({{ page.root }}/12-citation/).
{: .callout}

> ## How Reproducible Is My Work?
>
> Ask one of your labmates to reproduce a result you recently obtained
> using only what they can find in your papers or on the web.
> Try to do the same for one of their results,
> then try to do it for a result from a lab you work with.
{: .challenge}

> ## How to Find an Appropriate Data Repository?
>
> Surf the internet for a couple of minutes and check out the data repositories
> mentioned above: [Figshare](https://figshare.com/), [Zenodo](https://zenodo.org),
> [Dryad](https://datadryad.org/). Depending on your field of research, you might
> find community-recognized repositories that are well-known in your field.
> You might also find useful [these data repositories recommended by Nature](
> https://www.nature.com/sdata/data-policies/repositories).
> Discuss with your neighbor which data repository you might want to
> approach for your current project and explain why.
{: .challenge}

---
title: Licensing
teaching: 5
exercises: 0
questions:
- "What licensing information should I include with my work?"
objectives:
- "Explain why adding licensing information to a repository is important."
- "Choose a proper license."
- "Explain differences in licensing and social expectations."
keypoints:
- "People who incorporate General Public License (GPL'd) software into their own software must make their software also open under the GPL license; most other open licenses do not require this."
- "The Creative Commons family of licenses allow people to mix and match requirements and restrictions on attribution, creation of derivative works, further sharing, and commercialization."
- "People who are not lawyers should not try to write licenses from scratch."
---

When a repository with source code, a manuscript or other creative
works becomes public, it should include a file `LICENSE` or
`LICENSE.txt` in the base directory of the repository that clearly
states under which license the content is being made available. This
is because creative works are automatically eligible for intellectual
property (and thus copyright) protection. Reusing creative works
without a license is dangerous, because the copyright holders could
sue you for copyright infringement.

A license solves this problem by granting rights to others (the
licensees) that they would otherwise not have. What rights are being
granted under which conditions differs, often only slightly, from one
license to another. In practice, a few licenses are by far the most
popular, and [choosealicense.com](https://choosealicense.com/) will
help you find a common license that suits your needs.  Important
considerations include:

* Whether you want to address patent rights.
* Whether you require people distributing derivative works to also
  distribute their source code.
* Whether the content you are licensing is source code.
* Whether you want to license the code at all.

Choosing a license that is in common use makes life easier for
contributors and users, because they are more likely to already be
familiar with the license and don't have to wade through a bunch of
jargon to decide if they're ok with it.  The [Open Source
Initiative](https://opensource.org/licenses) and [Free Software
Foundation](https://www.gnu.org/licenses/license-list.html) both
maintain lists of licenses which are good choices.

[This article][software-licensing] provides an excellent overview of
licensing and licensing options from the perspective of scientists who
also write code.

At the end of the day what matters is that there is a clear statement
as to what the license is. Also, the license is best chosen from the
get-go, even if for a repository that is not public. Pushing off the
decision only makes it more complicated later, because each time a new
collaborator starts contributing, they, too, hold copyright and will
thus need to be asked for approval once a license is chosen.

> ## Can I Use Open License?
>
> Find out whether you are allowed to apply an open license to your software.
> Can you do this unilaterally,
> or do you need permission from someone in your institution?
> If so, who?
{: .challenge}

> ## What licenses have I already accepted?
>
> Many of the software tools we use on a daily basis (including in this workshop) are
> released as open-source software. Pick a project on GitHub from the list below, or
> one of your own choosing. Find its license (usually in a file called `LICENSE` or
> `COPYING`) and talk about how it restricts your use of the software. Is it one of
> the licenses discussed in this session? How is it different?
> - [Git](https://github.com/git/git), the source-code management tool
> - [CPython](https://github.com/python/cpython), the standard implementation of the Python language
> - [Jupyter](https://github.com/jupyter), the project behind the web-based Python notebooks we'll be using
> - [EtherPad](https://github.com/ether/etherpad-lite), a real-time collaborative editor
{: .challenge}

[software-licensing]: https://doi.org/10.1371/journal.pcbi.1002598
